# 🎬 MovieReview — Django Web App

A fully functional movie review website built using Django. It allows users to sign up, log in, and add, edit, or delete movie reviews. Designed with clean structure, template-based views, and user-friendly features.

---

## 🚀 Features

- 🔐 User Authentication (Signup, Login, Logout)
- 📝 Add, Edit, Delete Movie Reviews (CRUD)
- 🎥 Movie data stored in models with image support
- 🌙 Dark Mode Styling (optional)
- 🧩 Modular Django apps: `accounts`, `movie`, `news`
- 🗂️ Custom templates per app
- 🎯 Admin panel for data control

---

## 📁 Project Structure
├── accounts/         # Handles login/signup/logout
│   └── templates/    # loginaccount.html, signupaccount.html
├── movie/            # Review system and movie data
│   └── templates/    # movie-related HTML
│   └── images/       # movie posters etc.
├── moviereview/      # Project root with settings and URLs
│   └── templates/    # base.html, shared layout
│   └── static/       # CSS, JS files
├── news/             # (Optional app for news/blog if added)
├── db.sqlite3        # Default development database
└── manage.py

---

## 🛠️ Tech Stack

- **Backend:** Django (Python 3.11+)
- **Frontend:** HTML5, CSS3 (optionally dark mode)
- **Database:** SQLite (default)
- **Auth:** Django's built-in user auth system

