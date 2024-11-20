from pydantic import BaseModel, Field # type: ignore
from decimal import Decimal

class see_order_items(BaseModel):
    order_item_id: int
    order_id: int
    product_id: int
    quantity: int
    price: float
    item_discount: Decimal = Field(default=Decimal('0.00'), decimal_places=2)

class create_order_items(BaseModel):
    order_id: int
    product_id: int
    quantity: int
    price: float
    item_discount: Decimal = Field(default=Decimal('0.00'), decimal_places=2)

class update_order_items(BaseModel):
    order_id: int
    product_id: int
    quantity: int
    price: float
    item_discount: Decimal = Field(default=Decimal('0.00'), decimal_places=2)


