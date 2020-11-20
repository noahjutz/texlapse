#!/usr/bin/env python

import subprocess

commits = {}


def main():
    clone_repo()
    for commit in commits:
        show_info(commit)
        latexmk(commit)
        pdf_to_images(commit)
        combine_images(commit)
    pngs_to_timelapse()


def clone_repo():
    pass


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
