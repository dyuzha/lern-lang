import json
from db import OriginUI, TransUI, BaseUI
from repository import Repository

class TxtHandler:
    def __init__(self, data):
        self.data = data
        self.translates = list()

    def handle(self, data):
        self.original: str = data["original"]
        variants: list = data["variants"]

        # Добавляем все варианты перевода для origin в бд
        for variant in variants:
            sub_text: str = variant["sub_text"]
            synonyms: list = variant["synonyms"]
            synonyms_json = str(synonyms)
            # Добавляем trans в бд
            id_trans = self._repo.add_translate_entry(synonyms_json, id_origin,
                                                sub_text)


class DataBaseUI:
    """Создает объекты db из json формата"""
    def __init__(self, db_url):
        self._repo = Repository(db_url)

    def add_origin(self, origin: str, variants: list[str], sub_text:str):
        # Добавляем origin в базу данных
        id_origin = self._repo.add_origin_entry(origin)
        # Закрепляем trans за созданным origin в базе данных
        self.add_translate(variants, id_origin, sub_text)

    def add_translate(self, variants, id_origin, sub_text):
        self._repo.add_translate_entry(variants, id_origin, sub_text)

    def json_load_into_db(self, data):
        """Парсит json в дб"""
        # Добавляем origin в бд
        original: str = data["original"]
        id_origin = self._repo.add_origin_entry(original)

        variants: list = data["variants"]

        # Добавляем все варианты перевода для origin в бд
        for variant in variants:
            sub_text: str = variant["sub_text"]
            synonyms: list = variant["synonyms"]
            synonyms_json = str(synonyms)
            # Добавляем trans в бд
            id_trans = self._repo.add_translate_entry(synonyms_json, id_origin,
                                                sub_text)

    def re_creation_tables(self):
        self._repo.re_creation_tables()


src_file = "words.json"
db_url = "sqlite:///words.db"


def main():
    # Создаем обработчик json
    data_base_ui = DataBaseUI(db_url)

    # Пересоздаем таблицы
    data_base_ui.re_creation_tables()

    # Считываем json
    with open(src_file, mode="r") as f:
        data = json.load(f)

    # Считываем json в бд (поочередно)
    for obj in data:
        # Добавляем объект в бд
        data_base_ui.json_load_into_db(obj)

if __name__ == "__main__":
    main()
