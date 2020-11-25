# Kubeflow Cognito Infrastructure
The following project demonstrates the process of deploying the infrastructure needed for a Kubeflow deployment on Amazon Elastic Kubernetes Service (EKS). This project makes use of the AWS Cloud Development Kit (CDK), an open source software development framework that supports cloud application resources development using programming languages like Python, Java and TypeScript. This project defines the CDK Stacks and App using Python.

## Prerequisites
- [AWS access key ID and secret access key](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-delegated-user.html)
- [awscli](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) (v1.18.179)
- [pip](https://pip.pypa.io/en/stable/installing/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html#via-pip)
- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/work-with.html#work-with-prerequisites)

## 1. CDK Environment Setup
To setup a Python-based CDK environment, the following [guide](https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-python.html) is especially useful. Once the virtual enviroment is set up, the AWS Construct Library modules dependencies needed can be installed using the `requirements.txt` file like so:
```
python -m pip install -r requirements.txt
```

## 2. Deploy CDK Stacks
The `cognito_stack.py` file 
To deploy the CDK Stacks that have been defined, run the following command:
```
cdk deploy --all
```

## 3. Resource Cleanup
Any Stacks created as part of the CDK App can be deleted using the following command:
```
cdk destroy --all
```

## Additional Resources
- [CDK Documentation](https://docs.aws.amazon.com/cdk/api/latest/typescript/api/index.html)
- [CDK with Python](https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-python.html)
- [AWS CDK Examples](https://github.com/aws-samples/aws-cdk-examples)
- [Accessing SSM parameters with CDK](https://docs.aws.amazon.com/cdk/latest/guide/get_ssm_value.html)