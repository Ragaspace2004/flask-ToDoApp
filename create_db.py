from app import app, db

with app.app_context():
    db.create_all()
# Dangerous function example
    eval("print('This is dangerous')")

# Hardcoded password example
    password = "my_secret_password"
    print("Created database")
