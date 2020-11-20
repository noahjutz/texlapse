#!/usr/bin/env python

import subprocess

commits = []


def main():
    global commits
    clone_repo()
    commits = get_commits()
    for commit in commits:
        show_info(commit)
        latexmk(commit)
        pdf_to_images(commit)
        combine_images(commit)
    pngs_to_timelapse()


def run(command):
    cmd = subprocess.run(command, shell=True, capture_output=True, input="")
    print(f"    {cmd.returncode}: {cmd.args}")
    try:
        open("output/log", "a").write(f"\n==========================="
                                      f"\nargs: {cmd.args}"
                                      f"\nreturncode: {cmd.returncode}"
                                      f"\nstdout: {cmd.stdout}"
                                      f"\nstderr: {cmd.stderr}")
    except:
        print("failed to log")
    return cmd


def clone_repo():
    run("mkdir input")
    run("mkdir output")
    run("mkdir output/pdf")
    run("mkdir output/png")
    run("touch output/log")
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
    run(f"mkdir output/png/{commit}")
    run(f"pdftoppm -png output/pdf/{commit}.pdf output/png/{commit}/{commit}")


def combine_images(commit):
    pass


def pngs_to_timelapse():
    pass


def show_info(commit):
    subject = " ".join(
        run(f"git -C input/w-seminararbeit/ show --pretty=format:'%s' {commit} | head -1").stdout.decode().splitlines())
    body = " ".join(
        run(f"git -C input/w-seminararbeit/ show --pretty=format:'%b' {commit} | head -1").stdout.decode().splitlines())
    date = " ".join(run(
        f"git -C input/w-seminararbeit/ show --pretty=format:'%ci' {commit} | head -1").stdout.decode().splitlines())
    index = commits.index(commit)
    print(f"{commit[:16]} {subject} ({index}/{len(commits)})")


if __name__ == "__main__":
    main()
