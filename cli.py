from PyAutoAli import *

if __name__ == '__main__':
    pyAuto = PyAutoAli()
    while True:
        print("""Welcome to the PyAutoAli Open Source project
To start, select the operating mode and proceed according to the instructions:
0: exit
1: manual input
2: file input
3: settings""")
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
                    pyAuto.check_url(url)
                    print("Enter the path to the file where you want to save the result (by default ./file.csv)")
                    path=input()
                    if path == "": path = "./file.csv"
                    pyAuto.save_file(path)
                except Exception as e:
                    raise
        elif mode==2:
            print("In this mode, you must enter the path to the file")
            while True:
                try:
                    print("Enter path or 0 to exit")
                    path=input()
                    if path == "0": break
                    pyAuto.check_file(path)
                    print("Enter the path to the file where you want to save the result (by default ./file.csv)")
                    path=input()
                    if path == "": path = "./file.csv"
                    pyAuto.save_file(path)
                except Exception as e:
                    raise
        elif mode==3:
            print(f"""In this mode you can change the settings
time sleep: {pyAuto.timesleep}
max images: {pyAuto.maximages}
parser: {pyAuto.parser}""")
            while True:
                try:
                    print("Enter variable or 0 to exit")
                    targetvariable=input()
                    if targetvariable == "0":
                        break
                    for key, values in pyAuto.variables.items():
                        if targetvariable in values:
                            value = input("Enter new value: ")
                            pyAuto.set_settings(key, value)
                except Exception as e:
                    raise
        else:
            print("Invalid value entered!")
            input()
