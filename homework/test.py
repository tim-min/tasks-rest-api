from requests import get, post

print("Все работы:")
print(get('http://localhost:5000/api/jobs').json())


print("Изменяем значения collaborators и job в работе 1:")
print(post('http://localhost:5000/api/jobs/edit',
           json={'id': '1',
                 'collaborators': "56, 108",
                 'job': "[[[[edited job]]]]"}).json())

print("Все работы:")
print(get('http://localhost:5000/api/jobs').json())

print("Несуществующий id:")
print(post('http://localhost:5000/api/jobs/edit',
           json={'id': '325234652345',
                 'collaborators': "10, 10",
                 'job': "old new job"}).json())

print("Строка вместо id:")
print(post('http://localhost:5000/api/jobs/edit',
           json={'id': 'llop[',
                 'collaborators': "10, 10",
                 'job': "old new job"}).json())

print("Нету id в json:")
print(post('http://localhost:5000/api/jobs/edit',
           json={'collaborators': "10, 10",
                 'job': "old new job"}).json())

print("Неверное значение (в is_finished строка):")
print(post('http://localhost:5000/api/jobs/edit',
           json={'id': '1',
                 'is_finished': "no",
                 'job': "edited job"}).json())
