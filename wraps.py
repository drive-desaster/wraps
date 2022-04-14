#!/usr/bin/python3

def ask (question:str, default:bool=None) -> bool:
    """
    A function to ask the user a Y/N question in the cli
    the value of default (if set) is return in case the user gives an empty answer
    """
    if default != None and type(default) != bool:
        raise Exception('the provided value was not None and not a boolean')
    answers = '[y/n]'
    if default == True:
        answers = '[Y/n]'
    elif default == False:
        answers = '[y/N]'
    while True: 
        #a flag is not needed since a return statement automaticaly closes the loop
        response = input(F"{question} {answers} ").strip().lower()
        if response == '' and default != None:
            return default
        elif response in ('y', 'yes', 'true'):
            return True
        elif response in ('n', 'no', 'not', 'false'):
            return False
        else:
            print('Input invalid')
