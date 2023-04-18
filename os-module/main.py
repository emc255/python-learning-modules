import os
import shutil

if __name__ == '__main__':
    file = open("sample.txt", "w+")
    file.write("this is a test string")
    file.close()
    print(os.getcwd())
    print(os.listdir())
    print(os.listdir("C://Users"))

    shutil.move("sample.txt", "move-here")
