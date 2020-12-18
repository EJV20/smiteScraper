import requests
import hashlib
import config as cfg
import datetime
import json

# https://docs.google.com/document/d/1OFS-3ocSx-1Rvg4afAnEHlT3917MAK_6eJTR6rzr-BM/edit#

se = "http://api.smitegame.com/smiteapi.svc/"
rf = "JSON"
dev_id = cfg.cfg["devid"]
auth_key = cfg.cfg["authKey"]
lc = "1"


def timestamp():
    now = datetime.datetime.utcnow()
    now = now.strftime("%Y%m%d%H%M%S")
    return now

def create_signature(method):
    to_hash = str(dev_id + method + auth_key + timestamp())
    print("to hash: " + to_hash)
    signature = hashlib.md5(to_hash.encode())
    return signature.hexdigest()

def url_builder(session, method, lang):
    sig = create_signature(method=method)
    url = se + method + rf + "/" + dev_id + "/" + sig + "/"
    if session is None:
        print("No Session")
        url = url + timestamp()
    else:
        print("Session")
        url = url + session + "/" + timestamp()

    if lang is not None:
        url = url + "/" + lang

    return url

def test_session(session):
    url = url_builder(session=session, method="testsession", lang=None)
    t = requests.get(url)
    return t.status_code


def create_session():
    url = url_builder(session=None, method="createsession", lang=None)
    print("URL: " + url)
    r = requests.get(url)
    session = get_session_id(session_response=r)
    return session

def get_session_id(session_response):
    session_json = json.loads(session_response.content)
    session_id = session_json["session_id"]
    return session_id


def get_gods(session):
    url = url_builder(session=session, method="getgods", lang="1")
    r = requests.get(url)
    jsn = json.loads(r.text)

    d = {}
    i = 0
    with open('godList.txt', 'r') as gl:
        print("read")
        lines = gl.readlines()
        for line in lines:
            d[line.rstrip()] = jsn[i]
            i += 1

    with open('gods.json', 'w+') as f:
        json.dump(d, f, ensure_ascii=False, sort_keys=True, indent=2)


def get_patch(session):
    url = url_builder(session=session, method="getpatchinfo", lang=None)
    r = requests.get(url)
    version = json.loads(r.text)["version_string"]
    print(version)
    return version


def main():
    session_id = create_session()
    test_session(session=session_id)
    get_gods(session=session_id)
    get_patch(session=session_id)


if __name__ == "__main__":
    main()