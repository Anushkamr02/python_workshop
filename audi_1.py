

num_rows = int(input("Enter number of rows: "))
section1 = 6
section2 = 10
section3 = 6

total_seats = section1 + section2 + section3


# Create seating layout with '-' for available seats
auditorium = [["-" for _ in range(total_seats)] for _ in range(num_rows)]


# Function to book a seat
def book_seat(row, seat):
    if 0 <= row < num_rows and 0 <= seat < total_seats:

        if auditorium[row][seat] == "-":
            auditorium[row][seat] = "*"
            print(f"Seat ({row+1}, {seat+1}) booked successfully!")
        else:
            print(f"Seat ({row+1}, {seat+1}) is already booked.")
    else:
        print("Invalid seat number. Please try again.")

# Function to display seating with section dividers
def display_seating():

    print("\nCurrent Seating Arrangement:")
    for row in auditorium:
        line = ""
        for i, seat in enumerate(row):
            if i == section1 or i == section1 + section2:
                line += " |"  # Add section separator
            line += f" {seat}"
        print(line)

# User interaction loop
while True:
    display_seating()

   
    choice = input("\nDo you want to book a seat? (yes/no): ").lower()
    if choice == "no":
        break

    row = int(input(f"Enter row number to book (1 to {num_rows}): ")) - 1
    seat = int(input(f"Enter seat number to book (1 to {total_seats}): ")) - 1

    book_seat(row, seat)

# Final display

print("\nFinal Auditorium Seating Arrangement:")
display_seating()

print("Booking process complete. Enjoy the show! 🎭")
