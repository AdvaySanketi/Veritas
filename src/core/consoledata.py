import snoop

@snoop
def sfunc():
	a = 5
	b = 4
	print(a+b)

def func():
    not_my_data = set(dir())
    Veritas = "test"
    a = 5
    b = 4
    print(a+b)
    my_data = set(dir()) - not_my_data
    mem = []
    for name in my_data:
        if name != "not_my_data":
            val = eval(name)
            mem.append(name+ " ==> "+ str(type(val)) + " ==> "+ str(val))
    print(mem)
    
def run():
    snoop.install(out="gui\core\console.txt",overwrite=True,prefix="Veritas >>>",enabled=True)
    sfunc()
    snoop.install(enabled=False)
    
func()
