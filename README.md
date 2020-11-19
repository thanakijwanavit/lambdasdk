# lambdaSdk
> easy invoking lambda functions


written on top of boto3, for the shortest way to invoke aws lambda functions

## Install

`pip install lambdasdk` 

## How to use

## prepare
### Create user and set up creds
If not on aws, you need to create iam account and map the following keys
#### user and pw
##### if not on aws
```
user = aws_access_key_id
pw = aws_secret_access_key
```
##### if run on aws
```
user = None
pw = None
sessionToken = None
```

```python
from lambdasdk.lambdasdk import Lambda
```

```python
lambda_ = Lambda(
    user = None,
    pw = None,
    sessionToken = None,
    region = 'ap-southeast-1'
)
```

```python
lambda_.invoke(
    functionName= 'lambda-pip' ,
    input = {'test':'test'}, 
    invocationType= 'RequestResponse' 
)
```




    {'statusCode': 200, 'body': '"Hello from Lambda!"'}


