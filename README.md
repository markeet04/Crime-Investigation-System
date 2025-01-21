# Crime Management System

## Overview
A comprehensive Crime management system implemented in Python using Object-Oriented Programming principles. The system manages legal cases, various judicial personnel, evidence tracking, and case proceedings through a secure database-driven architecture.

## Features
- Multi-user role support (Judge, Lawyer, Investigating Officer, Witness, Victim)
- Case management and tracking
- Evidence management system
- Forensic report handling
- Criminal record management
- Court proceedings documentation
- Secure authentication system
- Database-driven architecture

## Technical Stack
- **Programming Language:** Python
- **Database:** MySQL
- **Architecture:** Object-Oriented Programming
- **Interface:** Tkinter Based GUI

## Project Structure
```
├── __pycache__/
├── Agency.gui.py
├── Case.gui.py
├── Crime.gui.py
├── Fix.gui.py
├── agency.py
├── article.py
├── article.gui.py
├── case.py
├── court.py
├── court.gui.py
├── crime.py
├── criminal_record.py
├── criminal_record.gui.py
├── database_schema.txt
├── database_operations.py
├── evidence.py
├── evidence.gui.py
├── fir.py
├── forensic.py
├── forensic.gui.py
├── investigating_officer.gui.py
├── judge.gui.py
├── lawyer.gui.py
├── login_page.py
├── persons.py
├── psettm.png
├── report.gui.py
├── statement.gui.py
├── tempCodeRunnerFile.py
├── user.gui.py
├── victim.gui.py
└── witness.gui.py
```

## Installation & Setup

### Prerequisites
- Python 3
- MySQL Server
- Required Python packages:
  ```bash
  pip install mysql-connector-python
  pip install tkinter  # For GUI components
  pip install matplotlib
  ```

### Database Setup
1. Install MySQL Server
2. Create a new database
3. Run the schema from `database_schema.txt`
4. Configure database connection in `database_operations.py`

### Running the Application
1. Clone the repository
2. Configure database settings
3. Run the application:
   ```bash
   python login_page.py
   ```

## Class Structure

### Core Classes
- **Person**: Base class for all user types
- **Case**: Manages case information and status
- **Evidence**: Handles evidence tracking and management
- **Court**: Manages court proceedings
- **Crime**: Handles crime classification and details

### User Roles
- **Judge**: Manages court proceedings and verdicts
- **Lawyer**: Handles case representation
- **InvestigatingOfficer**: Manages investigation and evidence
- **Witness**: Provides testimony
- **Victim**: Manages victim statements and information

## Database Schema
The system uses a relational database with tables for:
- Users
- Cases
- Evidence
- Court Proceedings
- Criminal Records
- Forensic Reports
- Statements

## Security Features
- User authentication
- Role-based access control
- Secure database operations
- Session management


