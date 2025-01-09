from sqlalchemy import create_engine
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Session


class Base(DeclarativeBase):
    pass


class BaseUI:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)

    def create_tables(self):
        Base.metadata.create_all(bind=self.engine)
        return

    def drop_tables(self):
        Base.metadata.drop_all(bind=self.engine)
        return

    def re_creation_tables(self):
        self.drop_tables()
        self.create_tables()
        return


class OriginTable(Base):
    """Таблица основного текста"""
    __tablename__ = "origin"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    data = Column(String, unique=True, comment="Основной текст")

    def __init__(self, data):
        self.data = data


class TransTable(Base):
    """Таблица перевода текста"""
    __tablename__ = "translates"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    id_origin = Column(Integer, ForeignKey("origin.id"))
    data = Column(String, comment="Переводы текста в формате json")
    sub_text = Column(String, comment="Вспомогательный текст")
    count = Column(Integer, default=0)
    win = Column(Integer, default=0)

    def __init__(self, data, id_origin, sub_text):
        # Тут необходимо будет добавить проверку с помощью json_scheme
        self.data = data
        self.id_origin = id_origin
        self.sub_text = sub_text


class OriginUI:
    """Класс для управления таблицей Origin"""
    def __init__(self, db_url):
        self.engine = create_engine(db_url)

    def add_entry(self, data):
        with Session(autoflush=False, bind=self.engine) as db:
            origin = OriginTable(data)
            db.add(origin)
            db.commit()
            return origin.id

    def delete_entry(self):
        return


class TransUI:
    """Класс для управления таблицей Trans"""
    def __init__(self, db_url):
        self.engine = create_engine(db_url)

    def add_entry(self, data, id_origin, sub_text):
        with Session(autoflush=False, bind=self.engine) as db:
            trans = TransTable(data, id_origin, sub_text)
            db.add(trans)
            db.commit()
            return trans.id

    def get_entry(self, id):
        with Session(autoflush=False, bind=self.engine) as db:
            trans = db.query(id=id)
            return trans
