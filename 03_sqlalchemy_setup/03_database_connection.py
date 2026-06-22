from sqlalchemy import create_engine

engine = create_engine("sqlite:///students.db")

# Open a database connection
with engine.connect() as connection:
    print("Database connected successfully.")

print("Connection closed.")