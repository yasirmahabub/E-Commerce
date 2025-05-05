# 🛒 E-Commerce Site Setup Guide

This guide walks you through building an e-commerce site using Python's Django framework.

---

## 🚀 Step 1: Set Up Project Folder

### 🗂️ 1.1 Create the Project Directory

1. Create a folder named `e-commerce`. This will be your main project directory.
2. Open a terminal inside the folder:
   - On **Windows**: Use Command Prompt or PowerShell.
   - On **macOS/Linux**: Use the default terminal.

```bash
mkdir e-commerce
cd e-commerce
```

This will be the root of your project. (Name it whatever you want.)

---

### 📜 1.2 Create a LICENSE File (MIT License)

**Why:**  
Adding a LICENSE shows that you allow others to use, modify, and share your code under certain conditions. For most personal, educational, or startup Django projects, the **MIT License** is ideal because it’s very permissive.

**How to add it:**

Inside the project root (`e-commerce/`), create a file named `LICENSE`.

Paste this content inside:

```plaintext
MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

👉 Replace `[Your Name]` with your real name or organization name.

---

### 🛡️ 1.3 Create a `.gitignore` File for Python/Django

**Why:**  
You don’t want to upload unnecessary files to GitHub (like virtual environment files, secret keys, database files, etc.). `.gitignore` tells Git which files to ignore.

Create a file named `.gitignore` in your project root.

Copy the content of [Python.gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore) file and paste it in your `.gitignore` file

👉 This will ignore compiled files, databases, media uploads, environment files, and IDE settings — exactly what you want.

---

### 📝 1.4 Create a README.md File

Create a simple `README.md` in the root folder to describe your project.

Example content:

```markdown
# E-Commerce Website
A simple e-commerce platform built with Django.
```

---

### 🛠️ 1.5 Initialize Git

#### ✅ Check Git Installation

Ensure Git is installed. If not, download and install it from [git-scm.com](https://git-scm.com/downloads).

#### 🔧 Initialize a Git Repository

```bash
git init
```

#### 📄 Create your first commit

Then, stage and commit the `.gitignore`, `LICENSE` and `README.md` files:

```bash
git add .gitignore LICENSE README.md
git commit -m "initial commit"
```

#### 🌐 Push to GitHub

1. Create a new repository on your GitHub account (e.g., `e-commerce`).
2. Follow GitHub’s instructions to push an existing local repo.

```bash
git remote add origin https://github.com/YOUR_USERNAME/e-commerce.git
git push -u origin master
```

> Replace `YOUR_USERNAME` with your actual GitHub username.

---

✅ After this first step, your folder structure should look like:

```plaintext
e-commerce/
    ├── .git/
    ├── .gitignore
    ├── LICENSE
    ├── README.md
```

(`.git/` is created by `git init`)

---

## ⚙️ Step 2: Create Virtual Environment + Setup Django Project

### 🐍 2.1 Set Up Python and Virtual Environment

#### 🔍 Check Python Installation

Make sure Python 3.10 or higher is installed on your system.
You can verify with:

```bash
python --version
```

#### 📦 Install `virtualenv`

If `virtualenv` is not already installed, you can install it using:

```bash
pip install virtualenv
```

#### 🧪 Create and Activate a Virtual Environment

```bash
python -m venv venv
```

> This will create a `venv` folder inside your Project folder.
> All Python dependencies will be installed inside the `venv` folder.
> This folder should be excluded from Git using `.gitignore`.

##### ▶️ Activate the Environment

- **On Windows** (PowerShell):

```powershell
Set-ExecutionPolicy Unrestricted -Scope Process
.\venv\Scripts\Activate.ps1
```

- **On macOS/Linux**:

```bash
source venv/bin/activate
```

---

### 📦 2.2 Install Django

Make sure your virtual environment is activated before proceeding.

To install Django:

```bash
pip install django==5.2
```

---

> ✅ Tip: It's a good practice to manage your project dependencies using a `requirements.txt` file. This makes it easy for others (or your future self) to install all required packages with a single command.

To generate the `requirements.txt` file:

```bash
pip freeze > requirements.txt
```

Later, you (or anyone else) can install the dependencies using:

```bash
pip install -r requirements.txt
```

---

### 🏗️ 2.3 Create a New Django Project

Create your Django project named `FastKart`:

```bash
django-admin startproject FastKart .
```

> ⚠️ **Important:** Don’t forget the `.` at the end of the command!
> This ensures the project files are created in the current folder instead of a nested one.

---

### ▶️ 2.4 Run the Development Server

Verify everything is set up correctly by starting the development server:

```bash
python manage.py runserver
```

Now, open your browser and visit:
👉 `http://127.0.0.1:8000/`

