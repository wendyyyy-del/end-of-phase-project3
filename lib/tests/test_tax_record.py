from models.client import Client
from models.tax_record import TaxRecord

def test_add_and_fetch_tax_records():
    client = Client(name="Alice", age=30)
    client.save()
    print(f"Added client: {client}")

    tax_record = TaxRecord(client=client, income=50000)
    tax_record.save()
    print(f"Added tax record: {tax_record}")

    records = TaxRecord.all()
    print("All tax records:")
    for record in records:
        print(record)

if __name__ == "__main__":
    test_add_and_fetch_tax_records()
