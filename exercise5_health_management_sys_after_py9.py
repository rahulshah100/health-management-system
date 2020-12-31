#3 clients -registered for 2 tasks they're:diet & exercise  #1 file for each task of each person
#ask person ->lock or retrieve->id ->diet or exercise   #if u lock thn mention time and date also

print("\t\t---Welcome TO Health Management System !!--- ")

def  getdate():
    import datetime
    return datetime.datetime.now()

lock_retrieve=int(input("\nEnter 1. to lock data\t 2.to retrieve :"))


if(lock_retrieve==1):
    user_id = int(input("Enter Ur Id :"))
    diet_exer = int(input("\nWhat would u like to Lock ?\n\t Press -> 1.Diet  2.Exercise :"))
    text = input("Enter the data u would like to lock   :")

    date_time=getdate()
    date_time=str(date_time)
    date_time="[" + date_time + "] :" + text +"\n"

    if user_id==1:
        if diet_exer==1:
            file_obj=open("exercise5_client_1_D.txt","a+")
            file_obj.write(date_time)
        elif diet_exer == 2:
            file_obj=open("exercise5_client_1_E.txt","a+")
            file_obj.write(date_time)
        else:
            print("Try Again,entering a valid i/p")
    elif user_id==2:
        if diet_exer == 1:
            file_obj = open("exercise5_client_2_D.txt","a+")
            file_obj.write(date_time)
        elif diet_exer == 2:
            file_obj = open("exercise5_client_2_E.txt","a+")
            file_obj.write(date_time)
        else:
            print("Try Again,entering a valid i/p")
    elif user_id == 3:
        if diet_exer == 1:
            file_obj = open("exercise5_client_3_D.txt","a+")
            file_obj.write(date_time)
        elif diet_exer == 2:
            file_obj = open("exercise5_client_3_E.txt","a+")
            file_obj.write(date_time)
    else:
            print("Try Again,entering a valid i/p")


elif(lock_retrieve==2):
    user_id = int(input("Enter Ur Id :"))
    diet_exer = int(input("\nWhat would u like to Retrieve ?\n\t Press -> 1.Diet \t2.Exercise :"))

    if user_id==1:
        if diet_exer == 1:
            file_obj = open("exercise5_client_1_D.txt","r")
            var=file_obj.read()
            print(var)
        elif diet_exer == 2:
            file_obj = open("exercise5_client_1_E.txt","r")
            var = file_obj.read()
            print(var)
        else:
            print("Try Again,entering a valid i/p")
    elif user_id==2:
        if diet_exer == 1:
            file_obj = open("exercise5_client_2_D.txt","r")
            var = file_obj.read()
            print(var)
        elif diet_exer == 2:
            file_obj = open("exercise5_client_2_E.txt","r")
            var = file_obj.read()
            print(var)
        else:
            print("Try Again,entering a valid i/p")
    elif user_id == 3:
        if diet_exer == 1:
            file_obj = open("exercise5_client_3_D.txt","r")
            var = file_obj.read()
            print(var)
        elif diet_exer == 2:
            file_obj = open("exercise5_client_3_E.txt","r")
            var = file_obj.read()
            print(var)
    else:
            print("Try Again,entering a valid i/p")


else:
    print("\nTry Again ,entering a valid i/p !")