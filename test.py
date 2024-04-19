def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    for student in student_info:
        print(student[0])
        print(student[1])

student_info = [["Charles", 90], ["Tony", 80], ["Alex", 100]]

print(perfect_score(student_info))