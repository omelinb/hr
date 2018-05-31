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

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Creating new employee after signing in as HRUser or admin:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   "username": "username",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   "rank": "[J/M/S/H]",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   "department": "[IT/HR/BU/DG]",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   "email": "required email for getting password"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; After creating employee will get email with password. 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Each employee from HR department will get staff status.
