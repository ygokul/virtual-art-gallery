from util.db_utils import DBConnection
from dao.implementation import VirtualArtGalleryDAO
from entity.artwork import Artwork
from entity.gallery import Gallery
from entity.userfavoriteartwork import UserFavoriteArtwork

def main():
    conn = DBConnection.connect()
    dao = VirtualArtGalleryDAO(conn)
    
    while True:
        
        print("\t")
        print("="*50)
        print("🎨  WELCOME TO THE VIRTUAL ART GALLERY  🎨".center(50))
        print("="*50)
        
        print("       a. Artwork Management")
        print("       b. Gallery Management")
        print("       c. Exit")

        main_choice = input("\nEnter your choice (a/b/c): ").lower()

        if main_choice == 'a':

            while True:
                    print("\nVirtual Art Gallery")
                    print("1. Create Account for artist")                      # Moved to the top
                    print("2. View Artworks")
                    print("3. Add Artwork")
                    print("4. Update Artwork")
                    print("5. Remove Artwork")
                    print("6. View Your Artwork with ID")
                    print("7. Search Artworks")
                    print("8. Add Artwork to Favorites")
                    print("9. Remove Artwork from Favorites")
                    print("10. View User's Favorite Artworks")
                    print("11. Back to main menu")
                    
                    choice = input("Enter your choice: ")

                    if choice == '1':  # Add artist functionality
                        name = input("Name: ")
                        biography = input("Biography: ")
                        birth_date = input("Birth Date (YYYY-MM-DD): ")
                        nationality = input("Nationality: ")
                        website = input("Website: ")
                        contact_info = input("Contact Information: ")
                        dao.add_artist(name, biography, birth_date, nationality, website, contact_info)

                    if choice == '2':
                        dao.view_artworks()

                    elif choice == '3':
                        title = input("Title: ")
                        description = input("Description: ")
                        medium = input("Medium: ")
                        image_url = input("Image URL: ")
                        dao.add_artwork(title, description, medium, image_url)
            
                    elif choice == '4':
                        print("\n✏️ Update Artwork")
                        artwork_id = int(input("Enter Artwork ID to update: "))
                        title = input("Title: ")
                        description = input("Description: ")
                        medium = input("Medium: ")
                        image_url = input("Image URL: ")

                        artwork = Artwork(
                            artwork_id=artwork_id,
                            title=title,
                            description=description,
                            creation_date=None,  # or pass a dummy value since it's auto-updated
                            medium=medium,
                            image_url=image_url
                        )

                        dao.update_artwork(artwork)


                    elif choice == '5':
                        identifier = input("Enter Artwork ID or Title to remove: ")

                        # Convert to int if possible (assume it's an ID)
                        if identifier.isdigit():
                            identifier = int(identifier)

                        dao.remove_artwork(identifier)

                    elif choice == '6':
                        artwork_id = int(input("Enter Artwork ID to view: "))
                        dao.get_artwork_by_id(artwork_id)

                    elif choice == '7':
                        keyword = input("Enter keyword to search in artwork titles: ")
                        dao.search_artworks(keyword)


                    elif choice == '8':
                        user_id = int(input("Enter User ID: "))
                        artwork_id = int(input("Enter Artwork ID: "))

                        favorite = UserFavoriteArtwork()
                        favorite.set_user_id(user_id)
                        favorite.set_artwork_id(artwork_id)

                        dao.add_artwork_to_favorite(favorite)


                    elif choice == '9':
                        artwork_id = int(input("Enter Artwork ID to remove from favorites: "))
                        print()  # One-line gap

                        favorite = UserFavoriteArtwork()
                        favorite.set_artwork_id(artwork_id)

                        dao.remove_artwork_from_favorite(favorite)

                    elif choice == '10':
                        user_id = int(input("Enter User ID to view favorite artworks: "))
                        print()  # Adds a one-line gap

                        dao.get_user_favorite_artworks(user_id)

                    elif choice == '11':
                        break

                    else:
                        print("valid option")

        elif main_choice == 'b':
             while True:
                    print("1. view all Galleries")
                    print("2. Create Gallery")
                    print("3. Update Gallery")
                    print("4. Search Gallery By Name")
                    print("5. Search by ID ")
                    print("6. Remove gallery")
                    print("7. Gallery Artist Impact Report")
                    print("8.Get Artworks From Gallery")
                    print("9. Get Artworks From Gallery")
                    print("10. Top Exhibited Artworks")
                    print("11. Back to main menu")
                    
                    choice=input("Enter Your Choice:")

                    if choice == '1':
                        print("\n📋 Viewing All Galleries...\n")
                        dao.view_all_galleries()

                    elif choice == '2':
                        name = input("Enter Gallery Name: ")
                        description = input("Enter Description: ")
                        location = input("Enter Location: ")
                        curator = input("Enter Curator ID (leave blank if none): ")
                        opening_hours = input("Enter Opening Hours: ")
                        print()

                        curator = int(curator) if curator.strip() else None

                        # Pass gallery_id=None explicitly since it's auto-incremented
                        gallery = Gallery(
                            gallery_id=None,
                            name=name,
                            description=description,
                            location=location,
                            curator=curator,
                            opening_hours=opening_hours
                        )

                        dao.add_gallery(gallery)


                    elif choice == '3':
                        print("\n🛠️  Update Gallery")
                        gallery_id = int(input("Enter Gallery ID to update: "))
                        name = input("Enter New Name: ")
                        description = input("Enter New Description: ")
                        location = input("Enter New Location: ")
                        curator = input("Enter New Curator ID: ")
                        opening_hours = input("Enter New Opening Hours: ")
                        print()

                        updated_gallery = Gallery(gallery_id, name, description, location, curator, opening_hours)
                        dao.update_gallery(updated_gallery)
                    

                    elif choice == '4':
                        keyword = input("Enter gallery name keyword to search: ").strip()
                        print()
                        dao.search_gallery_by_name(keyword)

                    elif choice == '5':
                        gallery_id = input("Enter Gallery ID to search: ").strip()
                        print()
                        dao.search_gallery_by_id(gallery_id)

                    elif choice == '6':
                        gallery_id = input("Enter Gallery ID to remove: ").strip()
                        print()
                        dao.remove_gallery(gallery_id)

                    elif choice == '7':
                        print()
                        dao.gallery_artist_impact_report()

                    elif choice == '8':
                        print("\n🎨 View Artworks in a Gallery")
                        gallery_id = int(input("Enter Gallery ID: "))
                        print()
                        dao.get_artworks_in_gallery(gallery_id)


                    
                    elif choice == '9':
                        print("\n🏛 View Galleries Displaying an Artwork")
                        artwork_id = int(input("Enter Artwork ID: "))
                        print()
                        dao.get_galleries_for_artwork(artwork_id)
                    

                    elif choice == '10':
                        print("\n📊 View Top Exhibited Artworks")
                        top_n = int(input("Enter how many top artworks you want to view: "))
                        print()
                        dao.get_top_exhibited_artworks(top_n)



                    elif choice == '11':
                        break

                    else:
                        print("Enter valid option")
        
        elif main_choice == 'c':
            break

        else:
            print("Invalid Option")
                    
                    


        

       

    conn.close()

if __name__ == "__main__":
    main()