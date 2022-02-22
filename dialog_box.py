import tkinter as tk
from tkinter import filedialog
import os
import arguments


def create_env():
    name = input("Enter the name of this env: ")
    print("Select all the exes which you want to add to this env. Press cancel after all the desired exes have been added")
    done = False
    path_list = []
    while not done:
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        path_list.append(file_path)
        if file_path == '':
            done = True
    return [name, path_list]


def write_env_to_file(name, path_list):
    values = arguments.arguments()
    if os.path.isfile('env.txt'):
        with open('env.txt', 'a', encoding='utf-8') as file:
            file.writelines(name)
            file.write('\n')
            file.writelines('\n'.join([path for path in path_list]))
            if values[3]:
                file.writelines('Websites')
                file.write('\n')
                file.writelines('\n'.join([links for links in values[3]]))
    else:
        with open('env.txt', 'w', encoding='utf-8') as file:
            file.writelines(name)
            file.write('\n')
            file.writelines('\n'.join([path for path in path_list]))
            if values[3]:
                file.writelines('Websites')
                file.write('\n')
                file.writelines('\n'.join([links for links in values[3]]))


def main():
    name_and_pathlist = create_env()
    write_env_to_file(name_and_pathlist[0], name_and_pathlist[1])
