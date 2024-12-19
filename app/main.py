from config import session
from models import Wholesale, Product, Employee, Consumer
import os

# ==================== WHOLESALE ==========================
def add_wholesale():
    name = input("Enter Wholesale Name: ")
    location = input("Enter Wholesale Location: ")
    wholesale = Wholesale(name=name, location=location)
    session.add(wholesale)
    session.commit()
    print("Wholesale added successfully.")

def view_wholesales():
    wholesales = session.query(Wholesale).all()
    for wholesale in wholesales:
        print(f"{wholesale.id} - {wholesale.name} - {wholesale.location}")

def update_wholesale():
    wholesale_id = int(input("Enter Wholesale ID to update: "))
    wholesale = session.query(Wholesale).filter_by(id=wholesale_id).first()
    if wholesale:
        wholesale.name = input(f"Enter new name (current: {wholesale.name}): ")
        wholesale.location = input(f"Enter new location (current: {wholesale.location}): ")
        session.commit()
        print("Wholesale updated successfully.")
    else:
        print("Wholesale not found.")
 
def delete_wholesale():
    wholesale_id = int(input("Enter Wholesale ID to delete: "))
    wholesale = session.query(Wholesale).filter_by(id=wholesale_id).first()
    if wholesale:
        session.delete(wholesale)
        session.commit()
        print("Wholesale deleted successfully.")
    else:
        print("Wholesale not found.")

# ==================== PRODUCT ==========================
def add_product():
    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: "))
    description = input("Enter Product Description: ")
    wholesale_id = int(input("Enter Wholesale ID: "))
    product = Product(name=name, price=price, description=description, wholesale_id=wholesale_id)
    session.add(product)
    session.commit()
    print("Product added successfully.")

def view_products():
    products = session.query(Product).all()
    for product in products:
        print(f"{product.id} - {product.name} - Price: {product.price} - Wholesale ID: {product.wholesale_id}")

def update_product():
    product_id = int(input("Enter Product ID to update: "))
    product = session.query(Product).filter_by(id=product_id).first()
    if product:
        product.name = input(f"Enter new name (current: {product.name}): ")
        product.price = float(input(f"Enter new price (current: {product.price}): "))
        product.description = input(f"Enter new description (current: {product.description}): ")
        session.commit()
        print("Product updated successfully.")
    else:
        print("Product not found.")

def delete_product():
    product_id = int(input("Enter Product ID to delete: "))
    product = session.query(Product).filter_by(id=product_id).first()
    if product:
        session.delete(product)
        session.commit()
        print("Product deleted successfully.")
    else:
        print("Product not found.")

# ==================== EMPLOYEE ==========================
def add_employee():
    name = input("Enter Employee Name: ")
    role = input("Enter Employee Role: ")
    salary = float(input("Enter Employee Salary: "))
    wholesale_id = int(input("Enter Wholesale ID: "))
    employee = Employee(name=name, role=role, salary=salary, wholesale_id=wholesale_id)
    session.add(employee)
    session.commit()
    print("Employee added successfully.")

def view_employees():
    employees = session.query(Employee).all()
    for employee in employees:
        print(f"{employee.id} - {employee.name} - Role: {employee.role} - Salary: {employee.salary} - Wholesale ID: {employee.wholesale_id}")

def update_employee():
    employee_id = int(input("Enter Employee ID to update: "))
    employee = session.query(Employee).filter_by(id=employee_id).first()
    if employee:
        employee.name = input(f"Enter new name (current: {employee.name}): ")
        employee.role = input(f"Enter new role (current: {employee.role}): ")
        employee.salary = float(input(f"Enter new salary (current: {employee.salary}): "))
        session.commit()
        print("Employee updated successfully.")
    else:
        print("Employee not found.")

