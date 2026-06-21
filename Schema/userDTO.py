from pydantic import BaseModel

class UserDTOCreate(BaseModel):
    name:str
    number:str

class  UserDTOResponse(BaseModel):
    statusCode:str
    message:str
    body:UserDTOCreate

class UserDTOUpdate(BaseModel):
    old_number:str
    new_number:str
