#!/usr/bin/env python

import subprocess


def main():
    clone_repo()
    for commit in get_commits():
        print(f"{commit}")
        show_info(commit)
        latexmk(commit)
        pdf_to_images(commit)
        combine_images(commit)
    pngs_to_timelapse()


def run(*args):
    cmdList = []
    for command in args:
        print(f"==> {command}")
        cmd = subprocess.run(command, shell=True, capture_output=True)
        is_success = cmd.returncode == 0
        print(f"    {'SUCCESS' if is_success else 'FAIL'}")
        cmdList.append(cmd)
    return cmdList


def clone_repo():
    run(
        "mkdir input",
        "git -C input/ clone https://github.com/noahjutz/w-seminararbeit.git"
    )


def get_commits():
    out = run(
        "git -C input/w-seminararbeit/ log --pretty=\"%H\""
    )
    commits = out[0].stdout.decode().split()
    return commits


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
