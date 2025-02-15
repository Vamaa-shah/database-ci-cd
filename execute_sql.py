import mysql.connector

# Database connection details
config = {
    'user': 'vamashah',
    'password': 'Secret55',
    'host': 'vshah3026-dbserver.mysql.database.azure.com',
    'database': 'mydb'
}

try:
    # Establish connection
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # Read and execute SQL file
    with open("schema_changes.sql", "r") as file:
        sql_script = file.read()
        
        # Execute the entire script at once
        for statement in sql_script.split(";"):
            if statement.strip():  # Ensure the statement is not empty
                cursor.execute(statement)

    # Commit changes
    connection.commit()
    print("✅ Database schema updated successfully.")

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")

finally:
    # Close the cursor and connection safely
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
