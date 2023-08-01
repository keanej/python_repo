# If-elif Statement Sample

bank_balance = 40000

if bank_balance > 50000:
  print('You have a Gold Standard Credit Rating')
  
elif bank_balance > 10000 and bank_balance < 50000:
    print('You have a Silver Standard Credit Rating')

elif bank_balance > 1000 and bank_balance < 10000:
    print('You have a Bronze Standard Credit Rating')

else:
    print('You have insufficient funds for a credit rating')
  