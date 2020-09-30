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
```

```python
from lambdasdk.lambdasdk import Lambda
```

```python
lambda_ = Lambda(
    user = USER,
    pw = PW,
    region = 'ap-southeast-1'
)
```

```python
lambda_.invoke(
    functionName= 'lambda-pip' ,
    input = input, 
    invocationType= 'RequestResponse' 
)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-5-920a01721d5e> in <module>
    ----> 1 lambda_.invoke(
          2     functionName= 'lambda-pip' ,
          3     input = input,
          4     invocationType= 'RequestResponse'
          5 )


    ~/pip/lambdasdk/lambdasdk/lambdasdk.py in invoke(self, functionName, input, invocationType)
         22       LogType='Tail',
         23       ClientContext= base64.b64encode(json.dumps({'caller': 'sdk'}).encode()).decode(),
    ---> 24       Payload= json.dumps(input)
         25     )


    /usr/local/Caskroom/miniconda/base/envs/python38/lib/python3.8/json/__init__.py in dumps(obj, skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, separators, default, sort_keys, **kw)
        229         cls is None and indent is None and separators is None and
        230         default is None and not sort_keys and not kw):
    --> 231         return _default_encoder.encode(obj)
        232     if cls is None:
        233         cls = JSONEncoder


    /usr/local/Caskroom/miniconda/base/envs/python38/lib/python3.8/json/encoder.py in encode(self, o)
        197         # exceptions aren't as detailed.  The list call should be roughly
        198         # equivalent to the PySequence_Fast that ''.join() would do.
    --> 199         chunks = self.iterencode(o, _one_shot=True)
        200         if not isinstance(chunks, (list, tuple)):
        201             chunks = list(chunks)


    /usr/local/Caskroom/miniconda/base/envs/python38/lib/python3.8/json/encoder.py in iterencode(self, o, _one_shot)
        255                 self.key_separator, self.item_separator, self.sort_keys,
        256                 self.skipkeys, _one_shot)
    --> 257         return _iterencode(o, 0)
        258 
        259 def _make_iterencode(markers, _default, _encoder, _indent, _floatstr,


    /usr/local/Caskroom/miniconda/base/envs/python38/lib/python3.8/json/encoder.py in default(self, o)
        177 
        178         """
    --> 179         raise TypeError(f'Object of type {o.__class__.__name__} '
        180                         f'is not JSON serializable')
        181 


    TypeError: Object of type method is not JSON serializable

