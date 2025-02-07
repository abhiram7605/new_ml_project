from setuptools import find_packages, setup
from typing import List

x = '-e .'
def get_requirements(file_path:str) -> List[str]:
    
    requirements =[]
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if x in requirements:
            requirements.remove(x)
    return requirements
    

setup(
name = "ml_project",
version = "0.01",
author = "Abhiram Yadav Myla",
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)