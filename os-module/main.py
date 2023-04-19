import os

if __name__ == '__main__':
    file = open("sample.txt", "w+")
    file.write("this is a test string")
    file.close()
    print(os.getcwd())
    print(os.listdir())
    print(os.listdir("C://Users"))

    # move file
    # shutil.move("sample.txt", "move-here")

    print("OS WALK")
    current_dir = os.getcwd()
    for folders, sub_folders, files in os.walk(current_dir):
        print(f"Currently looking at {folders}")

        print("The sub folders are:")
        for sub_folder in sub_folders:
            print(f"\tSub Folder: {sub_folder}")

        print("The files are")
        for file in files:
            print(f"\tFile: {file}")
        print("\n")
