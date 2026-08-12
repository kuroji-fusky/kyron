from argparse import ArgumentParser
from kyron_shared.fs import KyronFilesystem


def main():
    fak = KyronFilesystem("D:\\yt-archive\\@Ozzyfox-musicforkids")
    print(list(fak.dir_contents))

if __name__ == "__main__":
    main()
