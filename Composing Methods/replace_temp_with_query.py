# By Kamran Bigdely Nov. 2020
# Replace temp variable with query
# TODO: Use 'extract method' refactoring technique to improve this code.
# If required, use 'replace temp variable with query' technique to make
# it easier to extract methods.


class Employer:
    def __init__(self, name):
        self.name = name

    def send(self, students):
        print("Students' contact info were sent to", self.name + '.')


class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name

    def get_gpa(self):
        return self.gpa

    def send_congrat_email(self):
        print("Congrats", self.name + ". You graduated successfully!")


class School:
    def __init__(self, students) -> None:
        self.students = students

    def process_graduation(self):
        # Find the students in the school who have successfully graduated.
        passed_students = self.find_passed_students()

        # print student's name who graduated.
        self.print_student_names(passed_students)

        # Send congrat emails to them.
        self.send_congrats_emails(passed_students)

        # Find the top 10% of them and send their contact to the top employers
        self.send_top_to_employers(passed_students)

    def send_top_to_employers(self, passed_students):
        passed_students.sort(key=lambda s: s.get_gpa())
        percentile = 0.9
        index = int(percentile * len(passed_students))
        top_10_percent = passed_students[index:]
        top_employers = self.get_top_employers()
        for e in top_employers:
            e.send(top_10_percent)

    def get_top_employers(self):
        return [
            Employer('Microsoft'),
            Employer('Free Software Foundation'),
            Employer('Google')
        ]

    def send_congrats_emails(self, passed_students):
        for s in passed_students:
            s.send_congrat_email()
        return s

    def print_student_names(self, passed_students):
        # print student's name who graduated.
        print('*** Student who graduated *** ')
        for s in passed_students:
            print(s.name)
        print('****************************')

    def find_passed_students(self):
        # Find the students in the school who have successfully graduated.
        MIN_GPA = 2.5  # minimum acceptable GPA
        passed_students = []
        for s in self.students:
            if s.get_gpa() > MIN_GPA:
                passed_students.append(s)
        return passed_students


students = [
    Student(2.1, 'Pinocchio'),
    Student(2.3, 'goku'),
    Student(2.7, 'toro'),
    Student(3.9, 'naruto'),
    Student(3.2, 'kami'),
    Student(3, 'guts')
]
school = School(students)
school.process_graduation()
