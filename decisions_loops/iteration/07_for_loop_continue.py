# 07_for_loop_continue.py - for loop with continue statement
# ----------------------------------------------------------

cars = ['Toyota', 'Nissan', 'Ford', 'Volkswagen', 'Opel', 'Honda', 'Kia']

for car in cars:
  if car == 'Opel':
    continue
  print(car)
      
    