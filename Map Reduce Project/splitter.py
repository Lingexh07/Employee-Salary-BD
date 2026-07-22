def split_file():

    with open("input.txt","r") as file:
        lines=file.readlines()

    middle=len(lines)//2

    with open("chunk1.txt","w") as file:
        file.writelines(lines[:middle])

    with open("chunk2.txt","w") as file:
        file.writelines(lines[middle:])

    print("chunk1.txt and chunk2.txt created")