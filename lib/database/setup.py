from models.client import Client
from models.tax_record import TaxRecord

def setup_database():
    print("Creating tables...")
    Client.create_table()
    TaxRecord.create_table()
    print("Tables created successfully.")

if __name__ == "__main__":
    setup_database()
