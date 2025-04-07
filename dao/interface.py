from abc import ABC, abstractmethod
from entity.gallery import Gallery
from entity.userfavoriteartwork import UserFavoriteArtwork

class Interface(ABC):

    @abstractmethod
    def view_artworks(self):
        pass

    @abstractmethod
    def add_artwork(self, title, description, medium, image_url):
        pass

    @abstractmethod
    def update_artwork(self, artwork):
        pass

    @abstractmethod
    def remove_artwork(self, identifier):
        pass
    
    @abstractmethod
    def get_artwork_by_id(self, artwork_id):
        pass
    
    @abstractmethod
    def search_artworks(self, keyword):
        pass

    @abstractmethod
    def add_artwork_to_favorite(self, favorite: UserFavoriteArtwork):
        pass

    @abstractmethod
    def remove_artwork_from_favorite(self, favorite: UserFavoriteArtwork):
        pass

    @abstractmethod
    def get_user_favorite_artworks(self, user_id):
        pass

    @abstractmethod
    def add_artist(self, name, biography, birth_date, nationality, website, contact_info):
        pass

    @abstractmethod
    def add_gallery(self, gallery: Gallery):
        pass


    @abstractmethod
    def update_gallery(self, gallery: Gallery):
        pass
    

    @abstractmethod
    def search_gallery_by_name(self, name_keyword):
        pass
    

    @abstractmethod
    def view_all_galleries(self):
        pass

    @abstractmethod
    def search_gallery_by_id(self, gallery_id):
        pass

    
    @abstractmethod
    def remove_gallery(self, gallery_id):
        pass

    @abstractmethod
    def gallery_artist_impact_report(self):
        pass
    

    @abstractmethod
    def get_artworks_in_gallery(self, gallery_id):
        pass
    

    @abstractmethod
    def get_galleries_for_artwork(self, artwork_id):
        pass

    @abstractmethod
    def get_top_exhibited_artworks(self, top_n):
        pass





    


