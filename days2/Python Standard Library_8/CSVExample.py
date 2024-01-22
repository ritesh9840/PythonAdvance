import csv

# Writing to a CSV file
data_to_write = [
    ["Name", "Age", "Score"],
    ["Alice", 25, 95],
    ["Bob", 30, 85],
    ["Charlie", 22, 90]
]

with open("example.csv", mode="w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data_to_write)

print("Data written to 'example.csv' successfully.")

# Reading from a CSV file
with open("example.csv", mode="r") as csv_file:
    csv_reader = csv.reader(csv_file)

    # Skip the header row if it exists
    header = next(csv_reader, None)
    if header:
        print("CSV Header:", header)

    # Iterate through rows and print data
    for row in csv_reader:
        print("Row:", row)
