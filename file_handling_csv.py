import csv

filename = "students.csv"

try:
    # Writing data to CSV
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Course"])
        writer.writerow([1, "Sai Charan", "Python"])
        writer.writerow([2, "Rahul", "Data Science"])
        writer.writerow([3, "Anita", "Web Development"])

    # Reading data from CSV
    with open(filename, "r") as file:
        reader = csv.reader(file)
        print("CSV File Contents:")
        for row in reader:
            print(row)

except Exception as e:
    print("Error:", e)
finally:
    print("CSV file operation completed.")
