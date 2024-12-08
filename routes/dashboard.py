from fastapi import APIRouter, HTTPException # type: ignore
from utils.supabase_client import get_supabase_client

router = APIRouter()
supabase = get_supabase_client()

@router.get("/stats")
async def get_dashboard_stats():
    print("Dashboard stats endpoint hit")  
    try:
        # total products
        products_response = supabase.table("products").select("*").execute()
        total_products = len(products_response.data) if products_response.data else 0

        # active orders
        orders_response = supabase.table("orders").select("*").execute()
        active_orders = len(orders_response.data) if orders_response.data else 0

        # sales channels
        sales_channels_response = supabase.table("sales_channels").select("*").execute()
        total_sales_channels = len(sales_channels_response.data) if sales_channels_response.data else 0

        # total customers
        customers_response = supabase.table("customers").select("*").execute()
        total_customers = len(customers_response.data) if customers_response.data else 0

        return {
            "total_products": total_products,
            "active_orders": active_orders,
            "sales_channels": total_sales_channels,
            "total_customers": total_customers
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching dashboard stats: {str(e)}")
