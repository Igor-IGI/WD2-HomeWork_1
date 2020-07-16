from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("Chinook_Sqlite.sqlite")

db.pretty_print("SELECT ArtistId, Name FROM Artist")
