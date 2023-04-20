import shutil

if __name__ == '__main__':
    directory_to_zip = "zip"
    output_filename = "zip/example-zip"
    shutil.make_archive(output_filename, "zip", directory_to_zip)

    shutil.unpack_archive("zip/comp_file.zip", "unzip/final", "zip")
