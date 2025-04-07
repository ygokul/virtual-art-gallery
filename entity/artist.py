class Artist:
    def __init__(self, artist_id, name, biography, birth_date, nationality, website, contact_info):
        self._artist_id = artist_id
        self._name = name
        self._biography = biography
        self._birth_date = birth_date
        self._nationality = nationality
        self._website = website
        self._contact_info = contact_info

    # Getters
    def get_artist_id(self):
        return self._artist_id

    def get_name(self):
        return self._name

    def get_biography(self):
        return self._biography

    def get_birth_date(self):
        return self._birth_date

    def get_nationality(self):
        return self._nationality

    def get_website(self):
        return self._website

    def get_contact_info(self):
        return self._contact_info

    # Setters
    def set_artist_id(self, artist_id):
        self._artist_id = artist_id

    def set_name(self, name):
        self._name = name

    def set_biography(self, biography):
        self._biography = biography

    def set_birth_date(self, birth_date):
        self._birth_date = birth_date

    def set_nationality(self, nationality):
        self._nationality = nationality

    def set_website(self, website):
        self._website = website

    def set_contact_info(self, contact_info):
        self._contact_info = contact_info
