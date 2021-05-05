# HR_Website

By Jawad Srour, Mohammad Serhal, Ahmad Khalifeh, Joe Wakim, Frederic Zein, Hossam Younes.

HR plays a key role in developing, reinforcing and changing the culture of an organisation: pay, performance management, training and development.    
This HR management web application, is designed to help HR workers, employers and managers, in managing and keeping track of their employees.   

Website built using Django, HTML, CSS, Javascript, and Bootstrap.

## User Features

Using this web app, you will be able to:

1) Hire and fire employees.

2) Keep employee records and view them for each individual employee or as a group.  

3) Create and delete departements, allowing to add employees to each department, move employees from one department to another, and view the employees of each department.    
4) User authentication (Signing up, Login, and Logout).    

5) Keep track of each employee's absences and overtimes (View them and add to them).    
6) Get notified on each login about the number of employees that have overtimes or absences that go above a certain limit.    

7) A user with too many absences or too many overtime days is marked in red in the Employees table "Lookup Employees" option. 

8) In Employees table, each employee name is clickable and redirects to a page where it displays employee information in a nice manner.

## Authentication

1) Using Django's authentication library, the user (HR) is obliged to register then log-in in order to access the website and its features. 

2) If the user tries to access a route (page) that he/she is not authorized to access ( meaning they are not logged-in) the user will not be allowed to do that. The user will get re-directed to the log-in page where they are prompted to input their credentials. If the user inputs correct credentials, he/she is then redirected back to the page they were trying to access.

3) When the user accesses the Navigation bar before logging in, he/she does not see an option to go to the homepage or the news of the company. 

4) A logged-in user sees the option to log-out in the navigation bar and can browse to go to the home-page or the news page through the navigation bar.

5) Hashes password is stored for the user in the database and not the user password itself to avoid SQL injection attacks and getting user credentials stolen.

6) Newly registered users are welcomed on successful registration as they are redirected to the log-in page with a green welcome pop-up.

