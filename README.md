# **MovieMate — Backend (Django REST Framework)**

This is the **Django REST API backend** for MovieMate, an application for managing movies and TV shows.  
It provides authentication, CRUD operations, filtering, and progression tracking.  
The React frontend communicates with this backend using HTTP REST APIs.

---

## **Features**

### **Admin Features**
- Admin has **full CRUD** access to all admin movies and TV shows.
- Admin can run a seed script (`seed_admin_movies.py`) to insert **100+ default movies/shows**.
- Admin-managed movies/shows are stored in a separate **AdminMovies** table.
- Admin movies/shows are **read-only for normal users**.


### **User Features**
- User authentication (signup, login, get current user)
- Users can browse all admin-added movies/shows.
- Users can click **"Add to My Movies/Shows"** on an admin movie/show.
  - This creates a **separate entry** in the user's own **UserMovies** table.
  - Editing or deleting this item will **not affect the admin's original movie/show**.
- Users can create **custom movies/shows** if they cannot find them in the admin catalog.
- Users have **full CRUD permissions only** on:
  - Items they created themselves  
  - Items they added from admin list into **My Movies/Shows**
- Users **cannot update or delete** admin-managed items directly.
- Users can:
  - Edit their own movies/shows
  - Delete their own movies/shows
  - Track TV show progress (episodes watched)
  - Add rating and review (only to their own movies)
- Search and filter (genre, platform, status, type)
- CORS enabled for frontend communication

---

## **Tech Stack**
- Python  
- Django  
- Django REST Framework  
- django-filter  
- SQLite

---

## **Setup Instructions**

### **1. Clone this repository**
```bash
git clone https://github.com/orwel009/moviematebackend.git
cd moviematebackend
```

### **2. Create and activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate
```

### **3. Install dependencies**
```bash
pip install -r requirements.txt
```

### **4. Apply migrations**
```bash
python manage.py migrate
```

### **5. Admin Seeding Script (100 Movies & TV Shows)**
```bash
python manage.py seed_admin_movies
```
This script adds **100 movies and TV shows** into the database.  
This is helpful because TMDB may not work in some regions (like India) and OMDB requires a paid key.

### **6. Create superuser (optional)**
```bash
python manage.py createsuperuser
```

### **7. Start the development server**
```bash
python manage.py runserver
```

The backend will run at:

```
http://127.0.0.1:8000
```

Your frontend will not work unless this backend is running.

---

## **API Endpoints Overview**

### **Authentication**
| Method | Endpoint | Description |
|--------|----------|-------------|
| **POST** | `/auth/signup/` | Create a new user |
| **POST** | `/auth/login/` | Login and receive auth token |
| **GET**  | `/auth/me/`     | Get the currently authenticated user |

---

### **User Movies (User's Personal List)**
| Method | Endpoint | Description |
|--------|----------|-------------|
| **GET**    | `/movies/`           | List all movies/TV shows added by the user |
| **POST**   | `/movies/`           | Create/add a custom movie or show to the user's list |
| **GET**    | `/movies/<id>/`      | Retrieve a movie/show from the user's list |
| **PATCH**  | `/movies/<id>/`      | Update user's movie/show (rating, progress, status, etc.) |
| **DELETE** | `/movies/<id>/`      | Delete a movie/show from the user's list |

---

### **Admin Movies (Read-only for Users)**
| Method | Endpoint | Description |
|--------|----------|-------------|
| **GET** | `/admin-movies/`      | List all admin-added movies/TV shows |
| **GET** | `/admin-movies/<id>/` | Retrieve details of an admin movie/show |

---

### **Add Admin Movie to User's List**
| Method | Endpoint | Description |
|--------|----------|-------------|
| **POST** | `/movies/from-admin/<pk>/` | Add an admin movie/show into the user's personal movie list |

---

### **Filtering & Search**
Supported query parameters for `/api/movies/`:
```
?genre=
?platform=
?status=
?type=
?search=
?ordering=
```

---

## **CORS Configuration**

Make sure the following exist in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    "corsheaders",
    "rest_framework",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    ...
]

CORS_ALLOW_ALL_ORIGINS = True
```

---

## **Project Structure**
```
backend/
  api/
    models.py
    serializers.py
    views.py
    urls.py
  moviematebackend/
    settings.py
    urls.py
  manage/command/seed_admin_movies.py
  manage.py
```

---

## **Frontend Requirement**

To use the frontend, clone and follow the setup instructions from:

https://github.com/orwel009/movie-mate-frontend.git

The frontend expects this backend to be running at:

```
http://localhost:8000
```

(Or update the frontend `.env` accordingly.)

---

## **Author**
**ORWEL P V**