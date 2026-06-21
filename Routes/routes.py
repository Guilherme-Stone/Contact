from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from Controller.userZAPIController import UserZAPIController
from Database.database import db
from Schema.userDTO import UserDTOCreate, UserDTOResponse, UserDTOUpdate
from Controller.userController import UserController



router = APIRouter()

@router.post("/createUser",response_model=UserDTOResponse)
async def createUser(userDto:UserDTOCreate,session: AsyncSession = Depends(db.get_db)):
    userC = UserController()
    res = await userC.createUserC(userDto.name,userDto.number,session=session)
    return {
             "statusCode": 201,
             "message":"User Created",
             "body": res
            }

@router.put("/updateUser",response_model=UserDTOResponse)
async def updateNumber(userDto:UserDTOUpdate,session: AsyncSession = Depends(db.get_db)):
    userC = UserController()
    res = await userC.updateUserC(userDto.old_number,userDto.new_number,session=session)
    return {
        'statusCode': 200,
        "message": "User Updated",
        "body": res
    }

@router.get("/getUser",response_model=UserDTOResponse)
async def sendMessageByNumber(number:str,session: AsyncSession = Depends(db.get_db)):
    userC = UserZAPIController()
    res = await userC.sendMessageByNumberC(number,session)

    return {
        'statusCode': 200,
        "message": "User returned",
        "body": res
    }


@router.get("/getUser", response_model=UserDTOResponse)
async def sendMessageAll(session: AsyncSession = Depends(db.get_db)):
    userC = UserZAPIController()
    res = await userC.sendMessageForAllC(session)

    return {
        'statusCode': 200,
        "message": "User returned",
        "body": res
    }