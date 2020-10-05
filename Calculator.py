list_values = [0]

def initialize ():
    global current_value
    current_value = 0

def get_current_value():
    return current_value

def display_current_value():
    print ('Current value:', list_values[-1])

def add(to_add):
    global current_value
    current_value = current_value + to_add
    list_values.append(current_value)

def multiply(to_multiply):
    global current_value
    current_value = current_value * to_multiply
    list_values.append(current_value)

def divide(to_divide):
    global current_value
    if to_divide == 0:
        print ('Division by 0 is undefined')
    else:
        current_value = current_value / to_divide
        list_values.append(current_value)

def store():
    global stored
    stored = current_value

def recall():
    print ("Recalled " + str(stored))

def undo():
    remove = list_values [-1]
    del list_values[-1]

if __name__ == "__main__":
    print ("Welcome to the calculator program.")
    current_value = 0
    add(20)
    #store, recall, and undo function needs something in brackets but it doesn't matter what's in brackets
    #that's because it doesn't need a parameter, just remove the paramenter from the function (leave brackets empty)
    display_current_value()







