#Library Arrangement with Loop

isArrange = True


while isArrange == True:
    que = input("Are the books already back in their places? -->   ")

    if que.lower() == 'yes':
        print("loop continuously")
        continue
    
    else: 
        print("The loop has already stopped")
        break