cost = 1000000
good_credit = False

if good_credit:
    dp = 0.1*cost
else:
    dp = 0.2*cost

print(f"you have to pay downpayment of ${dp}")
