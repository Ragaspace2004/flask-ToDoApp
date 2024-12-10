# Flask Todo Application

This is a simple Todo application built using Flask and SQLAlchemy as part of my learning journey with Flask. The application allows users to create, read, update, and delete tasks.

## Features
- Add new tasks.
- View a list of all tasks, sorted by creation date.
- Update task content.
- Delete tasks.

## Technologies Used
Python: Programming language
Flask: Web framework
SQLAlchemy: Database ORM
SQLite: Database

## APPLICATION STRUCTURE
```TodoApp/
├── app.py            # Main application file
├── templates/
│   ├── index.html    # Template for displaying tasks and adding new tasks
│   ├── base.html     # html-boilerplate  
│   ├── update.html   # Template for updating tasks
├── static/css        # Folder for static assets like CSS, JS, and images
│   ├── main.css  
├── requirements.txt  # Python dependencies
└── README.md         # This README file
```
## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Ragaspace2004/flask-ToDoApp.git
   cd TodoApp
   pip install -r requirements.txt
 
   ```

## BEST PRACTICES
Set up a virtual environment
```python -m venv venv
source venv/bin/activate
```
On Windows, use 
```venv\Scripts\activate```




