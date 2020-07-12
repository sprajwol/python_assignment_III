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
        self.std_path = os.path.dirname(os.path.abspath(__file__))
        self.std_field_names = ["std_name", "std_age", "std_course",
                                'std_deposit_status', 'std_deposit_amount_remaining', 'std_paid_amount']

        with open(self.std_path+'/csvs/students.csv', 'w+', newline='') as std_file:
            writer = csv.DictWriter(
                std_file, fieldnames=self.std_field_names)
            writer.writeheader()

    def set_new_registration(self):
        input_name = input("Enter name:")
        input_age = int(input("Enter age:"))

        Course.view_list_of_available_course(self)
        input_course = input("Enter a course name from above list:")

        print("Do you want to pay the full deposit of 20000 or 2 installment of 10000(Select 1 or 2):")
        print("1. Full deposit")
        print("2. 2 Installment of 1000")
        entry = int(input())
        if (entry == 2):
            input_deposit_status = "paid"
            input_deposit_amount_remaining = 0
            input_paid_amount = 20000

        elif (entry == 1):
            input_deposit_status = "half installment left"
            input_deposit_amount_remaining = 20000 - 10000
            input_paid_amount = 10000

        data = {"std_name": input_name, "std_age": input_age, "std_course": input_course, "std_deposit_status": input_deposit_status,
                "std_deposit_amount_remaining": input_deposit_amount_remaining, "std_paid_amount": input_paid_amount}

        with open(self.std_path+'/csvs/students.csv', 'w+', newline='') as std_file:
            writer = csv.DictWriter(
                std_file, fieldnames=self.std_field_names)
            writer.writerow(data)

    def view_student_details(self, std_name):
        with open(self.std_path+'/csvs/students.csv', 'r') as std_file:
            data = csv.DictReader(std_file)

        for each_std in data:
            if (each_std["std_name"] == std_name):
                print(
                    f"Student Detail::\nName:{each_std.get('std_name')}\nAge:{each_std.get('std_age')}\nCourse:{each_std.get('std_course')}\nDeposit Status:{each_std.get('std_deposit_status')}\nRemaining:{each_std.get('std_deposit_amount_remaining')}\Paid:{each_std.get('std_paid_amount')}")
            else:
                print("Student with that name is not available in our records.")

    def view_all_payment_details(self):
        pass

    def update_student_details(self, std_name):
        pass

    def leave_program(self, std_name):
        with open(self.std_path+'/csvs/students.csv', 'r') as std_file:
            readdata = csv.DictReader(std_file)

            for eachdata in readdata:
                if (readdata.get('std_name') != std_name):
                    with open(self.std_path+'/csvs/students.csv', 'w') as std_file:
                        writer = csv.DictWriter(
                            std_file, fieldnames=self.std_field_names)
                        writer.writerow(eachdata)


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
        Course.__init__(self)
        Student.__init__(self)
        self.total_deposit_required = 20000

    def menu(self):
        print("Regarding Students")
        print("1. New Student Registration")
        print("2. View each Student Details")
        print("3. View payment details of all students")
        print("4. Update student info")
        print("5. Leave Program")

        print("Regarding Courses")
        print("6. View list of all courses")
        print("7. View complete detail of a course")
        print("8. Add new course")

        itemnum = int(
            input("Please enter the number of menu item you want to access:"))

        if (itemnum == 1):
            Student.set_new_registration(self)

        if (itemnum == 2):
            input_data = input(
                "Enter the name of student you want to see details of:")
            Student.view_student_details(self, input_data)

        if (itemnum == 3):
            Student.view_all_payment_details(self)

        if (itemnum == 4):
            input_data = input(
                "Enter the name of student you want to update:")
            Student.update_student_details(self, input_data)

        if (itemnum == 5):
            input_data = input(
                "Enter the name of student to leave program:")
            Student.leave_program(self, input_data)

        if (itemnum == 6):
            Course.view_list_of_available_course(self)

        if (itemnum == 7):
            input_data = input(
                "Enter the name of course you want the details of:")
            Course.detail_view_of_single_course(self, input_data)

        if (itemnum == 8):
            self.add_new_course()


obj1 = Academy()
obj1.menu()
