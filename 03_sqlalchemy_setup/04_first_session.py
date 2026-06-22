from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///students.db")


# Create a session factory
# Configure sessions to use our database engine
Session = sessionmaker(bind=engine)


# Create a database session
session = Session()

print("Session created successfully.")
print(session)

print(type(session))


# Close the session when finished
session.close()

print("Session closed.")