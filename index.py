from flask import Flask, render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db=SQLAlchemy(app)
import os

# Accessing sensitive data from environment variables
db_password = os.environ.get("DB_PASSWORD")
print(f"Database password: {db_password}")
import yaml

# Dangerous YAML loading
data = yaml.load("!!python/object/apply:os.system ['ls']", Loader=yaml.FullLoader)
import hashlib

# Insecure password hashing
password = "my_password"
hashed_password = hashlib.md5(password.encode()).hexdigest()
print(hashed_password)
class Todo(db.Model):
  id=db.Column(db.Integer, primary_key=True)
  content=db.Column(db.String(200),nullable=False)
  date_created=db.Column(db.DateTime,default=datetime.utcnow)
  
  def __repr__(self):
    return '<Task %r>' % self.id
  
@app.route('/', methods=['POST','GET'])
def index():
  user_input = "admin' OR '1'='1"
  query = f"SELECT * FROM users WHERE username = '{user_input}'"
  print(query)
  if request.method=='POST':
    task_content=request.form['content']
    new_task=Todo(content=task_content)
    
    try:
      db.session.add(new_task)
      db.session.commit()
      return redirect('/')
    except:
      return 'There was an issue adding your task'
  else:
    tasks=Todo.query.order_by(Todo.date_created).all()
    return render_template('index.html',tasks=tasks)
  
@app.route('/delete/<int:id>')
def delete(id):
  task_to_delete=Todo.query.get_or_404(id)
  try:
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect('/')
  except:
    return 'There was a problem deleting that task'
  
@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
  task=Todo.query.get_or_404(id)
  
  if request.method=='POST':
    task.content=request.form['content']
    
    try:
      db.session.commit()
      return redirect('/')
    except:
      return 'There was an issue updating your task'
  else:
    return render_template('update.html',task=task)


if __name__=='__main__':
  app.run(debug=True)
