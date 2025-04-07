class Artist:
    def __init__(self, artist_id, name, biography, birth_date, nationality, website, contact_info):
        self.artist_id = artist_id
        self.name = name
        self.biography = biography
        self.birth_date = birth_date
        self.nationality = nationality
        self.website = website
        self.contact_info = contact_info

class Gallery:
    def __init__(self, gallery_id, name, description, location, curator, opening_hours):
        self._gallery_id = gallery_id
        self._name = name
        self._description = description
        self._location = location
        self._curator = curator
        self._opening_hours = opening_hours

    def get_gallery_id(self):
        return self._gallery_id

    def set_gallery_id(self, value):
        self._gallery_id = value

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_description(self):
        return self._description

    def set_description(self, value):
        self._description = value

    def get_location(self):
        return self._location

    def set_location(self, value):
        self._location = value

    def get_curator(self):
        return self._curator

    def set_curator(self, value):
        self._curator = value

    def get_opening_hours(self):
        return self._opening_hours

    def set_opening_hours(self, value):
        self._opening_hours = value


class Artwork:
    def __init__(self, artwork_id, title, description,creation_date, medium, image_url):
        self._artwork_id = artwork_id
        self._title = title
        self._description = description
        self._creation_date = creation_date
        self._medium = medium
        self._image_url = image_url

    # Getters
    def get_artwork_id(self):
        return self._artwork_id

    def get_title(self):
        return self._title

    def get_description(self):
        return self._description
    
    def get_creation_date(self):
        return self._creation_date

    def get_medium(self):
        return self._medium

    def get_image_url(self):
        return self._image_url

    # Setters
    def set_artwork_id(self, artwork_id):
        self._artwork_id = artwork_id

    def set_title(self, title):
        self._title = title

    def set_description(self, description):
        self._description = description
    
    def set_creation_date(self, creation_date):
        self._creation_date = creation_date
        
    def set_medium(self, medium):
        self._medium = medium

    def set_image_url(self, image_url):
        self._image_url = image_url


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

