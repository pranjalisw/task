#Project for Basic School Administration tool
import csv

def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file == 0:
            writer.writerow(["Name", "Age","Contact Number", "E-Mail_Id"])

        writer.writerow(info_list)

if __name__ == '__main__':
    condition= True
    student_num = 1

    while(condition):
        student_info = input("Enter information of student #{} like (Name Age Contact_number E-mail_Id:".format(student_num))

        splited_row = student_info.split(' ')
        print("\n Entered information is - \n Name :{}\n Age:{}\n Contact_number:{}\n Email_id:{}\n".format(splited_row[0],splited_row[1],splited_row[2],splited_row[3]))

        choice_check = input("Is entered information is correct? (yes/no): ")
        if choice_check== "yes":
            write_into_csv(splited_row)

            check_status = input("Enter (yes/no) to add information of another student: ")
            if check_status == "yes":
              condition= True
              student_num =student_num + 1
            elif check_status == "no":
              condition= False
        elif choice_check== "no":
            print("Please Re-Enter information: ")
