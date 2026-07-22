def mapper(input_file,output_file):

    with open(input_file,"r") as file:
        lines=file.readlines()

    with open(output_file,"w") as file:

        for line in lines:

            data=line.strip().split(",")

            department=data[2]
            salary=data[3]

            file.write(f"{department},{salary}\n")

    print(output_file,"created")