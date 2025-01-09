from db import OriginUI, TransUI, BaseUI


class Repository:
    def __init__(self, db_url):
        self._origin_ui = OriginUI(db_url)
        self._trans_ui = TransUI(db_url)
        self._base_ui = BaseUI(db_url)

    def add_origin_entry(self, data):
        """Добавляет запись в таблицу origin и возвращает ее id"""
        origin_id = self._origin_ui.add_entry(data)
        return origin_id

    def add_translate_entry(self, data, id_origin, sub_text):
        """Добавляет запись в таблицу trans и возвращает ее id"""
        trans_id = self._trans_ui.add_entry(data, id_origin, sub_text)
        return trans_id

    def re_creation_tables(self):
        self._base_ui.re_creation_tables()

