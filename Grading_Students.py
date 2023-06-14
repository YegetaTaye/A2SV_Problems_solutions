def gradingStudents(grades):
    result = []

    for grade in grades:
        test = (((grade//5)*5)+5)-grade
        if grade >= 38:
            if test < 3:
                grade = (((grade//5)*5)+5)
                result.append(grade)
            if not test < 3:
                result.append(grade)
        elif grade <= 5:
            continue
        else:
            result.append(grade)
    return [print(i) for i in result]

grades = [4, 73, 67, 38, 33]
gradingStudents(grades)
