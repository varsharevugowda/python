def file_read(fname):
    with open(fname, "a") as myfile:
        myfile.write("python program\n")
        myfile.write("java program\n")
    myfile = open(fname)
    print(myfile.read())


file_read('ContentFile.txt')


def file_length(fname):
    with open(fname) as myfile:
        for i, l in enumerate(myfile):
            pass
    return i + 1


print("number of lines in the file: ", file_length('ContentFile.txt'))