import argparse
import secrets
from colorama import just_fix_windows_console as FIX_COLORS, Style


parser = argparse.ArgumentParser(
    description="Generates a tokens for the server and client"
)

parser.add_argument("--force-regen",
                    help="Regenerates the key and overrides the existing key from an .env file")

args = parser.parse_args()


def main():
    private_api_token = secrets.token_urlsafe(48)
    public_api_token = secrets.token_urlsafe(32)

    print(f"\n{Style.BRIGHT}Public token:{Style.RESET_ALL}\n{public_api_token}\n"
          f"{Style.BRIGHT}Internal token:{Style.RESET_ALL}\n{private_api_token}\n")

    print("Interal tokens are written under the `KYRON_PRIVATE_TOKEN`"
          " from the root of the project's `.env`.")


if __name__ == "__main__":
    FIX_COLORS()
    main()
