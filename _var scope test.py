
x = 1
end = 0
while end == 0:
    print('top of while loop: ')
    print('x = ' + str(x) + ', end = ' + str(end))
    print()
    if x == 5:
        end = 1
    x = x + 1
    print('bottom of while loop: ')
    print('x = ' + str(x) + ', end = ' + str(end))
    print()

print('outside of loop: ')
print('x = ' + str(x) + ', end = ' + str(end))


