students={
    "Alice":{"math":85, "English":92, "science":88},
     "Bob":{"math":78, "English":81, "science":85},
      "Charlie":{"math":95, "English":89, "science":94}
}
top_student= max(students, key=lambda x: sum(students(x).values())/len(students(x)))
print(top_student)
