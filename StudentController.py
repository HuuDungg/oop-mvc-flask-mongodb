import random

from bson import ObjectId
from flask import Flask, render_template, redirect, request
from pymongo import MongoClient

from Student import Student
app = Flask(__name__)
client = MongoClient("mongodb+srv://huudung038:1@clusterhuudung.z5tdrft.mongodb.net/?retryWrites=true&w=majority&appName=ClusterHuuDung")
app.db = client.firstflaskapp
@app.route('/')
def hello_world():
    # Pass the list to the template
    return render_template('index.html', listSt=app.db.student.find({}))
@app.route('/delete/<id>', methods=['GET'])
def deleteStudent(id):
    idg = ObjectId(id)
    app.db.student.delete_one({"_id": idg})
    return redirect('/')

@app.route('/detail/<id>', methods=['GET'])
def deatilNha(id):
    print(f"detail student id {id}")
    intG = ObjectId(id)
    st = app.db.student.find_one({"_id": intG})
    return render_template('detail.html', student=st)

@app.route("/add", methods=['POST'])
def addStudent():
    name = request.form.get('name')
    age = int(request.form.get('age'))
    gender = request.form.get('gender') == 'True'
    st = Student( name, age, gender)
    app.db.student.insert_one(st.__dict__)
    return redirect('/')

@app.route("/update", methods=['POST'])
def updateStudent():
    name = request.form.get('name')
    age = int(request.form.get('age'))
    gender = request.form.get('gender') == 'True'
    id = ObjectId(request.form.get('id'))
    newData = Student( name, age, gender)
    app.db.student.update_one({"_id": id}, {"$set": newData.__dict__})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
