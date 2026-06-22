from pydantic import BaseModel

class UserDTOCreate(BaseModel):
    name:str
    number:str

class UserDTO(BaseModel):
    id: int
    name:str
    phone:str

    class Config:
        from_attributes = True

class  UserDTOResponse(BaseModel):
    statusCode:int
    message:str
    body:UserDTO

class  UserDTOResponseList(BaseModel):
    statusCode:int
    message:str
    body:list[UserDTO]

class UserDTOUpdate(BaseModel):
    old_number:str
    new_number:str


