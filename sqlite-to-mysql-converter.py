import re

def convert_sqlite_to_mysql(sqlite_sql):
    """Convert SQLite SQL syntax to MySQL syntax."""
    # Convert SQLite SQL to MySQL SQL
    mysql_sql = (sqlite_sql
                 .replace("AUTOINCREMENT", "AUTO_INCREMENT")
                 .replace("INTEGER", "INT")
                 .replace("TEXT", "VARCHAR(255)")
                 .replace(r"PRAGMA.+?;", "")  # Remove PRAGMA statements
                 .replace("WITHOUT ROWID", "")  # Remove WITHOUT ROWID
                 .replace('"', '`')  # Change double quotes to backticks
                 .replace("DEFAULT CURRENT_TIMESTAMP", "CURRENT_TIMESTAMP")
                 .replace(" IF NOT EXISTS ", " ")  # Remove IF NOT EXISTS
                 .replace(";  ;", ";"))  # Clean up duplicate semicolons

    # Remove BEGIN TRANSACTION; and COMMIT; statements
    mysql_sql = re.sub(r'^\s*BEGIN TRANSACTION;\s*$', '', mysql_sql, flags=re.MULTILINE)
    mysql_sql = re.sub(r'^\s*COMMIT;\s*$', '', mysql_sql, flags=re.MULTILINE)

    return mysql_sql.strip()

def process_sql_file():
    """Read the SQLite SQL file and convert it to MySQL SQL."""
    # Input and output file paths
    input_filepath = 'sqlite.sql'  # Input SQLite file
    output_filepath = 'mysql.sql'  # Output MySQL file

    # Read the SQLite SQL from the input file
    with open(input_filepath, 'r', encoding='utf-8') as file:
        sqlite_sql = file.read()
        mysql_sql = convert_sqlite_to_mysql(sqlite_sql)

        # Save the converted SQL to the output file
        with open(output_filepath, 'w', encoding='utf-8') as output_file:
            output_file.write(mysql_sql.strip())  # Write the final SQL to the output file

    print("Converted MySQL SQL saved successfully to 'mysql.sql'.")

# Run the SQL processing function
process_sql_file()
