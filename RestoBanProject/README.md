Project Overview
This repository is part of the ALX Backend Web Development Program and serves as my ALX Graduation Project. The goal of this project is to build a restaurant management system that will contribute to earning my ALX certificate.

Progress Log
Today’s Actions:

Created a GitHub repository named ALX_GradProject to represent my graduation project.

Linked my local machine to this repository using:

bash
Copy
Edit
git clone https://github.com/HamzahElAnbary/ALX_GradProject.git
Initialized my first Django project named RestoBanProject.

Created my first Django app called RestoBan.

Registered the new app in RestoBanProject/settings.py by adding it to INSTALLED_APPS:


INSTALLED_APPS = [
    ...,
    'RestoBan',
]
Committed and pushed the changes to GitHub:

bash
Copy
Edit
git add .
git commit -m "Set up Django project and app"
git push origin main

Next Steps

Next week, I’ll focus on structuring the app by working on:

Models (to define the database structure)

Views (to handle application logic)

Templates (to build the user interface)

Second Push

During this stage of the project, I structured the RestoBan application by implementing the core components of the MVC pattern. I created Models to define the database structure, developed Views to handle application logic, and built Templates for the user interface. I also applied full CRUD operations for recipes, enabling users to create, read, update, and delete entries. Additionally, I set up the URL routing for proper navigation and added basic testing for the recipe functionality to ensure the application behaves as expected. Overall, these steps laid the foundation for a well-organized and functional web application.
Next week, I will be focusing on the below: 

Technical Requirements:
Database:
Authentication:
API Design:
Deployment:
Pagination and Sorting:
