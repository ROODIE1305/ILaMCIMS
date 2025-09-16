from pydantic import BaseModel # type: ignore

class see_products(BaseModel):
    product_id: int
    product_name: str
    sku: str
    price: float
    discount: float
    stock: int
    category: str

class add_products(BaseModel):
    product_name: str
    sku: str
    price: float
    discount: float
    stock: int
    category: str

class update_products(BaseModel):
    product_name: str
    sku: str
    price: float
    discount: float
    stock: int
    category: str
