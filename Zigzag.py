import sys, time
indent = 0  #How many spaces to indent
indentIncreasing = True   #Whether indent is increasing or not
try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)       # Pause for 1/10 sec

        if indentIncreasing:
            indent = indent + 2
            if indent == 10:
                indentIncreasing = False         #Change Diraction
        else:
            indent = indent - 2
            if indent == 0:
                indentIncreasing = True              #Change Diraction

except KeyboardInterrupt:
    sys.exit()             #quiting the programe


