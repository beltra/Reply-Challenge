start_points = []

class Stack:
    def __init__(self, stack = []) -> None:
        self.__stack = stack
    def __str__(self) -> str:
        return str(self.__stack)
    def push(self, arg) -> None:
        self.__stack.append(arg)
    def pop(self):
        return self.__stack.pop()
    def empty(self) -> None:
        self.__stack = []

with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()
    code = [line[:-1] for line in lines]

def getStartPoints():
    for i in range(len(code)):
        for j in findall('$', code[i]):
            start_points.append((i, j))

def findall(p, s):
    '''Yields all the positions of
    the pattern p in the string s.'''
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i+1)

getStartPoints()

print(start_points)

flag = ""
stack = Stack()

def interpreter(command):
    global flag
    global stack
    global i
    global j
    global code

    print(command)

    val = ""

    if command == "$":
        i += 1

    elif command == "#":
        j += 1

    elif command == "(":
        char = stack.pop()
        flag = char + flag

        jtmp = j + 1
        val = ""
        while (code[i][jtmp].isdigit()):
            val += code[i][jtmp]
            jtmp += 1

        j -= int(val)

    elif command == ")":
        char = stack.pop()
        flag = flag + char

        jtmp = j - 1
        val = ""
        while (code[i][jtmp].isdigit()):
            val += code[i][jtmp]
            jtmp -= 1

        j += int(val)

    elif command == "-":
        flag = flag[1:]
        
        itmp = i + 1
        val = ""
        while (code[itmp][j].isdigit()):
            val += code[itmp][j]
            itmp += 1
        
        i -= int(val)

    elif command == "+":
        flag = flag[:-1]

        itmp = i - 1
        val = ""
        
        while (code[itmp][j].isdigit()):
            val += code[itmp][j]
            itmp -= 1                 

        i += int(val)

    elif command == "%":
        flag = flag[::-1]
        i += 1

    elif command == "[":
        j += 1
        stack.push(code[i][j])
        j += 1

    elif command == "]":
        j -= 1
        stack.push(code[i][j])
        j -= 1
    
    elif command == "*":
        i -= 1
        stack.push(code[i][j])
        i -= 1

    elif command == ".":
        i += 1
        stack.push(code[i][j])
        i += 1

    elif command == "<":
        jtmp = j + 1
        val = ""
        while (code[i][jtmp].isdigit()):
            val += code[i][jtmp]
            jtmp += 1

        j -= int(val)

    elif command == ">":
        jtmp = j - 1
        val = ""
        while (code[i][jtmp].isdigit()):
            val += code[i][jtmp]
            jtmp -= 1

        j += int(val)
    
    elif command == "^":
        itmp = i + 1
        val = ""
        while (code[itmp][j].isdigit()):
            val += code[itmp][j]
            itmp += 1
        
        i -= int(val)

    elif command == "v":
        itmp = i - 1
        val = ""        
        while (code[itmp][j].isdigit()):
            val += code[itmp][j]
            itmp -= 1                 

        i += int(val)

    print(val)


for start in start_points:
    start_line = start[0]
    start_column = start[1]
    i = start_line
    j = start_column
    stack.empty()

    while True:
        cmd = code[i][j]
        print(i, j)

        if cmd == "@":
            print("End of path")
            break

        else:
            interpreter(cmd)

print(flag)