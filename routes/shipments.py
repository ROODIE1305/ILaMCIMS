from fastapi import APIRouter, HTTPException # type: ignore
from utils.supabase_client import get_supabase_client
from models.shipments import see_shipments, add_shipments, update_shipments

router = APIRouter()
supabase = get_supabase_client()

#get method
@router.get("/", response_model= list[see_shipments])
def get_shipments():
   try:
      response = supabase.table("shipments").select("*").execute()
      if response.data is None or len(response.data) == 0:
         raise HTTPException(status_code=404, detail="No shipment found/table empty")
      return response.data
   except Exception as e:
      raise HTTPException(status_code=500, detail="no such table exist")
   
#post method
@router.post('/', response_model= see_shipments)
def post_shipments(new_shipment= add_shipments):
   try:
      response = supabase.table("shipments").insert(new_shipment.dict()).execute()
      if not response.data:
         raise HTTPException(status_code=404, detail="Unable to add new sales channel")
      else:
         print(response.data)
         return {"message": "Shipment added successfully"}
   except Exception as e:
      raise HTTPException(status_code=500, detail="No such table named shipmentss")
   
#put method
@router.put('/{shipment_id}', response_model= see_shipments)
def put_shipments(shipment_id: int, modify_shipment= add_shipments):
   try:
      response = supabase.table("shipments").update(modify_shipment.dict()).eq("id", shipment_id).execute()
      if not response.data:
        raise HTTPException(status_code=404, detail="Unable to update the exiting shipment")
      else:
         print(response.data)
         return {"Message": "Shipment updated successfully"}
   except Exception as e:
      raise HTTPException(status_code=500, detail="No such table named shipments")
   
#delete method
@router.delete('/{shipment_id}')
def delete_shipments(shipment_id: int):
   try:
      response = supabase.table("shipments").delete().eq("id", shipment_id).execute()
      if not response.data or response.data == 0:
         raise HTTPException(status_code=404, detail="Unable to delete target id ")
      else:
         print(response.data)
         return {"message": "Target id deleted successfully"}
   except Exception as e:
      raise HTTPException(status_code=500, detail="No such table named sales channels")
