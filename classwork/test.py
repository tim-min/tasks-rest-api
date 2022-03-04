from requests import get, post
import datetime

# get запросы:
print("----------Get запросы-------------")
print("Все работы:")
print(get('http://localhost:5000/api/jobs').json())

print("Одна работа:")
print(get('http://localhost:5000/api/jobs/4').json())

print("Неверный id:")
print(get('http://localhost:5000/api/jobs/999').json())

print("Строка:")
print(get('http://localhost:5000/api/jobs/llop').json())


# post запросы:
print("------------- post запросы ---------------")
print("Всё нормально:")
print(post('http://localhost:5000/api/jobs',
           json={'id': 200,
                 'team_leader': 1,
                 'job': 'new job',
                 'work_size': 16,
                 'collaborators': "5, 10",
                 'start_date': "04.03.2022",
                 'end_date': "04.03.2022",
                 'is_finished': True}).json())

print("id уже существует:")
print(post('http://localhost:5000/api/jobs',
           json={'id': 1,
                 'team_leader': 1,
                 'job': 'new job',
                 'work_size': 16,
                 'collaborators': "5, 10",
                 'start_date': "04.03.2022",
                 'end_date': "04.03.2022",
                 'is_finished': True}).json())

print("Недостаточно аргументов:")
print(post('http://localhost:5000/api/jobs',
           json={'id': 6,
                 'team_leader': 1,
                 'job': 'new job',
                 'collaborators': "5, 10",
                 'start_date': "04.03.2022",
                 'end_date': "04.03.2022",
                 'is_finished': True}).json())

print("Неверное значение аргумента:")
print(post('http://localhost:5000/api/jobs',
           json={'id': 150,
                 'team_leader': 1,
                 'job': 'new job',
                 'work_size': 16,
                 'collaborators': "5, 10",
                 'start_date': "04.03.2022",
                 'end_date': "04.03.2022",
                 'is_finished': "no"}).json())
