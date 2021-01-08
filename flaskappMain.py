from flask import Flask
app= Flask(__name__)
@app.route('/')
def index():
  return "<h1>Congrats! The flask app is up!</h1>"