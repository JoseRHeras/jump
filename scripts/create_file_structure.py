import os
import sys
import json

notebook_content = {
    "cells": [
        {
            "cell_type": "code",
            "metadata": {},
            "source": [
                "import pandas as pd\n",
                "import numpy as np\n",
                "import seaborn as sns"
            ],
            "outputs": []
        }
    ],
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 2
}


def get_parent_dir_name() -> str:
    if len(sys.argv) < 2:
        print("Usage: python create_file_structure.py <parent_directory_name> Optional:<notebook_name> ...")
        sys.exit(1)

    return sys.argv[1]

def get_notebook_name() -> str | None:
    if len(sys.argv) < 3: return None

    return sys.argv[2]

def main() -> None:
    current_dir_path = os.getcwd()
    new_dir_path = os.path.join(current_dir_path, get_parent_dir_name())
    os.makedirs(new_dir_path, exist_ok=True)

    # Create subdirectories
    subdirs = ['data']

    for sub in subdirs:
        sub_path = os.path.join(new_dir_path, sub)
        os.makedirs(sub_path, exist_ok=True)


    # Create notebook file
    notebook_name = get_notebook_name()

    if not notebook_name:
        notebook_name = "data_analysis"

    notebook_name += ".ipynb"
    notebook_path = os.path.join(new_dir_path, notebook_name)

    with open(notebook_path, "w") as f:
        json.dump(notebook_content, f)

if __name__ == '__main__':
    main()