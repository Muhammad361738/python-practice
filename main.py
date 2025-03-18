import requests

try:
    res = requests.get('https://jsonplaceholder.typicode.com/users')
    result = res.json()
    print(result)  
except:
    print("Failed to fetch data!")
finally:
    print("Out from try catch")