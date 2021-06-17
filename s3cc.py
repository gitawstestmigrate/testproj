import boto3
import requests
import urllib3
import os

def list_folders(s3_client, bucket_name):
    folders = set()
    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix='Senior-Design-Bosch-Air-Quality/master/')

    for content in response.get('Contents', []):
        folders.add(os.path.dirname(content['Key']))

    return sorted(folders)
    
folder_list = list_folders(s3, 'rmrameshbucket222')

for folder in folder_list:
    print("Folders found ",folder)

def get_s3_keys(bucket):
    #s3 = boto3.client('s3')
    obs = []
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    """Get a list of keys in an S3 bucket."""
    resp = s3.list_objects_v2(Bucket=bucket)
    for obj in resp['Contents']:
      obs.append(obj['Key'])
    return obs



objs=get_s3_keys('rmrameshbucket222')

for k in objs:
    print("key list ",k)

repoName='testRepo25'
branch_name='main'
response = codecommit.create_repository(
    repositoryName=repoName,
    repositoryDescription='made for migration',
    tags={
        'string': 'string'
    }
)
i = 0
for x in objs:
    fileobj = s3.get_object(
        Bucket='rmrameshbucket222',
        Key=x
        ) 
    
    filedata = fileobj['Body'].read()
    counter = "commit num " + str(i)
    print(counter)
    if i == 0:     
        response = codecommit.put_file(
            repositoryName=repoName,
            branchName=branch_name,
            fileContent=filedata,
            filePath=x,
            fileMode='NORMAL',
            commitMessage=counter,
            name='roger',
            email='roger.m.ramesh@gmail.com'
        )
        
    else:    
        response = codecommit.put_file(
            repositoryName=repoName,
            branchName=branch_name,
            fileContent=filedata,
            filePath=x,
            fileMode='NORMAL',
            parentCommitId = comID,
            commitMessage=counter,
            name='roger',
            email='roger.m.ramesh@gmail.com'
        )
       
    branch_dict = codecommit.get_branch(repositoryName = repoName, branchName = branch_name)
    comID = str(branch_dict['branch']['commitId']) 
    i=i+1
