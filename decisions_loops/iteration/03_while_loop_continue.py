# 03_while_loop_continue.py - while loop with 'continue' statement
# ----------------------------------------------------------------

x = 15
while x > 0:
    x -= 1
    if x == 2:
        continue
    print(x)
print('Loop with continue has finished.')
