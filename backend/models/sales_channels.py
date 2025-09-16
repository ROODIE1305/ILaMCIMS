from pydantic import BaseModel # type: ignore

class see_sales_channels(BaseModel):
    channel_id: int
    channel_name: str



class add_sales_channels(BaseModel):
    channel_name: str
    

class update_sales_channels(BaseModel):
    channel_name: str
    