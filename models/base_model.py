#!/usr/bin/python3
import uuid
from datetime  import datetime as dt
import o
class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = dt.now()
        self.updated_at = dt.now()
    
    def __str__(self):
        return f"[{self.__class__.__name__}], ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = dt.now()
    
    def to_dict(self):
        defDict = self.__dict__.copy()
        defDict["__class__"] = self.__dict__.__class__
        defDict["created_at"] = self.created_at.isoformat()
        defDict["updated_at"] = self.updated_at.isoformat()
        return defDict

B = BaseModel()
print (B.id)
print (B.updated_at)
