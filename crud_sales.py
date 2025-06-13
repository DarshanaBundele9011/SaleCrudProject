import csv
import os

FILENAME = 'sales.csv'
FIELDS = ['id', 'customer_name', 'product', 'quantity', 'price']

def initialize_csv():
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()

def create_sale(sale):
    with open(FILENAME, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writerow(sale)

def read_sales():
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)

def update_sale(sale_id, updated_data):
    updated = False
    rows = []
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] == sale_id:
                row.update(updated_data)
                updated = True
            rows.append(row)

    with open(FILENAME, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

def delete_sale(sale_id):
    deleted = False
    rows = []
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] != sale_id:
                rows.append(row)
            else:
                deleted = True

    with open(FILENAME, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == '__main__':
    initialize_csv()

    create_sale({'id': '1', 'customer_name': 'Aarav Sharma', 'product': 'Laptop', 'quantity': '1', 'price': '75000'})
    create_sale({'id': '2', 'customer_name': 'Priya Verma', 'product': 'Mobile', 'quantity': '2', 'price': '45000'})
    create_sale({'id': '3', 'customer_name': 'Rohan Mehta', 'product': 'Tablet', 'quantity': '1', 'price': '28000'})
    create_sale({'id': '4', 'customer_name': 'Sneha Iyer', 'product': 'Smart Watch', 'quantity': '3', 'price': '18000'})
    create_sale({'id': '5', 'customer_name': 'Vikram Singh', 'product': 'Keyboard', 'quantity': '4', 'price': '6000'})
    create_sale({'id': '6', 'customer_name': 'Ananya Desai', 'product': 'Monitor', 'quantity': '1', 'price': '15000'})
    create_sale({'id': '7', 'customer_name': 'Kunal Nair', 'product': 'Speaker', 'quantity': '2', 'price': '9000'})
    create_sale({'id': '8', 'customer_name': 'Divya Kulkarni', 'product': 'Headphones', 'quantity': '1', 'price': '3000'})
    create_sale({'id': '9', 'customer_name': 'Manish Gupta', 'product': 'Router', 'quantity': '2', 'price': '4000'})
    create_sale({'id': '10', 'customer_name': 'Neha Joshi', 'product': 'Printer', 'quantity': '1', 'price': '12000'})

    read_sales()
    update_sale('1', {'quantity': '2', 'price': '150000'})
    delete_sale('10')
    read_sales()

    initialize_csv()
    create_sale({'id': '1', 'customer_name': 'Alice', 'product': 'Laptop', 'quantity': '1', 'price': '85000'})
    create_sale({'id': '2', 'customer_name': 'Bob', 'product': 'Mouse', 'quantity': '2', 'price': '1200'})
    read_sales()
    update_sale('1', {'quantity': '3', 'price': '255000'})
    delete_sale('2')
    read_sales()
