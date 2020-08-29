from flask import abort, jsonify, request
from .models import TeachWeek
from .. import db
from ..errorhanlder.views import *
from . import teachweek

@teachweek.route('/')
def get_all():
    results=[]
    teachweeks = TeachWeek.query.all()
    if not teachweeks:
        abort(404)
    for teachweek in teachweeks:
        results.append(teachweek.to_json())
    return jsonify(results=results, status="successed")

@teachweek.route('/add', methods = ['POST'])
def add():
    try:
        data = request.get_json()
        term = data.get('term')
        week_start = data.get('week_start')
        week_end = data.get('week_end')
        weekno_term = data.get('weekno_term')
        week_no = data.get('week_no')
        teachweek = TeachWeek(term, week_start, week_end, weekno_term, week_no)
        db.session.add(teachweek)
        db.session.commit()
    except Exception as e:
        print("Failed to add teachweek - {}".format(e))
        abort(500,str(e.args))
    return jsonify(result=teachweek.to_json(), status="successed")

@teachweek.route('/delete/<id>', methods = ['POST'])
def delete(id):
    try:
        teachweek = TeachWeek.query.filter_by(id = id).first_or_404()
        db.session.delete(teachweek)
        db.session.commit()
    except Exception as e:
        print("Failed to delete teachweek - {}".format(e))
        abort(500,str(e.args))
    return jsonify({'msg':'Deleted record successfully!'})

@teachweek.route('/edit/<id>', methods = ['PUT'])
def edit(id):
    try:
        data = request.get_json()
        teachweek = TeachWeek.query.filter_by(id = id).first_or_404()
        if data.get('term'):
            teachweek.term = data['term']
        if data.get('week_start'):
            teachweek.week_start = data['week_start']
        if data.get('week_end'):
            teachweek.week_end = data['week_end']
        if data.get('weekno_term'):
            teachweek.weekno_term = data['weekno_term']  
        if data.get('week_no'):
            teachweek.week_no = data['week_no'] 
        db.session.add(teachweek)
        db.session.commit()
    except Exception as e:
        print("Failed to edit teachweek - {}".format(e))
        abort(500,str(e.args))
    return jsonify(result=teachweek.to_json(), status="successed")

@teachweek.route('/query/<id>')
def query(id):
    teachweek = TeachWeek.query.filter_by(id = id).first_or_404()
    return jsonify(result=teachweek.to_json(), status="successed")



# @teachweek.route('/edit/<id>', methods = ['PUT'])
# def update_teachweek_by_id(id):
#     data = request.get_json()
#     get_product = Product.query.filter_by(id = id).first_or_404()
#     if data.get('title'):
#         get_product.title = data['title']
#     if data.get('productDescription'):
#         get_product.productDescription = data['productDescription']
#     if data.get('productBrand'):
#         get_product.productBrand = data['productBrand']
#     if data.get('price'):
#         get_product.price= data['price']    
#     db.session.add(get_product)
#     db.session.commit()
#     product_schema = ProductSchema(only=['id', 'title', 'productDescription','productBrand','price'])
#     product = product_schema.dump(get_product)
#     return make_response(jsonify({"product": product}))