from aws_cdk import (
    core,
    aws_ssm,
    aws_certificatemanager,
    aws_cognito
)

class CognitoStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Retrieves the ACM certificate arn from an SSM parameter
        certificate_arn = aws_ssm.StringParameter.value_from_lookup(self, 
            'cognito_certificate_arn')

        # Retrieves the domain name from an SSM parameter
        domain_name = aws_ssm.StringParameter.value_from_lookup(self, 
            'kubeflow-cognito-domain-name')

        # Creates the cognito user pool
        user_pool = aws_cognito.UserPool(self, 'UserPool',
            user_pool_name = 'mlplatform-user-pool',
            mfa = aws_cognito.Mfa.OFF,
            sign_in_aliases = aws_cognito.SignInAliases(
                username=True,
                email=True))

        # Creates the cognito user pool client
        user_pool_client = aws_cognito.UserPoolClient(self, 'UserPoolClient',
            user_pool = user_pool,
            generate_secret = True,
            o_auth = aws_cognito.OAuthSettings(
                flows = aws_cognito.OAuthFlows(
                    authorization_code_grant = True
                ),
                scopes = [
                    aws_cognito.OAuthScope.EMAIL, 
                    aws_cognito.OAuthScope.OPENID, 
                    aws_cognito.OAuthScope.PROFILE, 
                    aws_cognito.OAuthScope.COGNITO_ADMIN
                ],
                callback_urls = ['https://kubeflow.' + domain_name + '/oauth2/idpresponse']
            ),
            user_pool_client_name = 'mlplatform-user-pool-client')

        
        # Initialises the ACM certificate
        cognito_custom_domain_certificate = aws_certificatemanager.Certificate.from_certificate_arn(self, 'DomainCertificate', 
            certificate_arn)

        # Creates the cognito user pool domain
        user_pool_domain = aws_cognito.UserPoolDomain(self, 'UserPoolDomain',
            user_pool = user_pool,
            custom_domain = aws_cognito.CustomDomainOptions(
                certificate = cognito_custom_domain_certificate,
                domain_name = 'auth.' + domain_name
            )
        )