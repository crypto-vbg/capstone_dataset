import pandas as pd
try:
    import requests
    from bs4 import BeautifulSoup
except Exception as e:
    print("Some Modules are missing {}".format(e))

url = "https://github.com/twpayne?tab=repositories"


r = requests.get(url)

soup = BeautifulSoup(r.text,'html.parser')

li = soup.findAll('div' , class_ = 'd-inline-block mb-1')
base_url = "https://github.com/"


no = []
Repo = []
url = []

for _,i in enumerate(li):
    for a in i.findAll('a'):
        newUrl = base_url + a["href"]
    no.append(_)
    Repo.append(i.text.strip())
    url.append(newUrl)
    #print(_,i.text.strip(),newUrl)

tem = list(zip(no,Repo , url))
df = pd.DataFrame(data = tem, columns = ["No" , "Repo","Url"])
print(df)