Forex Market Analytics & Trading Signal System

A backend-focused Forex market analytics platform built with Python, Flask, SQL, MariaDB/MySQL, Docker, and cloud deployment technologies.

The project is being developed progressively from database and SQL fundamentals toward advanced market analytics, technical indicators, trading signals, backtesting, real-time processing, visualization, and production deployment.

---

Table of Contents

- "1. Project Overview" (#1-project-overview)
- "2. Project Purpose" (#2-project-purpose)
- "3. Project Goals" (#3-project-goals)
- "4. Development Philosophy" (#4-development-philosophy)
- "5. Technology Stack" (#5-technology-stack)
- "6. Repository" (#6-repository)
- "7. Project Architecture" (#7-project-architecture)
- "8. Backend Architecture" (#8-backend-architecture)
- "9. Application Factory" (#9-application-factory)
- "10. Flask Blueprints" (#10-flask-blueprints)
- "11. Market API Endpoints" (#11-market-api-endpoints)
- "12. Service and Repository Architecture" (#12-service-and-repository-architecture)
- "13. Database Architecture" (#13-database-architecture)
- "14. SQL Concepts Used" (#14-sql-concepts-used)
- "15. Common Table Expressions" (#15-common-table-expressions)
- "16. Window Functions" (#16-window-functions)
- "17. LAG and LEAD" (#17-lag-and-lead)
- "18. Time-Series Analysis" (#18-time-series-analysis)
- "19. Technical Indicators" (#19-technical-indicators)
- "20. Trading Signals" (#20-trading-signals)
- "21. Backtesting" (#21-backtesting)
- "22. API Request Flow" (#22-api-request-flow)
- "23. Centralized Error Handling" (#23-centralized-error-handling)
- "24. Separation of Concerns" (#24-separation-of-concerns)
- "25. High Cohesion and Low Coupling" (#25-high-cohesion-and-low-coupling)
- "26. Modular Monolith" (#26-modular-monolith)
- "27. Git and GitHub Workflow" (#27-git-and-github-workflow)
- "28. Docker" (#28-docker)
- "29. Deployment Architecture" (#29-deployment-architecture)
- "30. Environment Variables and Security" (#30-environment-variables-and-security)
- "31. Local Development" (#31-local-development)
- "32. Project Structure" (#32-project-structure)
- "33. Completed Work" (#33-completed-work)
- "34. Current Development Stage" (#34-current-development-stage)
- "35. Roadmap" (#35-roadmap)
- "36. Revision Notes" (#36-revision-notes)
- "37. Interview Explanation" (#37-interview-explanation)
- "38. Important Lessons" (#38-important-lessons)
- "39. Known Limitations" (#39-known-limitations)
- "40. Future Improvements" (#40-future-improvements)
- "41. Final Project Summary" (#41-final-project-summary)

---

1. Project Overview

The Forex Market Analytics & Trading Signal System is a portfolio project focused on foreign-exchange market data, database analysis, technical indicators, trading signals, and backend engineering.

The project combines:

- Python
- Flask
- MariaDB
- MySQL
- SQL
- Docker
- Git
- GitHub
- Render
- Aiven MySQL
- Technical indicators
- REST-style API development
- Time-series analysis
- Software architecture
- Software engineering principles

The project is being developed incrementally so that each component is understood, tested, documented, and integrated before moving to the next stage.

---

2. Project Purpose

The purpose of this project is to build a serious, practical software system around Forex market data while simultaneously developing skills in:

- Database design
- Advanced SQL
- Backend development
- API development
- Data analysis
- Software architecture
- Git and version control
- Docker
- Cloud deployment
- Technical indicators
- Time-series processing
- Testing and debugging
- Software engineering

The project is also being used as a practical learning environment for concepts studied in Computer Science and Software Engineering.

---

3. Project Goals

The long-term project goals are to build a system capable of:

1. Storing Forex market data.
2. Querying and analyzing market data using SQL.
3. Performing time-series analysis.
4. Calculating technical indicators.
5. Generating rule-based trading signals.
6. Comparing different market conditions.
7. Performing historical backtesting.
8. Supporting real-time or near-real-time analysis.
9. Exposing analytics through APIs.
10. Providing useful visualizations.
11. Running inside Docker.
12. Deploying the backend to the cloud.
13. Maintaining a modular and maintainable codebase.

The project is intentionally being developed in stages rather than implementing all features simultaneously.

---

4. Development Philosophy

The project follows a bottom-up, step-by-step development approach.

The general development progression is:

Database
    |
    v
SQL Fundamentals
    |
    v
Advanced SQL
    |
    v
Forex Data Analysis
    |
    v
Technical Indicators
    |
    v
Trading Signals
    |
    v
Flask Backend
    |
    v
Backend Refactoring
    |
    v
Error Handling
    |
    v
Docker
    |
    v
Cloud Deployment
    |
    v
Backtesting
    |
    v
Real-Time Processing
    |
    v
Visualization

The project is also used to practically apply software-engineering principles such as:

- Separation of concerns
- Modularity
- High cohesion
- Low coupling
- Refactoring
- Maintainability
- Layered architecture
- Application architecture
- Error handling

---

5. Technology Stack

Programming Language

Python

Python is used for:

- Backend development
- Data processing
- Market analytics
- Technical-indicator calculations
- API development

---

Backend Framework

Flask

Flask provides:

- HTTP routing
- API endpoints
- Application configuration
- Request handling
- Response handling
- Error handling

---

Database

Local Development

MariaDB

Production

MySQL

The production MySQL database is hosted through Aiven.

---

Containerization

Docker

Docker provides a consistent runtime environment for the backend.

---

Version Control

Git
GitHub

Git tracks changes locally while GitHub provides the remote repository.

---

Cloud Deployment

Render

Render is used to deploy the containerized Flask backend.

---

Production Database Hosting

Aiven MySQL

Aiven provides the production MySQL database used by the deployed application.

---

6. Repository

GitHub repository:

Justo701/forex-market-analytics

Default branch:

master

The repository contains the source code, database-related work, backend implementation, Docker configuration, and project documentation.

---

7. Project Architecture

The high-level system can be represented as:

                 FOREX MARKET DATA
                         |
                         v
                    DATABASE
                         |
                         v
                       SQL
                         |
                         v
                 MARKET ANALYTICS
                         |
          +--------------+--------------+
          |              |              |
          v              v              v
         SMA            RSI            MACD
          |              |              |
          +--------------+--------------+
                         |
                         v
                  TRADING RULES
                         |
                         v
                   SIGNALS
                         |
                         v
                    FLASK API
                         |
                         v
                      CLIENT

The backend architecture is:

Client
   |
   v
Flask Application
   |
   v
Application Factory
   |
   v
Blueprint
   |
   v
Route
   |
   v
Service
   |
   v
Repository
   |
   v
MariaDB / MySQL

The service and repository layers represent the intended separation of application logic from database access.

---

8. Backend Architecture

The Flask backend was refactored from a route-heavy application into a more modular Flask application.

The major architectural components are:

backend/
|
+-- app.py
|
+-- routes/
|     |
|     +-- market_routes.py
|
+-- errors/
      |
      +-- __init__.py
      |
      +-- handlers.py

The main architectural milestone completed so far is the migration toward:

Application Factory
        +
Flask Blueprint
        +
Modular Routes

---

9. Application Factory

The Application Factory is implemented in:

backend/app.py

The factory function is:

create_app()

What is an Application Factory?

An Application Factory is a function that creates and configures the Flask application.

Conceptually:

create_app()
     |
     v
Flask Application

Instead of placing all application configuration and functionality into one global application object, the application is created through a function.

---

Why Use an Application Factory?

An application factory helps with:

- Organization
- Configuration
- Testing
- Maintainability
- Application initialization
- Modular development

It also allows application creation to remain separate from individual feature modules.

---

Conceptual Flow

create_app()
     |
     +--> Create Flask application
     |
     +--> Configure application
     |
     +--> Register Blueprints
     |
     +--> Register error handlers
     |
     v
Configured Flask application

---

10. Flask Blueprints

Market-related routes were moved into:

backend/routes/market_routes.py

A Flask Blueprint allows related routes to be grouped into a separate module.

Instead of keeping many market endpoints directly inside:

backend/app.py

they are organized in:

backend/routes/market_routes.py

This separates application creation from market-specific route definitions.

---

Why Use a Blueprint?

Blueprints help with:

- Organization
- Modularity
- Maintainability
- Separation of concerns
- Grouping related routes

Conceptually:

Market Blueprint
       |
       +-- /api/prices
       +-- /api/rsi
       +-- /api/macd
       +-- /api/atr
       +-- /api/momentum
       +-- ...

---

Blueprint Migration

The Blueprint migration was recorded in Git with:

Commit: d910a83

Commit message:

Complete market routes blueprint migration

This represents an important backend refactoring milestone.

---

11. Market API Endpoints

The market Blueprint currently contains endpoints for different areas of market analysis.

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

Endpoint Categories

General Market Information

/api/status
/api/prices
/api/movements

These endpoints are related to general market data and application status.

---

Market Analysis

/api/crossovers
/api/support-resistance
/api/trends
/api/momentum
/api/advanced-volatility
/api/risk-classification
/api/multi-pair-comparison

These endpoints represent different analytical operations.

---

Technical Indicators

/api/sma-ema
/api/rsi
/api/macd
/api/bollinger-bands
/api/atr
/api/indicator-combinations

These endpoints expose technical-indicator functionality.

---

12. Service and Repository Architecture

The intended request flow separates HTTP handling, application logic, and database access.

Route
  |
  v
Service
  |
  v
Repository
  |
  v
Database

---

Route

The route is responsible primarily for HTTP-level operations.

Examples include:

- Receiving requests
- Reading request parameters
- Calling application logic
- Returning responses

---

Service

The service layer is responsible for application or business logic.

For example:

Route
  |
  v
Market Service
  |
  +--> calculate/process data
  |
  +--> apply rules
  |
  +--> prepare result

---

Repository

The repository layer is responsible for database access.

Conceptually:

Service
   |
   v
Repository
   |
   v
SQL
   |
   v
Database

This keeps database-specific operations separate from higher-level application logic.

---

13. Database Architecture

The project uses relational databases.

Local development has used:

MariaDB

The deployed application uses:

Aiven MySQL

The conceptual architecture is:

Flask
  |
  v
Repository
  |
  | SQL
  v
MySQL / MariaDB
  |
  v
Tables
  |
  v
Rows and Columns

---

Why a Relational Database?

Forex data is structured and naturally represented using tables.

For example:

prices

+----+------------+--------+--------+--------+--------+
| id | date       | pair   | open   | high   | close  |
+----+------------+--------+--------+--------+--------+
| 1  | 2026-01-01 | EURUSD | 1.1000 | 1.1200 | 1.1100 |
| 2  | 2026-01-02 | EURUSD | 1.1100 | 1.1300 | 1.1200 |
+----+------------+--------+--------+--------+--------+

The exact production schema should always be considered authoritative from the database implementation itself.

---

14. SQL Concepts Used

SQL is a major part of the project.

The project progresses from basic queries toward advanced analytical SQL.

Important concepts include:

- SELECT
- WHERE
- ORDER BY
- GROUP BY
- HAVING
- Aggregate functions
- JOIN
- EXISTS
- Common Table Expressions
- Window functions
- LAG
- LEAD
- Moving calculations
- Time-series analysis

---

SELECT

"SELECT" retrieves information from a table.

Example:

SELECT *
FROM prices;

Specific columns can also be selected:

SELECT trading_date, close_price
FROM prices;

---

WHERE

"WHERE" filters rows.

Example:

SELECT *
FROM prices
WHERE currency_pair = 'EURUSD';

The database returns rows matching the condition.

---

ORDER BY

"ORDER BY" controls the ordering of the result.

Example:

SELECT *
FROM prices
ORDER BY trading_date;

For time-series data, ordering by date/time is particularly important.

---

GROUP BY

"GROUP BY" creates groups of rows with matching values.

Example:

SELECT
    currency_pair,
    AVG(close_price) AS average_price
FROM prices
GROUP BY currency_pair;

---

HAVING

"HAVING" filters groups after aggregation.

A useful distinction is:

WHERE
    |
    +--> filters rows

HAVING
    |
    +--> filters groups

---

Aggregate Functions

Common aggregate functions include:

COUNT()
SUM()
AVG()
MIN()
MAX()

Example:

SELECT AVG(close_price)
FROM prices;

---

JOIN

A "JOIN" combines related information from multiple tables.

Conceptually:

Table A
   |
   | JOIN
   v
Table B

JOINs are useful when related information is stored in separate tables.

---

EXISTS

"EXISTS" checks whether a related query returns at least one row.

Conceptually:

Does a matching record exist?
        |
     +--+--+
     |     |
    YES    NO

It is useful when the purpose is to test existence rather than retrieve all matching records.

---

15. Common Table Expressions

A Common Table Expression is commonly abbreviated as:

CTE

A CTE creates a named intermediate result inside a SQL query.

Basic structure:

WITH result AS (
    SELECT ...
)
SELECT *
FROM result;

---

Why Use CTEs?

CTEs can make complicated SQL easier to understand.

Instead of writing one large nested query, the query can be broken into logical stages.

Example:

WITH daily_data AS (
    SELECT
        trading_date,
        AVG(close_price) AS average_price
    FROM prices
    GROUP BY trading_date
)
SELECT *
FROM daily_data;

Conceptually:

Raw Data
   |
   v
CTE
   |
   v
Intermediate Result
   |
   v
Final Query

---

16. Window Functions

Window functions perform calculations across related rows while preserving individual rows in the result.

Example:

SELECT
    trading_date,
    close_price,
    AVG(close_price) OVER (
        ORDER BY trading_date
    ) AS running_average
FROM prices;

---

GROUP BY vs Window Function

A useful mental model is:

GROUP BY

Many rows
    |
    v
Grouped result

while:

Window Function

Many rows
    |
    v
Calculation across rows
    |
    v
Individual rows remain visible

This makes window functions especially useful for time-series analysis.

---

17. LAG and LEAD

"LAG()" and "LEAD()" are particularly important for time-series data.

---

LAG

"LAG()" looks at a previous row.

Example:

SELECT
    trading_date,
    close_price,
    LAG(close_price) OVER (
        ORDER BY trading_date
    ) AS previous_price
FROM prices;

Conceptually:

Previous row
     |
     v
Current row

Remember:

LAG = look backward

---

LEAD

"LEAD()" looks at a following row.

Example:

SELECT
    trading_date,
    close_price,
    LEAD(close_price) OVER (
        ORDER BY trading_date
    ) AS next_price
FROM prices;

Conceptually:

Current row
     |
     v
Next row

Remember:

LEAD = look forward

---

18. Time-Series Analysis

Forex data is time-series data because observations occur in chronological order.

For example:

09:00 -> 1.1000
10:00 -> 1.1020
11:00 -> 1.1050
12:00 -> 1.1030
13:00 -> 1.1080

The order of the observations matters.

This makes the following SQL capabilities particularly useful:

ORDER BY
Window Functions
LAG()
LEAD()
Moving calculations
CTEs

---

19. Technical Indicators

The project includes technical-indicator functionality for:

- SMA
- EMA
- RSI
- MACD
- Bollinger Bands
- ATR
- Indicator combinations

These indicators transform raw market-price information into analytical measurements.

---

20. Simple Moving Average — SMA

SMA means:

«Simple Moving Average»

A moving average calculates the average of a specified number of recent observations.

For example:

10
12
14
16
18

A 5-period SMA is:

(10 + 12 + 14 + 16 + 18) / 5

Result:

14

The window then moves forward through the time series.

Conceptually:

10 12 14 16 18 20 22
---------------------
[10 12 14]
   [12 14 16]
      [14 16 18]
         [16 18 20]

---

21. Exponential Moving Average — EMA

EMA means:

«Exponential Moving Average»

EMA is another type of moving average.

The important conceptual difference is:

SMA
 |
 +--> treats observations more evenly

while:

EMA
 |
 +--> gives greater weight to recent observations

Therefore EMA can respond more quickly to recent changes.

---

22. Relative Strength Index — RSI

RSI means:

«Relative Strength Index»

RSI is a momentum indicator.

It analyzes recent upward and downward price movements to produce a momentum measurement.

Conceptually:

Price Data
    |
    v
RSI Calculation
    |
    v
Momentum Measurement

Endpoint:

/api/rsi

---

23. Moving Average Convergence Divergence — MACD

MACD means:

«Moving Average Convergence Divergence»

MACD uses moving averages to analyze changes in momentum and trend.

Conceptually:

Price Data
    |
    +------> Fast EMA
    |
    +------> Slow EMA
                |
                v
              MACD

Endpoint:

/api/macd

---

24. Bollinger Bands

Bollinger Bands combine a moving average with a measure of price variability.

Conceptually:

Upper Band
--------------------

Middle Band
--------------------

Lower Band
--------------------

They can be used to study price movement relative to a recent average and variability.

Endpoint:

/api/bollinger-bands

---

25. Average True Range — ATR

ATR means:

«Average True Range»

ATR is used to measure market volatility.

Conceptually:

Small price ranges
        |
        v
Lower volatility

Large price ranges
        |
        v
Higher volatility

Endpoint:

/api/atr

---

26. Indicators vs Trading Signals

An indicator is a calculated measurement.

A signal is a decision rule or output derived from one or more conditions.

Conceptually:

Market Data
     |
     v
Indicator
     |
     v
Rule
     |
     v
Signal

For example, a hypothetical strategy might define:

IF condition A
AND condition B
THEN generate signal

The exact rules should be explicitly documented and tested when the trading-signal stage is implemented.

---

27. Trading Signals

Trading signals are a planned major stage of the project.

The general concept is:

Market Data
      |
      v
Indicators
      |
      v
Trading Rules
      |
      v
Signal

Possible signal categories could include:

BUY
SELL
HOLD

However, the exact signal definitions should be based on documented rules rather than arbitrary assumptions.

---

28. Backtesting

Backtesting is a planned future stage.

Backtesting means applying trading rules to historical data to examine how those rules would have behaved historically.

Conceptually:

Historical Market Data
          |
          v
     Trading Rules
          |
          v
    Simulated Trades
          |
          v
       Results

Possible metrics include:

- Number of trades
- Winning trades
- Losing trades
- Return
- Drawdown
- Risk metrics

Backtesting is not the same as guaranteeing future performance.

---

29. API Request Flow

A typical backend request follows this conceptual path:

Client
   |
   | HTTP Request
   v
Flask Application
   |
   v
Application Factory
   |
   v
Blueprint
   |
   v
Route
   |
   v
Service
   |
   v
Repository
   |
   | SQL
   v
Database
   |
   | Result
   v
Repository
   |
   v
Service
   |
   v
Route
   |
   | JSON Response
   v
Client

For example:

GET /api/rsi

conceptually becomes:

Client
   |
   v
Flask
   |
   v
Market Blueprint
   |
   v
RSI Route
   |
   v
RSI Service
   |
   v
Repository
   |
   v
Database

The result then travels back to the client.

---

30. Centralized Error Handling

Centralized error handling is the current backend development stage.

The following files have been created:

backend/errors/__init__.py
backend/errors/handlers.py

The purpose is to create one consistent location for handling application errors.

---

Why Centralize Error Handling?

Without centralized handling:

Route A
   |
   +--> Error handling

Route B
   |
   +--> Error handling

Route C
   |
   +--> Error handling

This can produce duplicated logic.

With centralized handling:

Route
   |
   v
Error
   |
   v
Central Error Handler
   |
   v
Consistent Response

---

Planned Error Categories

The error-handling stage may address errors such as:

400 Bad Request
404 Not Found
500 Internal Server Error
Database-related errors

The exact handlers and response format will be implemented and tested as part of this development stage.

---

31. Separation of Concerns

Separation of concerns means dividing the application so that different components have clear responsibilities.

The intended structure is:

Route
 |
 +--> HTTP responsibilities

Service
 |
 +--> Application/business logic

Repository
 |
 +--> Database access

Database
 |
 +--> Persistent storage

This avoids placing too many unrelated responsibilities inside one component.

---

32. High Cohesion and Low Coupling

These are important software-engineering principles applied by the project architecture.

---

High Cohesion

High cohesion means related responsibilities belong together.

For example:

Market Module
   |
   +--> Price routes
   +--> RSI routes
   +--> MACD routes
   +--> ATR routes

The functionality is related to market analysis.

---

Low Coupling

Low coupling means components should avoid unnecessary dependencies on the internal details of other components.

For example:

Route
  |
  v
Service
  |
  v
Repository

The route does not need to know how the repository constructs its SQL.

This makes components easier to modify independently.

---

33. Modular Monolith

The current backend is organized as a modular monolith.

A monolith means the application is deployed as one main application.

Modular means the application is internally divided into logical components.

Conceptually:

                 Flask Application
                        |
        +---------------+---------------+
        |               |               |
      Routes         Services      Repositories
        |               |               |
        +---------------+---------------+
                        |
                     Database

The application remains one deployable system while its internal responsibilities are separated.

---

34. Git and GitHub Workflow

Git is used for version control.

The general workflow is:

Modify Code
    |
    v
git status
    |
    v
git diff
    |
    v
git add
    |
    v
git commit
    |
    v
git push
    |
    v
GitHub

---

Check Status

git status

Shows:

- Modified files
- Untracked files
- Staged files

---

Review Changes

git diff

Shows changes that have not yet been committed.

---

Stage Changes

git add .

Stages the changes.

---

Commit Changes

git commit -m "Describe the change"

Creates a commit containing the staged changes.

---

Push Changes

git push origin master

Pushes local commits to GitHub.

---

35. Important Git Commit

The Blueprint migration was recorded as:

Commit:
d910a83

Commit message:

Complete market routes blueprint migration

This commit represents an important backend-refactoring milestone.

---

36. Docker

Docker is used to package the backend into a consistent runtime environment.

The general flow is:

Dockerfile
     |
     v
Docker Image
     |
     v
Docker Container
     |
     v
Flask Application

The backend uses a Python 3.12 slim base environment.

The Docker configuration also installs system dependencies required by the application and its database-related packages.

---

37. Docker Image vs Container

These concepts should be understood separately.

Image

An image is the packaged template used to create containers.

Image

Container

A container is a running instance of an image.

Image
  |
  | run
  v
Container

---

38. Deployment Architecture

The deployment architecture is:

GitHub
   |
   v
Render
   |
   v
Docker Container
   |
   v
Flask Backend
   |
   | SQL
   v
Aiven MySQL

---

GitHub

Stores the source code and Git history.

---

Render

Hosts the deployed backend.

---

Docker

Provides the application runtime environment.

---

Flask

Runs the backend and exposes the API.

---

Aiven

Provides the production MySQL database.

---

39. Environment Variables and Security

Sensitive configuration should not be hard-coded into the repository.

For example, database credentials should not appear directly in source code.

Instead, configuration should be supplied through environment variables.

Conceptually:

Environment
    |
    +--> DATABASE_HOST
    +--> DATABASE_PORT
    +--> DATABASE_USER
    +--> DATABASE_PASSWORD
    +--> DATABASE_NAME

The application reads these values at runtime.

---

Security Rule

Never commit:

Passwords
API keys
Private tokens
Database credentials
Secret keys

to GitHub.

---

40. Local Development

The project has been developed using a local Python environment and MariaDB.

The general workflow is:

Open Repository
      |
      v
Activate Virtual Environment
      |
      v
Configure Database
      |
      v
Run Flask Application
      |
      v
Test API
      |
      v
Check Database
      |
      v
Review Git Changes
      |
      v
Commit
      |
      v
Push to GitHub

---

Run the Backend

The application is designed to start using:

python -m backend.app

The Flask application uses port:

5000

---

41. Project Structure

The important backend structure is:

forex-market-analytics/
|
+-- backend/
|   |
|   +-- app.py
|   |
|   +-- routes/
|   |   |
|   |   +-- market_routes.py
|   |
|   +-- errors/
|       |
|       +-- __init__.py
|       +-- handlers.py
|
+-- database/
|
+-- Dockerfile
|
+-- requirements.txt
|
+-- README.md

The exact repository structure may continue to evolve as additional features are implemented.

---

42. Completed Work

Major work completed so far includes:

- Forex analytics project structure
- SQL/database development
- Flask backend
- Market API endpoints
- Application Factory
- Flask Blueprint migration
- Technical-indicator API functionality
- Git/GitHub workflow
- Docker deployment configuration
- Render deployment
- Aiven MySQL production database
- Initial centralized error-handling structure

---

43. Current Development Stage

The current development stage is:

Centralized Error Handling

The files created for this stage are:

backend/errors/__init__.py
backend/errors/handlers.py

The immediate development sequence is:

1. Understand Flask exceptions
        |
        v
2. Understand HTTP error codes
        |
        v
3. Implement error handlers
        |
        v
4. Register handlers
        |
        v
5. Test error responses
        |
        v
6. Review implementation
        |
        v
7. Commit changes
        |
        v
8. Push to GitHub

---

44. Project Roadmap

The broader roadmap is:

1. Git Workflow
       |
       v
2. Forex Database
       |
       v
3. Data Ingestion
       |
       v
4. Advanced SQL
       |
       v
5. Technical Indicators
       |
       v
6. Trading Signals
       |
       v
7. Backtesting
       |
       v
8. Real-Time Processing
       |
       v
9. Visualization / Power BI
       |
       v
10. Documentation
       |
       v
11. Deployment Refinement

---

45. Revision Notes

This project is also a learning and revision resource.

The following concepts should be understood rather than simply memorized.

---

Flask

Know:

What is Flask?
What is a route?
What is an API?
What is a Blueprint?
What is an Application Factory?
What does create_app() do?

---

Software Architecture

Know:

What is separation of concerns?
What is high cohesion?
What is low coupling?
What is modularity?
What is a modular monolith?
What is refactoring?

---

SQL

Know:

SELECT
WHERE
ORDER BY
GROUP BY
HAVING
JOIN
EXISTS
CTE
Window Functions
LAG
LEAD

---

Technical Analysis

Know:

SMA
EMA
RSI
MACD
Bollinger Bands
ATR
Momentum
Volatility
Trading Signals

---

Deployment

Know:

Git
GitHub
Docker
Docker Image
Docker Container
Render
Aiven
Environment Variables

---

46. Key SQL Revision Questions

Basic SQL

1. What does "SELECT" do?
2. What does "WHERE" do?
3. What does "ORDER BY" do?
4. What does "GROUP BY" do?
5. What does "HAVING" do?
6. What is an aggregate function?

Intermediate SQL

7. What is a JOIN?
8. Why would you use EXISTS?
9. What is a primary key?
10. What is a foreign key?

Advanced SQL

11. What is a CTE?
12. Why use a CTE?
13. What is a window function?
14. How is a window function different from GROUP BY?
15. What does "LAG()" do?
16. What does "LEAD()" do?
17. Why are window functions useful for time-series data?

---

47. Key Backend Revision Questions

1. What is Flask?
2. What is an API?
3. What is an endpoint?
4. What is a route?
5. What is a Blueprint?
6. Why use Blueprints?
7. What is an Application Factory?
8. What is "create_app()"?
9. Why separate application creation from routes?
10. What is centralized error handling?
11. Why should API errors be consistent?
12. What is the purpose of a service layer?
13. What is the purpose of a repository layer?

---

48. Key Architecture Revision Questions

1. What is separation of concerns?
2. What is cohesion?
3. What is high cohesion?
4. What is coupling?
5. What is low coupling?
6. Why is low coupling desirable?
7. What is modularity?
8. What is a modular monolith?
9. What is refactoring?
10. Why refactor working code?
11. Why shouldn't every responsibility be placed inside "app.py"?

---

49. Key Technical Indicator Revision Questions

1. What is SMA?
2. How is SMA calculated?
3. What is EMA?
4. How does EMA differ from SMA?
5. What is RSI?
6. What does RSI measure conceptually?
7. What is MACD?
8. Why does MACD use moving averages?
9. What are Bollinger Bands?
10. What does ATR measure?
11. What is volatility?
12. What is momentum?
13. What is the difference between an indicator and a trading signal?

---

50. Key Docker and Deployment Questions

1. Why use Docker?
2. What is a Dockerfile?
3. What is a Docker image?
4. What is a Docker container?
5. What is Render?
6. What is Aiven?
7. Why use environment variables?
8. Why should credentials not be stored in Git?
9. What is the deployment flow?
10. How does the Flask backend communicate with the production database?

---

51. Interview Explanation

A concise explanation of the project is:

«I am building a Forex Market Analytics and Trading Signal System using Python, Flask, SQL, MariaDB/MySQL, Docker, and cloud deployment technologies. The project analyzes time-series market data using SQL techniques such as CTEs, window functions, LAG, and LEAD, and exposes market analytics through Flask API endpoints. As the backend grew, I refactored the application using the Application Factory pattern and Flask Blueprints to improve modularity and maintainability. I also containerized the backend with Docker and deployed it using Render with a production MySQL database hosted on Aiven.»

---

52. How to Explain the Architecture in an Interview

If asked:

«"How does a request move through your application?"»

Explain:

Client
   |
   v
Flask Application
   |
   v
Blueprint
   |
   v
Route
   |
   v
Service
   |
   v
Repository
   |
   v
MySQL

Then explain each part:

Client
    -> sends HTTP request

Flask
    -> receives request

Blueprint
    -> organizes the route

Route
    -> handles HTTP-level responsibilities

Service
    -> handles application logic

Repository
    -> handles database access

MySQL
    -> stores/retrieves persistent data

The response then travels back through the layers.

---

53. How to Explain the Refactoring

A useful interview explanation is:

«Initially, the Flask application contained many routes in the main application file. As the number of endpoints increased, this became harder to maintain. I refactored the backend using the Application Factory pattern and Flask Blueprints. The factory is responsible for creating and configuring the application, while the market Blueprint groups market-related routes. This improves separation of concerns and gives the project a more modular structure.»

---

54. How to Explain CTEs

A simple interview explanation:

«A Common Table Expression, or CTE, allows me to create a named intermediate result inside a SQL query. I can then use that result in the main query. I use CTEs because they make complex analytical queries easier to read and organize.»

---

55. How to Explain Window Functions

A simple explanation:

«Window functions allow SQL to perform calculations across related rows while still keeping the individual rows in the result. This is particularly useful for time-series data because I can calculate things such as running values or previous-row comparisons without collapsing the rows like GROUP BY does.»

---

56. How to Explain LAG and LEAD

A simple explanation:

«"LAG()" allows SQL to access a previous row, while "LEAD()" allows SQL to access a following row. They are useful in Forex time-series analysis because market observations are ordered by time and we often need to compare the current price with previous or subsequent observations.»

---

57. How to Explain Docker

A simple explanation:

«Docker allows me to package the application and its runtime dependencies into a consistent container environment. The Dockerfile defines how the image is built, and the resulting container runs the Flask backend.»

---

58. How to Explain Environment Variables

A simple explanation:

«Environment variables allow sensitive or environment-specific configuration such as database credentials to be supplied at runtime rather than hard-coded into the source code. This helps prevent secrets from being committed to GitHub and allows development and production environments to use different configuration values.»

---

59. Important Lessons

Lesson 1 — Working Code Is Not Automatically Well-Structured Code

An application can work correctly while becoming difficult to maintain.

Refactoring helps improve its internal organization.

---

Lesson 2 — Applications Need Better Organization as They Grow

A small application may work with a simple structure.

As functionality increases, modularity becomes more important.

---

Lesson 3 — Application Factory Separates Application Creation

"create_app()" provides a structured place for creating and configuring the Flask application.

---

Lesson 4 — Blueprints Organize Related Routes

Market-related routes can be grouped into:

market_routes.py

instead of putting everything into "app.py".

---

Lesson 5 — CTEs Help Structure Complex SQL

CTEs allow complicated analytical queries to be divided into logical stages.

---

Lesson 6 — Window Functions Are Powerful for Time-Series Data

They allow calculations across related rows without removing individual rows from the result.

---

Lesson 7 — LAG and LEAD Enable Row-to-Row Comparisons

They are particularly useful for chronological market data.

---

Lesson 8 — Separation of Concerns Improves Maintainability

Different components should have clear responsibilities.

---

Lesson 9 — High Cohesion Groups Related Functionality

Related functionality should live together.

---

Lesson 10 — Low Coupling Reduces Unnecessary Dependencies

Components should not depend unnecessarily on each other's internal implementation.

---

Lesson 11 — Docker Provides a Consistent Runtime

Docker packages the application and its dependencies into a reproducible environment.

---

Lesson 12 — Secrets Must Be Protected

Passwords and credentials should never be committed to GitHub.

---

60. Known Limitations

The project is still under active development.

The following areas should not be considered fully complete unless confirmed by the implementation:

- Full centralized error handling
- Complete trading-signal engine
- Full historical backtesting system
- Real-time market-data processing
- Production-grade monitoring
- Comprehensive automated testing
- Complete visualization/dashboard layer
- Final documentation for every endpoint

The README should be updated as each component is implemented and tested.

---

61. Future Improvements

Potential future improvements include:

Backend

- Complete centralized error handling
- Add automated tests
- Improve API validation
- Improve API documentation
- Add authentication where appropriate
- Improve logging
- Add monitoring

Database

- Improve indexing
- Optimize analytical queries
- Review schema as requirements evolve
- Improve data-ingestion pipelines

Analytics

- Expand technical indicators
- Implement trading-rule engine
- Implement signal generation
- Add strategy comparison
- Add historical backtesting
- Add risk analysis

Real-Time Processing

- Introduce real-time/near-real-time market-data ingestion
- Process incoming market events
- Recalculate indicators
- Generate signals dynamically

Visualization

- Build analytical dashboards
- Add charts for price movements
- Visualize indicators
- Visualize signals
- Visualize backtesting results

DevOps

- Improve CI/CD
- Add automated testing to deployment
- Add monitoring
- Improve logging
- Improve deployment reliability

---

62. Development Status

The project should be viewed in three categories.

Completed

Application Factory
        |
        v
Flask Blueprint Migration
        |
        v
Market API Organization
        |
        v
Docker Configuration
        |
        v
Cloud Deployment

---

In Progress

Centralized Error Handling

Current files:

backend/errors/__init__.py
backend/errors/handlers.py

---

Planned

Trading Signals
       |
       v
Backtesting
       |
       v
Real-Time Processing
       |
       v
Visualization
       |
       v
Further Production Refinement

---

63. Complete System Vision

The long-term architecture can be represented as:

                 EXTERNAL MARKET DATA
                         |
                         v
                  DATA INGESTION
                         |
                         v
                  MYSQL DATABASE
                         |
                         v
                    SQL LAYER
                         |
          +--------------+--------------+
          |              |              |
          v              v              v
       CTEs          Windows       LAG/LEAD
          |              |              |
          +--------------+--------------+
                         |
                         v
                  MARKET ANALYTICS
                         |
          +--------------+--------------+
          |              |              |
          v              v              v
        SMA            RSI            MACD
          |              |              |
          +--------------+--------------+
                         |
                         v
                  TRADING RULES
                         |
                         v
                   SIGNAL ENGINE
                         |
                         v
                    BACKTESTING
                         |
                         v
                 REAL-TIME ANALYSIS
                         |
                         v
                    FLASK API
                         |
                         v
                     CLIENT

---

64. Deployment Vision

The deployed architecture is:

                    GITHUB
                       |
                       v
                    RENDER
                       |
                       v
                DOCKER CONTAINER
                       |
                       v
                 FLASK BACKEND
                       |
                       | SQL
                       v
                  AIVEN MYSQL

---

65. Current Continuation Point

The project should currently continue from:

backend/errors/handlers.py

The next development task is:

Implement centralized Flask error handling.

The development sequence should be:

Understand Exceptions
        |
        v
Understand HTTP Error Codes
        |
        v
Create Error Handlers
        |
        v
Register Handlers
        |
        v
Return Consistent JSON
        |
        v
Test Errors
        |
        v
Review Code
        |
        v
Commit
        |
        v
Push

---

66. Final Project Summary

The Forex Market Analytics & Trading Signal System is a progressive software-engineering and data-analysis project.

It combines:

Forex Data
    |
    v
Database
    |
    v
SQL
    |
    v
Time-Series Analysis
    |
    v
Technical Indicators
    |
    v
Trading Signals
    |
    v
Flask API
    |
    v
Modular Backend
    |
    v
Docker
    |
    v
Cloud Deployment

The project demonstrates practical knowledge across several areas of Computer Science:

Database Systems
SQL
Data Structures and Algorithms Concepts
Backend Development
API Development
Software Architecture
Software Engineering
Data Analysis
Version Control
Containerization
Cloud Deployment

The backend has already progressed from a route-heavy Flask structure toward a more modular architecture using the Application Factory pattern and Flask Blueprints.

The current focus is centralized error handling.

The long-term goal is to continue building the system toward advanced market analytics, rule-based trading signals, historical backtesting, real-time processing, and visualization while maintaining a clean, modular, secure, and maintainable codebase.

---

Project Development Principle

The most important principle for continuing this project is:

Understand
   |
   v
Implement
   |
   v
Test
   |
   v
Refactor
   |
   v
Document
   |
   v
Commit
   |
   v
Deploy
   |
   v
Improve

Each stage should be understood before moving to the next one.

This README should be updated whenever a significant project milestone is completed.
