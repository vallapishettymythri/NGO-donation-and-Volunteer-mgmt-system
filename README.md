# NGO Donation and Volunteer Management System

## Project Description
The NGO Donation and Volunteer Management System is a Django-based web application designed to help non-governmental organizations manage donations and volunteer activities efficiently. It provides a centralized platform where admins can manage NGOs, donations, and volunteer opportunities, while users can donate and enroll as volunteers by providing contact details.

---

## Objectives
- To provide a centralized system for NGO operations
- To manage donations and volunteer activities digitally
- To reduce manual record keeping
- To enable easy coordination between NGOs and contributors

---

## User Roles

### Admin
- Login to admin dashboard
- Add and manage NGO details
- Create volunteer opportunities (role, location, required count)
- View volunteer opportunities
- View volunteer applications submitted by users
- View donation requests with donor contact details

### User
- Register and login
- View NGOs
- Submit donation requests (Money, Blood, Items)
- Provide phone number for NGO coordination
- View volunteer opportunities
- Enroll as a volunteer by submitting name and phone number

---

## System Workflow
1. Admin logs in and adds NGOs and volunteer opportunities.
2. Users register and log in to the system.
3. Users can donate by selecting donation type and submitting contact details.
4. Users can view available volunteer opportunities and enroll.
5. Admin views donation and volunteer data and contacts users offline.

---

## Donation Management
The system records donation intent instead of processing online payments. Users can donate money, blood, or items and provide contact details. NGOs coordinate the donation process offline.

---

## Volunteer Management
Admins create volunteer opportunities. Users view available roles and enroll by submitting their name and phone number. Admins can view all volunteer applications and contact volunteers directly.

---

## Technologies Used
- Frontend: HTML, CSS
- Backend: Python, Django Framework
- Database: SQLite
- ORM: Django ORM
- Tools: Django Admin Panel

---

---

## How to Run the Project
1. Download or clone the project
2. Navigate to the project directory
3. Run database migrations:
python manage.py makemigrations
python manage.py migrate
4. Create admin superuser:
5. Start the server: python manage.py runserver
6. Open the application in browser


---

## Key Features
- Role-based access (Admin and User)
- Multiple donation types (Money, Blood, Items)
- Volunteer opportunity management
- Contact-based coordination
- Simple and user-friendly interface
- No payment gateway complexity

---

## Academic Purpose
This project is developed for academic purposes to demonstrate Django-based web application development, database handling, and role-based functionality.

---

## Conclusion
The NGO Donation and Volunteer Management System provides an efficient and scalable solution for managing NGO donations and volunteer activities. It improves coordination between NGOs and contributors while maintaining simplicity and practicality.

---


