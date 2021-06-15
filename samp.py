import json
from github import Github
import requests
import urllib3
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    g=Github("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")
    target_repo = "gitawstestmigrate/testproj"
    repo = g.get_repo(target_repo)
    contents = repo.get_contents("")
    BucketName="migratev2test"
    res = s3.create_bucket(Bucket=BucketName,CreateBucketConfiguration={'LocationConstraint':'us-east-2' })
    
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
    print("\n") 
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
    
    url = "https://raw.github.com/"+target_repo+"/master/"
    print(url)
    #rmramesh22/Senior-Design-Bosch-Air-Quality /master/"
    total = len(url)
    finalLstV2 = []
    j=0
    while j < len(finalLst):
        rem = finalLst[j]
        #print(rem)
        mod = rem.replace('"','')
        finalLstV2.append(mod)
        j=j+1
    
    print(finalLstV2)
    i = 1
    for s in finalLstV2:
        i=i+1
        url_re = "https://raw.github.com/"+target_repo+"/master/"+s
        #rmramesh22/Senior-Design-Bosch-Air-Quality 
        print(url_re)
        fullFile = len(url_re)
        fileName = url_re[23:fullFile]
        print(fileName)
        s3.upload_fileobj(http.request('GET', url_re,preload_content=False), BucketName, fileName)
        print("complete " + str(i))
    
