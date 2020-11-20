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
    cmd = subprocess.run(command, shell=True, capture_output=True, input="")
    return cmd


def clone_repo():
    run("mkdir input")
    run("git -C input/ clone https://github.com/noahjutz/w-seminararbeit.git")


def get_commits():
    out = run("git -C input/w-seminararbeit/ log --pretty=\"%H\"")
    commits = out.stdout.decode().split()
    return commits


def latexmk(commit):
    run("git -C input/w-seminararbeit/ reset --hard")
    run(f"git -C input/w-seminararbeit/ checkout {commit}")
    run("latexmk -pdf -outdir=input/w-seminararbeit input/w-seminararbeit/main.tex")
    run(f"cp input/w-seminararbeit/main.pdf output/pdf/{commit}.pdf")


def pdf_to_images(commit):
    pass


def combine_images(commit):
    pass


def pngs_to_timelapse():
    pass


def show_info(commit):
    subject = " ".join(run(f"git -C input/w-seminararbeit/ show --pretty=format:'%s' {commit} | head -1").stdout.decode().splitlines())
    body = " ".join(run(f"git -C input/w-seminararbeit/ show --pretty=format:'%b' {commit} | head -1").stdout.decode().splitlines())
    date = " ".join(run(f"git -C input/w-seminararbeit/ show --pretty=format:'%ci' {commit} | head -1").stdout.decode().splitlines())
    print(f"{commit[:16]} {subject}")


if __name__ == "__main__":
    main()
