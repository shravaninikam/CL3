import Pyro5.api


@Pyro5.api.expose

class HotelBooking:
  
    def __init__(self):
      
        self.bookings = []
      

    def book_room(self, name):
      
        if name in self.bookings:
          
            return f"{name} already booked."
          
        self.bookings.append(name)
      
        return f"Room booked for {name}."
      

    def cancel_booking(self, name):
      
        if name in self.bookings:
          
            self.bookings.remove(name)
          
            return f"Booking for {name} canceled."
          
        return f"No booking found for {name}."
      

    def view_bookings(self):
      
        return self.bookings or "No current bookings."
      

def main():
  
    daemon = Pyro5.api.Daemon()
  
    ns = Pyro5.api.locate_ns()
  
    uri = daemon.register(HotelBooking())
  
    ns.register("hotel.booking", uri)
  
    print("Hotel Booking Server ready.")
  
    daemon.requestLoop()
  

if __name__ == "__main__":
  
    main()
  

