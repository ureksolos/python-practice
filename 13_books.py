import sqlite3

def create_table_authors():
    comm = sqlite3.connect('books.db')
    c = comm.cursor()

    c.execute ("""CREATE TABLE IF NOT EXISTS authors
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
        )
        """)
    comm.commit()
    comm.close()

def create_table_books():
    comm = sqlite3.connect('books.db')
    c = comm.cursor()
    c.execute ("""CREATE TABLE IF NOT EXISTS books
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        year INTEGER,
        author_id INTEGER,
        FOREIGN KEY (author_id) REFERENCES author(id)
        )
        """)
    comm.commit()
    comm.close()


def add_book(title, year):
    comm = sqlite3.connect('books.db')
    c = comm.cursor()
    author_name = input("Enter Author's name: ")
    c.execute("INSERT OR IGNORE INTO authors (name) VALUES (?)", (author_name,))

    # Get the author's ID
    c.execute("SELECT id FROM authors WHERE name = ?", (author_name,))
    author_id = c.fetchone()[0]

    c.execute("INSERT INTO books (title, year, author_id) VALUES (?, ?, ?)", (title, year, author_id),)
    comm.commit()
    comm.close()

def list_books():
    comm = sqlite3.connect('books.db')
    c = comm.cursor()
    c.execute("""SELECT books.title, authors.name, books.year
                FROM books
                JOIN authors ON books.author_id = authors.id
            """)

    items = c.fetchall()

    if len(items) < 1:
        print("No books yet")

    else:
        for item in items:
            print(format_book (item[0], item[1], item[2]))
            #print(item)

    comm.commit()
    comm.close()


def find_book():
    comm = sqlite3.connect('books.db')
    c = comm.cursor()

    author_name = input("Enter Author Name: ")
    c.execute(
        """ SELECT books.title, authors.name, books.year
                FROM books
                JOIN authors ON books.author_id = authors.id
                WHERE authors.name = (?) """,
                (author_name,)
    )
    
    items = c.fetchall()

    if len(items) < 1:
        print("Book not found!")
    else:
        for item in items:
            print(format_book(item[0], item[1], item[2]))
        #print(item)

    comm.commit()
    comm.close()


def delete_book(title):
    comm = sqlite3.connect('books.db')
    c = comm.cursor()

    c.execute("SELECT title FROM books WHERE title = (?)", (title,))

    items = c.fetchall()

    if len(items) < 1:
        print("No book found")
    else:
        c.execute("DELETE FROM books WHERE title = (?)", (title,))

        num = c.rowcount
        if num == 1:
            print ("Deleted 1 book")
        elif num > 1:
            print(f"Deleted {num} books")

    comm.commit()
    comm.close()

def format_book(title, author, year):
    if year is None:
        return f"{title} — {author}"
    return f"{title} — {author} ({year})"

def main():
    create_table_authors()
    create_table_books()

    while True:
        print("\n--- Books Menu ---")
        print("1) Add book")
        print("2) List all books (with author name)")
        print("3) Find book by author")
        print("4) Delete book")
        print("5) Quit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            title = input("Enter Book Title: ")
            try:
                year = int(input("Enter Year: "))
            except ValueError:
                print("Non-numeric year detected!")
                year = None


            add_book(title, year)

        elif choice == '2':
            list_books()
        elif choice == '3':
            find_book()
        elif choice == '4':
            title = input("Enter Book Title: ")
            delete_book(title)
        elif choice == '5':
            break

if __name__ == "__main__":
    main()

