from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs


def main():
    db_name = input()
    global_init(db_name)
    db_sess = create_session()
    for user in db_sess.query(User).all():
        if user.address == "module_1" and "engineer" not in user.speciality and "engineer" not in user.position:
            print(user)


if __name__ == '__main__':
    main()
