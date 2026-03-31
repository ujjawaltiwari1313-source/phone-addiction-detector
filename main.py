from sklearn.tree import DecisionTreeClassifier

X = [
    [5, 7, 3],
    [8, 5, 5],
    [2, 8, 1],
    [9, 4, 6],
    [3, 7, 2]
]

y = [0, 1, 0, 1, 0]

model = DecisionTreeClassifier()
model.fit(X, y)

phone = float(input("Daily phone usage (hours): "))
sleep = float(input("Sleep hours: "))
social = float(input("Social media usage (hours): "))

result = model.predict([[phone, sleep, social]])

if result[0] == 1:
    print("Result: Addicted to phone")
else:
    print("Result: Not addicted")
