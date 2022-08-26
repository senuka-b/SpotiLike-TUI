from interface.SpotiLike import SpotiLike
from spotilike.main import SpotiLikeWorker

SpotiLikeWorker().start_thread()
SpotiLike.run(log="spotilike.log", title="SpotiLike <3")

