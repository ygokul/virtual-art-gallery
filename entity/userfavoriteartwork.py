class UserFavoriteArtwork:
    def __init__(self, user_id: int = 0, artwork_id: int = 0):
        self._user_id = user_id
        self._artwork_id = artwork_id

    def get_user_id(self):
        return self._user_id

    def set_user_id(self, value):
        self._user_id = value

    def get_artwork_id(self):
        return self._artwork_id

    def set_artwork_id(self, value):
        self._artwork_id = value