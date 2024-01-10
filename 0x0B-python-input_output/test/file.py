with open("test_file.txt", "r+") as f:
    print(f.tell())
    print(f.readline(), end='')
    print(f.read(4))
    print(f.tell())
    print(f.seek(0, 2))
    print(f.seek(f.tell(), 1))
