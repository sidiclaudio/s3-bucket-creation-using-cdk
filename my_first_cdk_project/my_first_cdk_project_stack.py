from aws_cdk import (
    core,
    aws_s3 as _s3
)


class MyFirstCdkProjectStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        # Bucket construct
        _s3.Bucket(
            self,
            "myBucketId",
            bucket_name="myfirstcdkprojectbucket2021",
            versioned=True,
            encryption=_s3.BucketEncryption.KMS_MANAGED
        )