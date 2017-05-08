class Photo(object):
    PHOTO_ALBUM_PATH = '/home/rmotr/photos/'

    def __init__(self, name):
        self.name = name

    @property
    def full_path(self):
        return '{}{}'.format(self.PHOTO_ALBUM_PATH, self.name)

    def __str__(self):
        return self.full_path

    __repr__ = __str__


class PhotoAlbum(object):
    def __init__(self):
        self.current_photo = 0
        self.photos = []

    def add_photo(self, photo):
        self.photos.append(photo)

    # implement iteration here
