<h1 align="center">Kyron</h1>

A wrapper of `yt-dlp` for bulk downloading YouTube channels/playlists locally or for archival purposes. It can also download deleted or private YouTube videos via Wayback Machine, on your system locally

> [!WARNING]
> Certain parts of the code are tailored to *my* specific use case, since they're a part of a private scripts that I use. So it won't be full-featured like yt-dlp has to offer and it won't satisfy other needs and edge cases.
>
> In other words: this codebase is certified **hot garbage**

> [!NOTE]
> Downloading livestreams, especially ones that exceed from few to several hours, can significantly hog up disk space. Make sure you have available space first (preferably a formatted drive) before commiting to downloading them!

## CLI reference

### General

| Argument                                             | Description                                                                                                                                                                 |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `channel_name <...>`                                 | A list of YouTube channel handle(s) to download, will be ignored if config has `downloads` has items                                                                        |
| `--list <name,size,videos>` `--l <name,size,videos>` | List all downloaded channels from the current directory or from the config                                                                                                  |
| `--dir <DIR_NAME>`                                   | Set custom download directory (default is the terminal's working directory)                                                                                                 |
| `--download-from-config <CONFIG_DIR>`                | Reads a JSON config file. If option `downloads` is present in the config, positional arguments for channel_name is ignored completely and will adhere to the config you set |
| `--create-config`                                    | Creates a .kyron_config.json file. Option is ignored if a config file exists or is defined from `--download-from-config`                                                    |
| `--no-log`                                           | Disables logging; is enabled by default to keep track of what's changed and stores it from `.kyron_data` directory for each channel                                         |

### Thumbnails

Options for keeping track of thumbnail/avatar changes

| Argument                       | Description |
| ------------------------------ | ----------- |
| `--ignore-new-thumbnails`      | -           |
| `--delete-previous-thumbnails` | -           |

### Managing downloads

| Argument                                | Description |
| --------------------------------------- | ----------- |
| `--rename-handle <OLD_NAME> <NEW_NAME>` | -           |
| `--sleep-interval`                      | -           |
| `--download-livestreams`                | -           |
| `--download-shorts`                     | -           |
| `--cookies`                             | -           |

### Others/Misc.

For development stuff

| Argument          | Description                                                                                   |
| ----------------- | --------------------------------------------------------------------------------------------- |
| `--verbose`, `-v` | Enables verbose logging, useful for debugging, or... I dunno, showing your hacker superiority |

## Config reference

The default config generates this:

```json
{
  "shorts": {
    "include": false
  },
  "livestreams": {
    "include": false,
    "length_limit": 0
  },
  "downloads": []
}
```

### `downloads`

You can either specify a list of channels/playlists or have a specific condition of a channel, can be mixed with either option.

Example of a basic list of channels:

```json
{
  "downloads": [
    "@abc",
    "@def"
  ] 
}
```

Applying certain conditions of a channel:

```json
{
  "downloads": [
    {
      "handle": "@abc",
      "livestreams": {
        "include": true,
        "length": ">=1h30m"
      }
    },
    {
      "handle": "@def",
      "shorts": {
        "include": true
      }
    }
  ] 
}
```

### `shorts`

Download Shorts from a creator; can be enabled with the `shorts.include` flag.

**Defaults:**

```json
{
  "shorts": {
    "includes": false
  }
}
```

### `livestreams`

Download VODs/livestreams from a creator

**Defaults:**

```json
{
  "livestreams": {
    "includes": false
  }
}
```