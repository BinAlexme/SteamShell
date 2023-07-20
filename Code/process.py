import psutil, configparser, ctypes, time
from threading import Thread

try:
    open ('programms.ini', 'r')
except:
    ctypes.windll.user32.MessageBoxW(None, f"programms.ini не найден.", "Ошибка !", 0)
    exit()

config = configparser.ConfigParser()
config.read('programms.ini')

try:
    process_list = config.get("setting", "program_list")
    process_list = process_list.split(',')

    delay = float(config.get("setting", "delay"))
except:
    ctypes.windll.user32.MessageBoxW(None, f"Ошибка чтения файла.", "Ошибка !", 0)
    exit()

def complete_process():
    while True:
        for process in psutil.process_iter():
            if process.name() in process_list:
                try:
                    process.kill()
                except:
                    pass

        time.sleep(delay)

Thread(complete_process())