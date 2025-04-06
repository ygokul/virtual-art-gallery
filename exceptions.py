class ArtGalleryException(Exception):
    pass

class ArtworkNotFoundException(ArtGalleryException):
    pass

class ArtistNotFoundException(ArtGalleryException):
    pass

class GalleryNotFoundException(ArtGalleryException):
    pass

class FavoriteNotFoundException(ArtGalleryException):
    pass