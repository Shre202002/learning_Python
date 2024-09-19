#To find Out the line over which the data/Text  is present 

with open(r"D:\learning_Python\pratice\File_IO\five\data.txt") as f:
    p = f.readlines()
    print(p, type(p))
    line = 1
    if ("python" in f.readline()):
        print(f"yes {word} is present")