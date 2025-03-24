# CloudMore-AWS
CloudMore AWS Custom Service Integration

## Requirements

    * CloudMore SDK Swagger Client: https://github.com/AdrianCloudMore/CloudMorePythonSDK
    * Boto3 (AWS Python SDK): https://github.com/boto/boto3
    * FastAPI

## Install Requirements


### AWS boto3 Python SDK

Install the AWS boto3 Python SDK

#### Install

```shell
 python3 -m pip install boto3
```

#### Documentation

https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

#### Configure

Set your AWS_ACCESS_KEY & AWS_SECRET_KEY environment variables, or edit ~/.aws/credentials

### CloudMore Python SDK

Install CloudMore Python SDK Swagger Client

#### Download
https://cloudmore-aws-integration-bucket.s3.us-east-1.amazonaws.com/swagger_client-1.0.0-py3.12.egg

#### Install

```shell
 python3 -m pip install swagger_client
```

#### Configure

Set the following environment variables

    * CLOUDMORE_USERNAME
    * CLOUDMORE_PASSWORD
    * CLOUDMORE_SECRET

## Run 

```shell
 fastapi dev main.py
```

   