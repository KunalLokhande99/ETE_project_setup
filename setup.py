from setuptools import find_packages,setup
from typing import List

# if dont want to run this file write -e . in requirements.txt 
# this part of code is used to sort out requirements and installs the necessary one

"""HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements"""

setup(
    name='DimondPricePrediction',
    version='0.0.1',
    author='sunny savita',
    author_email='sunny.savita@ineuron.ai',
    # install_requires=get_requirements('requirements.txt')
    install_requires=["scikit-learn","pandas","numpy"],     # manual method
    packages=find_packages()
)