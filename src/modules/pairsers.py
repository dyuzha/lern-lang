# pairsers.py

import re


def normalize(src):
    if not isinstance(src, str):
        raise ValueError("Ожидаются строковые данные")
    return src.strip("() ").capitalize()


def get_sub_text(src: str):
    # Регулярное выражение для поиска текста в скобках, кроме : и |
    sub_text_regex = re.compile(r"\([^:|]+?\)")

    # Находим все вхождения sub_text
    matches = sub_text_regex.findall(src)

    # Проверяем кол-во вхождений
    sub_text_count = len(matches)

    if sub_text_count > 1:
        SyntaxError("Допускается не больше 1 sub_text на 1 variant" )
    elif sub_text_count >= 1:
        # Получим вспомогательный текст
        return matches[0]
    else:
        return None


def pairse_variant(src) -> dict:
    """
    Функция для парсинга variant.

    Функция принимает подобную строку
    "transWord1 (subText) | transWord2"

    В результате выполнения функции будет выведен словарь, подобного вида
    {
        "versions": ["transWord1", "transWord2"],
        "sub_text": "subText1"
    }
    """

    sub_text = get_sub_text(src)

    if sub_text:
        # Очистим текст от sub_text
        src = src.replace(sub_text, "")
        sub_text = normalize(sub_text)

    # Разделяем строку на на синонимы
    synonyms = list(map(normalize, src.split("|")))

    pairsed_variant = {
            "synonyms": synonyms,
            "sub_text": sub_text
                    }
    return pairsed_variant




class Pairser:
    def __init__(self):
        pass

    def pairse_file(self, src) -> list:
        pairsed_lines = list()
        # Чтение файла и парсинг
        with open(src, mode="r+") as f:
            content = f.read().split("\n")
            # Удаляем пустые строчки
            filtered_content = list(filter(None, content))

            # Парсим  текст
            for line in filtered_content:
                pairsed_line = self.pairse_line(line)
                pairsed_lines.append(pairsed_line)

            return pairsed_lines


    def pairse_line(self, src) -> dict:
        pairsed_variants = list()

        # Разделяем строку на варианты перевода
        variants = src.split(":")
        original = normalize(variants.pop(0))

        # Парсим все варианты перевода
        for variant in variants:
            new_variant = pairse_variant(variant)
            pairsed_variants.append(new_variant)

        return {
                "original": original,
                "variants": pairsed_variants
               }

def make_synonyms_str(src: list) -> str:
    synonyms_str = str(src.pop(0))
    while src:
        part = " | " + src.pop(0)
        synonyms_str += part
    return synonyms_str


def make_sub_text_str(src) -> str:
    if src:
        return " (" + str(src) + ")"
    else:
        return ""


def make_variants_str(src: list) -> str:
    variant = src.pop(0)
    synonyms_str = make_synonyms_str(variant["synonyms"])
    sub_text_str = make_sub_text_str(variant["sub_text"])
    target = synonyms_str + sub_text_str
    while src:
        variant = src.pop(0)
        synonyms_str = make_synonyms_str(variant["synonyms"])
        sub_text_str = make_sub_text_str(variant["sub_text"])
        part = " : " + synonyms_str + sub_text_str
        target += part
    return target




class DePairser:
    def __init__(self):
        pass

    def depairse_file(self, data, target) -> None:
        """
        Превращает json в человекочитаемый формат, и записывает его в файл

        Parameters:
        data: json
        target: file

        Return:
        None
        """
        with open(target, mode="w") as file:
            for i in data:
                # Записываем объект json в виде строки
                line = self.depairse_line(i)
                file.write(line + "\n")
            return


    def depairse_line(self, data) -> str:
        original_str = str(data["original"])

        variants_str = make_variants_str(data["variants"])

        return original_str + " : " + variants_str
