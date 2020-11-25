#!/usr/bin/env python3

import os
from aws_cdk import core

from kubeflow_cognito_infra.cognito_stack import CognitoStack

app = core.App()

CognitoStack(app, 'CognitoStack', env=core.Environment(
    account=os.environ["CDK_DEFAULT_ACCOUNT"], 
    region='eu-west-1'))

app.synth()
