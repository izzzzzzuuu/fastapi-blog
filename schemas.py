from pydantic import BaseModel, ConfigDict, Field

class PostBase(BaseModel):      # DRY concept 
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=50)

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):   # return from api 
    model_config = ConfigDict(from_attributes=True)

    id: int
    date_posted: str
    # ^ the 2 fields generated from systems


