# Django Voting System

A secure and user-friendly voting system built with Django. This project allows users to register, log in, and cast their votes for leaders. Admins can manage leaders and view voting results.

## Features

- **User Authentication:**
  - Secure registration and login.
  - Password validation and error messages for better UX.

- **Voting Functionality:**
  - Users can cast votes for listed leaders.
  - Prevents duplicate voting by marking voters who have already voted.
  
- **Leader Management:**
  - Display leader details dynamically from the database.
  
- **User-Friendly Interface:**
  - Bootstrap integration for a clean and responsive design.

## Screenshots

| Page          | Description                              |
|---------------|------------------------------------------|
| **Home**      | Login page for users to authenticate.   |
| **Register**  | Registration page for new users.        |
| **Vote**      | Voting page displaying leaders and vote options. |
| **Thank You** | Message displayed after a successful vote. |

## Tech Stack

- **Backend:** Django
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default for Django)
- **Language:** Python

## Installation and Setup

Follow the steps below to set up the project locally.

### 1. Clone the Repository

First, clone the project repository to your local machine:

```bash
git clone https://github.com/your-username/django-voting-system.git
cd django-voting-system
```
2. Create a Virtual Environment
Next, create a Python virtual environment to isolate dependencies:
```bash
python -m venv venv
```
3.Apply Migrations
Run the Django migrations to set up your database:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
4.Access the Application
Open your browser and navigate to http://127.0.0.1:8000

## FILE STRUCTURE
django-voting-system

├── voting               
│   ├── migrations/     
│   ├── templates/          
│   ├── views.py           
│   ├── models.py        
│   ├── urls.py            
│   └── ...
├── db.sqlite3              
├── manage.py              
├── mydb.py 
└── README.md     



### Key Elements:
1. **Tech Stack**: Provides an overview of the tools and technologies used.
2. **Installation**: Step-by-step instructions for installing and setting up the project.
3. **Usage**: A brief guide on how to use the system (register, login, vote).
4. **File Structure**: Shows the directory structure of the project.
