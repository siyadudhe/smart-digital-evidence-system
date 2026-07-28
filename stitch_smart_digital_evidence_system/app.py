username= "admin"
password = "admin123" 

#login
u = input("enter username: ")
p =input("enter password:")

if u!=username  or p!=password:
    print("Invalid login credentials!")
    exit()
while True:
     print("\n ------Smart digital Evidence system-----")
     print("1.Add Evidence")
     print("2.View Evidence")
     print("3.Search Evidence")
     print("4.Update Evidence")
     print("5.Delete Evidence")
     print("6.Exit")
     #choice
     
     choice =input("Enter your choice: ")
     
     #add evidence
     if choice=="1":
         evidence_id= input("Enter Evidence ID:")
         case_id=input("Enter case ID:")
         evidence_Title=input("Enter Evidence Title: ")
         officer_name=input("Enter officer Name: ")
         
         file =open("evidence.txt","a")
         file.write(evidence_id + "," + case_id + "," + evidence_Title + "," + officer_name + "\n")
         file.close()
        
         print("Evidence added successfilly")
         #view Evidence
     elif choice =="2":
         try:
                file = open("evidence.txt", "r")
                print("\n----- Evidence Records -----\n")
                print(file.read())
                file.close()

         except:
                print("No Evidence found.")
         # Search Evidence
     elif choice =="3":
         search = input("Enter Evidence ID to search:")
         found =False    #this will be used to track whether a match was found or not.
         try:
                file=open("evidence.txt","r")
                records=file.readlines()    #reads the file and splits it into a list, where each item is one line
                file.close()
                for record in records:
                    data = record.strip().split(",")
                    if data[0]==search:
                        print("\nEvidence Found")
                        print("Evidence ID :", data[0])
                        print("Case ID :", data[1])
                        print("Title :", data[2])
                        print("Officer :", data[3])

                        found = True

                if  not found:
                    print("Evidence Not Found")

         except:
                print("No Evidence Found")
         
         #update
     elif choice =="4":
        update = input("Enter Evidence ID to Update: ")
        try:
            file = open("evidence.txt","r")
            records= file.readlines()
            file.close()
            
            file = open("evidence.txt","w")
            found= False
            for record in records:
                data = record.strip().split(",")
                if data[0]==update:
                    case_id = input("Enter new Case ID: ")
                    evidence_Title = input("Enter new Evidence Title: ")
                    officer_name = input("Enter new Officer Name: ")
                    
                    file.write(update+","+case_id+","+evidence_Title+","+officer_name+"\n")
                    
                    found = True
                else:
                    file.write(record)
            file.close()
            if found:
                print("Evidence updated Successfully!")
            else:
                print("Evidence ID not found!")
                
        except:
            print("No Evidence found to update!")
            #delete
            
     elif choice =="5":
         delete= input("Enter Evidence Id to delete: ")
         try:
                file = open("evidence.txt","r")
                records = file.readlines()
                file.close()
                      
                file = open("evidence.txt","w")
                found =False
                for record in records:
                   data = record.strip().split(",")
                   if data[0]!=delete:
                      file.write(record)
                   else:
                      found=True
                file.close()
                if found:
                    print("Evidence deleted successfully!")
                else:
                    print("Evidence ID not found!") 
         except:
             print("No Evidence found to delete!")
        #Exit
     elif choice=="6":
         print("Thank you for using the Smart Digital Evidence System!")
         break
     else:
         print("Invalid Choice ! Please try again.")
        
            
        
                    
         
        
        
        