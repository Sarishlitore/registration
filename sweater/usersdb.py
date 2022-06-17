from sqlalchemy.exc import SQLAlchemyError

from sweater.models import Users, Profiles


class UsersDB:
    def __init__(self, session):
        self.__session = session

    def add_user(self, name: str, email: str, hash_psw: str) -> bool:
        try:
            if Users.query.filter_by(email=email).first():
                print("Пользователь с таким email уже существует")
                return False
            user = Users(email=email, psw=hash_psw)
            self.__session.add(user)
            self.__session.flush()
            profile = Profiles(name=name, user_id=user.id)
            self.__session.add(profile)
            self.__session.commit()
        except SQLAlchemyError as err:
            print('Ошибка при добавление нового пользователя ' + str(err))
            return False
        return True

    @staticmethod
    def get_user(user_id: int):
        try:
            user = Users.query.filter_by(id=user_id).first()
            if not user:
                print('Пользователь не найден')
                return False
            return user
        except SQLAlchemyError as err:
            print('Ошибка при получение данных из БД ' + str(err))
        return False

    @staticmethod
    def get_user_by_email(email):
        try:
            user = Users.query.filter_by(email=email).first()
            if not user:
                print('Пользователь не найден')
                return False
            return user
        except SQLAlchemyError as err:
            print('Ошибка при получение данных из БД ' + str(err))
        return False
