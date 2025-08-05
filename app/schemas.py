from pydantic import BaseModel, Field

class Item(BaseModel):
    prod_name: str 
    category: str 
    current_amount: float 
    target_amount: float 
    threshold_amount: float 
    tags: str 
    notes: str 

class ItemQuery(BaseModel):
    prod_name: str = Field(..., description="Product name")
    category: str = Field(..., description="Category of the product")
    current_amount: float = Field(..., description="Current amount of the product")
    target_amount: float = Field(..., description="Desireable amount of the product")	
    threshold_amount: float = Field(..., description="Limit amount of the product after which the user should be notified")	
    tags: str = Field(..., description="Tags of the product (separated by | (vertical line))")
    notes: str = Field(..., description="Notes about the product")
