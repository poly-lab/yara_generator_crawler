import requests
from urllib import urlretrieve
url='http://www.yara-generator.net/rules/'
for i in range(222,500):
    url=url+str(i)
    r=requests.get(url)
    print r.url
    if 'http://www.yara-generator.net/'==r.url:
        
        print i
    else:
        print i,"ok"
url3='http://www.yara-generator.net/rules/235/17404/simpleandsuperyararules?download=1'
urlretrieve(url,"1.zip")
    