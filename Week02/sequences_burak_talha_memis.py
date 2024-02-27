my_list = [1,2,3,4,5,1,2,3]
my_tuple = (1,2,3)
my_set = {"Ferrari", "Fiat", "Opel", "Ford"}
my_dict = {"Name" : "Burak", "Surname" : "Memis" , "Age" : "23" , "University" : "CBU"}


def remove_duplicates(my_list):
    new_list = []
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    return new_list  


def list_counts(my_list):
    return {i : my_list.count(i) for i in my_list} 


def reverse_dict(my_dict):
    new_dict = {}
    for key,value in my_dict.items():
        new_dict[value] = key
    return new_dict    
