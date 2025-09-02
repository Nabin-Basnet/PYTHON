# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

def name(**nam):
    print("my name is ",nam["firstName"],nam["lastName"])
    return nam

name(firstName="nabin",lastName="basnet")