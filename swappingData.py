def swappingFileData() :
    f1in = input("Enter name of the first file")
    f2in = input("Enter name of the second file")

    f1op = open(f1in, "r")
    f2op = open(f2in, "r")

    f1r = f1op.read()
    f2r = f2op.read()

    f1ow = open(f1in, "w")
    f2ow = open(f2in, "w")

    f1ow.write(f2r)
    f2ow.write(f1r)

swappingFileData()