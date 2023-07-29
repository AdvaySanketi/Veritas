from qt_core import *
import subprocess
from subprocess import Popen, PIPE

state = False

def file_data(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return data
    except:
        pass

def get_state(toggle):
    global state
    if toggle.isChecked():
        state = True
    else:
        state = False

def run_file(program):
    try:
        import gui.core.breakdown as breakdown
        output = breakdown.dismantle()
        with open("gui//core//console.txt", 'w') as file:
            pass
        import gui.core.consoledata as console
        output2 = console.run()
    except Exception as e:
        return e

def output_capture(cmd):
    args = cmd.split()
    proc = Popen(args, stdout = PIPE, stderr = PIPE)
    out, err = proc.communicate()
    return out, err

def terminal():
    subprocess.run('start cmd.exe /k "prompt $$Veritas$g$s & title Veritas Terminal"' , shell = True)

def pyint():
    subprocess.run('start cmd.exe /k "title Veritas Terminal & ptpython"' , shell = True)
