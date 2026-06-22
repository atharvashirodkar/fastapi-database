from sqlalchemy import create_engine

# Engine acts as the entry point to the database

# Create an engine for a SQLite database
engine = create_engine("sqlite:///students.db")


print("Engine created successfully.")
print()


# Display the database URL configured in the engine
print("Database URL:")
print(engine.url) 