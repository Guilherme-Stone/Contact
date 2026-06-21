from httpx import HTTPStatusError
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.asyncio import AsyncSession
import httpx
from Model.Entity.user import User
from Services.userService import UserService
from Services.Exceptions.userException import UserException


class UserController:

    def __init__(self):
        self.service = UserService()


    async def createUserC(self,name:str,number:str,session:AsyncSession)->User:

        try:
            user = await self.service.createUserS(name=name,number=number,session=session)
            return user

        except httpx.ConnectError as he:
            print(f"Something went wrong with your connection and the server [status->{he}]")

        except Exception as e:
            print(e)

        except OperationalError as oe:
            print(f"Could not create user [status->{oe}]")


    async def updateUserC(self,old_number:str,new_number:str,session:AsyncSession)->User:
        try:
            user = await self.service.updateUserS(old_number,new_number,session=session)
            return user
        except httpx.ConnectError as e:
            print(f"Something went wrong with your connection and the server [status->{e}]")
        except OperationalError as oe:
            print(f"Could not update the user number [status->{oe}]")
        except httpx.HTTPStatusError as he:
            print(f"Failed to find the user [status->{he}]")
