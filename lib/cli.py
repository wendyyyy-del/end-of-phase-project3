from models.client import Client
from models.tax_record import TaxRecord

def main():
    print("Welcome to the Tax Calculator CLI!")
    
    while True:
        print("\nChoose an option:")
        print("1. Add a new client")
        print("2. Add a tax record")
        print("3. View all clients")
        print("4. View all tax records")
        print("5. Exit")
        
        choice = input("Enter choice: ").strip()
        
        if choice == "1":
            name = input("Client name: ").strip()
            age_input = input("Client age (must be 18 or older): ").strip()
            try:
                age = int(age_input)
                if age < 18:
                    print("Client must be at least 18 years old.")
                    continue
                client = Client(name=name, age=age)
                client.save()
                print(f"Added client: {client}")
            except ValueError:
                print("Invalid age input, please enter a valid integer.")
        
        elif choice == "2":
            clients = Client.all()
            if not clients:
                print("No clients found. Please add a client first.")
                continue
            
            print("Clients:")
            for c in clients:
                print(f"{c.id}. {c.name} (Age: {c.age})")
            
            client_id_input = input("Enter client ID for tax record: ").strip()
            income_input = input("Enter income amount: ").strip()
            
            try:
                client_id = int(client_id_input)
                income = float(income_input)
                
                client = Client.get_by_id(client_id)
                if not client:
                    print("Client not found.")
                    continue
                
                tax_record = TaxRecord(client=client, income=income)
                tax_record.save()
                print(f"Added tax record: {tax_record}")
                
            except ValueError:
                print("Invalid input for client ID or income.")
        
        elif choice == "3":
            clients = Client.all()
            if not clients:
                print("No clients found.")
            else:
                for client in clients:
                    print(client)
        
        elif choice == "4":
            records = TaxRecord.all()
            if not records:
                print("No tax records found.")
            else:
                for record in records:
                    print(record)
        
        elif choice == "5":
            print("Exiting. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()
