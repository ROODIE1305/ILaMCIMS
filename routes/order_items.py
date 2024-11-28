from fastapi import APIRouter, HTTPException # type: ignore
from utils.supabase_client import get_supabase_client
from models.order_items import see_order_items, create_order_items, update_order_items

router = APIRouter()
supabase = get_supabase_client()

#get method
@router.get("/", response_model=list[see_order_items])
def get_order_items():
    try:
        response = supabase.table("order_items").select("*").execute()
        if response.data is None or len(response.data) == 0: # type: ignore 
            raise HTTPException(status_code=404, detail="No item found that has been ordered")
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching ordered or no such table with that name: {str(e)}")

#post method
@router.post("/", response_model= see_order_items)
def post_order_items(items_ordered: create_order_items):
   try:
       response = supabase.table("order_items").insert(items_ordered.dict(exclude_unset=True)).execute()
       if not response.data:
         raise HTTPException(status_code=404, detail="Unable to add new ordered item")
       return response.data[0] #checkpoint
   except Exception as e:
       raise HTTPException(status_code=500, detail=f"Error creating look into the code: {str(e)}")

#put method
@router.put("/{order_item_id}", response_model= see_order_items)
def put_order_items(order_item_id: int, new_oder_item: update_order_items):
    try:
        #checkpoint
        response = supabase.table("order_items").update(new_oder_item.dict(exclude_none=True)).eq("id", order_item_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Customer not found")
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"/Unable to modify the customer data: {str(e)}")
    
#delete method
@router.delete("/{order_item_id}")
def delete_order_items(order_item_id: int):
    try:
        #checkpoint
        response = supabase.table("order_items").delete().eq("id", order_item_id).execute()
        if response.data == 0:
            raise HTTPException(status_code=404, detail="No such item has been ordered")
        return {"message": "ordered items data removed suceesfully"}
    except  Exception as e:
        raise HTTPException(status_code=500, detail=f"Some error occured, unable to delete the data: {str(e)}")