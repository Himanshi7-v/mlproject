from setuptools import find_packages,setup
from typing import List 
# uppercase is always used for constants by convention 
HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return list of requirements
    '''
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() 
        # used strip here in place of replace as emoves all leading and trailing whitespace (including spaces, tabs, and newlines).
        requirements = [req.strip() for req in requirements] 
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)       
    return requirements        


setup(
    name = 'mlproject',
    version ='0.0.1',
    author = 'himanshisaini',
    author_email='himanshisaini757@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt') 
)
