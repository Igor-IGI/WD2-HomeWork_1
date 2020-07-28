from smartninja_sql.sqlite import SQLiteDatabase

chinook = SQLiteDatabase("Chinook_sqlite.sqlite")

# Most expensive order from Invoice table.
chinook.pretty_print("""
    SELECT MAX(Total) AS "ExpensiveOrder"
    FROM Invoice
""")

# Most cheapest order from Invoice table.
chinook.pretty_print("""
    SELECT MIN(Total) AS "CheapestOrder"
    FROM Invoice
""")

# Most orders by City from Invoice table.
chinook.pretty_print("""
    SELECT BillingCity, COUNT(*) AS Orders
    FROM Invoice
    GROUP BY BillingCity
    ORDER BY Orders DESC
    LIMIT 10;
""")

# Calculation how many tracks are Protected AAC audio file.
chinook.pretty_print("""
    SELECT MediaTypeID, COUNT(*) AS Tracks
    FROM Track
    WHERE MediaTypeID = 2;
""")

# Improved calculation how many tracks are Protected AAC audio file.
chinook.pretty_print("""
    SELECT MediaType.Name, COUNT(*) AS Tracks
    FROM Track
    JOIN MediaType 
    USING (MediaTypeId)
    WHERE MediaType.Name = 'Protected AAC audio file';
""")

# Artist with the most albums
chinook.pretty_print("""
    SELECT Artist.Name, COUNT(*) AS Albums
    FROM Album
    JOIN Artist ON Album.ArtistId=Artist.ArtistId
    GROUP BY Album.ArtistId
    ORDER BY Albums DESC
    LIMIT 5;
""")

# Genre with the most tracks
chinook.pretty_print("""
    SELECT Genre.Name, COUNT() AS Genre
    FROM Track
    JOIN Genre ON Track.GenreId=Genre.GenreId
    GROUP BY Track.GenreId
    ORDER BY Genre DESC
    LIMIT 10;
""")

# Improved genre with the most tracks
chinook.pretty_print("""
    SELECT Genre.Name, COUNT() AS Genre
    FROM Track
    JOIN Genre 
    USING (GenreId)
    GROUP BY Track.GenreId
    ORDER BY Genre DESC
    LIMIT 5;
""")

# Spent money by customers
chinook.pretty_print("""
    SELECT FirstName, LastName, SUM(Invoice.Total) Total_Price
    FROM Customer
    JOIN Invoice ON Invoice.CustomerId=Customer.CustomerId
    GROUP BY Customer.CustomerId
    ORDER BY Total_Price DESC
    LIMIT 1;
""")

# Song bought by the order(Order ID)
chinook.pretty_print("""
    SELECT Invoice.InvoiceId, Track.Name
    From Track
    JOIN InvoiceLine ON Track.TrackId=InvoiceLine.TrackId
    JOIN Invoice ON InvoiceLine.InvoiceId=Invoice.InvoiceId;
""")
