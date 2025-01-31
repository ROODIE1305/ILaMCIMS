from fastapi import FastAPI, Request # type: ignore
from routes import customers, order_items, products, orders, product_channels, sales_channels, shipments, dashboard
from fastapi.responses import HTMLResponse # type: ignore
from fastapi.templating import Jinja2Templates # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from routes import dashboard  
import os

app = FastAPI() 

templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "Frontend")) 


app.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    stats = await dashboard.get_dashboard_stats() 
    return templates.TemplateResponse("index.html", {"request": request, "stats": stats})

@app.get("/dashboard", response_class=HTMLResponse)
async def read_root(request: Request):
    stats = await dashboard.get_dashboard_stats()  
    return templates.TemplateResponse("index.html", {"request": request, "stats": stats})

@app.get("/Products.html", response_class=HTMLResponse)
async def read_products(request: Request):
    products_data = await products.get_products()  
    return templates.TemplateResponse("Products.html", {"request": request, "products": products_data})

@app.get("/index.html", response_class=HTMLResponse)
async def read_dashboard(request: Request):
    stats = await dashboard.get_dashboard_stats()  # dashboard 
    return templates.TemplateResponse("index.html", {"request": request, "stats": stats})

@app.get("/Customers.html", response_class=HTMLResponse)
async def read_customers(request: Request):
    try:
        customers_data = await customers.get_customers()  
        return templates.TemplateResponse("Customers.html", {"request": request, "customers": customers_data})
    except Exception as e:
        return HTMLResponse(content=f"Error fetching customers: {str(e)}", status_code=500)

@app.get("/Orders.html", response_class=HTMLResponse)
async def read_orders(request: Request):
    orders_data = orders.get_orders()  
    return templates.TemplateResponse("Orders.html", {"request": request, "orders": orders_data})

@app.get("/Order Items.html", response_class=HTMLResponse)
async def read_order_items(request: Request):
    order_items_data = order_items.get_order_items()  
    return templates.TemplateResponse("Order Items.html", {"request": request, "order_items": order_items_data})

@app.get("/Product Channel.html", response_class=HTMLResponse)
async def read_product_channels(request: Request):
    product_channels_data = product_channels.get_product_channels()  
    return templates.TemplateResponse("Product Channel.html", {"request": request, "product_channels": product_channels_data})

# Register routers
app.include_router(customers.router, prefix="/customers")
app.include_router(order_items.router, prefix="/order_items")
app.include_router(products.router, prefix="/products")
app.include_router(orders.router, prefix="/orders")
app.include_router(product_channels.router, prefix="/product_channels")
app.include_router(sales_channels.router, prefix="/sales_channels")
app.include_router(shipments.router, prefix="/shipments")
app.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])

