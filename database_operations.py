import mysql.connector
from mysql.connector import Error

# Establish a connection to the database
db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Sqm22104",
    database="cid"
)
class db_ops:
    def __init__(self, db):
        self.db_connection = db  

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.db_connection.close()

    def create(self, table, *args, **kwargs):
        try:
            with self.db_connection.cursor() as cursor:
                columns = ', '.join(kwargs.keys())
                values = ', '.join(['%s'] * len(kwargs))
                query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
                cursor.execute(query, tuple(kwargs.values()))
                self.db_connection.commit()
            return True, f"{table.capitalize()} record created successfully."
        except Error as e:
            return False, f"Error creating {table} record: {e}"
    def read(self, table, record_id):
     try:
        cursor = self.db_connection.cursor()
        query = f"SELECT * FROM {table} WHERE {table}_id = %s"
        cursor.execute(query, (record_id,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return True, result
        else:
            return False, f"{table.capitalize()} not found."
     except Error as e:
        return False, f"Error reading {table} record: {e}"



    def read_all(self, table):
      try:
        cursor = self.db_connection.cursor()
        query = f"SELECT * FROM {table}"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return True, result
      except Error as e:
        return False, f"Error reading {table} records: {e}"



    def update(self, table, record_id, **kwargs):
        try:
            cursor = self.db_connection.cursor()
            columns = ', '.join([f"{key} = %s" for key in kwargs.keys()])
            query = f"UPDATE {table} SET {columns} WHERE {table}_id = %s"
            values = list(kwargs.values())
            values.append(record_id)
            cursor.execute(query, tuple(values))
            self.db_connection.commit()
            cursor.close()
            return True, f"{table.capitalize()} record updated successfully."
        except Error as e:
            return False, f"Error updating {table} record: {e}"

    def delete(self, table, record_id):
        try:
            cursor = self.db_connection.cursor()
            query = f"DELETE FROM {table} WHERE {table}_id = %s"
            cursor.execute(query, (record_id,))
            self.db_connection.commit()
            cursor.close()
            return True, f"{table.capitalize()} record deleted successfully."
        except Error as e:
            return False, f"Error deleting {table} record: {e}"
# Base class for database operations
class DatabaseModel:
    @staticmethod
   
    def load_from_database(db_ops, table, record_id=None):
       if record_id:
           success, result = db_ops.read(table, record_id)
           if success:
            return result
           else:
            print(f"Error loading {table.capitalize()} record:", result)
            return None
       else:
        success, result = db_ops.read_all(table)
        if success:
            return result
        else:
            print(f"Error loading {table.capitalize()} records:", result)
            return None


    def save_to_database(self, db_ops, table, **kwargs):
        data = {
            "table_id": getattr(self, f"{table}_id"),
            **kwargs
        }
        success, message = db_ops.create(table.capitalize(), **data)
        if success:
            print(message)
        else:
            print(f"Error saving {table.capitalize()} record:", message)

    def update_in_database(self, db_ops, table, **kwargs):
        data = {
            **kwargs
        }
        success, message = db_ops.update(table.capitalize(), f"{table}_id", getattr(self, f"{table}_id"), **data)
        if success:
            print(message)
        else:
            print(f"Error updating {table.capitalize()} record:", message)

    def delete_from_database(self, db_ops, table):
        success, message = db_ops.delete(table.capitalize(), f"{table}_id", getattr(self, f"{table}_id"))
        if success:
            print(message)
        else:
            print(f"Error deleting {table.capitalize()} record:", message)
