from fastapi import APIRouter, HTTPException # type: ignore
from utils.supabase_client import get_supabase_client
from models.products import see_products, add_products, update_products

router = APIRouter()
supabase = get_supabase_client()

# Get method
@router.get("/", response_model=list[see_products])
def get_products():
    try:
        response = supabase.table("products").select("*").execute()
        if response.data is None or len(response.data) == 0:  # type: ignore
            raise HTTPException(status_code=404, detail="No products found/table empty")
        return [see_products(**product) for product in response.data]  # Ensuring data matches the model
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching products: {str(e)}")

# Post method
@router.post("/", response_model=see_products)
def post_products(new_products: add_products):
    try:
        response = supabase.table("products").insert(new_products.dict()).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Unable to add new product/products")
        return see_products(**response.data[0])  # Ensuring data matches the model
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding products: {str(e)}")

# Put method
@router.put("/{product_id}", response_model=see_products)
def put_products(product_id: int, change_product: update_products):
    try:
        response = supabase.table("products").update(change_product.dict(exclude_none=True)).eq("product_id", product_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Unable to update the existing product")
        return see_products(**response.data[0])  # Ensuring data matches the model
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating products: {str(e)}")

# Delete method
@router.delete("/{product_id}")
def delete_products(product_id: int):
    try:
        response = supabase.table("products").delete().eq("product_id", product_id).execute()
        if not response.data:  # Fix condition
            raise HTTPException(status_code=404, detail="Unable to delete target id")
        return {"message": "Target id deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting product: {str(e)}")
