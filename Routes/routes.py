from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from Database.database import db
from Schema.userDTO import UserDTOCreate, UserDTOResponse, UserDTOUpdate, UserDTOResponseList
from Services.userZAPIService import UserZapiService
from Services.userService import UserService

router = APIRouter()

@router.post("/createUser",response_model=UserDTOResponse)
async def createUser(userDto:UserDTOCreate,session: AsyncSession = Depends(db.get_db)):
    try:
        userS = UserService()
        res = await userS.createUserS(userDto.name,userDto.number,session=session)
        return {
                 "statusCode": 201,
                 "message":"User Created",
                 "body": res
                }
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))

@router.put("/updateUser",response_model=UserDTOResponse)
async def updateNumber(userDto:UserDTOUpdate,session: AsyncSession = Depends(db.get_db)):
    try:
        userS = UserService()
        res = await userS.updateUserS(userDto.old_number,userDto.new_number,session=session)
        return {
            'statusCode': 200,
            "message": "User Updated",
            "body": res
        }
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))


@router.get("/getUser",response_model=UserDTOResponse)
async def sendMessageByNumber(number:str,session: AsyncSession = Depends(db.get_db)):
    try:
        userS = UserZapiService()
        res = await userS.sendMessageByNumberS(number,session)

        return {
            'statusCode': 200,
            "message": "User returned",
            "body": res
        }
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))


@router.get("/getAllUser", response_model=UserDTOResponseList)
async def sendMessageAll(session: AsyncSession = Depends(db.get_db)):
    try:
        userC = UserZapiService()
        res = await userC.sendMessageForAllS(session)
        return {
            'statusCode': 200,
            "message": "User returned",
            "body": res
        }
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))