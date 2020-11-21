#!/usr/bin/env python

import subprocess
import math
from PIL import Image

commits = []


def main():
    global commits
    clone_repo()
    commits = get_commits()
    for commit in commits:
        show_info(commit)
        latexmk(commit)
        pdf_to_images(commit)
        merge_images(commit)
    render_timelapse()


def run(command):
    cmd = subprocess.run(command, shell=True, capture_output=True, input="")
    print(f"    {cmd.returncode}: {cmd.args}")
    try:
        open("output/log", "a").write(f"\n==========================="
                                      f"\nargs: {cmd.args}"
                                      f"\nreturncode: {cmd.returncode}"
                                      f"\nstdout: \n{cmd.stdout.decode()}"
                                      f"\nstderr: \n{cmd.stderr.decode()}")
    except FileNotFoundError:
        print("failed to log")
    return cmd


def clone_repo():
    run("mkdir input")
    run("mkdir output")
    run("mkdir output/pdf")
    run("mkdir output/png")
    run("touch output/log")
    run("mkdir output/mp4")
    run("git -C input/ clone https://github.com/noahjutz/w-seminararbeit.git")


def get_commits():
    out = run("git -C input/w-seminararbeit/ log --pretty=\"%H\"")
    return out.stdout.decode().split()


def latexmk(commit):
    run("git -C input/w-seminararbeit/ reset --hard")
    run(f"git -C input/w-seminararbeit/ checkout {commit}")
    run("latexmk -pdf -outdir=input/w-seminararbeit input/w-seminararbeit/main.tex")
    run(f"cp input/w-seminararbeit/main.pdf output/pdf/{commit}.pdf")


def pdf_to_images(commit):
    run(f"mkdir output/png/{commit}")
    run(f"pdftoppm -png output/pdf/{commit}.pdf output/png/{commit}/{commit}")


def merge_images(commit):
    column_width = 1241
    row_height = 1754
    panels = 26
    rows = 3
    columns = math.ceil(panels / rows)

    merged_width = columns * column_width
    merged_height = rows * row_height

    page_paths = run(f"ls output/png/{commit}").stdout.decode().splitlines()
    merged_image = Image.new("RGB", (merged_width, merged_height), (255, 255, 255))
    for row in range(0, rows):
        for column in range(0, columns):
            index = row * columns + column
            if len(page_paths) <= index:
                break
            page = Image.open(f"output/png/{commit}/{page_paths[index]}")
            merged_image.paste(im=page, box=(column * column_width, row * row_height))
    merged_image.save(f"output/png/{commit}/{commit}.png")


def render_timelapse():
    for i, commit in enumerate(commits):
        run(f"cp output/png/{commit}/{commit}.png output/mp4/{i}.png")
    run("ffmpeg -framerate 24 -i output/mp4/%d.png output/mp4/final.mp4")


def show_info(commit):
    subject = " ".join(
        run(f"git -C input/w-seminararbeit/ show --pretty=format:'%s' {commit} | head -1").stdout.decode().splitlines())
    index = commits.index(commit)
    print(f"{commit[:16]} {subject} ({index}/{len(commits)})")


if __name__ == "__main__":
    main()
