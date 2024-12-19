### Business Management System - CLI Project
 ### Author: Eugine Odera
 ## Description:
  - This project is a Command-Line Interface (CLI) based Business Management System designed to manage Wholesales, Employees, Products, and Consumers. It allows administrators to perform CRUD operations for all entities and provides an overview of their relationships. This system tracks which wholesalers provide a variety of products to consumers, and how employees contribute to the workflow within the business.

 ### Features
CRUD Operations for managing Wholesales, Employees, Products, and Consumers.
### Database Relationships:
  - Wholesale & Products: One-to-many relationship (One wholesale provides many products).
  - Wholesale & Employees: One-to-many relationship (One wholesale can have many employees).
  - Products & Consumers: Many-to-many relationship (Consumers can consume multiple products).
  - Consumers & Wholesale: Indirect relationship through products (Consumers buy from wholesalers via products).
 ### Technologies Used
 - SQLAlchemy: ORM for interacting with the database.
 - Alembic: For database migrations.
 - SQLite: Lightweight database for development.
 - Python: Programming language for the application logic.
 
## Usage
The application provides a menu-driven interface that allows administrators to:

1. Manage Technical Instructors: Add, view, update, and delete instructors.
2. Manage Courses: Add, view, update, and delete courses.
3. Manage Students: Add, view, update, and delete students.

## LICENSE
This project is licensed under the MIT License - see the LICENSE file for details.

