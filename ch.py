from flask import Flask

app = Flask(__name__)



@app.route('/')
def home():
    return "Welcome Page"
@app.route("/home")
def n():
    with open("data.txt", 'r') as f:
        d = f.read()
    return d



if __name__ == '__main__':
    app.run(debug=True)
