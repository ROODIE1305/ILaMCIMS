# Integrated Logistics and Multi-Channel Inventory Management Software (ILaMCIMS)

## **Overview**
ILaMCIMS is a Python-based software solution designed to streamline logistics and inventory management for businesses operating across multiple sales channels like Amazon, Flipkart, and Meesho. The software simplifies tasks such as inventory tracking, real-time delivery monitoring, and automated returns processing.  

The project is being developed incrementally, with each phase focusing on a specific feature set or technical foundation.  

---

## **Key Features**  
1. **Centralized Inventory Management**: Manage inventory levels across multiple channels from a single platform.  
2. **Real-Time Tracking**: Monitor live delivery progress (under development).  
   - **General Tracking**: Customers can track their orders in real-time, seeing the general location (city, area) of the delivery agent.  
   - **Exact Tracking**: Once a specific delivery is assigned (e.g., for customer A1), they will be able to see the precise location of the delivery agent in real-time. The exact tracking system is exclusive to the customer whose order is being delivered at that moment.  
3. **Sales and Purchase Reports**: Generate detailed analytics for business insights.  
4. **User-Friendly Interface**: A clean, intuitive frontend using HTML, CSS, JavaScript, and Bootstrap.  

---

## **Scope of the Project**  
ILaMCIMS aims to address the following:  
- Optimize inventory handling for businesses with a single supplier and multiple sales channels.  
- Provide tools for real-time order and delivery tracking, including both general and exact tracking options.  
- Automate inventory forecasting and returns processing.  
- Enable seamless integration with third-party e-commerce platforms.  

This software is ideal for small to medium-scale businesses dealing with low-to-moderate order volumes.  

---

## **Development Phases**  
The project is being developed in distinct phases, with a focus on learning and implementation at each stage:  

### **Completed Phases**  
#### **Phase 1: Define Project Scope and Requirements**  
- **Learning**: Project scoping, agile development basics.  
- **Practice**: Defined features, created project timeline and milestones.  

#### **Phase 2: Set Up Development Environment**  
- **Learning**: Git version control, IDE setup (VS Code), project structuring.  
- **Practice**: Initialized Git repository and structured project folders.  

#### **Phase 3: Database Design (SQL)**  
- **Learning**: ER diagram creation, SQL basics.  
- **Practice**: Designed schema for inventory, orders, and logistics tracking.  

#### **Phase 4: Build the Database (SQL)**  
- **Learning**: Advanced SQL operations, query optimization.  
- **Practice**: Created complex queries to fetch inventory and shipment data.  

#### **Phase 5: Backend Development - Basic API in FastAPI**  
- **Learning**: REST API basics, FastAPI framework.  
- **Practice**: Developed APIs for managing products and inventory.  

#### **Phase 6: Frontend Basics (HTML/CSS/JavaScript/Bootstrap)**  
- **Learning**: Basics of web development using HTML, CSS, JavaScript, and Bootstrap.  
- **Practice**:  
  - Designed a UI to display and manage inventory.  
  - Created sections for Dashboard, Inventory, Orders, Sales Channels, and Reports.  

---

### **Current Status**  
- **Phase 6**: Frontend development is **in progress**, with core UI elements for inventory management being designed and implemented.  
- **Phase 7 onwards**: Upcoming phases, including real-time tracking (General and Exact), inventory forecasting, and integration features, are under development.  

---

### **Learnings So Far**  
- Fundamentals of agile project planning and scoping.  
- SQL schema design   
- REST API development using FastAPI.  
- Frontend basics with a focus on Bootstrap for responsive design.  

---

### **Real-Time Tracking (General and Exact Tracking)**  

As part of the delivery tracking system, two types of tracking are being implemented:  

1. **General Tracking**:  
   - Customers can track their orders by receiving updates on the general location of the delivery agent (such as city or area).  
   - This provides a high-level view of the delivery status, allowing customers to know when their package is in their vicinity.  

2. **Exact Tracking**:  
   - When the delivery agent starts delivering a specific order (e.g., for customer A1), that customer will be able to see the precise, real-time location of the delivery agent.  
   - **Exclusive Tracking**: This exact tracking is exclusive to the customer whose order is being delivered. For example, while A1 can see the agent's exact location, customers A2 through A20 will only see the general location.  
   - As the delivery agent completes each delivery, the next customer (e.g., A2) will be able to start tracking the agent's exact location.  
   - This ensures that each customer gets a personalized and secure tracking experience.  

---

## **Technology Stack**  
- **Backend**: Python, FastAPI  
- **Frontend**: HTML, CSS, JavaScript, Bootstrap  
- **Database**: PostgreSQL (hosted on Supabase)  
- **Map Integration**: Google Maps API for real-time tracking  

---


---

## **Future Plans**  
1. Real-time tracking system (General and Exact) implementation.  
2. Advanced inventory forecasting using machine learning.  
3. Seamless integration with third-party platforms.  
4. Deployment on cloud platforms like Heroku or AWS.  

---

## **Contributions and Feedback**  
Contributions and feedback are welcome! Please feel free to raise issues or submit pull requests to improve the project.

---

**Note**: This project is a work in progress, and the current features are limited to Phase 6. Future updates will expand functionality significantly.
