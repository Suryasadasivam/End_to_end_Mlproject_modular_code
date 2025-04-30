import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name="datascience"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py" ,
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config__entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html"]



for filepath in list_of_files:
    filepath=Path(filepath) # Converts the filepath string into a Path object using pathlib.Path
    filedir,filename=os.path.split(filepath) #Split into directory and file name

    if filedir!="": #create a directory
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'creating directory{filedir}for the file:{filename}')

    if (not os.path.exists(filepath)) or(os.path.getsize(filepath)==0):
        with open(filepath,"w")as f: #create the file 
            pass 
        logging.info(f"Creating empty file:{filepath}")
    else:
        logging.info(f'{filename}is already exists')