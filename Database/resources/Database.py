
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def all_query(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM artists")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
def main():

    #Address of the Database
    database = "C:/Users/100592118/Desktop/Send Help/chinook.db"

    conn = create_connection(database)
    with conn:
        print("Querying All tasks")
        all_query(conn)
if __name__ == '__main__' :
    main()