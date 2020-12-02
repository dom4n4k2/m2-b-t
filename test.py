

to_do_command = 'delete'

def fun(*args):
    print(len(args))
    if((to_do_command == 'delete') and (len(args) == 0)) :
        print("aaaa")


fun()