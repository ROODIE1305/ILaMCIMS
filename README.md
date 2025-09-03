# Integrated Logistics and Multi-Channel Inventory Management Software (ILaMCIMS)

## **Overview**
ILaMCIMS is a Python-based software solution designed to streamline logistics and inventory management for businesses operating across multiple sales channels like Amazon, Flipkart, and Meesho. The software simplifies tasks such as inventory tracking, real-time delivery monitoring, and automated returns processing.  

The project is being developed incrementally, with each phase focusing on a specific feature set or technical foundation.  

---

## **Key Features**  
1. **Centralized Inventory Management**: Manage inventory levels across multiple channels from a single platform.  
2. **Real-Time Tracking**: Monitor live delivery progress, giving customers the ability to track their orders in real-time.  
3. **Inventory Forecasting** (Planned): Utilize basic machine learning to analyze sales trends and recommend which products are in high demand or declining in popularity.  
4. **Automated Returns Processing** (Planned): Streamline and automate the process of handling returns, ensuring quick and efficient resolution.  
5. **Sales and Purchase Reports**: Generate detailed analytics for business insights.  

---

## **Scope of the Project**  
ILaMCIMS aims to address the following:  
- Optimize inventory handling for businesses with a single supplier and multiple sales channels.  
- Provide tools for real-time order and delivery tracking.  
- Automate inventory forecasting to help businesses make data-driven decisions.  
- Simplify returns processing to enhance customer satisfaction.  
- Enable seamless integration with third-party e-commerce platforms.  

This software is ideal for small to medium-scale businesses dealing with low-to-moderate order volumes.  

---
## **Development Phases**
The project is being developed in distinct phases, with a focus on learning and implementation at each stage:

### **Completed Phases**

#### **Phase 1: Define Project Scope and Requirements**
- **Learning**: 
   - **Project scoping**: Understanding the problem and defining the solution.
   - **Agile Development**: Organizing the project into manageable phases.
   - **Project Milestones**: Setting goals for each phase and identifying necessary resources.
- **Practice**: 
   - Defined features and functionalities for the software.
   - Established a timeline and identified key technologies for backend and database management.

#### **Phase 2: Set Up Development Environment**
- **Learning**:
   - **Version Control**: Using Git for version control.
   - **IDE Setup**: Setting up VS Code for Python development.
   - **Project Structuring**: Organizing the project directory and files.
- **Practice**: 
   - Initialized the Git repository and committed the initial project structure.
   - Created folder structures for organizing the project: `models`, `routes`, `scripts`, `services`, `utils`.

#### **Phase 3: Database Design (SQL)**
- **Learning**:
   - **Database Schema Design**: Understanding how to structure data for business needs.
   - **Entity-Relationship Diagrams (ERD)**: Visualizing relationships between tables and entities.
   - **SQL Basics**: Learning how to write SQL queries for creating tables and inserting data.
- **Practice**: 
   - Designed the database schema, which includes the following tables:
     - `customers`, `order_items`, `orders`, `product_channels`, `products`, `sales_channels`, `shipments`.
   - Implemented basic SQL operations like `CREATE`, `INSERT`, `SELECT`, `UPDATE`.

#### **Phase 4: Build the Database (SQL)**
- **Learning**:
   - **SQL Operations**: Deep dive into SQL for database operations like joins, queries, and indexing.
   - **Query Optimization**: Writing efficient queries for data retrieval.
