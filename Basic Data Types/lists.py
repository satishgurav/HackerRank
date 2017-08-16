import fileinput
if __name__ == '__main__':
    N = int(raw_input())
    lst = list()
    for line in fileinput.input():
        cmd = line.split()
        if(cmd[0] == "insert"):
            lst.insert(int(cmd[1]), int(cmd[2]))
        elif(cmd[0] == "remove"):
            lst.remove(int(cmd[1]))
        elif(cmd[0] == "append"):
            lst.append(int(cmd[1]))
        elif(cmd[0] == "sort"):
            lst.sort()
        elif(cmd[0] == "pop"):
            lst.pop()
        elif(cmd[0] == "reverse"):
            lst.reverse()
        elif(cmd[0] == "print"):
            print(lst)
