create table Artwork(ArtworkID int primary key AUTO_INCREMENT,Title varchar(100),Description varchar(250),CreationDate DATE,Medium text,ImageURL varchar(500));

CREATE TABLE Artist(ArtistID int primary key,Name varchar(20),Biography varchar(200),BirthDate Date,Nationality varchar(20),Website varchar(100),ContactInformation varchar(500));

CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,         
    Username VARCHAR(50)  UNIQUE,          
    Password VARCHAR(200) ,                
    Email VARCHAR(100)  UNIQUE,            
    FirstName VARCHAR(50),                         
    LastName VARCHAR(50),                          
    DateOfBirth DATE,                              
    ProfilePicture VARCHAR(200),                   
    FavoriteArtwork INT,                           
    FOREIGN KEY (FavoriteArtwork) REFERENCES Artwork(ArtworkID)  
);

CREATE TABLE Gallery (
    GalleryID INT  PRIMARY KEY,          
    Name VARCHAR(100) ,                        
    Description TEXT,                                   
    Location VARCHAR(200),                             
    Curator INT,                                        
    OpeningHours VARCHAR(100),                         
    FOREIGN KEY (Curator) REFERENCES Artist(ArtistID)  
);

CREATE TABLE Gallery (
    GalleryID INT  PRIMARY KEY,          
    Name VARCHAR(100) ,                        
    Description TEXT,                                   
    Location VARCHAR(200),                             
    Curator INT,                                        
    OpeningHours VARCHAR(100),                         
    FOREIGN KEY (Curator) REFERENCES Artist(ArtistID)  
);


INSERT INTO Artwork (Title, Description, CreationDate, Medium, ImageURL)
VALUES
    ('Emperia Images', 
     'Emperia Art Gallery is an immersive, futuristic digital space showcasing innovative and interactive virtual artworks.', 
     '2023-01-15', 
     'Digital Painting', 
     'https://emperiavr.com/wp-content/uploads/2021/03/ArtGalleries-1.jpg'),

    ('Art meets AR', 
     'Where art meets augmented reality, creating immersive, interactive, and dynamic experiences that blend the physical and digital worlds.', 
     '2022-11-20', 
     'Augmented Reality (AR) Art', 
     'https://www.plugxr.com/augmented-reality/wp-content/uploads/2022/09/AR-art-1024x536.jpg'),

    ('DIGITAL MUSEUM', 
     'A virtual art gallery within a digital museum, showcasing immersive 3D artworks, interactive exhibits, and multimedia experiences.', 
     '2021-05-10', 
     'Multimedia Installation', 
     'https://www.invaluable.com/blog/wp-content/uploads/sites/77/2019/05/01-Kremer-Museum.jpg'),

    ('Human Metamorphosis', 
     'An immersive virtual exhibit exploring human metamorphosis through dynamic digital transformations and evolving 3D forms.', 
     '2023-03-08', 
     'Motion Graphics', 
     'https://img.freepik.com/premium-vector/natural-metamorphosis-human-head-tranquil-landscape-merge-art-prints_961038-5507.jpg?w=740'),

    ('Time meets Virtual Art', 
     'A captivating fusion where the concept of time intertwines with virtual art, creating immersive, ever-evolving digital experiences.', 
     '2023-07-01', 
     '3D Digital Art', 
     'https://static.tnn.in/thumb/msid-117633497,thumbsize-1366252,width-1280,height-720,resizemode-75/117633497.jpg'),

    ('Kids Favourite Art', 
     'A joyful collection of vibrant, playful, and whimsical digital artworks designed to spark imagination and delight young minds.', 
     '2022-12-05', 
     'Hand Painting', 
     'https://familyforeverychild.org/wp-content/uploads/2022/01/69824735.jpeg'),

    ('Galaxy meets Virtual Art', 
     'An awe-inspiring virtual experience where cosmic wonders collide with digital artistry, immersing viewers in a galaxy of surreal visuals and interstellar creativity.', 
     '2024-01-10', 
     'Animation', 
     'https://c02.purpledshub.com/uploads/sites/48/2021/06/solar-system-planets-2dff1b1.jpg?w=940&webp=1'),

    ('Delicious Explains the Art', 
     'A mouthwatering visual feast where vibrant colors, textures, and digital artistry come together to create deliciously captivating artworks.', 
     '2021-09-22', 
     'Canva Painting', 
     'https://cdn11.bigcommerce.com/s-x49po/images/stencil/800w/products/127776/294765/prints%2Fdownscaled%2Fp_rp771ai9bxp_2000x2000__65157.1713421001.jpg?c=2'),

    ('Exploring Simple and Wow Nature', 
     'A serene yet stunning virtual showcase capturing the simplicity and grandeur of nature through breathtaking digital landscapes and immersive art.', 
     '2024-02-28', 
     'Digital Painting', 
     'https://imgcdn.stablediffusionweb.com/2024/4/10/27d94784-0cd7-4096-ad0f-3b9a4cf53904.jpg'),

    ('Music Therapy', 
     'A harmonious blend of digital art and soothing soundscapes, offering a therapeutic, immersive experience that calms the mind and uplifts the spirit.', 
     '2023-10-18', 
     'Digital Art', 
     'https://i0.wp.com/london-post.co.uk/wp-content/uploads/2023/12/image002.jpeg?fit=649%2C433&ssl=1');

