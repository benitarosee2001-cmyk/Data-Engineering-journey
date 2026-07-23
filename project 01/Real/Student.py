class Student:

    def __init__(self,student_id, name, age, grade):

        self.id = student_id
        self.name = name
        self.agr = age
        self.grade = grade


    def show_info(self):

        print(f"""
            ID : {self.id}
            Name : {self.name}
            age : {self.age}
            grade : {self.grade}
            """)


    def update(self, age, grade):

        self.age = age
        self.grade = grade


    def to_dict(self):

        return{
            "ID" : self.id,
            "Name" : self.name,
            "age" : self.age,
            "grade" : self.grade
        }