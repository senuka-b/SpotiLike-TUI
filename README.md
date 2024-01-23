

# SpotiLike
Save Spotify songs on-the-go while you're listening to, to your Liked Songs library or your favorite playlists with custom hotkeys all through your keyboard!

⚠️ This application is still incomplete, only provides basic functionality.

# Installation

You can install your OS specific executable from the [releases](https://github.com/yetimeh/SpotiLike/releases/) section. See [Running SpotiLike](#configuration-and-running-spotilike).

I have bundled the app into a single stand alone executable but some users might find it slow (because it has to extract the code and run it that way). If you're facing such a problem feel feel to clone the repository and build it from source. For bundling I have used `pyinstaller` you can use anything you desire. 

```sh
$ pyinstaller --collect-all pyfiglet --name SpotiLike run.py
```


## Building from source

### Requirements

* Python version 3 or above

### Steps

1. Clone the repository

```sh
$ git clone https://github.com/yetimeh/SpotiLike && cd SpotiLike
```

2. Install required packages

```sh
$ pip install -r requirements.txt
```

3. Run the app!

```sh
$ python run.py config
```

> If you want to freeze/bundle the app into an executable, you can do so by providing the `run.py` file as the file that should be freezed.

___

# Why? The context behind the app & how it works.

This app basically allows you to have control over your _playlists_ and _liked songs_ library through your keyboard. This means that, you can ❤️ like the current playing song with a custom keyboard shortcut or save that song into a playlist with a custom keyboard shortcut.


The reason for writing this script is because I found it troublesome having to return to the Spotify application to save the current playing track to my collection of songs which indeed interupted my workflow. As an avid Spotify enjoyer I do this too often. The most annoying place I've found myself in this issue is when I'm gaming.

When I found out Spotify itself doesn't provide this functionality, I tried using other solutions and none of them satisfied all my needs. So I decided to come up with my own solution and here it is. I've already made multiple versions of this app(as a gui, etc) in the past but I decided that a TUI for this sort of application would be ideal for the purpose of configuration.

The application runs a global background thread with all the hotkeys the user has inputted and does what it's supposed to do accordingly. Therefore, you can use the hotkeys in any application outside of Spotify or within Spotify itself too.

# Configuration and running SpotiLike

The app is divided into two modes.

### configuration mode

```sh
$ spotilike config
```

would open up:

![config](./readme/config.png)

`1` - **Playlists section**

- These are all your playlists.
- You can click and edit the hotkey value inside them.

`2` - **Command Area**

- This is where you configure settings for each playlist or liked songs library.
- Type 'help` and press enter to see a list of various commands
- If you want to do additional stuff such as downloading for offline use, creating backups of playlists, exporting track lists, save to liked songs library automatically when saving to a playlist, etc... this is where you do that.

(Not implemented yet)

`3` - **Main View**

- Instructions to work with the app are all displayed in this section.
- Command output which you have executed in the command are also displayed here

`4` - **Quick Access**

- This section is mainly focused on performing quick actions. 
- This probably would contain a few buttons which you can click.

(Not implemented yet)

### app mode

```sh
$ spotilike
```

This mode would actually start up the hotkey process. You would be able to see logs of what's happening in this manner:

![logs](./readme/app.png)


# TODO:

- Add notification support
- Add hide to system tray functionality
- Add commands

    - help
    - download 
    - autosave
    - export_track_list
    - logout
    - reset_database
    - autobackup
    - home