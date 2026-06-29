from langchain_community.utilities import SQLDatabase

hospital_db = SQLDatabase.from_uri(
    "sqlite:///database/hospitals.db"
)

institution_db = SQLDatabase.from_uri(
    "sqlite:///database/institutions.db"
)

restaurant_db = SQLDatabase.from_uri(
    "sqlite:///database/restaurants.db"
)

print("✅ All SQLDatabase objects created.")