class Song:
    def __init__(self, position, name, artist) -> None:
        self.position = position
        self.name = name
        self.artist = artist

    def __str__(self) -> str:
        return f"{self.position}) {self.name} by {self.artist}"
