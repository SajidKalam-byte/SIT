'''A machine is purchased which will produce earning of Rs. 1000 per year while it lasts. The 
machine costs Rs. 6000 and will have a salvage of Rs. 2000 when it is condemned. If 12 percent 
per annum can be earned on alternate investments what would be the minimum life of the 
machine to make it a more attractive investment compared to alternative investment?'''

n=int(input("Enter number of years: "))
machine=6000
salvage=2000
bank=6000
machine_earning=0
bank_earning=0
machine_total=0
for year in range (1,n+1):
    machine_earning+=1000
    bank_earning+=720
    machine_total=machine_earning+salvage
    if(machine_total>bank_earning+bank):
        print(f"The machine becomes more profitable after {year} years.")
        print(f"Machine value: ₹{machine_total}")
        print(f"Bank value: ₹{bank + bank_earning}")
        break
else:
    print("The machine does not become more profitable within the given time.")