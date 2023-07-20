import os, subprocess, uuid, ctypes,  sys

def open_download():
    try:
        way = f"{os.getenv('USERPROFILE')}\Downloads"
        subprocess.run(['explorer', os.path.realpath(way)])
    except:
        pass

def open_recent():
    try:
        way = f"{os.getenv('USERPROFILE')}\AppData\Roaming\Microsoft\Windows\Recent"
        subprocess.run(['explorer', os.path.realpath(way)])
    except:
        pass

def open_prefetch():
    try:
        way = f"{os.getenv('SystemDrive')}\Windows\prefetch"
        subprocess.run(['explorer', os.path.realpath(way)])
    except:
        pass

def open_temp():
    try:
        way = f"{os.getenv('USERPROFILE')}\AppData\Local\Temp"
        subprocess.run(['explorer', os.path.realpath(way)])
    except:
        pass

def open_appdata():
    try:
        way = f"{os.getenv('USERPROFILE')}\AppData\Roaming"
        subprocess.run(['explorer', os.path.realpath(way)])
    except:
        pass

def clear_download():
    way = f"{os.getenv('USERPROFILE')}\Downloads"

    for root, dirs, files in os.walk(way):
        for file in files:
            try:
                new_file_name = uuid.uuid4()
                os.rename(f"{root}\{file}", f"{root}\{new_file_name}")
                os.remove(f"{root}\{new_file_name}")
            except PermissionError:
                ctypes.windll.user32.MessageBoxW(None, f"[Отказано в доступе] {root}\{file}", "Ошибка !", 0)
            except FileNotFoundError:
                ctypes.windll.user32.MessageBoxW(None, f"[Файл не найден] {root}\{file}", "Ошибка !", 0)

def clear_recent():
    way = f"{os.getenv('USERPROFILE')}\AppData\Roaming\Microsoft\Windows\Recent"

    for root, dirs, files in os.walk(way):
        for file in files:
            try:
                new_file_name = uuid.uuid4()
                os.rename(f"{root}\{file}", f"{root}\{new_file_name}")
                os.remove(f"{root}\{new_file_name}")
            except PermissionError:
                ctypes.windll.user32.MessageBoxW(None, f"[Отказано в доступе] {root}\{file}", "Ошибка !", 0)
            except FileNotFoundError:
                ctypes.windll.user32.MessageBoxW(None, f"[Файл не найден] {root}\{file}", "Ошибка !", 0)

def clear_prefetch():
    way = f"{os.getenv('SystemDrive')}\Windows\prefetch"

    for root, dirs, files in os.walk(way):
        for file in files:
            try:
                new_file_name = uuid.uuid4()
                os.rename(f"{root}\{file}", f"{root}\{new_file_name}")
                os.remove(f"{root}\{new_file_name}")
            except PermissionError:
                ctypes.windll.user32.MessageBoxW(None, f"[Отказано в доступе] {root}\{file}", "Ошибка !", 0)
            except FileNotFoundError:
                ctypes.windll.user32.MessageBoxW(None, f"[Файл не найден] {root}\{file}", "Ошибка !", 0)

def clear_temp():
    way = f"{os.getenv('USERPROFILE')}\AppData\Local\Temp"

    for root, dirs, files in os.walk(way):
        for file in files:
            try:
                new_file_name = uuid.uuid4()
                os.rename(f"{root}\{file}", f"{root}\{new_file_name}")
                os.remove(f"{root}\{new_file_name}")
            except PermissionError:
                ctypes.windll.user32.MessageBoxW(None, f"[Отказано в доступе] {root}\{file}", "Ошибка !", 0)
            except FileNotFoundError:
                ctypes.windll.user32.MessageBoxW(None, f"[Файл не найден] {root}\{file}", "Ошибка !", 0)

def complete_process():
    process_list = ['notepad.exe', 'osk.exe']

    for process in psutil.process_iter():
        if process.name() in process_list:
            try:
                process.kill()
            except:
                pass

def clear_event_log():
    try:
        os.system('powershell "Get-EventLog -LogName * | ForEach { Clear-EventLog $_.Log }"')
    except:
        pass

def clear_path():
    way = ""

    for root, dirs, files in os.walk(way):
        for file in files:
            try:
                new_file_name = uuid.uuid4()
                os.rename(f"{root}\{file}", f"{root}\{new_file_name}")
                os.remove(f"{root}\{new_file_name}")
            except PermissionError:
                ctypes.windll.user32.MessageBoxW(None, f"[Отказано в доступе] {root}\{file}", "Ошибка !", 0)
            except FileNotFoundError:
                ctypes.windll.user32.MessageBoxW(None, f"[Файл не найден] {root}\{file}", "Ошибка !", 0)