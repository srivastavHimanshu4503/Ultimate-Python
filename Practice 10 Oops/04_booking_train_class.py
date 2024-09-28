# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.
import random

class Train:
    number_of_tickets = 0
    per_ticket_fair = random.randint(90, 900)
    total_ticket_fair = per_ticket_fair*number_of_tickets
    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender
    
    def book_ticket(self, number_of_tickets):
        self.number_of_tickets = number_of_tickets
        self.total_ticket_fair = (self.number_of_tickets)*(self.per_ticket_fair)
        print("Ticket confirmed.")
    
    def get_status(self):
        if self.number_of_tickets:
            print(f"Your status is confirmed and {self.name} booked {self.number_of_tickets} tickets for your journey.")
        else:
            print(f"{self.name} did not book any tickets till now.")
    
    def get_fair(self):
        if self.total_ticket_fair:
            print(f"The total fare for your journey is {self.total_ticket_fair}")
        else:
            print(f"{self.name} don't book any tickets yet.")

passenger1 = Train("Ravi", 19, "Male")
passenger2 = Train("Kumari", 18, "Female")

passenger1.book_ticket(4)
passenger1.get_status()
passenger1.get_fair()

# passenger2.book_ticket()
passenger2.get_status()
passenger2.get_fair()
