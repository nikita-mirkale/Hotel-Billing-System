items={1:"tea",2:"poha",3:"samosa",4:"kachori",5:" vada-pav",6:" pavbhaji",7:"misal",8:"patis"}
price={1:10,2:20,3:15,4:20,5:15,6:35,7:45,8:25}
print("-"*89)
print(f"{" "*40} Gariboowala Hotel")
print("-"*89)
print(" Welcome to our Hotel!")
ik=[]
que=[]
while True:
    print("""
                        Menu
            1.Tea               2.Poha       
            3.Samosa            4 Kachoi
            5.vadapav           6 Pavbhaji
            7.Misal             8.Patis""")
    i=int(input("Enter your choice: "))
    q=int(input(" Enter the Quentity : "))
    ik.append(i)
    que.append(q)
    print(ik)
    print(que)
    ch=input("Do You want to Continue:")
    if ch=='n':
        print("-"*89)
        print("|{:^10}|{:^10}|{:^10}|{:^10}|".format("ItemName","Quantity","Price","Ammount"))
        print("-"*89)
        sum=0
        for i in range(len(ik)):
            print("|{:^10}|{:^10}|{:^10}|{:^10}|".format(items[ik[i]],que[i],price[ik[i]],que[i]*price[ik[i]]))
            print("-"*89)
            sum=sum+que[i]*price[ik[i]]
        print(f"Your total Ammount : {sum}\nThank you!! VIsit Again")
        break


