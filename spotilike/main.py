from api.main import SpotiLikeWorker
from interface.SpotiLike import SpotiLike


import argparse, sys

parser = argparse.ArgumentParser(
    description="Save Spotify songs on-the-go while you're listening, to your Liked Songs library or your favourite playlists with custom hotkeys all through your keyboard!",
)

parser.add_argument("gui", nargs="?", default="run", help="Run the configuration TUI")

args = parser.parse_args()

if args.gui == "gui":
    SpotiLike.run(log="spotilike.log", title="SpotiLike <3")
else:
    worker = SpotiLikeWorker()
    sys.excepthook = worker.handle_exception

    worker.run()
