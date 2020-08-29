from flask import abort, jsonify, request
from .models import Department
from .. import db
from ..errorhanlder.views import *
from . import department

@department.route('/')
def get_all():
    results = []
    departments = Department.query.all()
    if not departments:
        abort(404)
    
    for department in departments:
        results.append(department.to_json())
    return jsonify(results=results, status="successed")
    # return jsonify(departments)

@department.route('/add', methods = ['POST'])
def add():
    try:
        data = request.get_json()
        department_name = data.get('department_name')
        department = Department(department_name)
        db.session.add(department)
        db.session.commit()
    except Exception as e:
        print("Failed to add department - {}".format(e))
        abort(500,str(e.args))
    return jsonify(result=department.to_json(), status="successed")

@department.route('/delete/<id>', methods = ['POST'])
def delete(id):
    try:
        department = Department.query.filter_by(id = id).first_or_404()
        db.session.delete(department)
        db.session.commit()
    except Exception as e:
        print("Failed to delete department - {}".format(e))
        abort(500,str(e.args))
    return jsonify({'msg':'Deleted record successfully!'})

@department.route('/edit/<id>', methods = ['PUT'])
def edit(id):
    try:
        data = request.get_json()
        department = Department.query.filter_by(id = id).first_or_404()
        if data.get('department_name'):
            department.department_name = data['department_name']
        db.session.add(department)
        db.session.commit()
    except Exception as e:
        print("Failed to edit department - {}".format(e))
        abort(500,str(e.args))
    return jsonify(result=department.to_json(), status="successed")

@department.route('/query/<id>')
def query(id):
    department = Department.query.filter_by(id = id).first_or_404()
    return jsonify(result=department.to_json(), status="successed")