import os 
import json
import shutil
from subprocess import PIPE,run
import sys

Search_pattern = "game"

def Create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path,exist_ok=True)

def copy_games(sources,dest):
    for source in sources:
        if os.path.isdir(source):
            shutil.copytree(source,dest,dirs_exist_ok=True)
        else:
            shutil.copy2(source,dest)

        

def find_game_dir(source_path):
    game_paths = []
    for root,dirs,files in os.walk(source_path):
        for direct in dirs:
            if Search_pattern in direct.lower():
                path = os.path.join(root,direct)
                game_paths.append(path)
        for fileIn in files:
            if Search_pattern in fileIn:
                path = os.path.join(root,fileIn)
                game_paths.append(path)
        break

    print(game_paths)
    return game_paths


def main(source,dest):
    cwd = os.getcwd()
    source_path = os.path.join(cwd,source)
    dest_path = os.path.join(cwd,dest)
    game_paths=find_game_dir(source_path)
    Create_dir(dest_path)
    copy_games(game_paths,dest_path)

if __name__ == "__main__":
    args = sys.argv
    print(args)
    if len(args) != 3 :
        raise Exception("Usage: python script.py <source> <destination>")

    source = args[1]
    destination = args[2]

    if not os.path.exists(source):
        raise Exception("Source directory does not exist")

    main(source,destination)
