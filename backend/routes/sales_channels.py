from fastapi import APIRouter, HTTPException # type: ignore
from utils.supabase_client import get_supabase_client
from models.sales_channels import see_sales_channels, add_sales_channels, update_sales_channels 

router = APIRouter()
supabase = get_supabase_client()

#get method
@router.get("/", response_model= list[see_sales_channels])
def get_sales_channels():
   try:
      response = supabase.table("sales_channels").select("*").execute()
      if response.data is None or len(response.data) == 0:
         raise HTTPException(status_code=404, detail="No sales channel found/table empty")
      return response.data
   except Exception as e:
      raise HTTPException(status_code=500, detail="no such table exist")
   
#post method
@router.post("/", response_model=see_sales_channels)
def post_sales_channels(new_channel: add_sales_channels):
    try:
        response = supabase.table("sales_channels").insert(new_channel.dict()).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Unable to add new sales channel")
        return response.data[0]  
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

   
#put method
@router.put("/{channel_id}", response_model=see_sales_channels)
def put_sales_channels(channel_id: int, change_product: update_sales_channels):
    try:
        response = supabase.table("sales_channels").update(change_product.dict()).eq("channel_id", channel_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Unable to update the existing channel")
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

   
#delete method
@router.delete("/{channel_id}")
def delete_sales_channels(channel_id: int):
    try:
        response = supabase.table("sales_channels").delete().eq("channel_id", channel_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Target ID not found.")
        return {"message": "Target ID deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
