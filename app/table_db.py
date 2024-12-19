from config import engine
from models import Base

# Create all tables in the database
Base.metadata.create_all(engine)
print("Database tables created successfully!")

