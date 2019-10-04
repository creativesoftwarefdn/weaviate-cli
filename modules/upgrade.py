import os

from modules.Messages import Messages
import subprocess


def upgrade_weaviate_cli(entry_point):
    entry_point = entry_point[:-16]
    if os.system('git --version') != 0:
        print("The upgrade routine uses git. If you installed the weaviate-cli manually please upgrade manually.")
        exit(1)
    if os.system('git -C '+entry_point+' pull origin master') !=0:
        print("Sorry, but pulling the latest version failed. Consider a reinstall or a manual upgrade.")
    if os.system('pip3 install -r '+entry_point+'/requirements.txt') !=0:
        print("Sorry, but installing the new dependencies has failed. You might want to install them manually at "+entry_point+'/requirements.txt')
    print("Your upgrade is complete")
    exit(0)