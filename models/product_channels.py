from pydantic import BaseModel # type: ignore
from decimal import Decimal

class see_product_channels(BaseModel):
    product_id: int
    channel_id: int
    channel_price: Decimal
    discount: Decimal

    class Config:
        arbitrary_types_allowed = True  # Allows `Decimal` for precise monetary values


class add_product_channels(BaseModel):
    channel_id: int
    channel_price: Decimal
    discount: Decimal

    class Config:
        arbitrary_types_allowed = True


class update_product_channels(BaseModel):  # All fields required for updates
    channel_id: int
    channel_price: Decimal
    discount: Decimal

    class Config:
        arbitrary_types_allowed = True
