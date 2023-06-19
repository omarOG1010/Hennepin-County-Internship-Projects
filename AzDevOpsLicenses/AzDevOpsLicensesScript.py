import requests
import base64
import json
import csv 
from msal import ConfidentialClientApplication

# graph api setup
client_id = "Left out for security reasons"
client_secret = "Left out for security reasons"
tenant_id = "Left out for security reasons"

msal_authority = f"https://login.microsoftonline.com/{tenant_id}"

msal_scope = ["https://graph.microsoft.com/.default"]

msal_app = ConfidentialClientApplication(
    client_id=client_id,
    client_credential=client_secret,
    authority=msal_authority,
)

result = msal_app.acquire_token_silent(
    scopes = msal_scope,
    account=None,
)

if not result:
    result = msal_app.acquire_token_for_client(scopes=msal_scope)


if "access_token" in result:
    access_token = result["access_token"]
else:
    raise Exception("No Access Token found")

headers1 = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

# orginal azure devops call setup 
pat = 'Left out for security reasons' #required ticket and authorization
authorization = str(base64.b64encode(bytes(':'+pat, 'ascii')), 'ascii')
headers = {
    'Accept': 'application/json',
    'Authorization': 'Basic '+authorization
}

allAccountsRes = requests.get(
    url="https://vsaex.dev.azure.com/hennepin/_apis/userentitlements?top=10000&skip=0&api-version=4.1-preview.1", headers=headers)

fulljsonFile = allAccountsRes.json() 
# with open("UsersCall.json", "w") as outfile: #check output 
#     json.dump(fulljsonFile, outfile,indent=4)

arrUsers = fulljsonFile['value'] #is initially in array form 

with open("List of Employees, Departments, and Licenses.csv", 'w', newline='') as csvfile:
    fields = ['Name', 'Department' ,'License Type'] #creating the the header for the csv file 
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)

    for i in range(len(arrUsers)):
        arrUser = arrUsers[i]
        level = arrUser.get('accessLevel') # level is the dic with license info 
        nameAccess = arrUser.get('user')
        userName = nameAccess['displayName']
        licenseName = level["licenseDisplayName"]

        #graph api part to get department
        level2 = arrUser.get('user') # gets the level which contains the originid
        oneUserGraph = level2.get('originId') #selects the originid out of the dictionary returned
        urlGraph = "https://graph.microsoft.com/v1.0/users/" #setting up the individual get calls to get departments
        urlGraph  += oneUserGraph
        urlGraph += "?$select=department"
        responseGraph = requests.get(url=urlGraph, headers=headers1)

        oneUserDep = responseGraph.json()
        
        userDep = oneUserDep.get("department")
        row = [userName ,userDep,licenseName ]   #writing out to a csv file
        csvwriter.writerow(row)