# AUTOGENERATED! DO NOT EDIT! File to edit: lambdasdk.ipynb (unless otherwise specified).

__all__ = ['InvocationType', 'Lambda']

# Cell
from dataclasses import dataclass
from dataclasses_json import dataclass_json
@dataclass_json
@dataclass
class InvocationType:
  requestResponse = 'RequestResponse'
  event = 'Event'

# Cell
import boto3, base64, json
class Lambda:
  '''
    for invoking lambda functions
  '''
  def __init__(self, user=None, pw=None, sessionToken=None, region = 'ap-southeast-1'):
    self.lambdaClient = boto3.client(
        'lambda',
        aws_access_key_id=user,
        aws_secret_access_key=pw,
        region_name = region,
        aws_session_token=sessionToken
      )
  def invoke(self, functionName, input, invocationType= 'RequestResponse'):
    response = self.lambdaClient.invoke(
      FunctionName = functionName,
      InvocationType= invocationType,
      LogType='Tail',
      ClientContext= base64.b64encode(json.dumps({'caller': 'sdk'}).encode()).decode(),
      Payload= json.dumps(input)
    )
    if invocationType == 'Event':
      return True
    return json.loads(response['Payload'].read())
