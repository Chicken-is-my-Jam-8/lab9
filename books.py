library = {}
def main():
	on = True
	while on == True:
		print("Library Book Tracker")
		print("1. Add a Book")
		print("2. Display All Books")
		print("3. Exit")
		user_input = input("Enter your choice: ")
		if user_input == '1':
			add_book()
		elif user_input == '2':
			view_books()
		elif user_input == '3':
			on = False
			print("Goodbye!")
		else:
			print("Invalid Input")
			print()

def add_book():
	title = input("Enter the book title: ").title()
	library[title] = "Avaliable"
	print(f"The book '{title}' has been added to the library")
	print()

def view_books():
	print()
	print("Library Books")
	for x, y in library.items():
		print(f"{x}: {y}")
	print()
main()
