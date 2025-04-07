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
