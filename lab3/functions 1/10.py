def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list
input_list=input("List ").split()
print("Set", unique_elements(input_list))