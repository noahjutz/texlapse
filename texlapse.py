#!/usr/bin/env python

import subprocess


def main():
    clone_repo()
    for commit in get_commits():
        show_info(commit)
        latexmk(commit)
        pdf_to_images(commit)
        combine_images(commit)
    pngs_to_timelapse()


def run(command):
    print(f"==> {command}")
    cmd = subprocess.run(command, shell=True, capture_output=True)
    is_success = cmd.returncode == 0
    print(f"    {'SUCCESS' if is_success else 'FAIL'}")
    return cmd


def clone_repo():
    run("mkdir input")
    run("git -C input/ clone https://github.com/noahjutz/w-seminararbeit.git")


def get_commits():
    out = run("git -C input/w-seminararbeit/ log --pretty=\"%H\"")
    commits = out.stdout.decode().split()
    return commits


def latexmk(commit):
    pass


def pdf_to_images(commit):
    pass


def combine_images(commit):
    pass


def pngs_to_timelapse():
    pass


def show_info(commit):
    out = run(f"git -C input/w-seminararbeit/ show {commit}")
    print(out.stdout.decode())


if __name__ == "__main__":
    main()
