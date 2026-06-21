import os
from Model.Repository.userRepository import UserRepository
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession
import httpx
from Services.Exceptions.userException import UserException

load_dotenv()

class UserZapiService:
    def __init__(self):
        self.repo = UserRepository()
        self.token = os.getenv("ZAPITOKEN")
        self.id = os.getenv("ZAPIID")

        # use ZAPI
    async def sendMessageByNumberS(self,number_to_recive:str,session:AsyncSession)->str:

        user = await self.repo.getUserByNumber(number_to_recive,session=session)

        if user is None:
            raise UserException("User not found")

        url = f"https://api.z-api.io/instances/{self.id}/token/{self.token}/send-text"

        async with httpx.AsyncClient() as client:
            response = await client.post(
                url=url,
                headers={
                    "Client-Type": "application/json"
                },
                json={
                      "phone": f"{number_to_recive}",
                      "message": f"Olá, {user.name} tudo bem com você?"
                      }
            )

        response.raise_for_status()

        return response.json()


    async def sendMessageForAllS(self,session:AsyncSession)->str:
        listUsers =  await self.repo.getAllUsers(session=session)

        for user in listUsers:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    url=f"https://api.z-api.io/instances/{self.id}/token/{self.token}/send-text",
                    headers={
                        "Client-Type":"application/json"
                    },
                    json={
                        "phone":f"{user.phone}",
                        "message": f"Olá, {user.name} tudo bem com você?"
                    }
                )
        return response.json()
