from flask import Flask

app = Flask(__name__)

with open("data.txt" 'w') as f:
    f.write("jsonns")
    
@app.route('/')
def home():
    return "Welcome"
