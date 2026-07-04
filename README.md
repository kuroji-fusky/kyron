<h1 align="center">Kyron</h1>

An all-in-one downloader, archiver, and asset manager; built for an archivists' mind.

## Directory structure

- `client` - the Electron desktop client
- `server` - Python server written in FastAPI, which can also be used to be
   remote controlled via the desktop client or accessed via a browser
   that accesses `web_dashboard`
- `python_shared` - shared Python code for the backend and sidecar
- `sidecar` - the a Python background process responsible for communicating
  between the desktop client and OS-native APIs such as task scheduling
- `web_dashboard` - A dashboard similar to what the desktop client offers
- `web_shared` - shared code and Svelte components

## Contributing

This project requires a base prerequisites of Python 3.13, Node 22 or higher,
and the pnpm package manager installed. Docker is optional but recommended for
running or hosting the server.

> [!WARNING]
> pnpm should be at v10.x since there is a strange quirk with `electron-forge`
> not resolving other Electron dependencies, failing to run and build the
> application despite having `node-linker=hoisted` defined from the project's `.npmrc`.

At the root of this repository, install the necessary dependencies:

```bash
pnpm install

python -m venv venv
pip install -r requirements.txt
```

You can run a development build of the desktop client via:

```bash
pnpm run start
```

### Server

For running the server, you'll need to generate a private and public API tokens:

```bash
python server/generate-token.py
```

- `KYRON_API_TOKEN`: This will be solely be interfacing the client or elsewhere you'd use this on, this token can be safely regenerated from the dashboard
  > [!NOTE]
  > During development, once regenerated, the API token from the `.env` upon
  > initial setup is ignored and no longer valid. So please make sure your token
  > reflects from your `.env` file.

- `KYRON_PRIVATE_TOKEN`: A private token used on the server for performing destructive actions such as performing tasks in bulk and deleting files
  - This, however, can't be regenerated unless the server has shut down, then you can run the token script but with the `--force-regen private` flag to regenerate the private token


## License

The frontend, its desktop and web clients, and Python sidecar, are licensed under GPL-3.0, its backend is licensed under AGPL-3.0.