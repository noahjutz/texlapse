# texlapse
Create a timelapse of a tex repository.

## Script structure:
```
1 clone repo
2 get commit hashes in list
3 compile latex: for commit in commits:
    3.1 checkout
    3.3 latexmk -> output/pdf/commit.pdf
    3.4 git reset
    3.5 show info
4 convert pdf to pngs: for commit in commits:
    4.1 pdftoppm -> output/png/commit/n.png
    4.2 show info
5 stitch together pngs: for commit in commits:
    5.1 TODO
    5.2 show info
6 ffmpeg stiched pngs
    6.1 ffmpeg -> output/mp4/final.mp4
    6.2 show info
```

## Project structure:
```
texlapse
    texlapse.py
    input
        w-seminararbeit
    output
        pdf
            132kj3(...).pdf
            ...
        png
            9dg8u(...)
                1.png
                ...
        mp4
            final.mp4
```