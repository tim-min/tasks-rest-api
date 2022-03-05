import flask
from flask import jsonify, request

from . import db_session
from .jobs import Jobs
from .users import Users

blueprint = flask.Blueprint(
    'users_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/users/delete/<id>')
def delete_job(id):
    db_sess = db_session.create_session()
    if db_sess.query(Users.id).filter_by(id=id).scalar() is None:
        return jsonify({'error': 'not found'})
    try:
        user = db_sess.query(Users).filter(Users.id == id).first()
        db_sess.delete(user)
        db_sess.commit()
        return jsonify({'success': 'OK'})
    except Exception as e:
        return jsonify({'error': 'Bad request'})


@blueprint.route('/api/users')
def get_jobs():
    db_sess = db_session.create_session()
    users = db_sess.query(Users).all()
    return jsonify(
        {
            'users':
                [item.to_dict(
                    only=('surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'id'))
                    for item in users]
        }
    )


@blueprint.route('/api/users/<user_id>', methods=['GET'])
def get_one_job(user_id):
    if not user_id.isdigit():
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    users = db_sess.query(Users).get(user_id)
    if not users:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'users': users.to_dict(
                only=('surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'id'))
        }
    )


@blueprint.route('/api/users', methods=['POST'])
def create_job():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    if db_sess.query(Users.id).filter_by(id=request.json['id']).scalar() is not None:
        return jsonify({'error': 'Id already exists'})
    try:
        users = Users(
            id=request.json['id'],
            surname=request.json['surname'],
            name=request.json['name'],
            age=request.json['age'],
            position=request.json['position'],
            speciality=request.json['speciality'],
            address=request.json['address'],
            email=request.json['email']
        )
        db_sess.add(users)
        db_sess.commit()
        return jsonify({'success': 'OK'})
    except Exception as e:
        return jsonify({'error': 'Bad request'})


@blueprint.route('/api/users/edit', methods=['POST'])
def edit_job():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif 'id' not in request.json:
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    if db_sess.query(Users.id).filter_by(id=request.json['id']).scalar() is None:
        return jsonify({'error': 'Not found'})

    try:
        for user in db_sess.query(Users).all():
            if request.json.get('surname'):
                user.team_leader = request.json['surname']
            if request.json.get('name'):
                user.name = request.json['name']
            if request.json.get('age'):
                user.age = request.json['age']
            if request.json.get('position'):
                user.position = request.json['position']
            if request.json.get('speciality'):
                user.start_date = request.json['speciality']
            if request.json.get('address'):
                user.address = request.json['address']
            if request.json.get('email'):
                user.email = request.json['email']
        db_sess.commit()
        return jsonify({'success': 'ok'})
    except Exception as e:
        return jsonify({'error': 'Bad request'})
