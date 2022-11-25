import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="dict",
   user="postgres",
   password="Sqlkone"
)

print("Available commands: LIST, ADD, DELETE, QUIT")
# read_dict: returns the list of all dictionary entries:
# argument: C - the database connection.
def read_dict(conn):
    cur = conn.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows

#add_word: add word and translation to the dictionary
def add_word(conn, word, translation):
    cur = conn.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()

#delete_word: deletes a word and translation from the dictionary
def delete_word(conn, ID):
    cur = conn.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()

#save_dict: saved changes to dictionary
def save_dict(conn):
    cur = conn.cursor()
    cur.execute("COMMIT;")
    cur.close()

while True: ## REPL - Read Execute Program Loop
    cmd = input(" Write Command: ")
    if cmd == "list":
        print("The dictionary:")
        for i, wd, trans in read_dict(conn):
            print(f"{i}: {wd} - {trans}")
    elif cmd == "add":
        word = input("  Word: ")
        translation = input("  Translation: ")
        add_word(conn, word, translation)
        print(f"added {word}")
    elif cmd == "delete":
        ID = input("  ID: ")
        delete_word(conn, ID)
        print(f"deleted {id}")
    elif cmd == "quit":
        save_dict(conn)
        exit()

main()




