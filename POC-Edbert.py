import requests

ACCOUNT = {
    "name": "asd",
    "email": "asd@asd.com",
    "password": "asd",
}

HOST = "http://localhost:8080/"

COOKIE = ""

def do_signup(option: int):
    url = "auth/sign-up/job-seeker"
    
    body = {
        "name": "asd",
        "email": "asd@asd.com",
        "password": "asd",
    }
    
    res = requests.post(HOST + url, data=body)
    print(res.status_code, res.text)
    
def do_signin():
    url = "auth/sign-in"
    payload = {
        "email": ACCOUNT['email'],
        "password": ACCOUNT['password']
    }
    
    res = requests.post(HOST + url, data=payload)
    print(res.headers)
    print(res.cookies.)

def do_jobsearch():
    url = "jobs"
    params = {
      "search": "",
      "sort-created-at": "newest-first",
      "created-at-from": "",
      "created-at-to=": "",
      'job-types[]': ['full-time', 'part-time', 'internship']
    } 

if __name__ == "__main__":
    do_signin()