INSERT INTO Artist (ArtistID, Name, Biography, BirthDate, Nationality, Website, ContactInformation)
VALUES 
(101, 'Arjun Mehta', 'Contemporary digital artist specializing in virtual art galleries.', '1990-04-15', 'Indian', 'https://www.emperiavr.com', 'arjun.mehta@example.com'),
(102, 'Alex Rivera', 'Mixed media artist known for augmented reality exhibits.', '1987-09-21', 'American', 'https://www.artivive.com', 'alex.rivera@example.com'),
(103, 'Ishita Sharma', 'Abstract artist whose works are featured in major global tours.', '1993-07-03', 'Indian', 'https://www.theguardian.com/travel/2020/mar/23', 'ishita.sharma@example.com'),
(104, 'Taylor Morgan', 'Sculptor blending traditional and AR techniques.', '1985-02-10', 'Canadian', 'https://www.artstation.com/artwork/wrJm5L', 'taylor.morgan@example.com'),
(105, 'Rohan Patel', 'Painter focusing on nature and landscape themes.', '1992-05-27', 'Indian', 'https://www.shine.cn/feature/art-culture/2311227602/', 'rohan.patel@example.com'),
(106, 'Jordan Lee', 'Photographer and digital artist specializing in virtual spaces.', '1990-03-19', 'Australian', 'https://thinkplaycreate.org/explore/virtual-tours/', 'jordan.lee@example.com'),
(107, 'Ananya Iyer', 'Installation artist with a focus on virtual reality environments.', '1995-06-11', 'Indian', 'https://www.twinkl.cz/blog/twinkl-virtual-earth-day-art-gallery', 'ananya.iyer@example.com'),
(108, 'Casey Bennett', 'Artist known for interactive digital installations.', '1988-12-22', 'British', 'https://huwmessie.com/2020/03/04/the-virtual-artifact-gallery/', 'casey.bennett@example.com'),
(109, 'Kunal Desai', 'Oil painter blending traditional and digital techniques.', '1994-01-18', 'Indian', 'https://www.fizdi.com/trees-and-house-art_4551_27736-handpainted-art-painting-20in-x-20in/', 'kunal.desai@example.com'),
(110, 'Charlie Dawson', 'Multimedia artist specializing in music and art fusion.', '1986-08-09', 'American', 'https://harmonyarts.com/products/guitars-musical-instruments-paintings-artworks', 'charlie.dawson@example.com');


