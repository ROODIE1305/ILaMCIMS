from pydantic import BaseModel # type: ignore
from datetime import datetime
from decimal import Decimal

class see_orders(BaseModel):
    order_id: int
    customer_id: int
    order_date: datetime  # Correct usage of `datetime`
    total_amount: Decimal  # For monetary values
    status: str

    class Config:
        arbitrary_types_allowed = True  # Allows handling of `datetime` and `Decimal`

class create_orders(BaseModel):
    customer_id: int
    order_date: datetime
    total_amount: Decimal
    status: str

    class Config:
        arbitrary_types_allowed = True

class update_orders(BaseModel):  # All fields are required
    customer_id: int
    order_date: datetime
    total_amount: Decimal
    status: str

    class Config:
        arbitrary_types_allowed = True
