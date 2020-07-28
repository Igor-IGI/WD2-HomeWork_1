from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("Chinook_Sqlite.sqlite")

#  Print names of artist in Artist table.
db.pretty_print("SELECT ArtistId, Name FROM Artist")

#  Print all data from table Invoice where BillCountry is Germany.
db.pretty_print("""
    SELECT * FROM Invoice
    WHERE BillingCountry = "Germany"
""")

# Print the number of albums in the table.
db.pretty_print("""
    SELECT COUNT(Title)
    FROM Album
""")

# Print the number of customers from France.
db.pretty_print("""
    SELECT COUNT(Country)
    FROM Customer
    WHERE Country ="France"
""")
