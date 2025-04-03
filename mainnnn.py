from abc import ABC, abstractmethod
import pymysql
from tabulate import tabulate

class EventNotFoundException(Exception):
    pass

class InvalidBookingIDException(Exception):
    pass
#concrete classes
class Venue:
    def __init__(self, venue_name="", address=""):
        self.venue_name = venue_name
        self.address = address
    
    def display_venue_details(self):
        print(f"Venue: {self.venue_name}, Address: {self.address}")

class Event(ABC):
    def __init__(self, event_name, event_date, event_time, venue, total_seats, ticket_price, event_type):
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue = venue
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.ticket_price = ticket_price
        self.event_type = event_type
    
    def calculate_total_revenue(self):
        return (self.total_seats - self.available_seats) * self.ticket_price
    
    def getBookedNoOfTickets(self):
        return self.total_seats - self.available_seats
    
    def book_tickets(self, num_tickets):
        if num_tickets <= self.available_seats:
            self.available_seats -= num_tickets
            print("Tickets booked successfully!")
        else:
            print("Not enough available seats!")
    
    def cancel_booking(self, num_tickets):
        self.available_seats += num_tickets
        print("Booking cancelled successfully!")
    
    def display_event_details(self):
        print(f"Event: {self.event_name}, Date: {self.event_date}, Time: {self.event_time}, Venue: {self.venue.venue_name}, Available Seats: {self.available_seats}")

class Movie(Event):
    def __init__(self, event_name, event_date, event_time, venue, total_seats, ticket_price, genre, actor_name, actress_name):
        super().__init__(event_name, event_date, event_time, venue, total_seats, ticket_price, "Movie")
        self.genre = genre
        self.actor_name = actor_name
        self.actress_name = actress_name
    
    def display_event_details(self):
        super().display_event_details()
        print(f"Genre: {self.genre}, Actor: {self.actor_name}, Actress: {self.actress_name}")

class Concert(Event):
    def __init__(self, event_name, event_date, event_time, venue, total_seats, ticket_price, artist, concert_type):
        super().__init__(event_name, event_date, event_time, venue, total_seats, ticket_price, "Concert")
        self.artist = artist
        self.concert_type = concert_type
    
    def display_event_details(self):
        super().display_event_details()
        print(f"Artist: {self.artist}, Type: {self.concert_type}")

class Sport(Event):
    def __init__(self, event_name, event_date, event_time, venue, total_seats, ticket_price, sport_name, teams_name):
        super().__init__(event_name, event_date, event_time, venue, total_seats, ticket_price, "Sports")
        self.sport_name = sport_name
        self.teams_name = teams_name
    
    def display_event_details(self):
        super().display_event_details()
        print(f"Sport: {self.sport_name}, Teams: {self.teams_name}")

class Customer:
    def __init__(self, customer_name="", email="", phone_number=""):
        self.customer_name = customer_name
        self.email = email
        self.phone_number = phone_number
    
    def display_customer_details(self):
        print(f"Customer: {self.customer_name}, Email: {self.email}, Phone: {self.phone_number}")

class Booking:
    booking_counter = 1
    
    def __init__(self, customers, event, num_tickets):
        self.bookingId = Booking.booking_counter
        Booking.booking_counter += 1
        self.customers = customers
        self.event = event
        self.num_tickets = num_tickets
        self.total_cost = event.ticket_price * num_tickets
        print(f"Booking created successfully! Booking ID: {self.bookingId}")
    
    def display_booking_details(self):
        print(f"Booking ID: {self.bookingId}, Event: {self.event.event_name}, Total Cost: {self.total_cost}")


class DBUtil:
    @staticmethod
    def getDBConn():
        try:
            return pymysql.connect(
                host="127.0.0.1",
                user="root",
                password="root",
                database="ticketbookingsystem",
                port=3306
            )
        except pymysql.Error as err:
            print("Error: ", err)
            return None

class IBookingSystemRepository(ABC):
    @abstractmethod
    def create_event(self, event_name: str, date: str, time: str, total_seats: int, ticket_price: float, event_type: str, venue: Venue):
        pass
    
    @abstractmethod
    def getEventDetails(self):
        pass
    
    @abstractmethod
    def getAvailableNoOfTickets(self):
        pass
    
    @abstractmethod
    def calculate_booking_cost(self, num_tickets):
        pass
    
    @abstractmethod
    def book_tickets(self, eventname: str, num_tickets: int, listOfCustomer):
        pass
    
    @abstractmethod
    def cancel_booking(self, booking_id):
        pass
    
    @abstractmethod
    def get_booking_details(self, booking_id):
        pass

