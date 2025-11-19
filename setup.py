#This file contains info about packages and all names etc dependicies 
# project k name kya h 
# version kya h 
# kaunse modules intall h 

#Setuptools :-  find package dependiecies bnane m help kr raha h
#typing :- isse basically hm list import krte h taaki koi chiz list ki form m likhni ho to 

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e.'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()#  for an example :- ["numpy\n", "pandas\n", "scikit-learn\n"]
        requirements=[req.replace("\n","")for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='Fault detection',
    version='0.0.1',
    author='Armaan Joshi',
    author_email='vishu18012005@gmail.com',
    install_requirements=get_requirements('requirements.txt'),
    packages=find_packages()
)