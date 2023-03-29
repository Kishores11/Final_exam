from flask import Flask, render_template, request, flash, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///manage.sqlite'
app.config['SECRET_KEY'] = "random string"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['UPLOAD_FOLDER'] = "static\images"


db = SQLAlchemy(app)
app.app_context().push()


class Accessory(db.Model):
    __tablename__ = "gadjets"

    name = db.Column(db.Text, primary_key=True)
    quantities_ordered = db.Column(db.Integer)
    quantities_remaining = db.Column(db.Integer)
    vendor_name = db.Column(db.Text)
    purchase_price = db.Column(db.Integer)
    selling_price = db.Column(db.Integer)

    def __init__(self, name, quantities_ordered, quantities_remaining, vendor_name, purchase_price, selling_price):
        self.name = name
        self.qorder = quantities_ordered
        self.qremain = quantities_remaining
        self.vendor = vendor_name
        self.pprice = purchase_price
        self.sprice = selling_price

    def __repr__(self):
        return f"{self.name},{self.qorder},{self.qremain},{self.vendor},{self.pprice},{self.sprice}"


db.create_all()


class AccessorySchema(Schema):   # used to serialise class object when we wished to see gadjets table using postman
    name = fields.Str()
    quantities_ordered = fields.Int()
    quantities_remaining = fields.Int()
    vendor_name = fields.Str()
    purchase_price = fields.Int()
    selling_price = fields.Int()


@app.route("/table")
def table():
    all = Accessory.query.all()
    return render_template('table.html', all=all)


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        qorder = request.form['qorder']
        qremain = request.form['qremain']
        vendor = request.form['vendor']
        pprice = request.form['pprice']
        sprice = request.form['srice']
        item = Accessory(name, qorder, qremain, vendor, pprice, sprice)
        db.session.add(item)
        db.session.commit()
        return {"message": "Item added"}


@app.route('/update', methods=['PUT'])
def update():
    if request.method == 'PUT':
        try:
            Accessory.query.filter(Accessory.name == request.form['name'])
            name = request.form['name']
            item = Accessory.query.filter_by(name=name).first()
            item.qorder = request.form['qorder']
            item.qremain = request.form['qremain']
            item.vendor = request.form['vendor']
            item.pprice = request.form['pprice']
            item.sprice = request.form['srice']
            db.session.commit()
            return jsonify({"message": "success"})

        except:
            return jsonify({"message":"no such acc"})


@app.route('/delete', methods=['DELETE'])
def delete():
    if request.method == 'DELETE':
        name = request.form['name']
        item = Accessory.query.filter_by(name=name).first()
        db.session.delete(item)
        return jsonify({"message": "success"})


if __name__ == "__main__":
    app.run(debug=True)

