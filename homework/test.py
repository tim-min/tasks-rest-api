from requests import get

print("Удаление:")
print(get('http://localhost:5000/api/jobs/delete/200').json())
