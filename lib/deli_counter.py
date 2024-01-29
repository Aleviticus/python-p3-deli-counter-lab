# OTHER_DELI = ["Logan", "Avi", "Spencer"]
# ANOTHER_DELI = ["Amanda", "Annette", "Ruchi", "Jason", "Logan", "Spencer", "Avi", "Joe", "Rachel", "Lindsey"]

def line(line_list):
    if len( line_list) > 0:
        x = 1

        new_string = "The line is currently:"

        for person in line_list:
            new_string += f" {x}. {person}"
            x += 1
        print (new_string)
    else:
        print ("The line is currently empty.")

def take_a_number(list, person):

    x = len(list) + 1
    list.append(person)

    print(f"Welcome, {person}. You are number {x} in line.")
    pass

def now_serving():
    pass