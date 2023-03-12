from math import ceil


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] * i for i in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label):
        for i in range(self.pages):
            if len(self.photos[i]) < 4:
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(self.photos[i])}"

        return "No more free slots"

    def display(self):
        result = ['-' * 11]
        for i in range(self.pages):
            result.append(('[] ' * len(self.photos[i])).rstrip())
            result.append('-' * 11)

        return '\n'.join(result)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
