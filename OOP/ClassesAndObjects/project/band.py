from project.album import Album


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album.name in [x.name for x in self.albums]:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        if album_name not in self.albums:
            return f"Album {album_name} is not found."

        for album in self.albums:
            if album.published:
                return "Album has been published. It cannot be removed."

        self.albums.remove(album_name)
        return f"Album {album_name} has been removed."

    def details(self):
        result = f"Band {self.name}"

        for album in self.albums:
            result += f"\n{album.details()}"

        return result