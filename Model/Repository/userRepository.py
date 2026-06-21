from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from Model.Entity.user import User


class UserRepository:

    async def addUser(self,user:User,session:AsyncSession)-> User:
        session.add(user)
        await session.commit()

        return user

    async def updateUser(self,old_number: str,numberUpdated: str, session:AsyncSession) -> User:

        user = await session.execute(
            select(User).where(User.phone == old_number)
        )

        user.change_number(numberUpdated)

        await session.commit()

        return user

    async def getUserByNumber(self,number:str,session: AsyncSession) -> User:

        user = await session.execute(
            select(User).where(User.phone == number)
        )

        return user

    async def getAllUsers(self,session: AsyncSession) -> list[User]:

        result = await session.execute(
            select(User)
        )

        listUser = result.scalars().all()

        return listUser






