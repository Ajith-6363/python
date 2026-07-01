class train:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    def display_info(self):
        print(f"Train Name: {self.name}")
        print(f"Speed: {self.speed} km/h")
    def ticket_booking(self):
        print(f"Ticket booked for {self.name} at speed {self.speed} km/h")
        def ticket_price(self):
            print(f"Ticket price for {self.name} is ${self.speed * 0.5}")
        ticket_price(self)
    def ticket_cancellation(self):
            print(f"Ticket cancelled for {self.name}")
        
train1 = train("Express", 120)
train1.display_info()
train1.ticket_booking()
train1.ticket_cancellation()

