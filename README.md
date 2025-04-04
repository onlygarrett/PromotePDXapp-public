# PromotePDX App

A modern web application for [PromotePDX.com](https://PromotePDX.com), designed to replace the existing WordPress site and enhance the digital presence of PromotePDX.

## 🚀 Features

- **Dynamic Event Calendar**: Aggregates event data from Portland venues, allowing users to explore upcoming events and navigate to venue sites for tickets.
- **Contact Page**: Provides a direct communication channel for users to reach out to PromotePDX staff.
- **About Page**: Details the mission, services, and team behind PromotePDX.
- **Newsletter Service**: Enables users to subscribe to email updates.
- **Home Page**: Showcases key offerings and latest updates.

---

## 📦 Tech Stack

### Backend
- **Python** (Django)
- **PostgreSQL**
- **Celery + Redis** (for asynchronous tasks)
- **Docker** (Containerized development & deployment)

### Frontend
- **React** (JavaScript-based frontend)
- **Node.js + npm** (Package management)

### Deployment
- **Docker Compose**
- **Nginx** (Reverse proxy)
- **DigitalOcean** (Hosting)

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-repo/PromotePDXApp.git
cd PromotePDXApp
```

### 2️⃣ Set Up Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3️⃣ Install Backend Dependencies
```sh
pip install -r backend/requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env.dev` file in the root directory with the following configuration:

```ini
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
DEBUG=True
SECRET_KEY="your-secret-key"
DATABASE_URL=postgres://POSTGRES_USER:POSTGRES_PASSWORD@db:5432/POSTGRES_DB

POSTGRES_DB=your_db
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password

DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=admin_password
DJANGO_SUPERUSER_EMAIL=admin@admin.com

POSTGRES_HOST_AUTH_METHOD=trust
REACT_APP_API_URL=http://127.0.0.1:3000/api
```

### 5️⃣ Start the Application
```sh
docker compose up --build
```
Verify that all three containers (**backend, frontend, database**) are running.

### 6️⃣ Access the Application
- **Django Admin Panel**: [http://localhost:8000/admin](http://localhost:8000/admin)  
- **React Frontend**: [http://localhost:3000](http://localhost:3000)

---

## ✅ Project Milestones

- [x] Setup Django and Docker environment  
- [x] Implement admin panel  
- [x] Develop core pages (Home, About, Contact)  
- [x] Integrate Event Calendar system  
- [x] Implement Newsletter functionality  
- [x] Configure logging and error handling  
- [x] Finalize testing & bug fixes  
- [x] Prepare for production deployment  
- [x] Deploy application  
- [x] Complete project handoff  

---

## 🔧 Deployment Checklist

- [ ] Purchase DigitalOcean droplet  
- [ ] Obtain Instagram business account credentials  
- [ ] Configure Google Sheets API credentials  
- [ ] Set up superuser credentials  
- [ ] Register email for newsletters  
- [ ] Sign up for **EmailJS**  
- [ ] Secure & reserve domain URL  

---

## 📝 Additional Information

### .env.dev Configuration
Ensure you create a `.env.dev` file in the root directory for local development with the necessary environment variables.

### Local Development Setup (WIP)
1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install backend dependencies.
4. Run `docker compose up --build` to start the containers.
5. Access the Django admin panel at `http://localhost:8000/admin`.
6. Access the frontend at `http://localhost:3000`.

---

## 📄 License

This project is licensed under the **MIT License**.
