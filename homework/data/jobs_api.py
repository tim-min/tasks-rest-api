import flask
from flask import jsonify, request

from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs/delete/<id>')
def delete_job(id):
    db_sess = db_session.create_session()
    if db_sess.query(Jobs.id).filter_by(id=id).scalar() is None:
        return jsonify({'error': 'not found'})
    try:
        job = db_sess.query(Jobs).filter(Jobs.id == id).first()
        db_sess.delete(job)
        db_sess.commit()
        return jsonify({'success': 'OK'})
    except Exception as e:
        return jsonify({'error': 'Bad request'})


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(
                    only=('team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))
                    for item in news]
        }
    )


@blueprint.route('/api/jobs/<job_id>', methods=['GET'])
def get_one_job(job_id):
    if not job_id.isdigit():
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(job_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'jobs': jobs.to_dict(
                only=('team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_job():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    if db_sess.query(Jobs.id).filter_by(id=request.json['id']).scalar() is not None:
        return jsonify({'error': 'Id already exists'})
    try:
        jobs = Jobs(
            id=request.json['id'],
            team_leader=request.json['team_leader'],
            job=request.json['job'],
            work_size=request.json['work_size'],
            collaborators=request.json['collaborators'],
            start_date=request.json['start_date'],
            end_date=request.json['end_date'],
            is_finished=request.json['is_finished']
        )
        db_sess.add(jobs)
        db_sess.commit()
        return jsonify({'success': 'OK'})
    except Exception as e:
        return jsonify({'error': 'Bad request'})


@blueprint.route('/api/jobs/edit', methods=['POST'])
def edit_job():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif 'id' not in request.json:
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    if db_sess.query(Jobs.id).filter_by(id=request.json['id']).scalar() is None:
        return jsonify({'error': 'Not found'})

    try:
        for job in db_sess.query(Jobs).all():
            if request.json.get('team_leader'):
                job.team_leader = request.json['team_leader']
            if request.json.get('job'):
                job.job = request.json['job']
            if request.json.get('work_size'):
                job.work_size = request.json['work_size']
            if request.json.get('collaborators'):
                job.collaborators = request.json['collaborators']
            if request.json.get('start_date'):
                job.start_date = request.json['start_date']
            if request.json.get('end_date'):
                job.end_date = request.json['end_date']
            if request.json.get('is_finished'):
                job.is_finished = request.json['is_finished']
        db_sess.commit()
        return jsonify({'success': 'ok'})
    except Exception as e:
        return jsonify({'error': 'Bad request'})
