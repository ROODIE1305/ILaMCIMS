from fastapi import APIRouter, HTTPException # type: ignore
from backend.utils.supabase_client import get_supabase_client
from backend.models.product_channels import see_product_channels, add_product_channels, update_product_channels

router = APIRouter()
supabase = get_supabase_client()

# GET method
@router.get("/", response_model=list[see_product_channels])
def get_product_channels():
    try:
        response = supabase.table("product_channels").select("*").execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="No product channels available.")
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching product channels: {str(e)}")


# POST method
@router.post("/", response_model=see_product_channels)
def post_product_channels(pro_cha: add_product_channels):
    try:
        response = supabase.table("product_channels").insert(pro_cha.dict()).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Unable to add product channel.")
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating product channel: {str(e)}")


# PUT method
@router.put("/{product_id}", response_model=see_product_channels)
def put_product_channels(product_id: int, update: update_product_channels):
    try:
        response = supabase.table("product_channels").update(update.dict()).eq("product_id", product_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Product channel not found.")
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating product channel: {str(e)}")


# DELETE method
@router.delete("/{product_id}")
def delete_product_channels(product_id: int):
    try:
        response = supabase.table("product_channels").delete().eq("product_id", product_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Product channel ID not found.")
        return {"message": "Product channel deleted successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting product channel: {str(e)}")
