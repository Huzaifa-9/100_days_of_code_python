import pandas

student = {
    "student": ["Angela", "James", "Lily"],
    "score": [56,76,98]
}

# for key,value in student.items():
#     print(key)
#     print(value)

student_data_frame = pandas.DataFrame(student)
print(student_data_frame, "\n","-"*30)

for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row.student)
    print(row.score)