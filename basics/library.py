#Programm to record library information

#Lists to store information
all_books = []
available_books = []
available_genres = []

#Start of the program
option = "0"

print("""Welcome to the library system
  ...................................
        """)

while option != "e":
  
  option = input("Please choose an option:\n"
        "1 See the list of all books.\n"
        "2 Add a new book.\n"
        "3 See available books.\n"
        "4 See the available book genres.\n"
        "e Exit the program."
        "\n")
  
  if option == "1":
    #TODO extraer los libros de la lista e imprimirlos en una lista ordenada
    print(all_books)
    option = input("r to return the main menu.\n"
                   "e to exit the program.\n")
    
    
