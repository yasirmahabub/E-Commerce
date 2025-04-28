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
