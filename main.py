from fastapi import FastAPI # type: ignore
from routes import customers, order_items, products, orders, product_channels, sales_channels, shipments

app = FastAPI()

# Register routers
app.include_router(customers.router, prefix="/customers")
app.include_router(order_items.router, prefix="/order_items")
app.include_router(products.router, prefix="/products")
app.include_router(orders.router, prefix="/orders")
app.include_router(product_channels.router, prefix="/product_channels")
app.include_router(sales_channels.router, prefix="/sales_channels")
app.include_router(shipments.router, prefix="/shipments")
