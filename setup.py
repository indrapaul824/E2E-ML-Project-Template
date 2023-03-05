from typing import List
from setuptools import setup, find_packages

def get_requirements(folder_name: str) -> List[str]:
    '''
    This function reads the dev and prod requirements from the requirements folder and returns a list of requirements.
    '''
    reqs = []
    with open(f"{folder_name}/dev.in", "r") as f:
        reqs += f.read().splitlines()
    with open(f"{folder_name}/prod.in", "r") as f:
        reqs += f.read().splitlines()
    return reqs

setup(
    name = "E2EMLProject",
    version = "0.0.1",
    author = "Indrashis Paul",
    author_email = "indrashis985@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements")
)