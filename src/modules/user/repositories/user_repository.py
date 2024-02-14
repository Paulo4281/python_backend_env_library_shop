from src.modules.user.entities.user import User
from src.modules.user.dtos.user_dto import UserDTO
from src.database.database_config import session
from typing import List
from uuid import uuid4
import datetime

class UserRepository:
    @staticmethod
    def save(data: UserDTO) -> User:
        try:
            with session.begin():
                user = User(
                        id_ = uuid4(),
                        name = data["name"],
                        mail = data["mail"],
                        password = data["password"],
                        age = data["age"],
                        created_at = datetime.datetime.now()
                )

                session.add(user)

            return user.to_dict()
        except:
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def find() -> List[User]:
        try:
            with session.begin():
                users = session.query(User)

                users_list = []

                for user in users:
                    users_list.append(user.to_dict())
                    
            return users_list
        except:
            session.rollback()
        finally:
            session.close()
            
    @staticmethod
    def find_by_id(id_: str) -> User:
        try:
            with session.begin():
                user = session.query(User).filter(User.id_==id_).first()

            return user.to_dict()
        except:
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def find_by_mail(mail: str) -> User:
        try:
            with session.begin():
                user = session.query(User).filter(User.mail==mail).first()

            return user.to_dict()
        except:
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def update(id_: str, data: UserDTO) -> None:
        try:
            with session.begin():
                session.query(User).filter(User.id_==id_).update(data)
        except:
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def delete(id_: str) -> None:
        try:
            with session.begin():
                session.query(User).filter(User.id_==id_).delete()
        except:
            session.rollback()
        finally:
            session.close()