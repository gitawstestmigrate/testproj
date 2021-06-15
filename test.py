from github import Github
import requests
import boto3
import urllib3
#import boto
#from boto.s3.key import Key

repo = g.get_repo("rmramesh22/Senior-Design-Bosch-Air-Quality")
contents = repo.get_contents("")
res = s3.create_bucket(Bucket='rmrameshbucket222')
BucketName = 'rmrameshbucket222'

#print(contents)
for content_file in contents:
    print(content_file)
initialLst = []
while contents:
    file_content = contents.pop(0)
    if file_content.type == "dir":
        contents.extend(repo.get_contents(file_content.path))
    else:
        alpha = str(file_content)
        initialLst.append(alpha)
        
#print(initialLst)
finalLst = []
i=0
while i < len(initialLst):
    x=initialLst[i]
    y=x.replace('ContentFile(path=','')
    a=y.replace(')','')
    finalLst.append(a)
    i = i+1;
    
#print(finalLst)
http=urllib3.PoolManager()

url = "https://raw.github.com/rmramesh22/Senior-Design-Bosch-Air-Quality/master/"
total = len(url)
finalLstV2 = []
j=0
while j < len(finalLst):
    rem = finalLst[j]
    #print(rem)
    mod = rem.replace('"','')
    finalLstV2.append(mod)
    j=j+1


for s in finalLstV2:
    url_re = "https://raw.github.com/rmramesh22/Senior-Design-Bosch-Air-Quality/master/"+s
    print(url_re)
    fullFile = len(url_re)
    fileName = url_re[34:fullFile]
    print(fileName)
    s3.upload_fileobj(http.request('GET', url_re,preload_content=False), BucketName, fileName)