- **Practice**:
   - Created and populated tables in PostgreSQL (Supabase).
   - Used SQL queries to fetch and modify data from the database, ensuring smooth integration with the backend.
   - 
 ![dd](https://github.com/user-attachments/assets/be6feb0a-45b4-4f52-b13a-cfc246a85efc)

  
#### **Phase 5: Backend Development - Basic API in FastAPI**
- **Learning**:
   - **FastAPI Framework**: Building REST APIs using FastAPI for handling CRUD operations.
   - **Routing**: Creating routes to handle API requests and organizing them using routers.
   - **PostgreSQL Integration**: Connecting FastAPI with a PostgreSQL database (Supabase).
   - **Handling JSON**: Understanding request and response formats for APIs.
- **Practice**:
   - Developed backend APIs to handle CRUD operations for the following resources:
     - `products`, `orders`, `order_items`, `customers`, `sales_channels`, `product_channels`, `shipments`.
   - Implemented GET, POST, PUT, and DELETE operations for each table.
   - Tested API endpoints to ensure the functionality of the database interactions.

---

### **Current Status**
- **Phase 6**: Frontend development is **in progress**, with core UI elements for inventory management being designed and implemented.
- **Phase 7 onwards**: Upcoming phases, including real-time tracking, inventory forecasting, and integration features, are under development.

---

### **Learnings So Far**

#### **Phase 1: Define Project Scope and Requirements**
- Gained insights into defining the project’s features and scope.
- Understood how to break down a project into manageable phases and tasks.

#### **Phase 2: Set Up Development Environment**
- Learned to structure a project and organize files in a way that supports scalability.
- Mastered setting up version control with Git to track and manage changes in the project.

#### **Phase 3: Database Design (SQL)**
- Designed an efficient relational database schema using SQL.
- Understood the importance of properly structuring tables and relationships for ease of data retrieval and manipulation.

#### **Phase 4: Build the Database (SQL)**
- Refined SQL querying skills to handle data in real-time applications.
- Implemented database population and data verification through queries.

#### **Phase 5: Backend Development - Basic API in FastAPI**
- Learned to build RESTful APIs with FastAPI to handle CRUD operations.
- Gained experience integrating FastAPI with a PostgreSQL database hosted on Supabase.
- Familiarized with API testing tools (Postman, cURL) for verifying endpoint functionality.

---

### **Tools and Technologies Used**
- **Backend**: 
   - **Python**: Core programming language for backend development.
   - **FastAPI**: Framework for building APIs.
   - **PostgreSQL**: Relational database system, used in combination with **Supabase** for cloud hosting.
   - **Uvicorn**: ASGI server to run FastAPI applications.
   - **cURL/Postman**: Tools used for testing API endpoints.

- **Version Control**: 
   - **Git**: Used for version control and collaboration.

- **Database Management**:
   - **Supabase**: PostgreSQL as a managed service for database hosting.

## **Setup and Usage Instructions**  

### **1. Backend Setup**  
#### Prerequisites:  
- Python installed on your system.  
- PostgreSQL database hosted on Supabase.  
- Git installed.  

#### Steps:  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/ILaMCIMS.git
   cd ILaMCIMS

2.Create a Virtual Environment:
python -m venv ILaMCIMS
source ILaMCIMS/bin/activate  # On Windows: ILaMCIMS\Scripts\activate

3.Install Project Dependencies:
pip install -r requirements.txt

4.Set Up Environment Variables:
Create a .env file in the project directory and add the following variables:
SUPABASE_URL=#your_supabase_url
SUPABASE_KEY=#your_supabse_public_key
SUPABASE_SERVICE_ROLE_KEY=#optional

Note: Make sure to iclude your .env file in .gitignore

5.Run Database Migrations (if applicable):
alembic upgrade head  # Or the specific migration tool for the project

6.Start the Backend Server:
uvicorn main:app --reload

### **Next Steps After Starting the Server**

1. **Access the API Documentation**:
   Once the server is running, you can visit the automatically generated documentation page by opening your browser and navigating to:
   http://localhost:8000/docs
This page provides an interactive API documentation, where you can test each of the available API endpoints directly.

2. **API Endpoints**:
The FastAPI app includes several routes based on the routers you've registered in the `main.py` file. These are grouped by their respective prefixes:
- **Customers**: `/customers`
- **Order Items**: `/order_items`
- **Products**: `/products`
- **Orders**: `/orders`
- **Product Channels**: `/product_channels`
- **Sales Channels**: `/sales_channels`
- **Shipments**: `/shipments`

3. **Performing CRUD Operations**:
You can use the API documentation to interact with each of the endpoints (GET, POST, PUT, DELETE) for managing the resources. Here's how you can interact with each:
- **GET**: Retrieve data, such as all products or orders.
- **POST**: Add new records, such as creating a new customer or adding an order.
- **PUT**: Update existing records, like modifying a product’s price or quantity.
- **DELETE**: Remove records, such as deleting an order item.

For example, to view all products, you would navigate to:
http://localhost:8000/products

yaml
Copy code
Or use the **POST** method to add a new product by providing the required details.

4. **Testing the API with cURL/Postman**:
Alternatively, you can use tools like **cURL** or **Postman** to manually make requests to the API. For example:
- **GET** request to retrieve all products:
  ```bash
  curl http://localhost:8000/products
  ```
- **POST** request to add a new product:
  ```bash
  curl -X 'POST' \
    'http://localhost:8000/products' \
    -H 'Content-Type: application/json' \
    -d '{
    "name": "New Product",
    "quantity": 10,
    "price": 50
  }'
  ```

5. **Verify Data in Supabase**:
After making requests to the API (such as adding or updating records), you can log into your Supabase dashboard and check the corresponding tables (like `products`, `orders`, etc.) to ensure that the data is being stored and updated as expected.

---

### **Conclusion**
By visiting the API documentation at `http://localhost:8000/docs`, you can easily interact with your FastAPI application, perform CRUD operations on the database, and check that everything is working properly.

---

## **Technology Stack**
- **Backend**: Python, FastAPI
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: PostgreSQL (hosted on Supabase)
- **Map Integration**: Google Maps API for real-time tracking

---

## **Future Plans**
1. Real-time tracking system implementation.
2. Advanced inventory forecasting using machine learning.
3. Seamless integration with third-party platforms.
4. Deployment on cloud platforms like Heroku or AWS.

---

**Note**: This project is a work in progress, and the current features are limited to Phase 6.

<<<<<<< HEAD
=======

>>>>>>> b94ef631f5333295580cdf46980188a68e34c9a4
