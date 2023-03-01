from math import ceil


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] * self.pages for i in range(self.pages)]
        self.current_page = 1
        self.current_slot = 0

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(photos_count)

    def add_photo(self, label):
        if self.current_page <= self.pages:
            self.photos[self.current_page - 1].append(label)
            self.current_slot += 1
            result = f"{label} photo added successfully on page {self.current_page} slot {self.current_slot}"

            if self.current_slot == 4:
                self.current_page += 1
                self.current_slot = 0

            return result
        else:
            return "No more free slots"

    def display(self):
        result = ['-----------']
        for current_page in self.photos:
            current_photos = ""
            for i in range(4):
                try:
                    if current_page[i] != "":
                        current_photos += "[] "
                except IndexError:
                    continue
            result.append(current_photos.rstrip())
            result.append('-----------')

        return '\n'.join(result)


album = PhotoAlbum(3)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

