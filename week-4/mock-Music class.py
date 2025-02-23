class Song:
    def __init__(self, name, genre, duration):
        self.name = name
        self.genre = genre
        self.duration = duration
    
    def show_info(self):
        min = self.duration // 60
        sec = self.duration % 60
        return f"{self.name} <|> {self.genre} <|> {min}.{sec:02d}"

Rickroll = Song(input(), input(), int(input()))
print(Rickroll.show_info())