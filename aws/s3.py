import boto3
import json
import exceptions.AwsException
from exceptions.AwsException import AwsException


class AwsS3:

    s3 = boto3.resource('s3')

    def listObjects(self,bucketName):
        try:
            bucket = self.s3.Bucket(bucketName)
            _files = []
            for obj in bucket.objects.all():
                print(obj.key)
                _files.append(obj.key)

            return {"status": "ok", "files": _files}
        except Exception as error:
            errorClass = error.__class__.__name__
            msg = json.dumps({"status": "error", "type": errorClass, "details": error.__str__()})
            raise AwsException(msg.__str__())