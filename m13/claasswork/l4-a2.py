# Connect with sqlite database
# Import necessary libraries
import pandas as pd
import sqlite3

# Database file
database = 'database.sqlite'

# Connect to the database
conn = sqlite3.connect(database)
print("Opened database successfully")

# --------------------------------------------------------------------

# Display all the tables of the database
df = pd.read_sql("""
    SELECT *
    FROM sqlite_master
    WHERE type='table';
""", conn)

print(df)

# --------------------------------------------------------------------

# Display the first five rows of the Player_Match table
player_match = pd.read_sql("""
    SELECT *
    FROM Player_Match
""", conn)

print(player_match.head())

null_player_match = pd.read_sql("""
    SELECT *
    FROM Player_Match
    WHERE Team_Id IS NULL
""", conn)

print(null_player_match)



toss_dec = pd.read_sql("""
    SELECT *
    FROM Match
""", conn)

print(toss_dec.head())



null_match = pd.read_sql("""
    SELECT *
    FROM Match
    WHERE MATCH_Winner IS NULL
""", conn)

print(null_match)