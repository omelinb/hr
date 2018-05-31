## Description    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Application for creating, retrieving, listing and deleting employees inside company.

## Installing  
```shell
$ pip install -r requirments.txt  
$ python3 manage.py makemigrations  
$ python3 manage.py migrate  
$ python3 manage.py loaddata fixtures.json  
$ python3 manage.py runserver  
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; It will create a database with following employees:
*  login: admin, password: admin123  
*  login: HRUser, password: LDJ7LZ59  
*  login: Buyer, password: CGP7RNGG  

## Endpoints  
*   /api/employees/ GET list of employees
*   /api/employees/ POST  create employee (only for staff)  
*   /api/employees/:id/ GET retrieve employee  
*   /api/employees/:id/ PUT update employee (only for staff)  
*   /api/employees/:id/ PATCH partial update (only for owner)  
*   /api/employees/:id/ DELETE  delete employee (only for staff)  

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

## Usage with curl:  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Create new employee with username "NewUser", rank "Senior, department "Digital" and email "djangotestmail4@gmail.com".  
```shell
curl -u HRUser -d "username=NewUser&rank=S&department=DG&email=djangotestmail4@gmail.com" -X POST http://localhost:8000/api/employees/
```  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Get list of employees.  
```shell  
curl http://localhost:8000/api/employees/  
```  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Retrieve data of employee with id 3.  
```shell  
curl http://localhost:8000/api/employees/3/
```  
