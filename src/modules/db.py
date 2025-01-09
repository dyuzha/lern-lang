from sqlalchemy import create_engine
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship

db_path = "data/words.db"
engine = create_engine("sqlite:///" + db_path, echo=True)


# Создаем базовый класс для моделей
class Base(DeclarativeBase):
    pass



class Origin(Base):
    __tablename__ = "origin"
    id = Column(Integer, primary_key=True, autoincrement=True,
                index=True)
    data = Column(String, unique=True, comment="Основной текст")



class Trans(Base):
    __tablename__ = "translates"
    id = Column(Integer, primary_key=True, autoincrement=True,
                index=True)
    id_origin = Column(Integer)
    data = Column(String, comment="Перевод")
    sub_text = Column(String, default=None)



class State(Base):
    __tablename__ = "state"
    id_trans = Column(Integer, ForeignKey("trans.id", ondelete="CASCADE"),
                      unique=True)
    id_origin = Column(Integer, ForeignKey("origin.id", ondelete="CASCADE"),
                       primary_key=True)
    win_trans = Column(Integer, default=0)
    win_origin = Column(Integer, default=0)
    loss_trans = Column(Integer, default=0)
    loss_origin = Column(Integer, default=0)

    id_trans = relationship( "",
        back_populates="patient",
        cascade="all, delete",
        passive_deletes=True)


    def __init__(self, id_trans, id_en, win_en=0, win_trans=0, loss_en=0, loss_trans=0):
        self.id_tr = id_trans
        self.id_en = id_en
        self.win_en = win_en
        self.win_trans = win_trans
        self.loss_en = loss_en
        self.loss_trans = loss_trans


    # Создание виртуальных столбцов

    # Победного коэффициента origin
    @property
    def win_coeff_origin(self):
        return self.win_origin / self.loss_origin


    # Победного коэффициента trans
    @property
    def win_coeff_trans(self):
        return self.win_trans / self.loss_trans


    # Общего кол-ва использований origin
    @property
    def all_used_origin(self):
        return self.win_origin + self.loss_origin


    # Общего кол-ва использований trans
    @property
    def all_used_trans(self):
        return self.win_trans + self.loss_trans







# Создаем таблицы
Base.metadata.create_all(bind=engine)


