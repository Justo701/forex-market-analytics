Forex Market Analytics & Trading Signal System

A backend-focused data analytics platform built with Python, Flask, SQL, Docker, and cloud infrastructure.

The project demonstrates the development of a modular backend system, from database queries and SQL analytics to REST APIs, application architecture, containerization, and cloud deployment.

---

Technology Stack

Backend

- Python
- Flask
- Flask Application Factory
- Flask Blueprints
- REST API
- Service Layer
- Repository Layer
- Centralized Error Handling

Database & SQL

- MariaDB
- MySQL
- SQL
- Common Table Expressions (CTEs)
- Window Functions
- "LAG()" / "LEAD()"
- Aggregations
- JOINs
- Time-series queries

DevOps & Deployment

- Git
- GitHub
- Docker
- Render
- Aiven MySQL
- Environment Variables

---

System Flow

The backend follows a layered request flow:

                    CLIENT
                      │
                      │ HTTP Request
                      ▼
              FLASK APPLICATION
                      │
                      ▼
             APPLICATION FACTORY
                      │
                      ▼
                  BLUEPRINT
                      │
                      ▼
                    ROUTE
                      │
                      ▼
                  SERVICE
                      │
                      ▼
                REPOSITORY
                      │
                      ▼
                 DATABASE
                      │
                      ▼
              SQL / DATA ANALYSIS
                      │
                      ▼
                REPOSITORY
                      │
                      ▼
                  SERVICE
                      │
                      ▼
                   ROUTE
                      │
                      ▼
               JSON RESPONSE
                      │
                      ▼
                    CLIENT

This separation keeps HTTP handling, application logic, database access, and data storage from being tightly coupled.

---

Backend Architecture

The project is structured as a modular Flask monolith.

backend/
│
├── app.py
│
├── routes/
│   └── market_routes.py
│
└── errors/
    ├── __init__.py
    └── handlers.py

The architecture is designed around:

Application
     │
     ├── Routes
     │
     ├── Services
     │
     ├── Repositories
     │
     ├── Error Handling
     │
     └── Database

The objective is high cohesion and low coupling.

---

Application Factory

The Flask application uses the Application Factory pattern.

Location:

backend/app.py

Main function:

create_app()

The factory is responsible for creating and configuring the Flask application and registering the required components.

Conceptually:

create_app()
     │
     ├── Create Flask App
     ├── Load Configuration
     ├── Register Blueprints
     ├── Register Error Handlers
     └── Return App

This makes the application easier to configure, test, and extend.

---

Flask Blueprint

Market API routes are organized in:

backend/routes/market_routes.py

Instead of keeping all routes inside "app.py", the Blueprint provides a separate module for market-related endpoints.

Current endpoints include:

/api/status
/api/prices
/api/movements
/api/crossovers
/api/support-resistance
/api/trends
/api/momentum
/api/advanced-volatility
/api/risk-classification
/api/multi-pair-comparison
/api/sma-ema
/api/rsi
/api/macd
/api/bollinger-bands
/api/atr
/api/indicator-combinations

---

SQL Technology

SQL is a major part of the project.

The database layer is used not only for storing data but also for performing analytical operations.

The project uses:

SQL
 ├── SELECT
 ├── WHERE
 ├── GROUP BY
 ├── HAVING
 ├── JOIN
 ├── EXISTS
 ├── CTE
 ├── Window Functions
 ├── LAG
 ├── LEAD
 └── Time-Series Analysis

---

Common Table Expressions

CTEs are used to break complex queries into logical steps.

WITH analysis AS (
    SELECT ...
)
SELECT *
FROM analysis;

Conceptually:

Database Data
      ↓
     CTE
      ↓
Intermediate Result
      ↓
Final Query

---

Window Functions

Window functions allow calculations across related rows while keeping individual records.

Examples include:

OVER()

PARTITION BY

ORDER BY

They are particularly useful for sequential and time-based data.

---

LAG and LEAD

"LAG()" accesses a previous record.

