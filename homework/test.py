from requests import get

print("Все работы:")
print(get('http://localhost:5000/api/jobs').json())


print("Удаление:")
print(get('http://localhost:5000/api/jobs/delete/1').json())

print("Все работы:")
print(get('http://localhost:5000/api/jobs').json())

print("Несуществующий id:")
print(get('http://localhost:5000/api/jobs/delete/8798769').json())

print("Строка:")
print(get('http://localhost:5000/api/jobs/delete/ewf').json())
