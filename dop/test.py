from requests import get, post

print("Все пользователи:")
print(get('http://localhost:5000/api/users').json())

print("1 пользователь:")
print(get('http://localhost:5000/api/users/1').json())

print("Удаление пользователя:")
print(get('http://localhost:5000/api/users/delete/3').json())

print("Изменение имени первого пользователя:")
print(post('http://localhost:5000/api/users/edit',
           json={'id': '1',
                 'name': 'Artur'}).json())

print("Все пользователи:")
print(get('http://localhost:5000/api/users').json())

print("Добавление нового пользователя:")
print(post('http://localhost:5000/api/users',
           json={'id': 5567,
                 'name': 'name55',
                 'surname': 'surname55',
                 'age': 26,
                 'position': 'position55',
                 'speciality': 'speciality55',
                 'address': 'module_55',
                 'email': 'emaillljk@gmail.com'}).json())

print("Все пользователи:")
print(get('http://localhost:5000/api/users').json())
