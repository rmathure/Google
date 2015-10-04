__author__ = 'rohanmathure'


import json
import requests

url = "https://app.close.io/hackwithus/"
data = dict()
data['first_name']='Rohan'
data['last_name'] = 'Mathure'
data['email'] = 'rmathure@indiana.edu'
data['phone'] = '8122729734'
data['cover_letter'] = """Hi,

I am a motivated and enthusiastic software developer who's willing to learn and master any technology stack that the job requires.
My favorite programming language is Python(very comfortable with it)  and I have strong experience with object-oriented programming with Java and C#. More than everything, I really like challenges and the joy they give when you solve one.
My forte is learning and adapting to any technology stack as the need arises and I have proven that in the past.
I would be more than happy to work with you if you find my profile to be a good match for you.

Thanks
Rohan"""
data ['urls']= ['https://github.com/rmathure',
'http://www.codewars.com/users/rmathure',
'https://www.linkedin.com/pub/rohan-mathure/47/a60/a63']

#headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data))
print r.status_code
print r.json

