class User:
    def __init__(self, user_id, username, password, email, first_name, last_name, date_of_birth, profile_picture, favorite_artworks=None):
        self._user_id = user_id
        self._username = username
        self._password = password
        self._email = email
        self._first_name = first_name
        self._last_name = last_name
        self._date_of_birth = date_of_birth
        self._profile_picture = profile_picture
        self._favorite_artworks = favorite_artworks

    def get_user_id(self):
        return self._user_id

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_email(self):
        return self._email

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_date_of_birth(self):
        return self._date_of_birth

    def get_profile_picture(self):
        return self._profile_picture

    def get_favorite_artworks(self):
        return self._favorite_artworks
