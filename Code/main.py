import os, subprocess, uuid, psutil, sys, shutil, resourse

from PyQt5 import QtCore, QtGui, QtWidgets
from GUI import *
from threading import Thread

try:
    resourse.start()
except:
    pass

if __name__ == "__main__":
   app = QtWidgets.QApplication(sys.argv)
   ui = Widget()
   ui.show()

   def open_download():
    try:
        way = f"{os.getenv('USERPROFILE')}\Downloads"
        subprocess.run(['explorer', os.path.realpath(way)])
        ui.textBrowser.append('[Download] Папка открыта.')
    except:
        ui.textBrowser.append('[Download] Не удалось открыть папку.')

   def clear_download():
        way = f"{os.getenv('USERPROFILE')}\Downloads"

        for root, dirs, files in os.walk(way):
            for file in files:
                try:
                    new_file_name = uuid.uuid4()
                    os.rename(f"{root}\{file}", f"{root}\{new_file_name}")
                    os.remove(f"{root}\{new_file_name}")
                    ui.textBrowser.append(f'[Delete] {file} удален.')
                except PermissionError:
                    ui.textBrowser.append(f'[Delete] {file} отказано в доступе.')
                except FileNotFoundError:
                    ui.textBrowser.append(f'[Delete] {file} файл больше не существует.')

   def open_recent():
    try:
        way = f"{os.getenv('USERPROFILE')}\AppData\Roaming\Microsoft\Windows\Recent"
        subprocess.run(['explorer', os.path.realpath(way)])
        ui.textBrowser.append('[Recent] Папка открыта.')
    except:
        ui.textBrowser.append('[Recent] Не удалось открыть папку.')

   def clear_recent():
    way = f"{os.getenv('USERPROFILE')}\AppData\Roaming\Microsoft\Windows\Recent"

    for root, dirs, files in os.walk(way):
        for file in files:
            try:
                new_file_name = uuid.uuid4()
                os.rename(f"{root}\{file}", f"{root}\{new_file_name}")
                os.remove(f"{root}\{new_file_name}")
                ui.textBrowser.append(f'[Delete] {file} удален.')
            except PermissionError:
                ui.textBrowser.append(f'[Delete] {file} отказано в доступе.')
            except FileNotFoundError:
                ui.textBrowser.append(f'[Delete] {file} файл больше не существует.')

   def open_prefetch():
    try:
        way = f"{os.getenv('SystemDrive')}\Windows\prefetch"
        subprocess.run(['explorer', os.path.realpath(way)])
        ui.textBrowser.append('[Prefetch] Папка открыта.')
    except:
        ui.textBrowser.append('[Prefetch] Не удалось открыть папку.')

   def clear_prefetch():
    way = f"{os.getenv('SystemDrive')}\Windows\prefetch"

    for root, dirs, files in os.walk(way):
        for file in files:
            try:
                new_file_name = uuid.uuid4()
                os.rename(f"{root}\{file}", f"{root}\{new_file_name}")
                os.remove(f"{root}\{new_file_name}")
                ui.textBrowser.append(f'[Delete] {file} удален.')
            except PermissionError:
                ui.textBrowser.append(f'[Delete] {file} отказано в доступе.')
            except FileNotFoundError:
                ui.textBrowser.append(f'[Delete] {file} файл больше не существует.')

   def open_temp():
    try:
        way = f"{os.getenv('USERPROFILE')}\AppData\Local\Temp"
        subprocess.run(['explorer', os.path.realpath(way)])
        ui.textBrowser.append('[Temp] Папка открыта.')
    except:
        ui.textBrowser.append('[Temp] Не удалось открыть папку.')

   def clear_temp():
    way = f"{os.getenv('USERPROFILE')}\AppData\Local\Temp"

    for root, dirs, files in os.walk(way):
        for file in files:
            try:
                new_file_name = uuid.uuid4()
                os.rename(f"{root}\{file}", f"{root}\{new_file_name}")
                os.remove(f"{root}\{new_file_name}")
                ui.textBrowser.append(f'[Delete] {file} удален.')
            except PermissionError:
                ui.textBrowser.append(f'[Delete] {file} отказано в доступе.')
            except FileNotFoundError:
                ui.textBrowser.append(f'[Delete] {file} файл больше не существует.')

   def open_appdata():
    try:
        way = f"{os.getenv('USERPROFILE')}\AppData\Roaming"
        subprocess.run(['explorer', os.path.realpath(way)])
        ui.textBrowser.append('[AppData] Папка открыта.')
    except:
        ui.textBrowser.append('[AppData] Не удалось открыть папку.')

   def clear_path():
    way = ui.lineEdit.text()

    for root, dirs, files in os.walk(way):
        for file in files:
            try:
                new_file_name = uuid.uuid4()
                os.rename(f"{root}\{file}", f"{root}\{new_file_name}")
                os.remove(f"{root}\{new_file_name}")
                ui.textBrowser.append(f'[Delete] {file} удален.')
            except PermissionError:
                ui.textBrowser.append(f'[Delete] {file} отказано в доступе.')
            except FileNotFoundError:
                ui.textBrowser.append(f'[Delete] {file} файл больше не существует.')

   def clear_event_log():
    try:
        os.system('powershell "Get-EventLog -LogName * | ForEach { Clear-EventLog $_.Log }"')
        ui.textBrowser.append('[Event Log] Очищен.')
    except:
        ui.textBrowser.append('[Event Log] Ошибка очистки.')
   
   def start_complete_process():
       try:
            os.startfile('process.exe','runas')
            ui.textBrowser.append('[Kill Process] Файл запущен.')
       except FileNotFoundError:
            ui.textBrowser.append('[Kill Process] Файл не найден.')
       except:
           ui.textBrowser.append('[Kill Process] Не удалось запустить.')

   def stop_complete_process():
       i = 0 
       for process in psutil.process_iter():
           if process.name() == "process.exe":
               process.kill()
               ui.textBrowser.append('[Kill Process] process.exe завершен.')
               i += 1
       
       if i == 0:
           ui.textBrowser.append('[Kill Process] process.exe не найден.')

   try:
       os.remove('main_ico.png')
   except:
       pass

   ui.pushButton.clicked.connect(lambda: app.exit())
   ui.pushButton_2.clicked.connect(lambda: ui.showMinimized())
   ui.pushButton_3.clicked.connect(lambda: Thread(open_download()))
   ui.pushButton_4.clicked.connect(lambda: Thread(clear_download()))
   ui.pushButton_5.clicked.connect(lambda: Thread(open_recent()))
   ui.pushButton_6.clicked.connect(lambda: Thread(clear_recent()))
   ui.pushButton_7.clicked.connect(lambda: Thread(open_prefetch()))
   ui.pushButton_8.clicked.connect(lambda: Thread(clear_prefetch()))
   ui.pushButton_9.clicked.connect(lambda: Thread(open_temp()))
   ui.pushButton_10.clicked.connect(lambda: Thread(clear_temp()))
   ui.pushButton_11.clicked.connect(lambda: Thread(open_appdata()))
   ui.pushButton_12.clicked.connect(lambda: Thread(start_complete_process()))
   ui.pushButton_13.clicked.connect(lambda: Thread(stop_complete_process()))
   ui.pushButton_14.clicked.connect(lambda: Thread(clear_event_log()))
   ui.pushButton_15.clicked.connect(lambda: Thread(clear_path()))

   sys.exit(app.exec_())
