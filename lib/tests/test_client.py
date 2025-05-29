from models.client import Client

def test_list_clients():
    clients = Client.all()
    for client in clients:
        print(client)

if __name__ == "__main__":
    test_list_clients()
from models.client import Client

def test_add_and_fetch_clients():
    client = Client(name="Bob", age=25)
    client.save()
    print(f"Added client: {client}")
    clients = Client.all()
    print("All clients:")
    for c in clients:
        print(c)

if __name__ == "__main__":
    test_add_and_fetch_clients()
