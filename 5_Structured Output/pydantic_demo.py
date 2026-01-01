from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Student(BaseModel):
    name : str = 'Bob'
    age : Optional[int] = None
    email : Optional[EmailStr] = None
    cgpa : float = Field(gt=0,lt=10,default=0.0,description='A decimal value representing the cgpa of the student')  # gt = greater than, lt = less than

# new_student = {'name': 32} # Throws an 'error' [Unlike TypedDict]

# new_student = {'name': 'Aryan Gupta','age':'21'}  # Pydantic will convert 'age' to 'int'[Type Coercion]
# new_student = {'name': 'Aryan Gupta','age':'21',email='abc'}  # Throws an 'error' [Built-in Validation]

new_student = {'name': 'Aryan Gupta','age':21,'email':'abc@gmail.com','cgpa':8.6}  
new_student2 = {}  # Using default value

student = Student(**new_student)
student2 = Student(**new_student2)

print('\n',student)
print('\n',student2)

# print(type(student))  ==> <class '__main__.Student'>

student_dict = dict(student)  # Convert to dictionary
print('\nDictionary : ',student_dict)
print("Age : ",student_dict['age'])
print("Name : ",student_dict['name'])

student_json = student.model_dump_json()  # Convert to JSON
print('\nJSON :',student_json)