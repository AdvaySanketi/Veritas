import dis
def func():
	a = 5
	b = 4
	print(a+b)

def dismantle():
    f = open(r"gui\core\breakdown_output.txt", "w")
    return dis.dis(func, file = f)
