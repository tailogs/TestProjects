import os
import sys

class COLOR:
    RESET = '\u001b[0m'
    BLACK = '\u001b[30m'
    RED = '\u001b[31m'
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33m'
    BLUE = '\u001b[34m'
    PURPLE = '\u001b[35m'
    CYAN = '\u001b[36m'
    WHITE = '\u001b[37m'
    BACKGROUND_BLACK = '\u001b[40m'
    BACKGROUND_RED = '\u001b[41m'
    BACKGROUND_GREEN = '\u001b[42m'
    BACKGROUND_YELLOW = '\u001b[43m'
    BACKGROUND_BLUE = '\u001b[44m'

def search_files(keyword):
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith(('.txt', '.html')):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        for i, line in enumerate(lines):
                            if keyword in line:
                                start = max(0, i - 1)  # Starting index for the context
                                end = min(i + 2, len(lines))  # Ending index for the context
                                context = ''.join(lines[start:end])
                                print(f"{COLOR.CYAN}Найдено в файле: {file_path}{COLOR.RESET}")
                                print(f"{COLOR.WHITE}Контекст:{COLOR.RESET}")
                                print(f"    {context}")
                                print("--------------------")
                except UnicodeDecodeError:
                    print(f"{COLOR.BACKGROUND_RED}{COLOR.BLACK}Ошибка чтения файла: {file_path}{COLOR.RESET}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Пожалуйста, укажите ключевое слово в кавычках в качестве аргумента")
        print("main.py <слово_которое_вы_пытаетесь_найти>")
    else:
        keyword = sys.argv[1]
        search_files(keyword)
