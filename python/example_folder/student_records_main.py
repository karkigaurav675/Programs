import os
import json

path = "C:/Users/asus/Documents/Programs/python/example_folder/student_records.json"

def get_student_data():
    student = {
        "id": int(input("Enter student ID: ")),
        "Name": input("Enter student Name: "),
        "Address": input("Enter student Address: "),
        "Age": int(input("Enter student Age: ")),
        "Number": int(input("Enter student Mobile Number: ")),
        "EducationalQualification": []
    }
    
    print("Enter educational qualifications. Type 'skip' to finish.")
    
    while True:
        qualification_name = input("Enter educational qualification name (or type 'skip' to finish): ")
        if qualification_name.lower() == 'skip':
            break
        
        passing_year = int(input("Enter year of passing: "))
        percentage = float(input("Enter percentage: "))
        
        student['EducationalQualification'].append({
            "qualificationName": qualification_name,
            "passingyear": passing_year,
            "percentage": percentage
        })
    
    return student

def load_data():
    if os.path.isfile(path):
        with open(path, "r") as file:
            return json.load(file)
    return []

def save_data(data):
    with open(path, "w") as file:
        json.dump(data, file, indent=4)
    print("Data saved successfully!")

def register_student():
    students = load_data()
    students.append(get_student_data())
    save_data(students)

def display_students():
    students = load_data()
    if students:
        for student in students:
            print(json.dumps(student, indent=4))
    else:
        print("No student data available.")

def find_student_by_number():
    number = int(input("Enter the mobile number of the student to search: "))
    students = load_data()
    for student in students:
        if student['Number'] == number:
            print("Student found:")
            print(json.dumps(student, indent=4))
            return
    print("No student found with that mobile number.")

def search_by_educational_qualification():
    qualification_name = input("Enter educational qualification name to search (or leave blank to skip): ")
    passing_year = int(input("Enter year of passing to search (or 0 to skip): "))
    percentage_min = float(input("Enter minimum percentage to search (or 0 to skip): "))
    
    students = load_data()
    found = False

    for student in students:
        eqs = student.get('EducationalQualification', [])
        for eq in eqs:
            if (qualification_name.lower() in eq.get('qualificationName', '').lower() or qualification_name == '') and \
               (passing_year == 0 or eq.get('passingyear') == passing_year) and \
               (percentage_min == 0 or eq.get('percentage') >= percentage_min):
                print("Student found:")
                print(json.dumps(student, indent=4))
                found = True
                break  # Break after finding the first match for this student

    if not found:
        print("No student found matching the criteria.")

def get_total_percentage(student):
    """Return the total percentage of a student."""
    return student.get('TotalPercentage', 0)

def show_top_3_students_by_percentage_sum():
    # Load student data
    students = load_data()
    
    # Check if student data is available
    if not students:
        print("No student data available.")
        return
    
    # Calculate the total percentage for each student
    for student in students:
        qualifications = student.get('EducationalQualification', [])
        total_percentage = 0
        for eq in qualifications:
            total_percentage += eq.get('percentage', 0)
        student['TotalPercentage'] = total_percentage
    
    # Sort students by total percentage in descending order and get the top 3
    sorted_students = sorted(students, key=lambda student: student['TotalPercentage'], reverse=True)
    top_students = sorted_students[:3]
    
    # Print the top 3 students
    if top_students:
        print("Top 3 students based on total percentage:")
        for student in top_students:
            # Print summary line with student ID and total percentage
            print(f"Student ID: {student['id']}, Total Percentage: {student['TotalPercentage']:.2f}%")
            # Print full details in JSON format
            print(json.dumps(student, indent=4))
            print()  # Print a blank line for better readability

def show_menu():
    menu = {
        '1': register_student,
        '2': display_students,
        '3': find_student_by_number,
        '4': search_by_educational_qualification,
        '5': show_top_3_students_by_percentage_sum,
        '0': exit
    }

    while True:
        print("1. Register Student")
        print("2. View Students")
        print("3. Search Student by Mobile Number")
        print("4. Search Student by Educational Qualification")
        print("5. Show Top 3 Students by Total Percentage")
        print("0. Exit")
        
        choice = input("Choose an option: ")
        action = menu.get(choice)
        if action:
            action()
        else:
            print("Invalid option, please try again.")

# if __name__ == "__main__":
#     show_menu()
show_menu()