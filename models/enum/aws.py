import enum


class AWS(enum.Enum):
    ACCOUNT_ID = "760460643864"
    US_EAST_1 = "us-east-1"
    US_WEST_2 = "us-west-2"


class Environment(enum.Enum):
    DEV = "dev"
    STAGING = "staging"
    PROD = "prod"
