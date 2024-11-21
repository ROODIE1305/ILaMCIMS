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
SUPABASE_URL=https://cvkyeqhdiimxroujaojn.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN2a3llcWhkaWlteHJvdWphb2puIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzA5MjEyNzIsImV4cCI6MjA0NjQ5NzI3Mn0.CR3w_pKHwgOP0EwKpljruHoFzoJYkytacHvxFwODYlY
SUPABASE_SERVICE_ROLE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN2a3llcWhkaWlteHJvdWphb2puIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTczMDkyMTI3MiwiZXhwIjoyMDQ2NDk3MjcyfQ.ihPBPuJdxfp7laTxWJYZDMrVHslQItl6X0o_BtS3Gd8

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


