num_of_people=int(input("enter the number of workers: "))
amount=int(input("enter the amount to be paid: "))
tips_percent=int(input("enter the how much tpis you want to provide enter in percentage: "))

total_amount=amount+(tips_percent/100*amount)

perperson_tips=total_amount/num_of_people

print("per person amout =",perperson_tips)

