# Python program to illustrate *args for a variable number of arguments
def myFun(*args):
    for arg in args:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# Output: Hello
#         Welcome
#         to
#         GeeksforGeeks

# Explain me above written code
# In this program, we use *args as a parameter which allows us to pass variable length of argument.
# When we run the above program, the output will be:
# Hello
# Welcome
# to
# GeeksforGeeks