def delete_employee():
    employee_id = int(input("Enter Employee ID to delete: "))
    employee = session.query(Employee).filter_by(id=employee_id).first()
    if employee:
        session.delete(employee)
        session.commit()
        print("Employee deleted successfully.")
    else:
        print("Employee not found.")

# ==================== CONSUMER ==========================
def add_consumer():
    name = input("Enter Consumer Name: ")
    contact_info = input("Enter Contact Information: ")
    preferences = input("Enter Preferences: ")
    consumer = Consumer(name=name, contact_info=contact_info, preferences=preferences)
    session.add(consumer)
    session.commit()
    print("Consumer added successfully.")

def view_consumers():
    consumers = session.query(Consumer).all()
    for consumer in consumers:
        print(f"{consumer.id} - {consumer.name} - Contact: {consumer.contact_info} - Preferences: {consumer.preferences}")

def update_consumer():
    consumer_id = int(input("Enter Consumer ID to update: "))
    consumer = session.query(Consumer).filter_by(id=consumer_id).first()
    if consumer:
        consumer.name = input(f"Enter new name (current: {consumer.name}): ")
        consumer.contact_info = input(f"Enter new contact info (current: {consumer.contact_info}): ")
        consumer.preferences = input(f"Enter new preferences (current: {consumer.preferences}): ")
        session.commit()
        print("Consumer updated successfully.")
    else:
        print("Consumer not found.")

def delete_consumer():
    consumer_id = int(input("Enter Consumer ID to delete: "))
    consumer = session.query(Consumer).filter_by(id=consumer_id).first()
    if consumer:
        session.delete(consumer)
        session.commit()
        print("Consumer deleted successfully.")
    else:
        print("Consumer not found.")

# ==================== MAIN CLI ==========================
def main():
    while True:
        os.system('clear')
        print("Welcome to the Business Management System")
        print("1. Manage Wholesales")
        print("2. Manage Products")
        print("3. Manage Employees")
        print("4. Manage Consumers")
        print("5. Exit")
        main_choice = input("Enter your choice: ")

        if main_choice == '1':
            while True:
                os.system('clear')
                print("1. Add Wholesale")
                print("2. View Wholesales")
                print("3. Update Wholesale")
                print("4. Delete Wholesale")
                print("5. Back to Main Menu")
                choice = input("Enter your choice: ")
                if choice == '1': add_wholesale()
                elif choice == '2': view_wholesales()
                elif choice == '3': update_wholesale()
                elif choice == '4': delete_wholesale()
                elif choice == '5': break
                input("Press Enter to continue...")

        elif main_choice == '2':
            while True:
                os.system('clear')
                print("1. Add Product")
                print("2. View Products")
                print("3. Update Product")
                print("4. Delete Product")
                print("5. Back to Main Menu")
                choice = input("Enter your choice: ")
                if choice == '1': add_product()
                elif choice == '2': view_products()
                elif choice == '3': update_product()
                elif choice == '4': delete_product()
                elif choice == '5': break
                input("Press Enter to continue...")

        elif main_choice == '3':
            while True:
                os.system('clear')
                print("1. Add Employee")
                print("2. View Employees")
                print("3. Update Employee")
                print("4. Delete Employee")
                print("5. Back to Main Menu")
                choice = input("Enter your choice: ")
                if choice == '1': add_employee()
                elif choice == '2': view_employees()
                elif choice == '3': update_employee()
                elif choice == '4': delete_employee()
                elif choice == '5': break
                input("Press Enter to continue...")

        elif main_choice == '4':
            while True:
                os.system('clear')
                print("1. Add Consumer")
                print("2. View Consumers")
                print("3. Update Consumer")
                print("4. Delete Consumer")
                print("5. Back to Main Menu")
                choice = input("Enter your choice: ")
                if choice == '1': add_consumer()
                elif choice == '2': view_consumers()
                elif choice == '3': update_consumer()
                elif choice == '4': delete_consumer()
                elif choice == '5': break
                input("Press Enter to continue...")

        elif main_choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()
