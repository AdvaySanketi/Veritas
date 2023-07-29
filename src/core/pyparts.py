def dismantle(code):
    data = """import dis
def func():
"""
    data2 = """import snoop

@snoop
def sfunc():
"""
    for i in code.split('\n'):
        if  i != '':
            data = data + '\t' + i + '\n'
            data2 = data2 + '\t' + i + '\n'

    data += """
def dismantle():
    f = open(r"gui\\core\\breakdown_output.txt", "w")
    return dis.dis(func, file = f)
"""
    data2 += """
def func():
    not_my_data = set(dir())
    Veritas = "test"
"""
    for i in code.split('\n'):
        if  i != '':
            data2 = data2 + '    ' + i + '\n'
            
    data2 += """    my_data = set(dir()) - not_my_data
    mem = []
    for name in my_data:
        if name != "not_my_data":
            val = eval(name)
            mem.append(name+ " ==> "+ str(type(val)) + " ==> "+ str(val))
    print(mem)
    
def run():
    snoop.install(out="gui\\core\\console.txt",overwrite=True,prefix="Veritas >>>",enabled=True)
    sfunc()
    snoop.install(enabled=False)
    
func()
"""

    with open("gui//core//breakdown.py", 'w') as file:
        file.write(data)
        
    with open("gui//core//consoledata.py", 'w') as file:
        file.write(data2)
        
    with open("gui//core//console.txt", "w") as file:
        pass