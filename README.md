## Description:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;API for creating, retrieving, listing and deleting employees inside company.

## Install dependencies:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pip install -r requirments.txt
    
## Loading data:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python3 manage.py loaddata fixtures.json
  
## Endpoints:
*   http://localhost/api/employees/ GET list of employees
*   http://localhost/api/employees/ POST  create employee (only for staff)  
*   http://localhost/api/employees/:id/ GET retrieve employee  
*   http://localhost/api/employees/:id/ PUT update employee (only for staff)  
*   http://localhost/api/employees/:id/ PATCH partial update (only for owner)  
*   http://localhost/api/employees/:id/ DELETE  delete employee (only for staff)  

## Usage:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; After loading data using fixtures you will get 3 employees in db:
*  login: admin, password: admin123
*  login: HRUser, password: LDJ7LZ59
*  login: Buyer, password: CGP7RNGG

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Creating new employee after signing in as HRUser or admin using UI:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   "username": "username",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   "rank": "[J/M/S/H]",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   "department": "[IT/HR/BU/DG]",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   "email": "required email for getting password"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; After creating employee will get email with login and password.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Each employee with department HR will get staff status.

## Usage with curl:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; curl -u HRUser -d "username=NewUser&rank=S&department=DG&email=djangotestmail4@gmail.com" -X POST http://localhost/api/employees/  - Create new employee.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; curl http://localhost/api/employees/ - Get list of employees.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; curl http://localhost/api/employees/:id/ - Retrieve employee data.




