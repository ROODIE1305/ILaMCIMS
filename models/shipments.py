from pydantic import BaseModel # type: ignore
from datetime import datetime

class see_shipments(BaseModel):
    shipment_id: int
    order_id: int
    shipment_date: datetime
    delivery_date: datetime
    status: str
    tracking_number: str

    class Config:
        arbitrary_types_allowed = True

class add_shipments(BaseModel):
    order_id: int
    shipment_date: datetime
    delivery_date: datetime
    status: str
    tracking_number: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda dt: dt.isoformat()  
        }

class update_shipments(BaseModel):
    order_id: int
    shipment_date: datetime
    delivery_date: datetime
    status: str
    tracking_number: str

    class Config:
        arbitrary_types_allowed = True
     