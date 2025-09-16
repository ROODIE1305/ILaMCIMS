from pydantic import BaseModel # type: ignore
from pydantic import EmailStr # type: ignore

class see_customers(BaseModel):
    customer_id: int
    name: str
    email: str
    phone: str
    address: str

   #CHECKPOINT
    class Config:
        from_attributes = True

class add_customers(BaseModel):
    name: str
    email: EmailStr
    phone: str 
    address: str

class update_customers(BaseModel):
    name: str
    email: EmailStr
    phone: str
    address: str