LAG(close_price) OVER (
    PARTITION BY currency_pair
    ORDER BY timestamp
)

"LEAD()" accesses a following record.

These functions allow the backend to perform sequential comparisons directly in SQL.

---

Data Processing Flow

The data-analysis flow is:

Database
   │
   ▼
SQL Query
   │
   ├── Filtering
   ├── Aggregation
   ├── CTE
   ├── Window Functions
   └── Time-Series Analysis
   │
   ▼
Processed Data
   │
   ▼
Service Layer
   │
   ▼
REST API
   │
   ▼
JSON Response

This keeps analytical processing close to the database while allowing the Flask application to expose the results through APIs.

---

Separation of Responsibilities

Each layer has a specific responsibility.

Route
  │
  └── HTTP request/response

Service
  │
  └── Application/business logic

Repository
  │
  └── Database operations

Database
  │
  └── Persistent data

This structure makes the application easier to understand, test, modify, and maintain.

---

Error Handling

Centralized error handling is currently being implemented.

Current structure:

backend/errors/
├── __init__.py
└── handlers.py

The intended flow is:

Error
  ↓
Flask Error Handler
  ↓
Standardized Response
  ↓
JSON
  ↓
Client

The goal is to provide consistent API error responses instead of implementing separate error handling inside every route.

---

Docker

The backend is containerized using Docker.

Dockerfile
     ↓
Python Environment
     ↓
Application Dependencies
     ↓
Flask Application
     ↓
Container

Docker provides a consistent environment between development and deployment.

---

Deployment Architecture

The current deployment flow is:

Developer
    │
    ▼
Git
    │
    ▼
GitHub
    │
    ▼
Render
    │
    ▼
Docker Container
    │
    ▼
Flask Backend
    │
    ▼
Aiven MySQL

Database credentials and other environment-specific configuration are supplied through environment variables.

---

Git Workflow

Development follows the standard Git workflow:

Make Changes
     ↓
git status
     ↓
git add
     ↓
git commit
     ↓
git push
     ↓
GitHub

Example:

git status
git add .
git commit -m "Describe the change"
git push origin master

---

Project Structure

forex-market-analytics/
│
├── backend/
│   ├── app.py
│   │
│   ├── routes/
│   │   └── market_routes.py
│   │
│   └── errors/
│       ├── __init__.py
│       └── handlers.py
│
├── database/
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore

The structure will expand as additional service, repository, testing, and processing components are implemented.

---

Development Status

Completed

- Git/GitHub project setup
- Database development
- SQL analytics
- Flask REST API
- Application Factory
- Flask Blueprint architecture
- Market API routes
- Docker configuration
- Render deployment
- Aiven MySQL integration

Current

Centralized error handling

backend/errors/handlers.py

Planned

- Complete Service Layer
- Repository Layer improvements
- API validation
- Automated testing
- Advanced SQL analytics
- Data ingestion pipeline
- Background processing
- Real-time processing
- WebSockets
- Dashboard/API integration
- Monitoring and logging
- Performance optimization

---

Technology Flow

The overall project can be summarized as:

                GITHUB
                   │
                   ▼
                DOCKER
                   │
                   ▼
             FLASK BACKEND
                   │
          ┌────────┴────────┐
          ▼                 ▼
       ROUTES            ERRORS
          │
          ▼
       SERVICES
          │
          ▼
     REPOSITORIES
          │
          ▼
      MYSQL / MARIADB
          │
          ▼
         SQL
          │
    ┌─────┼─────┐
    ▼     ▼     ▼
   CTE   WINDOW LAG/LEAD
    │     │     │
    └─────┼─────┘
          ▼
    DATA ANALYSIS
          │
          ▼
       REST API
          │
          ▼
        CLIENT

---

Project Goal

The primary goal is to demonstrate practical backend engineering skills by building a complete data-driven application using:

Python + Flask + SQL + REST APIs + Software Architecture + Docker + Git/GitHub + Cloud Deployment

The project is being developed incrementally, with emphasis on understanding the technology and architecture behind each component rather than simply assembling the final application.
