import pandas as pd 


orders = [
    {"order_id": 1, "customer_id": 1, "product_id": 101, "date": "2024-01-01", "quantity": 1},
    {"order_id": 2, "customer_id": 2, "product_id": 102, "date": "2024-01-02", "quantity": 2},
    {"order_id": 3, "customer_id": 1, "product_id": 103, "date": "2024-01-03", "quantity": 1},
    {"order_id": 4, "customer_id": 3, "product_id": 101, "date": "2024-01-04", "quantity": 3},
    {"order_id": 5, "customer_id": 2, "product_id": 101, "date": "2024-01-05", "quantity": 1},
]

customers = [
    {"customer_id": 1, "name": "Ana", "city": "Beograd"},
    {"customer_id": 2, "name": "Marko", "city": "Novi Sad"},
    {"customer_id": 3, "name": "Jovan", "city": "Niš"},
]


products = [
    {"product_id": 101, "product_name": "Laptop", "price": 800},
    {"product_id": 102, "product_name": "Mouse", "price": 20},
    {"product_id": 103, "product_name": "Keyboard", "price": 50},
]


df_orders = pd.DataFrame(orders)
df_customers = pd.DataFrame(customers)
df_products = pd.DataFrame(products)

#spajanje tabela 

df_merge = pd.merge(df_orders,df_customers,on = 'customer_id')
print(df_merge)

df = pd.merge(df_merge,df_products,on = 'product_id')
print(df)

# total_amoint 

df['total_amount'] = df['price'] * df['quantity']
print(df['total_amount'])


#ukupan prihod po kupcu 

total_revenue_per_customer = df.groupby('customer_id')['total_amount'].sum()
print("Total revenue per customer:",total_revenue_per_customer)

# best customer 

best_customer = total_revenue_per_customer.idxmax()
print('Best customer:',best_customer)

#ukupan prihod po proizvodu 


total_revenue_per_product = df.groupby('product_name')['total_amount'].sum()
print('Total revenue per product:',total_revenue_per_product)

#best product

best_product = total_revenue_per_product.idxmax()
print('Best product:',best_product)

#najprodavaniji proizvod po kolicini

best_sold_product_by_quantity = df.groupby('product_name')['quantity'].sum().idxmax()
print('Best sold product by quantity:', best_sold_product_by_quantity)

#ukupan prihod po gradu

total_revenue_per_city = df.groupby('city')['total_amount'].sum()
print('Total revenue per city:',total_revenue_per_city)


#parsiranje datuma

df['date'] = pd.to_datetime(df['date'])

# trend prodaje po datumu 

sales_by_date = df.groupby('date')['total_amount'].sum()
print(sales_by_date)

#najbolji kupac u svakom gradu 

best_customer_in_every_city = df.groupby(['name','city'])['total_amount'].sum().idxmax()
print('Best customer in every city:',best_customer_in_every_city)
