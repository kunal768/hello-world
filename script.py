import requests
import pandas as pd
from strgen import StringGenerator as SG

url = "http://localhost:8080/signup"


def gen_pass():
    return SG("[a-zA-Z0-9]{16}").render()


def load_users(filename):
    data = pd.read_csv(filename)

    usernames = data["username"]
    passwords = data["password"]
    user_type = data["user_type"]
    profile_picture_url = data["profile_picture_url"]

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    for entry in range(0,len(data)):
        load = {"username":usernames[entry],"password":passwords[entry],"user_type":user_type[entry],"profile_picture_url":profile_picture_url[entry]}
        requests.post(url,json = load,headers = headers)
    return
