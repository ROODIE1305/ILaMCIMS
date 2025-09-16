from fastapi import APIRouter, HTTPException # type: ignore
from utils.supabase_client import get_supabase_client
from models.orders import see_orders, create_orders, update_orders

router = APIRouter()
supabase = get_supabase_client()

# GET method
@router.get("/", response_model=list[see_orders])
def get_orders():
    try:
        response = supabase.table("orders").select("*").execute()
        if not response.data:  
            raise HTTPException(status_code=404, detail="No current orders found")
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching orders: {str(e)}")

# POST method
@router.post("/", response_model=see_orders)
def post_orders(order: create_orders):
    try:
        response = supabase.table("orders").insert(order.dict(exclude_unset=True)).execute()
        if not response.data:
            raise HTTPException(status_code=400, detail="Unable to create order")
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating order: {str(e)}")

# PUT method
@router.put("/{order_id}", response_model=see_orders)
def put_order_items(order_id: int, new_order: update_orders):
    try:
        response = supabase.table("orders").update(new_order.dict(exclude_none=True)).eq("order_id", order_id).execute() ###ID ISSUE RESOLVE Potential
        if not response.data:
            raise HTTPException(status_code=404, detail="Order not found")
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating order: {str(e)}")

# DELETE method
@router.delete("/{order_id}")
def delete_orders(order_id: int):
    try:
        response = supabase.table("orders").delete().eq("order_id", order_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="No such order found")
        return {"message": "Order deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting order: {str(e)}")