INSERT INTO users (UserID, Username, Password, Email, FirstName, LastName, DateOfBirth, ProfilePicture, FavoriteArtwork)
VALUES
(001, 'priya', 'Priya@123', 'priya@example.com', 'Priya', 'Sharma', '1995-04-10', 'https://example.com/profiles/priya.jpg',4 ),
(002, 'charlie', 'Charlie@456', 'charlie@example.com', 'Charlie', 'Dawson', '1990-08-09', 'https://example.com/profiles/charlie.jpg',6 ),
(003, 'ram', 'Ram@789', 'ram@example.com', 'Ram', 'Patel', '1992-12-01', 'https://example.com/profiles/ram.jpg',5 ),
(004, 'sai', 'Sai@234', 'sai@example.com', 'Sai', 'Krishnan', '1998-06-15', 'https://example.com/profiles/sai.jpg',4 ),
(005, 'suba', 'Suba@567', 'suba@example.com', 'Suba', 'Iyer', '1994-11-23', 'https://example.com/profiles/suba.jpg',2),
(006, 'sudeesh', 'Sudeesh@890', 'sudeesh@example.com', 'Sudeesh', 'Menon', '1991-03-05', 'https://example.com/profiles/sudeesh.jpg', 5),
(007, 'pradeep', 'Pradeep@321', 'pradeep@example.com', 'Pradeep', 'Verma', '1989-07-11', 'https://example.com/profiles/pradeep.jpg', 6),
(008, 'alice', 'Alice@654', 'alice@example.com', 'Alice', 'Bennett', '1993-05-30', 'https://example.com/profiles/alice.jpg',1 ),
(009, 'bob', 'Bob@987', 'bob@example.com', 'Bob', 'Lee', '1996-01-17', 'https://example.com/profiles/bob.jpg',  9),
(010, 'rocky', 'Rocky@543', 'rocky@example.com', 'Rocky', 'Desai', '1997-09-29', 'https://example.com/profiles/rocky.jpg', 1);


INSERT INTO Gallery (GalleryID, Name, Description, Location, Curator, OpeningHours)
VALUES
(10, 'art sphere', 'Art unites everyone together', 'india', 104, '9 am to 1 pm'),
(20, 'zumba art', 'experiencing each and every art brings peace', 'indonesia', 106, '8 am t0 10 am'),
(30, 'flying colours', 'life becomes flying colours when you work hard', 'singapore', 102, '6pm t0 8 pm'),
(40, 'wondering sculpture', 'mind blowing ideas and pictures', 'malaysia', 101, '10 am to 12 pm'),
(50, 'beauty of art', 'beauty lies in the way we design an art', 'indore', 102, '1 pm to 4 pm'),
(60, 'epics of art', 'whole universe is made of art', 'bhutan', 104, '2 pm to 4 pm');


CREATE TABLE User_Favorite_Artwork (
    UserID INT,
    ArtworkID INT,
    PRIMARY KEY (UserID, ArtworkID),  
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (ArtworkID) REFERENCES Artwork(ArtworkID)
);

INSERT INTO User_Favorite_Artwork (UserID, ArtworkID) VALUES
(1, 1), (1, 2),(1,3),  
(2, 1), (2, 4),  
(3, 2), (3, 6),  
(4, 3), (4,5),            
(5, 1), (5, 5), (5, 8),  
(6, 9), (6,7),            
(7, 9), (7, 2),  
(8, 1),(8,2),              
(9, 6),  
(10, 9), (10, 8);

CREATE TABLE Artwork_Gallery (
    ArtworkID INT,
    GalleryID INT,
    PRIMARY KEY (ArtworkID, GalleryID),  
    FOREIGN KEY (ArtworkID) REFERENCES Artwork(ArtworkID),
    FOREIGN KEY (GalleryID) REFERENCES Gallery(GalleryID)
);

INSERT INTO Artwork_Gallery (ArtworkID, GalleryID) VALUES
(1, 10), (1, 20),  
(2, 60),  
(3, 40), (3, 50),  
(4, 20),             
(5, 30), (5, 10),  
(6, 60), 
(7, 40),  (7,60) ,           
(8, 10),              
(9, 40), (9, 60),  
(10, 10);   


alter table artwork add column ArtistID int, add constraint ar_foreign foreign key (ArtistID) references artist(ArtistID);

insert into artwork(artistid) values(101),(102),(103),(102),(105),(104),(106),(107),(108),(109);




