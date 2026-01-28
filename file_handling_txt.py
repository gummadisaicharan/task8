# TXT File Handling Example

filename = "userdata.txt"

try:
    # Write data to file
    with open(filename, "w") as file:
        file.write("Name: Sai Charan\n")
        file.write("Role: Python Developer Intern\n")
        file.write("Domain: Software Development\n")

    # Read data from file
    with open(filename, "r") as file:
        print("File Contents:")
        print(file.read())

    # Append data to file
    with open(filename, "a") as file:
        file.write("Status: Learning File Handling\n")

    print("\nData appended successfully.")

except FileNotFoundError:
    print("File not found.")
except IOError:
    print("File handling error occurred.")
finally:
    print("TXT file operation completed.")
