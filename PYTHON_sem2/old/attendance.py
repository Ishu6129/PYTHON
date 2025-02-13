subjects=["Maths","Chemistry","Physics","Computer","English"]
student_list=["Aakriti","Akshita","Astha","Anushka","Princy","Palak","Twinkle"]
student_rollno=[101,102,103,104,105,106,107]
maths={}
chemistry={}
physics={}
computer={}
english={}
all_record=[maths,chemistry,physics,computer,english]
date_month=input("Enter date as per format dd-mm-yy : ")
main=True
while main:
    if len(date_month)==8 and date_month[2]=="-" and date_month[5]=="-":
        print()
        print("1.Mark Attendance")
        print("2.Attendace record")
        print("3.Update record")
        print("4.Exit")
        print()
        ch=int(input("Enter choosen number : "))
        while True:
            if ch==1:
                print()
                print("******* subjects *******")
                print()
                print("1.Maths")
                print("2.Chemistry")
                print("3.Physics")
                print("4.Computer")
                print("5.English")
                print()
                sub=int(input("Enter subject number: "))
                a=[]
                if sub in [1,2,3,4,5]:
                    print("Mark A/P")
                    for i in range(0,len(student_list)):
                        while True:
                            print(student_rollno[i],student_list[i],":",end=" ")
                            m=input().upper()
                            if m!=" " and m!="" and (m in ["A","P"]):
                                a.append(m)
                                break
                            else:
                                print("!!! please mark A/P only !!!")
                                print()
                    all_record[sub-1][date_month]=a
                    print()
                    print("*** ATTENDACE MARKED ***")
                    print()
                    break
                else:
                    print()
                    print("!!! please enter valid subject number !!!")
                    print()
            elif ch==2:
                print()
                print("******* subjects *******")
                print()
                print("1.Maths")
                print("2.Chemistry")
                print("3.Physics")
                print("4.Computer")
                print("5.English")
                print("6.Exit")
                print()
                c=int(input("Enter subject number : "))
                if c in [1,2,3,4,5]:
                    s=0
                    for i in all_record[c-1]:
                        s=1
                        print()
                        print("Date :- ",i)
                        print()
                        for j in all_record[c-1][i]:
                            print(student_rollno[s-1],":",j.upper())
                            s+=1
                    if s==0:
                        print()
                        print("!!! No record Found !!!")
                        print()
                elif c==6:
                    print()
                    break
                else:
                    print()
                    print("!!! please enter valid subject number !!!")
                    print()
                
            elif ch==3:
                print()
                print("******* subjects *******")
                print()
                print("1.Maths")
                print("2.Chemistry")
                print("3.Physics")
                print("4.Computer")
                print("5.English")
                print()
                us=int(input("Enter subject number: "))
                if us in [1,2,3,4,5]:
                       while True:
                           u_date=input("Enter Date : ")
                           if len(u_date)==8 and u_date[2]=="-" and u_date[5]=="-":
                               if u_date not in all_record[us-1]:
                                   print()
                                   print("!!! Record not found for ",u_date,"!!!")
                                   print()
                               else:
                                   print()
                                   s_rollno=int(input("Enter student rollno : "))
                                   if s_rollno in student_rollno:
                                       a_p=input("Enter A/P : ")
                                       all_record[us-1][u_date][student_rollno.index(s_rollno)]=a_p
                                       print()
                                       print("*** UPDATION SUCCESSFUL ***")
                                       print()
                                       break
                                   else:
                                       print()
                                       print("!!! Student Rollno.",s_rollno,"not found !!!")
                                       print()
                               break
                           else:
                               print()
                               print("!!! Please match the format dd-mm-yy !!!")
                               print()
                       break
                else:
                    print()
                    print("!!! please enter valid subject number !!!")
                    print()
            elif ch==4:
                main=False
                break
            else:
                print()
                print("!!! Please enter valid choice !!!")
                print()
                ch=int(input("Enter choosen number : "))           
    else:
        print()
        print("!!! Please match the format \'dd-mm-yy\' !!!")
        print()
        date_month=input("enter dd-mm- yy : ")
