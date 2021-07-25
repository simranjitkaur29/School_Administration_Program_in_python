import csv

def write_into_csv(info_list):
    with open('student_info.csv','a',newline='')as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
          writer.writerow(["Name","Age","Contact-No.","Email-Id"])
        writer.writerow(info_list)

if __name__=='__main__':

 condition=True

 student_num=1
while(condition):
     student_info=input("Enter  student number #{} information in the following format[Name,Age,Contact,Email_Id]: ".format(student_num))
     print("Entered Information is: "+ student_info)
     #here using split 
     student_info_list=student_info.split(' ')
     print("Entered split information is: "+ str(student_info_list))
     print("\n The Entered information is: \nName: {}\nAge: {}\nContact_number:{}\nEmail-Id:{}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
     #by using format in the place of {} these braces student_information will come
     
     choice_check=input("Is the entered information correct(yes/no): ")

     if choice_check=="yes":
       write_into_csv(student_info_list)
       condition_check=input("Enter [yes/no], if you want to add information for another student: ")
       if condition_check=="yes":
           condition=True
           student_num+=1
       elif condition_check=="no":
          condition=False
     elif choice_check=="no":
         print("/n Please re-enter the value!")

