def partition():

    files = ["map1.txt", "map2.txt"]

    p0 = open("partitions/partition0.txt", "w")
    p1 = open("partitions/partition1.txt", "w")

    for filename in files:

        with open(filename, "r") as file:

            for line in file:

                data = line.strip().split(",")

                department = data[0]
                salary = data[1]

                reducer = hash(department) % 2

                if reducer == 0:
                    p0.write(f"{department},{salary}\n")
                else:
                    p1.write(f"{department},{salary}\n")

    p0.close()
    p1.close()

    print("partition0.txt and partition1.txt created")