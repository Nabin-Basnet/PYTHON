# Recursion is when a function calls its


def countdown(n):   #here functiono coundown is created and it accept the single value
    if n<=0:        #it is the condition to check whether n is zero or not to stop the recursion 
        print("count down completes")
    else:
       print(n)
       countdown(n-1)    #it re call the function with the modified value

countdown(5)