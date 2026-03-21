import requests

def fetchandsave(url,path):
    r=requests.get(url)
    with open (path,"w") as f:
        f.write(r.text)


url="https://www.geeksforgeeks.org/batch/da-skill-up/track/su-da-day30/article/NzI2ODMx"

fetchandsave(url,"data/times.html")