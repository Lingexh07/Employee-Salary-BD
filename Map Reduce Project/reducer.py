def reducer(input_file, output_file):

    totals = {}

    with open(input_file, "r") as file:

        for line in file:

            department, salary = line.strip().split(",")

            salary = int(salary)

            if department in totals:
                totals[department] += salary
            else:
                totals[department] = salary

    with open(output_file, "a") as file:

        for department in sorted(totals):
            file.write(f"{department} : {totals[department]}\n")

    print(output_file, "updated")