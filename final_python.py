purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

def total_revenue(purchases):
    counter=0
    for i in purchases:
        counter+=i["price"]*i["quantity"]
    return f'Общая выручка: {counter}'

def items_by_category(purchases):
    dict1={}
    for i in purchases:
        category=i["category"]
        item=i["item"]    
        dict1.setdefault(category, []).append(item)
    return f'Товары по категориям: {dict1}'

def expensive_purchases(purchases, min_price):
    list1=[i for i in purchases if i["price"]>=min_price]
    return f'Покупки дороже {min_price}: {list1}'

def average_price_by_category(purchases):
    dict1={}
    for i in purchases:
        category=i["category"]
        price=i["price"]    
        dict1.setdefault(category, []).append(price)
    dict2={i: sum(dict1[i])/len(dict1[i]) for i in dict1}
    return f'Средняя цена по категориям: {dict2}'

def most_frequent_category(purchases):
    dict1={}
    for i in purchases:
        category=i["category"]
        quantity=i["quantity"]
        dict1[category]=dict1.get(category, 0)+quantity
    return f'Категория с наибольшим количеством проданных товаров: {max(dict1)}'




print(total_revenue(purchases))
print(items_by_category(purchases))
print(expensive_purchases(purchases, 1.0))
print(average_price_by_category(purchases))
print(most_frequent_category(purchases))
        

