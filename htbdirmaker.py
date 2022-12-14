#!/usr/bin/python3

import os
import sys
import subprocess


def main():
    try:
        if not os.path.exists("/usr/local/bin/htbdirmaker.py"):
            path = os.getcwd()
            print(path)
            subprocess.run(
                "sudo ln -s "+path+"/htbdirmaker.py /usr/local/bin/htbdirmaker.py", shell=True) #change 'shell=True' later because of shell injection.
            subprocess.run("sudo chmod +x /usr/local/bin/htbdirmaker.py", shell=True)
            print("Link Created - Use Command Anywhere.")
    except:
        print("Could Not Create Link.")
        exit()
    try:
        option = sys.argv[1]
    except:
        print("Error: Wrong format")
        print("Usage: htbdirmaker.py -[Option]")
        exit()

    if option == "-h":
        _h()
    elif option == "-d":
        _d()


def _h():
    print("Usage: htbdirmaker.py -[Option]")
    print("Options:")
    print("-h : Display this help message")
    print("-d : Specify directory")
    print("More to come...")
    print()


def _d():
    try:
        parent_dir = sys.argv[2]
        os.mkdir(parent_dir, mode=0o666)
        print("Directory '% s' is built!" % parent_dir)
        print()
    except:
        print("Error: Specify a valid directory path!")
        print()
        print("Usage: htbdirmaker.py -d [directory name]")
        exit()

    try:
        sub_dir_nmap = os.path.join(parent_dir, "nmap")
        sub_dir_scripts = os.path.join(parent_dir, "scripts")
        sub_dir_notes = os.path.join(parent_dir, "notes")

        os.mkdir(sub_dir_nmap, mode=0o666)
        print("Directory '% s' is built!" % sub_dir_nmap)
        print()

        os.mkdir(sub_dir_scripts, mode=0o666)
        print("Directory '% s' is built!" % sub_dir_scripts)
        print()

        os.mkdir(sub_dir_notes, mode=0o666)
        print("Directory '% s' is built!" % sub_dir_notes)
        print()
    except:
        print("Error: Failed to build sub directories!")
        exit()


main()
