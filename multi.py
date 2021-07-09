import os
import boto3
from github import Github
import github3


access_TOKEN = ""
gh = github3.login(token=access_TOKEN)
USERNAME = ""
print("")
#user = g.get_user("rmramesh22") # target user
#repos = user.get_repos()
privateLST = []
publicLST = []
for repos in gh.repositories(type='private'):
    privateLST.append(repos)
    #print(repos)
    
for repos in gh.repositories(type='public'):
    publicLST.append(repos)

prvLST = []
for i in privateLST:
    prvLST.append(str(i))
    
pblLST = [] 
for i in publicLST:
    pblLST.append(str(i))


print(prvLST)
print(pblLST)

totalRepos= []

for items in pblLST:
    if USERNAME in items:
        totalRepos.append(items)

for items in prvLST:
    if USERNAME in items:
        totalRepos.append(items)
    
print(totalRepos)

for items in totalRepos:
    user,content = items.split('/',1)
    URL = "https://"+access_TOKEN+"@github.com/"+user+"/"+content
    os.mkdir(content)
    repoURL = "https://git-codecommit.us-east-1.amazonaws.com/v1/repos/"+content
    response = codecommit.create_repository(
    repositoryName=content,
    repositoryDescription=content,
    tags={
        'string': 'string'
        }
    )
    os.system("git clone --mirror " + URL +" "+content)
    os.chdir(content)
    cwd = os.getcwd()
    print("Current working directory: {0}".format(cwd))
    os.system("git push " + repoURL + " --all")
    print("Current working directory: {0}".format(cwd))
    os.chdir("..")
    cwd1 = os.getcwd()
    print("Current working directory: {0}".format(cwd1))
    os.system("rm -rf "+content)
    arr = os.listdir()
    print(arr)
    #print(URL)


