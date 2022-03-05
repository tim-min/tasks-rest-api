from flask import Flask, render_template
from data import db_session, user_api
from data.users import Users
from data.jobs import Jobs
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def add_users(name, surname, age, position, speciality, address, email):
    users = Users()
    users.name = name
    users.surname = surname
    users.age = age
    users.position = position
    users.speciality = speciality
    users.address = address
    users.email = email
    db_sess = db_session.create_session()
    db_sess.add(users)
    db_sess.commit()


def add_job(team_leader, job, work_size, collaborators, start_date, is_finished):
    jobs = Jobs()
    jobs.team_leader = team_leader
    jobs.job = job
    jobs.work_size = work_size
    jobs.collaborators = collaborators
    jobs.start_date = start_date
    jobs.is_finished = is_finished
    db_sess = db_session.create_session()
    db_sess.add(jobs)
    db_sess.commit()


def main():
    now = datetime.datetime.now()
    db_session.global_init("db/mars_explorer.db")
    app.register_blueprint(user_api.blueprint)
    # add_users("Name", "Surname", 21, "position", "spec", "module_1", "email@email.com")
    # add_job(1, "deployment of residential modules 1 and 2", 15, "2, 3", now, False)

    app.run()


def get_jobs():
    result = list()
    db_sess = db_session.create_session()
    for job in db_sess.query(Jobs).all():
        job_info = [job.job, f"{job.user.name} {job.user.surname}", job.work_size, job.collaborators, job.is_finished]
        job_info[-1] = "is not finished" if not job_info[-1] else "finished"
        result.append(job_info)

    return result


@app.route("/")
@app.route("/index")
def index():
    jobs = get_jobs()
    return render_template('index.html', jobs=jobs)


if __name__ == '__main__':
    main()
