from fastapi import APIRouter, HTTPException  # type: ignore
from backend.utils.supabase_client import get_supabase_client
from backend.models.customers import see_customers, add_customers, update_customers

router = APIRouter()
supabase = get_supabase_client()

# Get method
@router.get("/", response_model=list[see_customers])
async def get_customers():
    try:
        response = supabase.table("customers").select("*").execute()
        if response.data is None or len(response.data) == 0:
            raise HTTPException(status_code=404, detail="No customers found/table empty")
        return [see_customers(**customer) for customer in response.data]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching customers: {str(e)}")

# Post method
@router.post("/", response_model=see_customers)
async def post_customers(new_customers: add_customers):
    try:
        response = supabase.table("customers").insert(new_customers.dict()).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Unable to add new customer")
        return see_customers(**response.data[0])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding customers: {str(e)}")

# Put method
@router.put("/{customer_id}", response_model=see_customers)
async def put_customers(customer_id: int, change_customer: update_customers):
    try:
        response = supabase.table("customers").update(change_customer.dict(exclude_none=True)).eq("customer_id", customer_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Unable to update the existing customer")
        return see_customers(**response.data[0])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating customers: {str(e)}")

# Delete method
@router.delete("/{customer_id}")
async def delete_customers(customer_id: int):
    try:
        response = supabase.table("customers").delete().eq("customer_id", customer_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Unable to delete target id")
        return {"message": "Target id deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting customer: {str(e)}")
        