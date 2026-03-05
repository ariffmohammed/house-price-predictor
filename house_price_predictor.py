import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = {
    'size': [1000, 1500, 1200, 1800, 2000, 900, 1300, 1600, 2200, 2500,
             800, 1100, 1400, 1700, 2100, 950, 1250, 1550, 1900, 2300],
    'rooms': [2, 3, 2, 4, 4, 1, 3, 3, 5, 5,
              1, 2, 3, 4, 4, 2, 2, 3, 4, 5],
    'age': [10, 5, 15, 3, 1, 20, 8, 6, 2, 1,
            25, 12, 7, 4, 3, 18, 9, 5, 2, 1],
    'location': [7, 8, 6, 9, 9, 5, 7, 8, 9, 10,
                 4, 6, 7, 8, 9, 5, 6, 8, 9, 10],
    'price': [200000, 350000, 240000, 480000, 550000, 150000, 280000, 380000, 600000, 750000,
              120000, 210000, 300000, 430000, 570000, 160000, 250000, 370000, 500000, 680000]
}

df = pd.DataFrame(data)

X = df[['size','rooms', 'age', 'location']]
y = df['price']

model = LinearRegression()
model.fit(X, y)

size = int(input("Enter size: "))
rooms = int(input("Enter rooms: "))
age = int(input("Enter age: "))
location = int(input("Enter locatin: "))

new_house = [[size, rooms, age,location]] 
print("price: ",model.predict(new_house))
