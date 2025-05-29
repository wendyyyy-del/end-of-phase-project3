import sqlite3

class Client:
    def __init__(self, name, age, id=None):
        self.name = name
        self.age = age
        self.id = id  

    def __repr__(self):
        return f"<Client name={self.name}, age={self.age}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        self._name = value.strip()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer.")
        if value < 18:
            raise ValueError("Client must be at least 18 years old.")
        self._age = value

    def save(self):
        with sqlite3.connect("tax_calc.db") as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO clients (name, age) VALUES (?, ?)",
                (self.name, self.age)
            )
            self.id = cursor.lastrowid
            conn.commit()

    @classmethod
    def create_table(cls):
        with sqlite3.connect("tax_calc.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL
                )
            """)
            conn.commit()

    @classmethod
    def get_by_id(cls, client_id):
        with sqlite3.connect("tax_calc.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, age FROM clients WHERE id = ?", (client_id,))
            row = cursor.fetchone()
            if row:
                return cls(name=row[1], age=row[2], id=row[0])
            else:
                return None

    @classmethod
    def all(cls):
        with sqlite3.connect("tax_calc.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, age FROM clients")
            rows = cursor.fetchall()
        clients = []
        for row in rows:
            client = cls(name=row[1], age=row[2], id=row[0])
            clients.append(client)
        return clients