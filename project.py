from datetime import datetime, timedelta

class Hotel:
    def __init__(self, name):
        self.name = name
        self.accommodations = Accommodations()

    def display_available_rooms(self, check_in, check_out):
        return self.accommodations.display_available_rooms(check_in, check_out)

class Accommodations:
    def __init__(self):
        self.rooms = {'Pool view': {'single': 5, 'double': 5},
                      'Nile view': {'single': 5, 'double': 5},
                      'Garden view': {'single': 5, 'double': 5}}

    def display_available_rooms(self, check_in, check_out):
        available_rooms = {}
        for view, room_types in self.rooms.items():
            available_rooms[view] = {}
            for room_type, quantity in room_types.items():
                if self.is_room_available(view, room_type, check_in, check_out):
                    available_rooms[view][room_type] = quantity
        return available_rooms

    def is_room_available(self, view, room_type, check_in, check_out):
        # Placeholder logic to check room availability
        return True

    def reserve_room(self, view, room_type):
        if self.rooms[view][room_type] > 0:
            self.rooms[view][room_type] -= 1
            return True
        else:
            return False

class Reservations:
    def __init__(self):
        self.reservations = []

    def add_reservation(self, reservation):
        self.reservations.append(reservation)

    def display_reservations(self):
        return self.reservations

class SignUp:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def display_customers(self):
        return self.customers

class Payment:
    def process_payment(self, credit_card_number, amount):
        # Placeholder for payment processing logic
        print(f"Payment of {amount} with credit card {credit_card_number} processed successfully.")

class Customer:
    def __init__(self, name, phone, email, password):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password

def get_date_input(prompt):
    while True:
        try:
            date_str = input(prompt)
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def main():
    hotel = Hotel("Sample Hotel")
    reservations = Reservations()
    signup = SignUp()
    payment = Payment()

    for _ in range(5):
        # Customer information
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        email = input("Enter your email address: ")
        password = input("Create a password: ")

        # Creating a customer
        customer = Customer(name, phone, email, password)
        signup.add_customer(customer)

        # Display available rooms
        print(f"\nAvailable rooms at {hotel.name}:")
        check_in = get_date_input("Enter check-in date (YYYY-MM-DD): ")
        check_out = get_date_input("Enter check-out date (YYYY-MM-DD): ")
        available_rooms = hotel.display_available_rooms(check_in, check_out)
        print(available_rooms)

        # Room reservation
        view = input("Choose a room view (Pool view, Nile view, Garden view): ")
        room_type = input("Choose room type (single or double): ")

        if view in available_rooms and room_type in available_rooms[view]:
            print("Room is available.")
            credit_card_number = input("Enter credit card number: ")

            # Process payment (placeholder)
            payment.process_payment(credit_card_number, 100)  # Assuming a fixed price for the room

            # Reserve room
            hotel.accommodations.reserve_room(view, room_type)

            print("Reservation successful.")
            reservation = {'customer': customer, 'view': view, 'room_type': room_type,
                           'check_in': check_in, 'check_out': check_out}
            reservations.add_reservation(reservation)

        else:
            print("Sorry, the selected room is not available for the specified dates. Please choose another room.")

    # Display reservations and customer information
    print("\nReservations:")
    print(reservations.display_reservations())

    print("\nCustomer Information:")
    print(signup.display_customers())

if __name__ == "__main__":
    main()
