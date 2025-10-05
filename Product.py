import os

DOCUMENTS_FOLDER_PATH = os.getcwd()
doc_path = DOCUMENTS_FOLDER_PATH

def register_student():
    print("============== Register Student ==============")
    student_no = input("Enter Student ID: ")
    last_name = input("Enter Last Name: ")
    first_name = input("Enter First Name: ")
    mid_initial = input("Enter Middle Initial: ")
    program = input("Enter Program: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender: ")
    birthday = input("Enter Birthday: ")
    contact_no = input("Enter Contact Number: ")

    data = [
        f"Student No.: {student_no}",
        f"Full Name: {last_name}, {first_name} {mid_initial}.",
        f"Program: {program}",
        f"Age: {age}",
        f"Gender: {gender}",
        f"Birthday: {birthday}",
        f"Contact Number: {contact_no}"
    ]
    file_path = os.path.join(doc_path, f"{student_no}.txt")
    try:
        with open(file_path, "w") as f:
            for line in data:
                f.write(line + "\n")
        print(f"\nSUCCESS: Student record for {student_no} saved to {file_path}")
    except Exception as e:
        print(f"\nERROR: Could not save file. Details: {e}")

def open_student_record():
    print("\n============== Open Student Record ==============")
    student_no = input("Enter Student ID to view record: ")
    file_path = os.path.join(doc_path, f"{student_no}.txt")

    try:
        with open(file_path, 'r') as f:
            print(f"\n--- RECORD FOR ID: {student_no} ---")
            for line in f:
                print(line.strip())
            print("-----------------------------------")
    
    except FileNotFoundError:
        print(f"\nERROR: Student record {student_no}.txt not found.")
    except Exception as e:
        print(f"\nAn error occurred while reading the file: {e}")

def main_menu():
    print("\n--- Student Records Management System ---")
    print(f"File Location: {doc_path}")
    print("-" * 40)
    
    while True:
        print("\nMain Menu:")
        print("1. Register Student")
        print("2. Open Student Record")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            register_student()
        elif choice == '2':
            open_student_record()
        elif choice == '3':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()
