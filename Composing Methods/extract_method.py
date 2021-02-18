# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math


def print_stat():
    grade_list = input_grades()

    # Calculate the mean and standard deviation of the grades
    mean, sd = calculate_mean_and_sd(grade_list)
    # print out the mean and standard deviation in a nice format.
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')


def calculate_mean_and_sd(grade_list):
    sum = sum_of_grades(grade_list)
    mean = sum / len(grade_list)
    sd = 0  # standard deviation
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list))
    return mean, sd


def input_grades():
    grade_list = []
    # Get the inputs from the user
    n_student = 5
    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))
    return grade_list


def sum_of_grades(grade_list):
    # Calculate the mean and standard deviation of the grades
    sum = 0  # Do you think 'sum' is a good var name? Run pylint to figure out!
    for grade in grade_list:
        sum = sum + grade
    return sum


print_stat()