class BookingSystemRepositoryImpl(IBookingSystemRepository):
    def __init__(self):
        self.conn = DBUtil.getDBConn()
        self.cursor = self.conn.cursor()
    
    def create_event(self, event_name, date, time, total_seats, ticket_price, event_type, venue):
        sql = """INSERT INTO events (event_name, event_date, event_time, total_seats, available_seats, ticket_price, event_type, venue_name, venue_address) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (event_name, date, time, total_seats, total_seats, ticket_price, event_type, venue.venue_name, venue.address)
        self.cursor.execute(sql, values)
        self.conn.commit()
        print("Event created successfully!")
    
    def getEventDetails(self):
        self.cursor.execute("SELECT * FROM event")
        columns = [desc[0] for desc in self.cursor.description]
        events = self.cursor.fetchall()
        print("Event details retrieved successfully!")
        if events:
            print(tabulate(events, headers=columns, tablefmt="grid"))
        else:
            print("No events found.")
       
        
    def getAvailableNoOfTickets(self):
        self.cursor.execute("SELECT SUM(available_seats) FROM events")
        available_tickets = self.cursor.fetchone()[0]
        print("Available tickets retrieved successfully!")
        return available_tickets
    
    def calculate_booking_cost(self, num_tickets, ticket_price):
        return num_tickets * ticket_price
    
    def book_tickets(self, eventname, num_tickets, listOfCustomer):
        self.cursor.execute("SELECT available_seats, ticket_price FROM events WHERE event_name=%s", (eventname,))
        event = self.cursor.fetchone()
        if not event:
            raise EventNotFoundException("Event not found!")
        if event[0] >= num_tickets:
            total_cost = self.calculate_booking_cost(num_tickets, event[1])
            sql = "INSERT INTO bookings (event_name, num_tickets, total_cost) VALUES (%s, %s, %s)"
            values = (eventname, num_tickets, total_cost)
            self.cursor.execute(sql, values)
            self.conn.commit()
            self.cursor.execute("UPDATE events SET available_seats = available_seats - %s WHERE event_name=%s", (num_tickets, eventname))
            self.conn.commit()
            print("Tickets booked successfully!")
        else:
            print("Not enough available seats!")
    
    def cancel_booking(self, booking_id):
        self.cursor.execute("SELECT event_name, num_tickets FROM bookings WHERE booking_id=%s", (booking_id,))
        booking = self.cursor.fetchone()
        if not booking:
            raise InvalidBookingIDException("Invalid booking ID!")
        self.cursor.execute("UPDATE events SET available_seats = available_seats + %s WHERE event_name=%s", (booking[1], booking[0]))
        self.conn.commit()
        self.cursor.execute("DELETE FROM bookings WHERE booking_id=%s", (booking_id,))
        self.conn.commit()
        print("Booking cancelled successfully!")
    
    def get_booking_details(self, booking_id):
        self.cursor.execute("SELECT * FROM bookings WHERE booking_id=%s", (booking_id,))
        booking = self.cursor.fetchone()
        print("Booking details retrieved successfully!")
        return booking

class TicketBookingSystem:
    def __init__(self):
        self.repository = BookingSystemRepositoryImpl()
    
    def run(self):
        while True:
            try:
                print("1. Create Event")
                print("2. Book Tickets")
                print("3. Cancel Tickets")
                print("4. Get Available Seats")
                print("5. Get Event Details")
                print("6. Exit")
                
                choice = int(input("Enter your choice: "))
                
                if choice == 1:
                    event_name = input("Enter event name: ")
                    date = input("Enter event date (YYYY-MM-DD): ")
                    time = input("Enter event time (HH:MM:SS): ")
                    total_seats = int(input("Enter total seats: "))
                    ticket_price = float(input("Enter ticket price: "))
                    event_type = input("Enter event type (Movie/Sports/Concert): ")
                    venue_name = input("Enter venue name: ")
                    address = input("Enter venue address: ")
                    venue = Venue(venue_name, address)
                    self.repository.create_event(event_name, date, time, total_seats, ticket_price, event_type, venue)
                elif choice == 2:
                    eventname = input("Enter event name: ")
                    num_tickets = int(input("Enter number of tickets: "))
                    customers = [Customer(input("Enter customer name: "), input("Enter email: "), input("Enter phone number: ")) for _ in range(num_tickets)]
                    self.repository.book_tickets(eventname, num_tickets, customers)
                elif choice == 3:
                    booking_id = int(input("Enter booking ID: "))
                    self.repository.cancel_booking(booking_id)
                elif choice == 4:
                    print("Available seats:", self.repository.getAvailableNoOfTickets())
                elif choice == 5:
                    self.repository.getEventDetails()
                elif choice == 6:
                    break
                else:
                    print("Invalid choice!")
            except EventNotFoundException as e:
                print(e)
            except InvalidBookingIDException as e:
                print(e)
            except Exception as e:
                print("An error occurred:", e)

if __name__ == "__main__":
    system = TicketBookingSystem()
    system.run()
