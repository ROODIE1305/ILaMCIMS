from pydantic import BaseModel # type: ignore
from pydantic import EmailStr # type: ignore

class Customers(BaseModel):
    customer_id: int
    name: str
    email: str
    phone: str
    address: str

   #CHECKPOINT
    class Config:
        from_attributes = True

class CustomersCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str 
    address: str

class CustomersUpdate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    address: str

