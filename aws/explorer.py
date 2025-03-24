import boto3
import exceptions.AwsException
import json
from exceptions.AwsException import AwsException


class AwsCostExplorer:

    client = boto3.client('ce')

    def getCostAndUsage(self):

        try:
            response = self.client.get_cost_and_usage(
                TimePeriod={
                    'Start': '2025-03-20',
                    'End': '2025-03-23'
                },
                Granularity='DAILY',
                Metrics=[
                    'BlendedCost',
                ],
                GroupBy=[
                    {
                        'Type': 'DIMENSION',
                        'Key': 'AZ'
                        },
                ]
            )
            print(response)
            return {"status":"ok","data": response}
        except Exception as error:
            errorClass = error.__class__.__name__
            msg = json.dumps({"status": "error", "type": errorClass, "details": error.__str__()})
            raise AwsException(msg.__str__())


