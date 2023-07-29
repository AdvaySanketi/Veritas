from qt_core import *
from gui.core.terminal import output_capture
from gui.core.terminal import run_file

outputs_list = []
memory_list = []
inputs = []
stack = []
prev_list = []
commands = []
code = []
liners = []
linenum = 1
serial = 1

def visualizer(pre, text_edit=None, console=None, memory=None, output=None, inputs=None, save=False, tabindex=0):
    global serial
    global input_box
    if save == True:
        prev = [serial] + [pre[-1]]
        prev_list.append(prev)
        input_box = inputs
        context = [text_edit, console, memory, output, inputs]
        with open("gui//core//vislist.txt",'a') as file:
            file.write(str(serial)+'\n')
            for i in context:
                file.write(str(i)+'\n')
        serial += 1
    else:
        global memory_list
        f = open("gui//core//vislist.txt",'r')
        data = f.readlines()
        for i in data:
            if i.replace('\n','') == str(tabindex+1):
                index = data.index(i)
                context = [data[index+1],data[index+2],data[index+3],data[index+4]]
        for i in prev_list:
            if i[0] == tabindex+1:
                dataset = i
        out, err = output_capture("python gui/core/consoledata.py")
        out = out.decode('utf-8').split('\n')
        for i in out:
            if i.startswith('['):
                if "Veritas ==> <class 'str'> ==> test" in i:
                    out.remove(i)
                    for k in i.split(','):
                        k = k.strip('""')
                        k = k.split('"')
                        k = ''.join(k[1:])
                        k = k.split(']')[0]
                        if "Veritas" not in k:
                            memory_list.append(k)

        if True:
            memory = context[2].replace('\n', '')
            for i in dataset[1]:
                if str(i) == memory:
                    memory = i
            string = ''
            for i in memory_list:
                string += i + '\n'
            memory.setPlainText(string)
        if True:
            console = context[1].replace('\n', '')
            for i in dataset[1]:
                if str(i) == console:
                    console = i
            file = open(f"gui//core//console.txt", 'r')
            consoletxt = file.readlines()
            for i in range(len(consoletxt)):
                consoletxt[i] = " ".join(consoletxt[i].split()[:2]+consoletxt[i].split()[3:])
            console.setPlainText('\n'.join(consoletxt[2:-1]))
        if True:
            output = context[3].replace('\n', '')
            for i in dataset[1]:
                if str(i) == output:
                    output = i
            output.setPlainText('\n'.join(out))

def visualize(_code,tabindex=0):
    global prev_list
    global inputs
    flag = True
    if check_input(_code):
        expected = _code.count("input")
        inputdata = input_box.toPlainText().split(',')
        inputdata = list(filter(lambda x: x != "", inputdata))
        given = len(inputdata)
        if expected == given:
            embed_input(inputdata)
            err = run_file("gui//core//breakdown.py")
            if err != None:
                display_error(err)
        else:
            input_box.setPlainText(f"!! Expected " + str(expected) + " Inputs, Got " + str(given) + " Inputs !!")
            flag = False
    if flag:
        visualizer(prev_list[-1],tabindex=tabindex)

def setting_up():
    global memory_list
    global outputs_list
    global console_txt
    memory_list.clear()
    outputs_list.clear()
    
def check_input(code):
    for line in code.split('\n'):
        if "input" in line:
            return True
    return False

def embed_input(inputdata):
    extra = list(inputdata)
    with open("gui//core//consoledata.py", 'r') as file:
        data = file.readlines()
    modified = []
    for i in data:
        if "input" in i:
            index = i.index("=")
            try:
                if len(inputdata)>0:
                    if inputdata[0].isdigit():
                        try:
                            i = i[:index+1]+" "+str(inputdata[0])+"\n"
                            inputdata.pop(0)
                        except:
                            i = i[:index+1]+" "+str(extra[0])+"\n"
                            extra.pop(0)
                    elif isinstance(float(inputdata[0]), float):
                        try:
                            i = i[:index+1]+" "+str(inputdata[0])+"\n"
                            inputdata.pop(0)
                        except:
                            i = i[:index+1]+" "+str(extra[0])+"\n"
                            extra.pop(0)
                    elif inputdata[0].startswith('['):
                        x = ''
                        for i in range(len(inputdata)):
                            x += inputdata[i]
                            if inputdata[i].endswith(']'):
                                inputdata = inputdata[i+1:]
                                break
                        i = i[:index+1]+" "+x+"\n"
                    else:
                        try:
                            i = i[:index+1]+" '"+str(inputdata[0])+"' \n"
                            inputdata.pop(0)
                        except:
                            i = i[:index+1]+" '"+str(extra[0])+"' \n"
                            extra.pop(0)
                elif len(extra)>0:
                    if extra[0].isdigit():
                        try:
                            i = i[:index+1]+" "+str(inputdata[0])+"\n"
                            inputdata.pop(0)
                        except:
                            i = i[:index+1]+" "+str(extra[0])+"\n"
                            extra.pop(0)
                    elif isinstance(float(extra[0]), float):
                        try:
                            i = i[:index+1]+" "+str(inputdata[0])+"\n"
                            inputdata.pop(0)
                        except:
                            i = i[:index+1]+" "+str(extra[0])+"\n"
                            extra.pop(0)
                    elif extra[0].startswith('['):
                        x = ''
                        for i in range(len(extra)):
                            x += extra[i]
                            if extra[i].endswith(']'):
                                extra = extra[i+1:]
                                break
                        i = i[:index+1]+" "+x+"\n"
                    else:
                        try:
                            i = i[:index+1]+" '"+str(inputdata[0])+"' \n"
                            inputdata.pop(0)
                        except:
                            i = i[:index+1]+" '"+str(extra[0])+"' \n"
                            extra.pop(0)
            except:
                pass
        modified.append(i)
    with open("gui//core//consoledata.py", 'w') as file:
        for line in modified:
            file.write(line)
            
def display_error(error):
    global input_box
    try:
        input_box.setPlainText("!! "+str(error)[:str(error).index('(')]+" !!")
    except:
        input_box.setPlainText("!! "+str(error)+" !!")