import random

students = []

try:
    file = input("File name : ")
    fp = open("README.md",'r')
    readme_list = fp.readlines()
    rls = readme_list[0].split('_')
    print(readme_list)
    print(rls)
    fp.close()
except FileNotFoundError as err:
    print(f"{file} is not exist. {err}")
