# yt-archiver

## Development

### Prerequisites

- Python 3.10 or higher
- Node.js' LTS supported version (currently 22.x.x)
  - PNPM package manager
- [Rust](https://www.rust-lang.org/tools/install)
  - Development for Tauri's prerequisities can be found [here](https://v2.tauri.app/start/prerequisites/)

### Setup

There are two directories: `client` and `archiver`, both of their dependencies can be installed one way or the other.

#### From `client`

1. Install the projects dependencies with:
    ```console
    pnpm install
    ```

1. Run the development version of the app with 
    ```console
    pnpm tauri dev
    ```

    For Windows: if you run to issues running the desktop app, you might need to double-check if you have [Microsoft C++ Build Tools](https://v2.tauri.app/start/prerequisites/#windows) installed.

#### From `archiver`

1. Create a virtual environment with `python -m venv venv`, and activate it with:
    - Most platforms:
      ```console
      ./venv/Scripts/activate
      ```

    - Using PowerShell:
      ```ps1
      .\venv\Scripts\Activate.ps1
      ```

    - macOS:
      ```sh
      source venv/bin/activate
      ```

    - Linux:
      ```sh
      source venv/Scripts/activate
      ```

2. Install project dependencies with `python install -r requirements.txt`