#!/usr/bin/env python3
import os
import aws_cdk as cdk
from aws_infra.sqs import SQS
from models.enum.aws import AWS, Environment

app = cdk.App()

env_default = cdk.Environment(
    account=AWS.ACCOUNT_ID.value,
    region=AWS.US_EAST_1.value,
)
us_east_1 = cdk.Environment(
    account=AWS.ACCOUNT_ID.value,
    region=AWS.US_EAST_1.value,
)
us_west_2 = cdk.Environment(
    account=AWS.ACCOUNT_ID.value,
    region=AWS.US_WEST_2.value,
)


SQS(app, "SQSQueue", env=us_east_1, stack_name="sqs-queue-stack")

app.synth()
