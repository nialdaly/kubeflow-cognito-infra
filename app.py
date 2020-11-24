#!/usr/bin/env python3

from aws_cdk import core

from kubeflow_cognito_infra.kubeflow_cognito_infra_stack import KubeflowCognitoInfraStack


app = core.App()
KubeflowCognitoInfraStack(app, "kubeflow-cognito-infra")

app.synth()
