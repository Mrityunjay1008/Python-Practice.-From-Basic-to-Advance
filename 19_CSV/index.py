import csv

with open("19_CSV/students.csv", "r") as f, \
    open("19_CSV/new_students1.csv", "w", newline="") as new_file:

    reader = csv.reader(f)
    writer = csv.writer(new_file, delimiter="\t")

    for row in reader:
        writer.writerow(row)

with open("19_CSV/new_students1.csv", "r") as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        # print(row)
        pass


with open("19_CSV/students.csv") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    for row in reader:
        # print(f'Name: {row["Name"]}, Class: {row["Class"]}, Age: {row["Age"]}')
        pass

    with open("19_CSV/new_students2.csv", "w") as new_file:
        field_names = ["StudentID","Name","Class","Age","Maths","Science","English"]
        csv_writer = csv.DictWriter(new_file,delimiter="\t",fieldnames=field_names)
        csv_writer.writeheader()
        for lines in rows:
            csv_writer.writerow(lines)

        