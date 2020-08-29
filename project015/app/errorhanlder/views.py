from flask import jsonify, abort
from . import error
from .. import  db


@error.app_errorhandler(403)
def forbidden(e):
    return jsonify({'result':None, 'msg':'Forbidden!', 'status':'failed'}), 404

@error.app_errorhandler(404)
def resource_not_found(e):
    return jsonify({'result': None, 'msg':'Not found!','status':'failed'}), 404

@error.app_errorhandler(405)
def forbidden(e):
    return jsonify({'result':None, 'msg':'Method Not Allowed!', 'status':'failed'}), 405

@error.app_errorhandler(500)
def internal_server_error(e):
    db.session.rollback()
    return jsonify({'result': None, 'msg':str(e), 'status':'failed'}), 500
