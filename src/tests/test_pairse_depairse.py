from ..modules.pairsers import Pairser, DePairser
import json


def pairse():
    src_file = "data/words_for_pairs.txt"
    trg_file = "data/words.json"

    # Создаем парсер
    pairser = Pairser()

    # Парсим файл
    pairsed_rows = pairser.pairse_file(src_file)

    # Записываем json в файл
    with open(trg_file, mode="r+") as f:
        f.write(json.dumps(pairsed_rows, indent=4, ensure_ascii=False))


def depairse():
    src_file = "data/words.json"
    trg_file = "data/words_after_json.txt"

    # Создаем депарсер
    depairser = DePairser()

    # Загружаем json из файла
    with open(src_file) as file:
        data = json.load(file)

    # Записываем json в виде человекоудобного формата в файл
    depairser.depairse_file(data, trg_file)


def main():
    if PAIRS == True:
        pairse()
    else:
        depairse()


PAIRS = False


if __name__ == "__main__":
    main()
