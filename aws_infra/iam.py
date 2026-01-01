from aws_cdk import (
    Stack,
    aws_iam as iam,
)
from constructs import Construct


class IAM(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        policy = self._create_policy()
        self._create_role_with_policy(policy)

    def _create_role_with_policy(self, policy: iam.Policy) -> iam.Role:
        role = iam.Role(
            self,
            id="AppIamRole",
            role_name="lambda-role",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            description="Role with lambda access for application workloads",
        )

        policy.attach_to_role(role)
        return role

    def _create_policy(self) -> iam.Policy:
        return iam.Policy(
            self,
            "AppIamPolicy",
            policy_name="lambda-policy",
            statements=[
                iam.PolicyStatement(
                    effect=iam.Effect.ALLOW,
                    actions=["lambda:GetFunction"],
                    resources=["*"],
                )
            ],
        )
