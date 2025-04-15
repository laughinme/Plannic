from pydantic import BaseModel

class ORMModel(BaseModel):
    pass

    class Config():
        from_attributes = True