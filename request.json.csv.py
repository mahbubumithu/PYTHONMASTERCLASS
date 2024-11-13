import requests
import csv

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    with open("users2.csv", "w", newline="") as csvfile:
        fieldnames = ["name", "email", "City", "phone", "company"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for user in data:
            writer.writerow(
            {'name': user['name'], 
             'email': user['email'], 
             'City': user['address']['city'], 
             'phone': user['phone'], 
                'company': user['company']['name']
                }
            )

    print("CSV file has been created successfully.")

 

else:
    print("Bad Request: ", response.status_code)