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