def compute_grade(class_standing, exam_grade):
    return round((class_standing * 0.6) + (exam_grade * 0.4), 2)

class StudentRecordManager:
    def __init__(self):
        self.records = {}
        self.file_path = None
    
    def open_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 5:
                        student_id, first_name, last_name, class_standing, exam = parts
                        self.records[student_id] = {
                            "name": (first_name, last_name),
                            "class_standing": float(class_standing),
                            "exam": float(exam)
                        }
            self.file_path = filename
            print("File loaded successfully.")
        except FileNotFoundError:
            print("File not found.")
    
    def save_file(self):
        if self.file_path:
            with open(self.file_path, 'w') as file:
                for sid, data in self.records.items():
                    file.write(f"{sid},{data['name'][0]},{data['name'][1]},{data['class_standing']},{data['exam']}\n")
            print("File saved successfully.")
        else:
            print("No file path specified. Use 'Save As' option.")
    
    def save_as_file(self, filename):
        self.file_path = filename
        self.save_file()
    
    def show_all_records(self):
        for sid, data in self.records.items():
            print(f"{sid}: {data}")
    
    def order_by_last_name(self):
        sorted_records = sorted(self.records.items(), key=lambda x: x[1]['name'][1])
        for sid, data in sorted_records:
            print(f"{sid}: {data}")
    
    def order_by_grade(self):
        sorted_records = sorted(self.records.items(), key=lambda x: compute_grade(x[1]['class_standing'], x[1]['exam']), reverse=True)
        for sid, data in sorted_records:
            print(f"{sid}: {data}")
    
    def show_student_record(self, student_id):
        if student_id in self.records:
            print(self.records[student_id])
        else:
            print("Student not found.")
    
    def add_record(self, student_id, first_name, last_name, class_standing, exam):
        if student_id in self.records:
            print("Student ID already exists.")
        else:
            self.records[student_id] = {"name": (first_name, last_name), "class_standing": class_standing, "exam": exam}
            print("Record added successfully.")
    
    def edit_record(self, student_id, first_name=None, last_name=None, class_standing=None, exam=None):
        if student_id in self.records:
            if first_name:
                self.records[student_id]['name'] = (first_name, self.records[student_id]['name'][1])
            if last_name:
                self.records[student_id]['name'] = (self.records[student_id]['name'][0], last_name)
            if class_standing is not None:
                self.records[student_id]['class_standing'] = class_standing
            if exam is not None:
                self.records[student_id]['exam'] = exam
            print("Record updated successfully.")
        else:
            print("Student not found.")
    
    def delete_record(self, student_id):
        if student_id in self.records:
            del self.records[student_id]
            print("Record deleted successfully.")
        else:
            print("Student not found.")

def main():
    manager = StudentRecordManager()
    while True:
        print("\nMenu:")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("11. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            filename = input("Enter filename: ")
            manager.open_file(filename)
        elif choice == "2":
            manager.save_file()
        elif choice == "3":
            filename = input("Enter filename: ")
            manager.save_as_file(filename)
        elif choice == "4":
            manager.show_all_records()
        elif choice == "5":
            manager.order_by_last_name()
        elif choice == "6":
            manager.order_by_grade()
        elif choice == "7":
            student_id = input("Enter student ID: ")
            manager.show_student_record(student_id)
        elif choice == "8":
            student_id = input("Enter student ID (6 digits): ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            class_standing = float(input("Enter class standing grade: "))
            exam = float(input("Enter major exam grade: "))
            manager.add_record(student_id, first_name, last_name, class_standing, exam)
        elif choice == "9":
            student_id = input("Enter student ID: ")
            first_name = input("Enter new first name (or press Enter to skip): ")
            last_name = input("Enter new last name (or press Enter to skip): ")
            class_standing = input("Enter new class standing grade (or press Enter to skip): ")
            exam = input("Enter new major exam grade (or press Enter to skip): ")
            manager.edit_record(student_id, first_name or None, last_name or None, float(class_standing) if class_standing else None, float(exam) if exam else None)
        elif choice == "10":
            student_id = input("Enter student ID: ")
            manager.delete_record(student_id)
        elif choice == "11":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
