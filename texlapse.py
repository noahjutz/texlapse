#!/usr/bin/env python

import subprocess

commits = {}


def main():
    clone_repo()
    get_commits()
    for commit in commits:
        show_info(commit)
        latexmk(commit)
        pdf_to_images(commit)
        combine_images(commit)
    pngs_to_timelapse()


def run(*args):
    for command in args:
        print(f"==> {command}")
        output = subprocess.run([f"{command} &> /dev/null"], shell=True, )
        is_success = output.returncode == 0
        print(f"    {'SUCCESS' if is_success else 'FAIL'}")


def clone_repo():
    run(
        "mkdir input",
        "git -C input/ clone https://github.com/noahjutz/w-seminararbeit.git"
    )


def get_commits():
    commits = {}


def latexmk(commit):
    pass


def pdf_to_images(commit):
    pass


def combine_images(commit):
    pass


def pngs_to_timelapse():
    pass


def show_info(comit):
    pass


if __name__ == "__main__":
    main()