You should see the Django welcome page, which confirms your project is working!

---

## 👤 Step 3: Set Up the Users App

In this step, we'll create a dedicated Django app for managing users and define a custom user model. Using a custom user model from the start is a best practice in Django, as it allows you to easily add fields (like profile pictures, addresses, etc.) later without complex database migrations.

### 🖼️ 3.1 Install Pillow for Image Handling

Since our custom user model will include a profile_picture field (an ImageField), we need to install the Pillow library, which Django uses for image processing.

Make sure your virtual environment is activated, then run:

```bash
pip install Pillow
```

---

### ➕ 3.2 Create the Users App

Now, let's create a new Django app specifically for handling user-related functionality.

From your project root (e-commerce/, where manage.py is located), run:

```bash
python manage.py startapp users
```

This command creates a new directory named `users` with the basic app structure inside your project.

---

### ⚙️ 3.3 Register the Users App

For Django to recognize and use the new users app, you need to register it in your project's settings.

Open the `FastKart/settings.py` file and add "users" to the INSTALLED_APPS list:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "users", # Add this line
]

# ... rest of the settings
```

---

### 📝 3.4 Define the Custom User Model

Now, let's define our CustomUser model. This model will inherit from Django's built-in AbstractUser but add extra fields for email (made unique), verification status, address details, mobile number, and a profile picture.

Open the `users/models.py` file and replace its content with the following:

```python
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)

    address = models.CharField(null=True, blank=True, max_length=255)
    city = models.CharField(null=True, blank=True, max_length=30)
    postcode = models.CharField(null=True, blank=True, max_length=10)
    mobile = models.CharField(null=True, blank=True, max_length=15)
    profile_picture = models.ImageField(null=True, blank=True, upload_to="users/profile")
```

---

### 🔒 3.5 Tell Django to Use the Custom User Model

You need to tell Django to use your new CustomUser model instead of the default one.

Open `FastKart/settings.py` again and add the following line at the bottom:

```python
# ... (rest of your settings)

# Tell Django to use our custom user model
AUTH_USER_MODEL = "users.CustomUser"
```

---

### 📊 3.6 Register the Custom User Model in the Admin Site

To manage your CustomUser model through Django's admin interface, you need to register it.

Open `users/admin.py` and add the following code:

```python
from django.contrib import admin

from .models import CustomUser


admin.site.register(CustomUser)
```

---

### 🧬 3.7 Create Database Migrations

Whenever you make changes to your models (like adding a new model or adding fields to an existing one), you need to create database migrations. Migrations are Django's way of propagating changes to your database schema.

From your project root (e-commerce/), with the virtual environment activated, run:

```bash
python manage.py makemigrations
```

You should see output indicating that a new migration file was created in the users/migrations/ directory. This file contains the instructions to create the CustomUser table in the database.

---

### 💾 3.8 Apply Database Migrations

Now that the migration file is created, you need to apply it to your database. This command reads the migration file and executes the necessary SQL commands to modify your database schema.

Run the following command:

```bash
python manage.py migrate
```

This will apply the migration for your users app, as well as any pending migrations for Django's built-in apps (like auth, admin, etc.) which haven't been applied yet.

---

### 🦸 3.9 Create a Superuser

To access the Django admin site and test your custom user model, you'll need a superuser account.

Run the following command and follow the prompts to create a username, email, and password:

```bash
python manage.py createsuperuser
```

---

### ✅ 3.10 Verify in the Admin Site

Finally, let's verify that your custom user model is working correctly in the admin interface.

Start the development server:

```bash
python manage.py runserver
```

Open your browser and navigate to the admin URL:
👉 `http://127.0.0.1:8000/admin/`

