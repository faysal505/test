from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://mydata_839h_user:J56VGKBunMhYrRrPjdJxTrcnYD55bdDl@dpg-cgts3nt269vbmevj9tfg-a.oregon-postgres.render.com/mydata_839h"
db.init_app(app)

class Nid(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    nid = db.Column(db.String(50), nullable=False)
    birth = db.Column(db.String(50), nullable=False)



with app.app_context():
    db.create_all()



@app.route('/users', methods=['GET'])
def get_users():
    users = Nid.query.all()  # Retrieve all records from the User table
    user_list = []
    for user in users:
        user_data = {
            'name': user.name,
            'nid': user.nid,
            'birth': user.birth
        }
        user_list.append(user_data)
    return jsonify(user_list)


if __name__ == '__main__':
    app.run()

