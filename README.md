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


Debugging & Fixes Summary

During development and deployment on PythonAnywhere, I encountered and resolved several issues with my Django project (RestoBan). Below is a summary of the key problems and how they were fixed:

1. ⚠️ Recipe List showing only dots (.)

Problem: Visiting /recipes/ displayed only empty bullets instead of recipe details.

Cause: The template was rendering optional fields (get_category_display, servings, total_time_minutes) that were either empty or misconfigured, resulting in blank output.

Fix:

Created a minimal debug template to first confirm recipes were loading correctly.

Verified title and id fields rendered properly.

Gradually added other fields back to pinpoint issues.

Result: Recipes now display correctly with all necessary details.

2. ⚠️ Sign Up working, but Login link returned Server Error (500)

Problem:

The signup page rendered and created accounts successfully.

Clicking "Login here" redirected to {% url 'restoban:login' %}, which caused a NoReverseMatch → 500 error.

Cause: Django’s built-in auth URLs (django.contrib.auth.urls) are not namespaced. Using restoban:login was invalid.

Fix:

Updated signup.html and login.html to use {% url 'login' %} and {% url 'password_reset' %} instead of restoban:....

Kept restoban:signup since signup is a custom view in the app.

Result: Login, password reset, and signup navigation now work without errors.

3. ⚠️ Messages not displaying correctly

Problem: Flash messages after signup were not styled consistently.

Fix: Updated template to use alert-{{ message.tags }}, so Django’s message levels (success, error, info) map correctly to Bootstrap alerts.

Result: Messages now show in the correct style (green for success, red for errors, etc.).

4.  Local development server issues

Problem: Running python manage.py runserver failed because port 8000 and later 8080 were already in use.

Fix: Specified an alternate port (python manage.py runserver 8001) which resolved the conflict.

Result: Local debugging could continue without needing to kill processes.

✅ Final Outcome

Homepage (/) now links to Recipes, Orders, and Sign Up — all working.

Recipes display correctly from the database.

User registration, login, and password reset work as expected.

Admin and API endpoints function correctly.

