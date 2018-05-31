## Description:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;API for creating, retrieving, listing and deleting employees inside company.

## Install dependencies:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pip install -r requirments.txt
    
## Loading data:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python3 manage.py loaddata fixtures.json  
*  login: admin, password: admin123  
*  login: HRUser, password: LDJ7LZ59  
*  login: Buyer, password: CGP7RNGG  

## Endpoints:
*   /api/employees/ GET list of employees
*   /api/employees/ POST  create employee (only for staff)  
*   /api/employees/:id/ GET retrieve employee  
*   /api/employees/:id/ PUT update employee (only for staff)  
*   /api/employees/:id/ PATCH partial update (only for owner)  
*   /api/employees/:id/ DELETE  delete employee (only for staff)  

## Usage:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; pip install -r requirments.txt  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; python3 manage.py makemigrations  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; python3 manage.py migrate  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; python3 manage.py loaddata fixtures.json  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; python3 manage.py runserver  

### UI  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Creating new employee after signing in as HRUser or admin using UI:  

```json
{  
   "username": "username",  
   "rank": "[J/M/S/H]",  
   "department": "[IT/HR/BU/DG]",  
   "email": "required email for getting password"  
 }
 ```  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; After creating employee will get email with login and password.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Each employee with department HR will get staff status.

### Curl:  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; curl -u HRUser -d "username=NewUser&rank=S&department=DG&email=djangotestmail4@gmail.com" -X POST http://localhost:8000/api/employees/  - Create new employee.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; curl http://localhost:8000/api/employees/ - Get list of employees.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; curl http://localhost:8000/api/employees/:id/ - Retrieve employee data.




