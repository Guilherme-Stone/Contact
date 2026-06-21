from httpx import HTTPStatusError
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.asyncio import AsyncSession
import httpx
from Model.Entity.user import User
from Services.Exceptions.userException import UserException
from Services.userService import UserService
from Services.userZAPIService import UserZapiService


class UserZAPIController:

    def __init__(self):
        self.service = UserZapiService()

    async def sendMessageByNumberC(self,number:str,session:AsyncSession)->str:
         try:
             res = await self.service.sendMessageByNumberS(number,session)
             return res
         except OperationalError as oe:
             print(f"Could not get user from the database [status->{oe}]")
         except httpx.ConnectError as ce:
             print(f"Something went wrong with your connection and the server [status->{ce}]")
         except httpx.HTTPStatusError as he:
             print(f"Failed to find the user [status->{he}]")
         except UserException as ue:
                print(ue)

    async def sendMessageForAllC(self,session: AsyncSession) -> str:
        try:
            res = await self.service.sendMessageForAllS(session)
            return res
        except OperationalError as oe:
            print(f"Could not get user from the database [status->{oe}]")
        except httpx.ConnectError as ce:
            print(f"Something went wrong with your connection and the server [status->{ce}]")
        except httpx.HTTPStatusError as he:
            print(f"Failed to find the user [status->{he}]")
