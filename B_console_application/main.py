# B. Create a console application for an IT Academy with the
# following features:
# a) The academy program should have a fixed course of study.
# b) If a new student is interested in the academy program the student can
# inquiry about the course of study.
# c) Student Registration with Rs. 20000 (deposit). Students are allowed to
# pay in two installments with Rs. 10000 each.
# d) Display all the student’s information from the academy with their payments
# and remaining payments.
# e) Update the student information if needed.
# f) Delete the student information if he/she left the program.
# g) Return the deposit amount(Rs. 20000) to the students after the
# successful completion of the course and check the balance.
# Remember it should be a full feature CONSOLE APP. You can store
# the course of study and the student’s detail in your preferred file
# format(.csv, .txt, etc).
# Ignore the permissions for now. Anyone who runs the script is allowed to
# access all the features. Develop the app with OOP Approach.

import csv
import os


class Student:
    def __init__(self):
        self.std_name = ''
        self.std_age = 0
        self.std_course = ''

        self.deposit_status = ''
        self.deposit_amount_remaining = ''

        self.std_path = os.path.dirname(os.path.abspath(__file__))
        self.std_field_names = ["std_name", "std_age", "std_course",
                                'std_deposit_status', 'std_deposit_amount_remaining']

        with open(self.std_path+'/csvs/students.csv', 'w+', newline='') as std_file:
            writer = csv.DictWriter(
                std_file, fieldnames=self.std_field_names)
            writer.writeheader()

    def set_new_registration(self):
        pass

    def view_student_details(self, std_name):
        pass

    def update_student_details(self, std_name):
        pass


class Course:
    def __init__(self):
        self.course_path = os.path.dirname(os.path.abspath(__file__))
        self.course_field_names = ["course_id",
                                   "course_name", "course_duration"]

        with open(self.course_path+'/csvs/courses.csv', 'w+', newline='') as courses_file:
            writer = csv.DictWriter(
                courses_file, fieldnames=self.course_field_names)
            writer.writeheader()

    def add_new_course(self):
        input_course_id = input("Enter course id:")
        input_course_name = input("Enter course name:")
        input_course_duration = input("Enter course duration:")
        data = {"course_id": input_course_id, "course_name": input_course_name,
                "course_duration": input_course_duration}

        with open(self.course_path+'/csvs/courses.csv', 'w+', newline='') as courses_file:
            writer = csv.DictWriter(
                courses_file, fieldnames=self.course_field_names)
            writer.writerow(data)

    def view_list_of_available_course(self):
        with open(self.course_path+'/csvs/courses.csv', 'r') as courses_file:
            data = csv.DictReader(courses_file)

            for everyrow in data:
                print(everyrow.get('course_name'))

    def detail_view_of_single_course(self, course_name):
        with open(self.course_path+'/csvs/courses.csv', 'r') as courses_file:
            data = csv.DictReader(courses_file)

            for each_course in data:
                if (each_course["course_name"] == course_name):
                    print(
                        f"Course Details::\nCourse ID:{each_course.get('course_id')}\nCourse Name:{each_course.get('course_name')}\nCourse Name:{each_course.get('course_name')}\nDuration:{each_course.get('course_duration')}")
                else:
                    print("Sorry, we dont have that course available as of now.")


class Academy(Course, Student):
    def __init__(self):
        self.total_deposit_required = 20000

    def menu(self):
        pass
