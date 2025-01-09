# facade.py


from pairsers import Pairser, DePairser
import json


class Facade:

    def __init__(self):
        self._pairser = Pairser()
        self._depairser = DePairser()


    def pairse_file(self):
        src_file = "data/words_for_pairs.txt"
        trg_file = "data/words.json"

        # Парсим файл
        pairsed_rows = self._pairser.pairse_file(src_file)

        # Записываем json в файл
        with open(trg_file, mode="r+") as f:
            f.write(json.dumps(pairsed_rows, indent=4, ensure_ascii=False))


    def depairse_file(self):
        src_file = "data/words.json"
        trg_file = "data/words_after_json.txt"

        # Загружаем json из файла
        with open(src_file) as file:
            data = json.load(file)

        # Записываем json в виде человекоудобного формата в файл
        self._depairser.depairse_file(data, trg_file)


def main():
    ui = Facade()
    ui.pairse_file()
    ui.depairse_file()

if __name__ == "__main__":
    main()

