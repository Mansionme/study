from flask import abort, jsonify, request
from .models import TeachPlan
from .. import db
from ..department.models import Department 
from ..errorhanlder.views import *
from . import teachplan

@teachplan.route('/')
def get_all():
    results=[]
    teachplans = TeachPlan.query.all()
    if not teachplans:
        abort(404)
    for teachplan in teachplans:
        results.append(teachplan.to_json())
    return jsonify(results=results, status="successed")

@teachplan.route('/add', methods = ['POST'])
def add():
    try:
        data = request.get_json()
        subject = data.get('subject')
        remarks = data.get('remarks') or ''
        department_id = data.get('department_id')
        status = data.get('status')
        week_no = data.get('week_no')
        teachplan = TeachPlan(subject, remarks, department_id, status, week_no)
        db.session.add(teachplan)
        db.session.commit()
    except Exception as e:
        print("Failed to add teachplan - {}".format(e))
        abort(500 ,str(e.args))
    return jsonify(result=teachplan.to_json(), status="successed")

@teachplan.route('/delete/<id>', methods = ['POST'])
def delete(id):
    try:
        teachplan = TeachPlan.query.filter_by(id = id).first_or_404()
        db.session.delete(teachplan)
        db.session.commit()
    except Exception as e:
        print("Failed to delete teachplan - {}".format(e))
        abort(500, str(e.args))
    return jsonify({'msg':'Deleted record successfully!'})

@teachplan.route('/edit/<id>', methods = ['PUT'])
def edit(id):
    try:
        data = request.get_json()
        teachplan = TeachPlan.query.filter_by(id = id).first_or_404()
        if data.get('subject'):
            teachplan.subject = data['subject']
        if data.get('remarks'):
            teachplan.remarks = data['remarks']
        if data.get('department_id'):
            teachplan.department_id = data['department_id']
        if data.get('status'):
            teachplan.status = data['status']  
        if data.get('week_no'):
            teachplan.week_no = data['week_no'] 
        db.session.add(teachplan)
        db.session.commit()
    except Exception as e:
        print("Failed to edit teachplan - {}".format(e))
        abort(500,str(e.args))
    return jsonify(result=teachplan.to_json(), status="successed")

@teachplan.route('/query/<id>')
def query(id):
    teachplan = TeachPlan.query.filter_by(id = id).first_or_404()
    return jsonify(result=teachplan.to_json(), status="successed")

@teachplan.route('/query/department/<id>')
def query_by_department(id):
    results = []
    matchedplans = []
    department = Department.query.filter_by(id = id).first_or_404()
    teachplans = TeachPlan.query.all()
    for teachplan in teachplans:
        if str(id) in teachplan.department_id.split(","):
            matchedplans.append(teachplan)
    if matchedplans:
        for matchedplan in matchedplans:
            results.append(matchedplan.to_json())
    return jsonify(result=results, status="successed")