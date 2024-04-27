import pyperclip #для копирования в буфер
import subprocess # работы с командной строкой
from colorama import init, Fore, Back, Style #покрасить текст
init()
ytdlp="yt-dlp "
n=" && "


def trim_after_phrase(string, phrase):
    index = string.find(phrase)
    if index != -1:
        return string[:index + len(phrase)]
    else:
        return string

# Считываем строку и фразу от пользователя
string = input("Введите ссылку: ")
name = input("Введите новое название файла: ")
phrase = ".m3u8"
name_quotes = f'"{name}"' 

# Обрезаем строку и выводим результат
trimmed_string = trim_after_phrase(string, phrase)

file_to_rename = f'"{"720 [720].mp4"}"'
finish_name = f'"{name + ".mp4"}"' 

# pyperclip.copy(result)
cdDownloads = "cd downloads && "
create_dir = "mkdir " + name_quotes
cd= "cd " + name_quotes
cd_back = "cd.."

result = cdDownloads + create_dir + n + cd + n + ytdlp + trimmed_string + n + "ren "+ file_to_rename + " " + finish_name + n + cd_back + cd_back
command = result

print(Fore.YELLOW + "Процесс Скачивания " + finish_name + " начался")
# print(Fore.RED + "Ваш готовый, скопированный результат:", result)
subprocess.run(command, shell=True)
print(Fore.GREEN + "Видео " + finish_name + " скачано!")