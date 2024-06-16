from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements by reading a file 
    where each line contains a requirement.

    Args:
        file_path (str): The path to the requirements file.

    Returns:
        List[str]: A list of requirements with newline characters removed.
    """
    HYPEN_E_DOT = '-e .'
    try:
        with open(file_path, 'r') as file_obj:
            requirements = [line.strip() for line in file_obj]
            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)                
        return requirements
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except IOError as e:
        print(f"Error: An IOError occurred while reading the file {file_path}. {e}")
        return []


setup(
    name='mlproject',
    version='0.0.1',
    description='mlproject tempelate',
    author='rafay bajwa',
    author_email='rafay.mhddn@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)