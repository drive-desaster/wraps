#!/usr/bin/python3

import os

def ask_yn (question:str, default:bool=None) -> bool:
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


def ask_number(min_value:float, max_value:float, question:str="please enter a number") -> float:
    """
    ask the user for an number
    ensures the input is a number within the given range
    """
    flag = True
    while flag:
        try:
            userinput = float(input(question).replace(',','.'))
            if (max_value < userinput or min_value > userinput):
                raise Exception()
            else:
                flag = False
        except:
            print(F"please enter a number betwen {min_value} and {max_value}")
    return userinput

def ask_path(question:str="please enter a Path", notvalid:str="you did not enter a valid path") -> str:
    """
    aks the user for a filepath
    check if the filepath is valid and exists on the system
    returns the filepath
    """
    flag = True
    while flag:
        try:
            path = input(question)
            if os.path.exists(path):
                falg = False
                return str(path)
            else:
                print(notvalid)
                falg = True
        except:
            print(notvalid)
            flag = False

def read_file(filepath:str) -> str:
    """
    open given path if it is a file
    return content of file after closing it
    """
    if not os.path.isfile(filepath):
        raise Exception("please ensure to use a valid filepath")
    tmp_file = open(filepath, 'r')
    tmp_content = tmp_file.read()
    tmp_file.close()
    return tmp_content
