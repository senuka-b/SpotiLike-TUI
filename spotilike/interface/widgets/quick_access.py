from textual.widgets import ScrollView, Button


class QuickAccess(ScrollView):
    def __init__(self, *args, **kwargs):
        super().__init__(contents=Button("Help", style="cyan"), *args, **kwargs)
