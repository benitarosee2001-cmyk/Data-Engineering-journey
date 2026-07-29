student_id = 1000

def generat_id():

    global student_id

    student_id += 1

    return student_id


def update_last_id(students):

    global student_id

    if not students:
        student_id = 1000
        return

    student_id = max(student_id for student in students)