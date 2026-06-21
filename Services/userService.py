from Model.Repository.userRepository import UserRepository
from Model.Entity.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from Services.Exceptions.userException import UserException

class UserService:

    def __init__(self):
        self.repo = UserRepository()

    async def createUserS(self,name:str,number:str,session:AsyncSession)-> User:
        result = await self.repo.getUserByNumber(number=number,session=session)

        if result is not None:
            raise Exception("User already exists")

        user = User(name=name,phone=number)
        await self.repo.addUser(user,session)
        return user

    async def updateUserS(self,old_number:str,new_number:str,session:AsyncSession)-> User:
        result = await self.repo.updateUser(old_number=old_number,numberUpdated=new_number,session=session)
        return result

