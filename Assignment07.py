# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   VPreap,5/28/2024,Created Script
# ------------------------------------------------------------------------------------------ #

import json

class FileProcessor:
    """Handles reading from and writing to a file."""

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """Reads data from a JSON file."""
        try:
            with open(file_name, 'r') as file:
                student_data.extend(json.load(file))
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from '{file_name}'.")

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """Writes data to a JSON file."""
        try:
            with open(file_name, 'w') as file:
                json.dump(student_data, file, indent=4)
        except Exception as e:
            output_error_messages("Error writing data to file.", e)

class IO:
    """Handles input and output operations."""

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """Outputs error messages."""
        print(f"Error: {message}")
        if error:
            print(f"Details: {str(error)}")

    @staticmethod
    def output_menu(menu: str):
        """Outputs the program menu."""
        print(menu)

    @staticmethod
    def input_menu_choice():
        """Gets user menu choice."""
        return input("Enter your choice: ")

    @staticmethod
    def output_student_courses(student_data: list):
        """Outputs student data."""
        for student in student_data:
            print(f"Student: {student['first_name']} {student['last_name']}, Course: {student['course_name']}")

    @staticmethod
    def input_student_data():
        """Gets input for student data."""
        first_name = input("Enter student's first name: ")
        last_name = input("Enter student's last name: ")
        course_name = input("Enter course name: ")
        return {"first_name": first_name, "last_name": last_name, "course_name": course_name}

class Person:
    """Represents a person."""

    def __init__(self):
        self._first_name = ""
        self._last_name = ""

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not value:
            raise ValueError("First name cannot be empty.")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not value:
            raise ValueError("Last name cannot be empty.")
        self._last_name = value

class Student(Person):
    """Represents a student."""

    def __init__(self):
        super().__init__()
        self._course_name = ""

    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, value):
        if not value:
            raise ValueError("Course name cannot be empty.")
        self._course_name = value

def main():
    MENU = """---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
-----------------------------------------"""
    FILE_NAME = "Enrollments.json"
    menu_choice = ""
    students = []

    # Load data from file
    FileProcessor.read_data_from_file(FILE_NAME, students)

    while menu_choice != "4":
        IO.output_menu(MENU)
        menu_choice = IO.input_menu_choice()

        if menu_choice == "1":
            try:
                student_data = IO.input_student_data()
                students.append(student_data)
            except ValueError as e:
                IO.output_error_messages(str(e))
        elif menu_choice == "2":
            IO.output_student_courses(students)
        elif menu_choice == "3":
            FileProcessor.write_data_to_file(FILE_NAME, students)
            print("Data saved to file.")
        elif menu_choice == "4":
            print("Exiting the program...")
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()