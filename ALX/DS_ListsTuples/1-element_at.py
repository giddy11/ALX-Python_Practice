#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return ("None")
    return (my_list[idx])

'''
#!/usr/bin/python3
def element_at(my_list, idx):
    return(my_list[idx] if 0 <= idx < len(my_list) else "None")
'''