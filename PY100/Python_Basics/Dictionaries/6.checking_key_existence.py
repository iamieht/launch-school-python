# Check whether the keys 'name' and 'grade' exist in the following dictionary:
student = {
    'id': 123,
    'grade': 'B',
}

print(student.get('name'))
print(student.get('grade'))
print('name' in student)
print('grade' in student)
