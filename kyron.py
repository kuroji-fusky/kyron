"""
Kyron - a tool for bulk downloading YT videos
"""

import os
import sys
import json
from typing import Optional
from argparse import ArgumentParser

import config_parser as kyron_conf
from kyron_utils import tables as ky_tables
from kyron_utils.constants import CWD, default_config

# region Arguments
parser = ArgumentParser(
    description="Bulk download YouTube videos locally or for archival purposes. "
                "Can also check for thumbnail and avatar changes",
)

parser.add_argument("channel_name", type=str, nargs="*",
                    help="YouTube channel handle(s) to download (optional if using -l)")

parser.add_argument("-l", "--list",
                    metavar="list_contents",
                    choices=["name", "size", "videos"],
                    type=str, nargs="?",
                    help="List all downloaded channels from the current directory "
                    "or from the config")

parser.add_argument("--dir", type=str, metavar="DIR_NAME",
                    help=f"Set custom download directory (default is the terminal's cwd: {CWD})")

parser.add_argument("--create-config", action="store_true",
                    help="Creates a .kyron_config.json file. Option is ignored if a config file "
                         "exists or is defined from `--download-from-config`")

parser.add_argument("--download-from-config", type=str, metavar="config_dir",
                    help="Reads a JSON config file. If option `downloads` is set in the config, "
                         "positional arguments for `channel_name` is ignored completely and will "
                         "adhere to the config you set")

pg_thumb = parser.add_argument_group("Thumbnails or avatars")
pg_thumb.add_argument("--ignore-new-thumbnails", action="store_true",
                      help="Ignores keeping previous revisions of thumbnails and avatars")
pg_thumb.add_argument("--delete-previous-thumbnails", action="store_true",
                      help="Deletes previous revisions from thumbnails and avatars")


pg_dl = parser.add_argument_group("Managing downloads")
pg_dl.add_argument("--skip-download", "--no-download", action="store_true",
                   help="Mirrors yt-dlp arg for skipping video downloads")

pg_dl.add_argument("--rename-handle", nargs=2, metavar=("OLD_NAME", "NEW_NAME"),
                   help="Renames a handle of a channel")

pg_dl.add_argument("--sleep-interval", type=int, metavar="SLEEP_SEC", default=9,
                   help="Adds a delay in seconds for each request. Mirrors the option from yt-dlp. "
                        "Default: 9")

pg_dl.add_argument("--download-livestreams", "--download-streams", action="store_true",
                   help="Include livestreams")
pg_dl.add_argument("--download-shorts", action="store_true",
                   help="Include Shorts content")

pg_dl.add_argument("--cookies", "-c", type=str, metavar="cookies_dir",
                   help="Use cookies from browser, only use for certain edge cases (i.e. accessing age-restricted or private videos)")

pg_misc = parser.add_argument_group("Miscellaneous")
pg_misc.add_argument("--no-log", action="store_true",
                     help="Disables writing progress to log file")

pg_misc.add_argument("--verbose", "-v", action="store_true",
                     help="Prints more stuff from the console for debugging")


args = parser.parse_args()
# endregion

# Arguments
pos_args_channels: list[str] = args.channel_name

args_dir: Optional[str] = args.dir
args_dl_livestreams: bool = args.download_livestreams
args_dl_shorts: bool = args.download_shorts

args_cfg_download: bool = args.download_from_config
args_cfg_create: bool = args.create_config

args_thumb_ignore: bool = args.ignore_new_thumbnails
args_thumb_remove_prev: bool = args.delete_previous_thumbnails

args_dl_skip: bool = args.skip_download

args_rename_handle: tuple[str, str] = args.rename_handle

args_eepy_interval: int = args.sleep_interval

args_cookies: str = args.cookies

args_nolog: bool = args.no_log
args_verbose_mode: bool = args.verbose


def verbose_log(*args):
    if not args_verbose_mode:
        return

    print(*args)


def main():
    # yes = ky_tables.table_maker(heading="Downloaded channels")
    # yes.show()

    print(args)

    # Initialize configs
    if not args_dir:
        base_path = CWD
    else:
        base_path = args_dir

    if args_cfg_create \
            and not (os.path.exists(".kyron_config.json") or os.path.exists(".kyron_config.jsonc")):
        print("INFO: No config file found, automatically generated one")
        with open(os.path.join(base_path, ".kyron_config.json"), "w") as f:
            json.dump(default_config, f, indent=2)

    if len(sys.argv) == 1:
        # parser.print_help()
        print("some minimal help here")
        sys.exit(2)


def process_ytdlp_command(has_livestream: bool = False, has_shorts: bool = False, cookies: Optional[str] = None, slep_interval=9):
    base_args = ["yt-dlp"]
    ...


if __name__ == "__main__":

    main()
