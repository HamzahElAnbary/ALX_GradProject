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
