import sys

sourceFileName = sys.argv[1]
sourceFileName = sourceFileName[:-4]
extension = "nocom"
name = sourceFileName + extension

with open(sys.argv[1], 'r') as file:
    with open(name, 'w') as compose:
        for line in file:
            if(line.find('//') != -1):
                continue
            elif (line.find('/*') != -1):
                continue
            elif (line.find('*') != -1):
                continue   
            elif (line.find('*/') != -1):
                continue        
            else:
                compose.write(line)
                print(line, end = '')

stack = []
with open(name, 'r') as file:
    for i in range(len(line)):
        if (line[i] == "{" or line[i] == '(' or line[i] == "["):
            stack.append(line[i])
        if (line[i] != "}" or line[i] != ")" or line[i] != "]"):
            continue
        if (line[i] == "}" and stack[-1] == "{"):
            stack.pop()
        else:
            print("not balanced")
            break
        if (line[i] == ")" and stack[-1] == "("):
            stack.pop()
        else:
            print("not balanced")
            break
        if (line[i] == "]" and stack[-1] == "["):
            stack.pop()
        else:
            print("not balanced")
            break
if (len(stack) == 0):
    print("balanced")
else:
    print("not balanced")