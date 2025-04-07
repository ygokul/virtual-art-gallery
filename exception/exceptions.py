class ArtGalleryException(Exception):
    pass

class ArtworkNotFoundException(ArtGalleryException):
    pass

class ArtistNotFoundException(ArtGalleryException):
    pass

class GalleryNotAddedException(ArtGalleryException):
    pass

class FavoriteNotFoundException(ArtGalleryException):
    pass

class UserNotFoundException(ArtGalleryException):
    pass

class GalleryNotFoundException(ArtGalleryException):
    pass