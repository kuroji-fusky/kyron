from argparse import ArgumentParser
from kyron_shared.fs import KyronFilesystem

parser = ArgumentParser(
    description="Manage downloads and archived content"
)

parser.add_argument("--directory", "--dir", "--path", type=str,
                    help="Specify a directory to scan or to download from (defaults to current working directory)")

# requires a child process to be spawn atop of the Electron process
parser.add_argument("--client-attach", type=str,
                    help="Only used for the Kyron desktop frontend, will fail when used as standalone mode")

exec_grp = parser.add_argument_group("Executables",
                                     description="Required dependencies required for Kyron for function")
exec_grp.add_argument("--ffmpeg-dir", type=str,
                      help="Point to an FFmpeg executable")
exec_grp.add_argument("--ytdlp-dir", type=str,
                      help="Point to an yt-dlp executable, recommended to have FFmpeg to be installed "
                           "alongside it")

advanced_grp = parser.add_argument_group("Advanced")
advanced_grp.add_argument("--clear-cache", "--cache-clear", action="store_true",
                         help="Clears global app cache and resets options for the desktop app")
advanced_grp.add_argument("--specs", action="store_true",
                          help="")

args = parser.parse_args()


def main():
    fak = KyronFilesystem("D:\\yt-archive\\@Ozzyfox-musicforkids")
    print(list(fak.dir_contents))


if __name__ == "__main__":
    main()
