from fastapi import APIRouter, HTTPException # type: ignore
from utils.supabase_client import get_supabase_client
from models.customers import Customers, CustomersCreate, CustomersUpdate

router = APIRouter()
supabase = get_supabase_client()

#Get method
@router.get("/", response_model=list[Customers])
def get_customers():
    try:
        response = supabase.table("customers").select("*").execute()
        if response.data is None or len(response.data) == 0: # type: ignore 
            raise HTTPException(status_code=404, detail="No customers found in the table")
        customers = [Customers(**customer) for customer in response.data]
        return customers
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching customers or no such table with that name: {str(e)}")

#post method
@router.post("/", response_model=Customers)
def create_customers(Customer: CustomersCreate):
    try:
        # Insert data without customer_id, which is auto-generated in the database
        response = supabase.table("customers").insert(Customer.dict(exclude_unset=True)).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Failed to add the new customer")
        return response.data[0]  # Return the created customer
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating customer: {str(e)}")

#put method
@router.put("/{customer_id}", response_model= Customers)
def modify_customers(customer_id: int, Customers_change: CustomersUpdate):
    try:
        #checkpoint
        response = supabase.table("customers").update(Customers_change.dict(exclude_none=True)).eq("customer_id", customer_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Customer not found")
        return {
            "message": "Customer details updated successfully",
            "updated_customer": response.data[0]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"/Unable to modify the customer data: {str(e)}")
    
#delete method
@router.delete("/{customer_id}")
def delete_customers(customer_id: int):
    try:
        #checkpoint
        response = supabase.table("customers").delete().eq("customer_id", customer_id).execute()
        if response.data == 0:
            raise HTTPException(status_code=404, detail="No such customer")
        return {"message": "Customer data removed suceesfully"}
    except  Exception as e:
        raise HTTPException(status_code=500, detail=f"Some error occured, unable to delete the data: {str(e)}")
        