# 📚 BookWyrm | Advanced Django Library System

A high-performance, containerized personal library and review management system built with **Django 6.0**, **PostgreSQL**, and **Docker**. This project is designed for scalability and follows modern DevOps practices.

---

## 🛠 Project Architecture & Tech Stack

- **Backend:** Python 3.14 (Bleeding Edge) / Django 6.0
- **Database:** PostgreSQL 16 (Relational Data Storage)
- **Containerization:** Docker & Docker Compose (Multi-container setup)
- **Frontend:** Tailwind CSS (Currently via CDN for rapid development)
- **Env Management:** Python-dotenv for secure configuration

---

## 🐳 Docker Infrastructure

The project runs in a multi-service environment:
1. **Web Service:** The Django application running on a Python 3.14-slim image.
2. **DB Service:** A dedicated PostgreSQL instance with persistent data volumes.

### The Entrypoint Magic
The project uses an \`entrypoint.sh\` script which:
- Waits for the PostgreSQL service to be healthy.
- Automatically applies database migrations.
- Collects static files for production readiness.

---

## 🚀 Quick Start

### 1. Environment Configuration
Create a \`.env\` file in the root directory to manage sensitive data:
\`\`\`env
DEBUG=1
SECRET_KEY=generate-your-own-secure-key
DB_NAME=bookwyrm
DB_USER=admin
DB_PASSWORD=yoursecurepassword
DB_HOST=db
DB_PORT=5432
\`\`\`

### 2. Launch the Environment
Build and start the containers with a single command:
\`\`\`bash
docker-compose up --build
\`\`\`
- **Web App:** http://localhost:8000
- **Admin Panel:** http://localhost:8000/admin/

### 3. Create Admin Access
While the containers are running, create a superuser:
\`\`\`bash
docker-compose exec web python manage.py createsuperuser
\`\`\`

---

## 📅 Roadmap & Future Enhancements

### 🔹 1. Professional Asset Management
Transition from **Tailwind CDN** to a **Local Build Process**:
- Implement a Multi-stage Docker build to include Node.js.
- Use \`npx tailwindcss\` to compile a minified \`dist.css\`.
- Remove the CDN overhead for better performance and offline support.

### 🔹 2. Automated Testing
- Implement **Pytest-django** for unit and integration testing.
- Achieve >80% code coverage for models and views.

### 🔹 3. CI/CD Pipeline (GitHub Actions)
Setup \`.github/workflows/main.yml\` to:
- Automatically run tests on every Push or Pull Request.
- Lint code with **Flake8** or **Black**.
- Build the Docker image to ensure no breaking changes are merged.

### 🔹 4. Deployment
- Ready for deployment on **DigitalOcean**, **AWS**, or **Hetzner** using Docker Swarm or Kubernetes.

---

## 📂 Project Structure
- \`/books\` - Core logic, models (Book, Review, Genre), and CBVs.
- \`/templates\` - Custom HTML structured with Tailwind utility classes.
- \`docker-compose.yml\` - Orchestration for Web and DB services.
- \`.env\` - (Ignored) Sensitive environment variables.

---

## Contributions are welcome!

**Author:** [https://github.com/snushev]
