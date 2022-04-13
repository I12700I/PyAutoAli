from PyAutoAli import *

if __name__ == '__main__':
    pyAuto = PyAutoAli()
    while True:
        print("""Welcome to the PyAutoAli Open Source project
To start, select the operating mode and proceed according to the instructions:
0: exit
1: manual input
2: file input""")
        mode = int(input(""))
        if mode==0:
            break
        elif mode==1:
            print("In this mode you have to enter by one link")
            while True:
                try:
                    print("Enter url or 0 to exit")
                    url = input()
                    if url == "0": break
                    pyAuto.checkurl(url)
                    print("Enter the path to the file where you want to save the result (by default ./file.csv)")
                    path=input()
                    if path == "": path = "./file.csv"
                    pyAuto.savefile(path)
                except Exception as e:
                    raise
        elif mode==2:
            print("In this mode, you must enter the path to the file")
            while True:
                try:
                    print("Enter path or 0 to exit")
                    path=input()
                    if path == "0": break
                    pyAuto.checkfile(path)
                    print("Enter the path to the file where you want to save the result (by default ./file.csv)")
                    path=input()
                    if path == "": path = "./file.csv"
                    pyAuto.savefile(path)
                except Exception as e:
                    raise
        else:
            print("Invalid value entered!")
            input()
