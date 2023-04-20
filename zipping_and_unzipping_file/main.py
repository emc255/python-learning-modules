import zipfile

if __name__ == '__main__':
    file = open("file_one.txt", "w+")
    file.write("one file")
    file.close()

    file = open("file_two.txt", "w+")
    file.write("two file")
    file.close()

    compress_file = zipfile.ZipFile("zip/comp_file.zip", "w")
    compress_file.write("file_one.txt", compress_type=zipfile.ZIP_DEFLATED)
    compress_file.write("file_two.txt", compress_type=zipfile.ZIP_DEFLATED)
    compress_file.close()

    zip_object = zipfile.ZipFile("zip/comp_file.zip", "r")
    zip_object.extractall("unzip")
