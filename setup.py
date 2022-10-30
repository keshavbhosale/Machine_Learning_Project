from setuptools import setup
from typing import List


def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file

    return this is going to return a list which contain name of libraaries mentioned 
    in requirements.txt file
    
    """
    with open(REQUIREMENT_FILE_NAME) as requirements_file:
        return requirements_file.readlines()


DESCRIPTION="This is a first ML project"
REQUIREMENT_FILE_NAME="requirements.txt"
setup(
name="housing-predictor",
version="0.0.2",
author="keshav",
description="DESCRIPTION",
packages=['housing'],
install_requires=get_requirements_list()
)
if __name__=="main":
    print(get_requirements_list())