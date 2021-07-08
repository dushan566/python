import urllib.request

def get_status():
    appurl = urllib.request.urlopen("https://api.github.com/users/hadley/orgs")
    status_code = appurl.getcode()
    print(status_code)
    response = appurl.read()
    if status_code == 200:
        print("Site is accessible")
        print(response)
    else:
        print("Site is unreachable")
        print(response)

if __name__ == "__main__":
    get_status()    