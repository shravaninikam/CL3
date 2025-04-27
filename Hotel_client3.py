import Pyro5.api


def main():
  
    hotel = Pyro5.api.Proxy("PYRONAME:hotel.booking")
  
    menu = {
        "1": "Book Room", 
        "2": "Cancel Booking", 
        "3": "View Bookings", 
        "4": "Exit"
    }
  
    while True:
      
        print("\nHotel Booking System:")
      
        for k, v in menu.items():
          
            print(f"{k}. {v}")
          
        choice = input("Enter choice: ")
      

        if choice == "1":
          
            print(hotel.book_room(input("Guest name: ")))
          
        elif choice == "2":
          
            print(hotel.cancel_booking(input("Guest name to cancel: ")))
          
        elif choice == "3":
          
            bookings = hotel.view_bookings()
          
            if isinstance(bookings, list):
              
                print("Current Bookings:", ', '.join(bookings))
              
            else:
              
                print(bookings)
              
        elif choice == "4":
          
            print("Goodbye!")
          
            break
          
        else:
          
            print("Invalid choice.")
          

if __name__ == "__main__":
  
    main()

