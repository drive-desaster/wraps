#!/usr/bin/python3

import os

def ask_yn (question:str, default:bool|None=None) -> bool:
    """
    A function to ask the user a Y/N question in the cli
    the value of default (if set) is return in case the user gives an empty answer
    """
    if default != None and not isinstance(default, bool):
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
    aks the user for a path in the file system
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

def ask_filepath(question:str = "please enter a file path ", notvalid:str="the entered path is not a valid filepath") -> str:
    """
    ask the user for a valid filepath in the filesystem
    returns the filepath
    """
    path = ""
    while not os.path.isfile(path):
        path = ask_path(question, notvalid)
    return path

def read_file(filepath:str, encoding:None|str=None) -> str:
    """
    open given path if it is a file
    if encoding is set read file using the encoding
    return content of file after closing it
    """
    if not os.path.isfile(filepath):
        raise FileNotFoundError("please ensure to use a valid filepath")
    if encoding == None:
        with open(filepath, 'r') as tmp_file:
            content = tmp_file.read()
    else:
        with open(filepath, 'rb') as tmp_file:
            tmp_content = tmp_file.read()
            content = tmp_content.decode(encoding)
    return content

def write_file(filepath:str, content:str|bytes, append:bool=False, question_exists:str="this file already exists, do you want to overrite it?", alternativemethod:str="throw", encoding:None|str=None):
    """
    writes content to file
    if append is False, will ask user if file should be replaced -> if not, then thows error, appends or doesn't write at all depending on parameter (default is throw, valid options are: "throw", "append", "skip")
    uses system default encoding if encoding is None
    """
    #raise error if supplied path is a directory
    if os.path.isdir(filepath): 
        raise IsADirectoryError(F"{os.path.realpath(filepath)} is a Directory and not a file")
    #check if the file exists and if it should be appendet to it
    if os.path.isfile(filepath) and not append:
        #overwrite file (after asking user for consent)
        if ask_yn(question_exists):
            if encoding == None and not isinstance(content, bytes):
                with open(filepath, 'wb') as tmp_file:
                    tmp_file.write(content)
            else:
                with open(filepath, 'wb') as tmp_file:
                    if isinstance(content, bytes):
                        tmp_file.write(content)
                    else:
                        tmp_file.write(bytes(content, encoding))
        else:
            if alternativemethod.lower().trim() == "throw":
                raise FileExistsError("target file exists and it was requested to thow here")
            elif alternativemethod.lower().trim() == "append":
                #append content to file
                if encoding == None and not isinstance(content, bytes):
                    with open(filepath, 'a') as tmp_file:
                        tmp_file.write(content)
                else:
                    with open(filepath, 'ab') as tmp_file:
                        if isinstance(content, bytes):
                            tmp_file.write(content)
                        else:
                            tmp_file.write(bytes(content, encoding))
            elif alternativemethod.lower().trim() == "skip":
                print("not modifing the file, as requested")
            else:
                raise SyntaxWarning("alternativemethod should be \"throw\", \"append\" or \"skip\", not \"" + str(alternativemethod) + "\"")
    else:
        #append content to file (create if not exists)
        if encoding == None and not isinstance(content, bytes):
            with open(filepath, 'a') as tmp_file:
                tmp_file.write(content)
        else:
            with open(filepath, 'ab') as tmp_file:
                if isinstance(content, bytes):
                    tmp_file.write(content)
                else:
                    tmp_file.write(bytes(content, encoding))
        
