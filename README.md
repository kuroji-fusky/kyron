<h1 align="center">Kyron</h1>

An all-in-one downloader, archiver, and asset manager; built for an archivists' mind.

## Directory structure

- `client` - the Electron desktop client
- `server` - Python server written in FastAPI, which can also be used to be
   remote controlled via the desktop client or accessed via a browser
   that accesses `web_dashboard`
- `python_shared` - shared Python code for the backend and sidecar
- `sidecar` - the a Python background process responsible for communicating
  between the desktop client and native OS APIs such as task scheduling
- `web_dashboard` - A dashboard similar to what the desktop client offers
- `web_shared` - shared code and Svelte components

## Contributing

WIP

## License

The frontend, its desktop and web clients, and Python sidecar, are licensed under GPL-3.0, its backend is licensed under AGPL-3.0.