Log in with the superuser credentials you just created. You should now see "Users" listed under the "USERS" section. Click on "Users" and then click on your superuser account. You should see the standard user fields along with the new custom fields you added (email, is_verified, address, city, postcode, mobile, profile_picture).

✅ After this step, your folder structure should look something like this:

```plaintext
e-commerce/
    ├── .git/
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    ├── FastKart/              # Your Django project directory
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py        # Updated with 'users' app and AUTH_USER_MODEL
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    ├── users/                 # Your new Django app directory
    │   ├── migrations/        # Contains migration files (e.g., 0001_initial.py)
    │   │   └── __init__.py
    │   ├── __init__.py
    │   ├── admin.py           # Updated to register CustomUser
    │   ├── apps.py
    │   ├── models.py          # Updated with CustomUser model
    │   ├── tests.py
    │   └── views.py
    ├── venv/                  # Your virtual environment (ignored by Git)
    └── requirements.txt       # Updated with Pillow and Django
```

---

## ✅ Step 4: Set Up User Signup Page

To allow new users to sign up, we’ll configure templates, static and media files, and create the signup form and view.

---

### 🔧 4.1 Create the Base Template and Static Files

First, set up the `templates` and `staticfiles` directories at the project root level.

**Structure:**

```plaintext
e-commerce/
    ├── templates/
    │   └── base.html
    └── staticfiles/
        ├── css/
        ├── js/
        └── images/
```

Add shared layout (e.g., navigation bar, footer) in `base.html`, and include all CSS, JS, and image files in `staticfiles`.

---

### ⚙️ 4.2 Update `settings.py` for Templates, Static and Media Files

In your `settings.py`, add the following configurations:

```python
import os

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        # ...
    }
]

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "staticfiles")]
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Media files (Uploaded by users)
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
```

This configuration does the following:

- Uses `templates/` for global HTML templates.
- Serves static files from `staticfiles/` during development and collects them into `static/` during production.
- Handles user-uploaded content through the `media/` directory. User profile image, product images etc will be stored here.

---

### 🌐 4.3 Serve Static and Media Files in `Fastkart/urls.py`

In `Fastkart/urls.py`, add static and media file serving when `DEBUG=True`:

```python
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

---

### 🚫 4.4 Exclude Static and Media Directories from Git

Add the following to your `.gitignore` file to avoid committing static and media files:

```plaintext
static/
media/
```

> The `staticfiles` and `static` directories are not the same. The `staticfiles` directory contains all your CSS and JavaScript code during development and should be committed to Git. In contrast, the `static` directory is typically used in production to serve the collected static files.

---

### 🧾 4.5 Create Signup Form in `users/forms.py`

Inside the `users` app, create a file named `forms.py` and define a registration form:

```python
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
```

This form inherits from Django’s built-in `UserCreationForm` and uses the `CustomUser` model.

---

### 🧠 4.6 Create the Signup View in `users/views.py`

Add the following logic to handle form submission and validation:

```python
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import CustomUserRegistrationForm

def user_signup(request):
    if request.method == "POST":
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # TODO: send verfication email to user
            messages.info(request, "We have sent you an verfication email")
            return redirect("signup")
        return render(request, "users/signup.html", context={"form": form})
    
    form = CustomUserRegistrationForm()
    return render(request, "users/signup.html", context={"form": form})
```

---

### 🗂 4.7 Create the Signup Template

Place the signup HTML file here:

```plaintext
users/templates/users/signup.html
```

In the template, make sure to load static files and extend `base.html`.

```django
{% extends 'base.html' %}
{% load static %}
{% block title %}Sign In{% endblock %}

{% block content %}
<!-- Write Signup Page Content Here -->
{% endblock %}
```

---

### 🌐 4.8 Add URL Patterns in `users/urls.py`

Create `users/urls.py` and register the signup view:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.user_signup, name="signup"),
]
```

Then include this in the main `urls.py`:

```python
# Fastkart/urls.py
# ...
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
]

# ...
```

---

Once the setup is complete, open your browser and go to `http://127.0.0.1:8000/users/signup/`. This URL should display the user registration form.

- Try creating a new account to ensure the registration process works as expected.
- Intentionally trigger form validation errors (e.g., leave fields empty or enter mismatched passwords) to confirm that error messages are shown correctly.
