import os
import sys
import psycopg2

def list_directory_contents(directory='.'):
    """
    Traverse a directory tree and print the names of all folders and files.

    Args:
        directory (str): The directory to traverse. Defaults to the current directory.
    """
    try:
        for foldername, subfolders, filenames in os.walk(directory):
            print(f'Folder: {foldername}')
            for filename in filenames:
                print(f'  - {filename}')
    except Exception as e:
        print(f"Error: {e}")

def connect_to_postgresql():
    """
    Connect to a PostgreSQL database and fetch data from a sample table.
    """
    try:
        # Update these credentials with your PostgreSQL database details
        connection = psycopg2.connect(
            dbname="baza_projekt",
            user="admin",
            password="admin",
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()

        # Example query: Fetch data from a table
        cursor.execute("SELECT * FROM your_table_name;")
        rows = cursor.fetchall()

        print("\nData from PostgreSQL:")
        for row in rows:
            print(row)

        # Close the connection
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")

if __name__ == "__main__":
    # Allow the user to specify a directory as a command-line argument
    directory = sys.argv[1] if len(sys.argv) > 1 else '.'

    # List directory contents
    list_directory_contents(directory)

    # Connect to PostgreSQL and fetch data
    connect_to_postgresql()