Contributions: Omar Elgohary, 6/13/2023

# Project Name: AzDevOpsLicensesScript 

(Possible authentication issues described below)


# Task preformed:

- This Python script makes one large get request to Azure DevOps API and many smaller get requests 
  to Microsoft Graph API in order to match users' Name, Department, and License Type
  which is then outputed onto a csv file. 


# Installation

- Download the file AzDevOpsLicensesScript.py and place in a distinct folder 
- Download required python libraries by clicking on your windows button 
  looking up the terminal and individually inputing these lines:
  pip install requests
  pip install pybase64
  pip install python-csv
  pip install msal


# Usage 

(Assuming you have python downloaded)

- Using VS code: Open the folder on VS code by opening the folder you downloaded the 
  Python file on. Then press the run buuton on the top right 

- Using the terminal: 
  1. Open the folder you have downloaded the python file on. 
  Copy the path from the long rectangular bar on the top of your screen which contains
  your folder name. 

  what you copy should something look like this: C:\Users\OMEL001\Desktop\Projects\Project License

  2. then open your terminal like described above write cd then paste the path and hit enter

  should look like this: cd C:\Users\OMEL001\Desktop\Projects\Project License

  3. Now, copy and paste this into your terminal and hit enter: python AzDevOpsLicensesScript.py

  4. Now wait under a 1 minute and in the same folder a csv file titled List of Employees, Departments, and Licenses
  will appear with the desired info. 



# Possible Future Contributions 

- If additional data is wanted from the Azure DevOps API one could view the entire ouptut 
  of the general Azure DevOps get request by uncommenting lines 55 and 56. These will
  output a seperate file that displays all data gathered in that api. 

- for the graph API one could just use the graph api simulator which is linked below.

- adding additional information from any of these two onto the csv file would only involve 
  simple dictionary/array navigation within the for loop which demonstrates that action already

# Possible Errors

- Important clarification: This script uses two authentication keys that eventually expire!
- If this error is encountered or a similar one: 

    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
    File "c:\Users\OMEL001\Desktop\Projects\Project License\AzDevOpsLicensesScript.py", line 54, in <module>
        fulljsonFile = allAccountsRes.json()
                    ^^^^^^^^^^^^^^^^^^^^^
    File "C:\Users\OMEL001\AppData\Local\Programs\Python\Python311\Lib\site-packages\requests\models.py", line 975, in json
        raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)
    requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

 - Then the issue is that you need to create a new Azure DevOps key and replace the variable 'pat' with the new key
   you have created. Here's a link on how to create one: https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=Windows   



 - If the error looks like this then the issue is with the Microsoft Graph authentication:

    Traceback (most recent call last):
    File "c:\Users\OMEL001\Desktop\Projects\Project License\AzDevOpsLicensesScript.py", line 35, in <module>
        raise Exception("No Access Token found")
    Exception: No Access Token found


 - Then you'd have to create a new graph key with these specific permissions: 
    Directory.Read.All 
    User.Read.All

 - and replace variables client_id, client_secret, and tenant_id with the relevant information 

 - here's a link for that too: https://learn.microsoft.com/en-us/graph/auth/auth-concepts


# Resources Used

- https://learn.microsoft.com/en-us/rest/api/azure/devops/memberentitlementmanagement/user-entitlement-summary/get?view=azure-devops-rest-7.1

- https://developer.microsoft.com/en-us/graph/graph-explorer



  