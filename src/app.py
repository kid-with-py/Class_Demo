#python Object Oriented Programming-->



class Students:

    def __init__(self, firts_name, last_name, roll_num ):
        self.first_name = firts_name
        self.last_name = last_name
        self.roll_num = roll_num

# To Print Full-Name Using First_name And Last_name-->

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)    
# To Create Email With Rspect to Name-->

    def email(self):
        return self.first_name + '.' + '@class.demo'


std_1 = Students('Chris', 'Hemsworth', 10)
std_2 = Students('Chris', 'Pratt', 15)
std_3 = Students('Tom', 'Holland', 20)


#<---- To Get The Roll Number Of Each Students ---->

#print(std_1.roll_num)
#print(std_2.roll_num)
#print(std_3.roll_num)

#<---- To Get The Fullname Of Each Students---->

#print(Students.fullname(std_1)) / #print(std_1.fullname())
#print(Students.fullname(std_2)) / #print(std_2.fullname())
#print(Students.fullname(std_3)) / #print(std_3.fullname())

#<----To Get The Email OF The Each Students---->

#print(Students.email(std_1)) / #print(std_1.email())
#print(Students.email(std_2)) / #print(std_2.email())
#print(Students.email(std_3)) / #print(std_3.email())