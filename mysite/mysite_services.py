import json

from CoffeeHouse_SoftwareTools.settings import BASE_DIR

PATH = BASE_DIR / 'questions.json'


def refresh_json(question: str, mail: str, name: str) -> None:
    """Записывает данные в JSON файл в формате {почта: [имя, вопрос1, вопрос2...]}"""
    try:
        with open(PATH, encoding='utf-8') as file_in:
            data = json.load(file_in)
    except json.decoder.JSONDecodeError:
        write_json({mail: [name, question]})
    else:
        if mail in data:
            data[mail][0] = name
            if question.lower().strip() not in (i.lower().strip() for i in data[mail][1:]):
                data[mail].append(question)
        else:
            data[mail] = [name, question]
        write_json(data)


def write_json(data: dict | list) -> None:
    """Записывает словарь или список в JSON файл пути PATH"""
    with open(PATH, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
