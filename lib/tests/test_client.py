import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from models.client import Client

def test_list_clients():
    clients = Client.all()
    for client in clients:
        print(client)

def test_add_and_fetch_clients():
    client = Client(name="Bob", age=25)
    client.save()
    print(f"Added client: {client}")

    test_list_clients()

if __name__ == "__main__":
    test_add_and_fetch_clients()
