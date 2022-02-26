from importlib.resources import contents
import pathlib
import shutil
import os
import requests


from main import query
from main import API_TOKEN
from main import API_URL

POST_URL = 'https://hook.integromat.com/rybiz8a5yhxhsitywjbhixb38rcku5qm'

#https://www.kite.com/python/answers/how-to-iterate-through-the-contents-of-a-directory-in-python

#https://www.w3schools.com/python/ref_requests_post.asp

contents = pathlib.Path("./data/assignment_1").iterdir()
for path in contents:
    obj = query(path, API_URL, API_TOKEN)
    imageId = os.path.basename(path)
    entry = {
        "image": imageId,
        "result": obj}
    requests.post(POST_URL, json = entry)
    os.remove(path)