def sort_file(input_file, output_file):

    with open(input_file, "r") as file:
        lines = file.readlines()

    lines.sort()

    with open(output_file, "w") as file:
        file.writelines(lines)

    print(output_file, "sorted")