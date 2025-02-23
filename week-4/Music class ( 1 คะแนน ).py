class Song:
    def __init__(self, name, genre, durations):
        self.name = name
        self.genre = genre
        self.durations = durations
    
    def show_info(self):
        min = self.durations // 60
        sec = self.durations % 60
        return (f"{self.name} <|> {self.genre} <|> {min}.{sec:02d}")

Rickroll = Song(input(), input(), int(input()))
print(Rickroll.show_info())