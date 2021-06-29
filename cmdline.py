import os
import boto3

ACCESS_KEY = ''
SECRET_KEY = ''
codecommit=boto3.client('codecommit',aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)

os.mkdir("Geeks26")
repoName = "MyDemoRepoV26"
repoURL = "https://git-codecommit.us-east-1.amazonaws.com/v1/repos/"+repoName
print(repoURL)
# Print the current working directory
#repoDICT = os.system("aws codecommit create-repository --repository-name "+repoName)
response = codecommit.create_repository(
    repositoryName=repoName,
    repositoryDescription='made for migration',
    tags={
        'string': 'string'
    }
)

os.system("git clone --mirror https://github.com/rmramesh22/Senior-Design-Bosch-Air-Quality.git Geeks26")
os.chdir("Geeks26")
cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))
os.system("git push " + repoURL + " --all")
# repoURL = repoDICT
#os.system("git clone --mirror https://github.com/rmramesh22/Senior-Design-Bosch-Air-Quality.git Geeks1")
#os.chdir("Geeks1")
#cwd = os.getcwd()
#print("Current working directory: {0}".format(cwd))
#os.system("git push https://git-codecommit.us-east-1.amazonaws.com/v1/repos/MyDemoRepo11 --all")
