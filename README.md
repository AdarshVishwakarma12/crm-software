# Customer Relationship Management Software – CRM

**CRM software built with Django to organize contacts, tasks, documents, and user roles efficiently.**

## Overview

This project provides core features of a customer relationship management system, including contact management, task tracking, document storage, and multi-user access. It is designed for individuals and small teams who need an easy-to-use tool without the overhead of complex enterprise solutions.

## Key Features

- **User Authentication**  
  Register, login, logout, and Google OAuth integration.

- **Dashboard Overview**  
  Centralized view of total contacts, tasks, documents, and recent activity.

- **Contact Management**  
  Organize clients by project, view detailed info, and manage soft-delete/restore.

- **Task Management**  
  Create and track tasks with priorities, status updates, and related entities.

- **Document Storage**  
  Upload and manage files linked to contacts or projects, with restore support.

- **Role-Based Access Control**  
  Assign granular permissions (read/write/delete) to users across the app.

- **Multi-User Account Switching**  
  Switch between personal and shared accounts for collaborative workspaces.

- **Activity Tracking**  
  Automatic logging of recent actions for historical context.

- **Theme Support**  
  Light, dark, and system themes with persistent local storage.

- **Trash System**  
  Soft-delete logic for reversible deletion of tasks, contacts, and documents.

- **Feedback Submission**  
  Built-in form for sending issues, or suggestions.

## Tech Stack

- **Backend:** Django
- **Frontend:** HTML/CSS (Django templating)
- **Database:** SQLite (default, can be switched)
- **Hosting:** PythonAnywhere (demo)

## Live Demo

[Live Application](https://ctrlcrm.pythonanywhere.com)

## Running from Source
Follow these steps to run the project on your local machine:

1. Clone the repository:
   ```bash
   git clone https://github.com/AdarshVishwakarma12/crm-software.git
   ```

2. Navigate to the project directory:
   ```bash
   cd crm-software
   ```

3. Start the Docker service on your machine.

4. Build and run the Docker containers:
   ```bash
   docker-compose up -d --build
   ```

5. Open your browser and navigate to:
   ```
   http://localhost:8000
   ```

6. Bingo! The application is now running locally.

## Running via Docker Image (Recommended)
Follow these steps to run the project on your local machine:

1. Make sure Docker is installed and running

2. Pull the latest image
   ```bash
   docker pull ghcr.io/adarshvishwakarma12/crm-software:latest
   ```

3. Run the container
   ```bash
   docker run -p 8000:8000 ghcr.io/adarshvishwakarma12/crm-software:latest
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:8000
   ```

You should now see the CRM application running.

## Environment Variables

The app uses environment variables for email configuration (send-feedback section).

In `docker-compose.yml` / `Dockerfile`, placeholder values are provided for development:

```yaml
EMAIL_HOST_USER=none@gmail.com
EMAIL_HOST_PASSWORD=None
```

These are **not real credentials**. To use actual email features, replace them with valid SMTP credentials.

## Disclaimer

> This project is actively being improved and is intended for educational or small-scale personal use. While fully functional, it may lack the scalability and advanced features found in commercial CRM systems.
