rate = [None,1500,4540,7090]
bank = [20,50,100,500,1000]
name_rate = [None,"Standard","Premium","Rare"]
print("################Menu################\n ####  1.Standard 2.Premium 3.Rare  ####\n####################################")
for index, value in enumerate(rate):
    if index == 0:
        continue  # ข้ามตำแหน่งที่ 0
    print(f"Rate {index} : {value} Bath ", end="  ")
print(" ")
selectRate = int(input("Welcome CPE_SUCK chose your rate : [1-3] : "))
selectShe = rate[selectRate]
print(f"Cost {name_rate[selectRate]} = {selectShe}")
print("####################################")
pay = selectShe
while pay > 0 :
    bank_insert = int(input("please insert bank : [20,50,100,500,1000] "))
    if bank_insert == 20 or bank_insert == 50 or bank_insert == 100 or bank_insert == 500 or bank_insert == 1000:
        if pay > 0 :
            pay = pay - bank_insert
            print(f"please insert: = {pay}")
    else:
        print("invalid value bank") 
change = -pay
if change == 0 :
    print("no change")
print(f"change {change}")
amount1 = 0
amount2 = 0
amount3 = 0
amount4 = 0 
amount5 = 0
while change > 0:
    if change >= 1000:
        print("##########change money###########")
        amount1 = change//1000
        change = change%1000
        if amount1 >= 1:
            print(f"change : 1000  Amount : {amount1}")
    elif change < 1000 and change >= 500:
        print("##########change money###########")
        amount2 = change//500
        change = change%500
        if amount2 >= 1:
            print(f"change : 500  Amount : {amount2}")
        
    elif change < 500 and change >=100:
        print("##########change money###########")
        amount3 = change//100
        change = change%100
        if amount3 >= 1:
            print(f"change : 100  Amount : {amount3}")
        
    elif change <100  and change >=50 :
        print("##########change money###########")
        amount4 = change//50
        change = change%50
        if amount4 >= 1:
            print(f"change : 50  Amount : {amount4}")

    elif change <50  and change >=20 :
        print("##########change money###########")
        amount5 = change//20
        change = change%20
        if amount5 >= 1:
            print(f"change : 20  Amount : {amount5}") 

    elif change == 10 :
        print("##########change money###########")
        change = change-10
        print(f"change : 10  Amount : 1 ")         

     
print("################END#################")
