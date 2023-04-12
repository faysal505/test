from flask import Flask

app = Flask(__name__)

with open("data.txt", 'w') as f:
    f.write("jsonns")

@app.route('/')
def home():
    with open("data.txt", 'r') as f:
        d = f.read()
    return d

app.run()

if __name__ == '__main__':
    app.run(debug=True)
