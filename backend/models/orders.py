from pydantic import BaseModel # type: ignore
from datetime import datetime
from decimal import Decimal
from typing import Optional

class see_orders(BaseModel):
    order_id: int
    customer_id: int
    order_date: datetime  
    total_amount: Decimal  
    status: str

    class Config:
        arbitrary_types_allowed = True  
class create_orders(BaseModel):
    customer_id: Optional[int]  
    order_date: Optional[datetime]  
    total_amount: Optional[float]  
    status: Optional[str] = "pending" 

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda v: v.isoformat()  
        }

class update_orders(BaseModel): 
    customer_id: int
    order_date: datetime
    total_amount: Decimal
    status: str

    class Config:
        arbitrary_types_allowed = True
