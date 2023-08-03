# 02_while_loop_break.py - while loop with break statement
# --------------------------------------------------------

i = 12
while i > 0:
    i -= 1
    if i == 2:
        break
    print(i)
print('Loop with break has finished.')