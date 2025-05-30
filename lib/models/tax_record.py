import sqlite3

from models.client import Client
from models.tax_calculator import calculate_tax

class TaxRecord:
    DB_PATH = "tax_calc.db"

    def __init__(self, client: Client, income, id=None):
        if not isinstance(client, Client):
            raise TypeError("client must be a Client instance.")
        self.client = client
        self.income = income
        self.id = id

    def __repr__(self):
        return (
            f"<TaxRecord id={self.id}, client={self.client.name}, "
            f"income={self.income}, tax={self.tax}>"
        )

    @property
    def income(self):
        return self._income

    @income.setter
    def income(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Income must be a number.")
        if value < 0:
            raise ValueError("Income cannot be negative.")
        self._income = float(value)

    @property
    def tax(self):
        return calculate_tax(self._income)

    @property
    def client_id(self):
        return self.client.id

    @classmethod
    def create_table(cls):
        with sqlite3.connect(cls.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tax_records (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    client_id INTEGER NOT NULL,
                    income REAL NOT NULL,
                    tax REAL NOT NULL,
                    FOREIGN KEY(client_id) REFERENCES clients(id)
                )
            ''')
            conn.commit()

    def save(self):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO tax_records (client_id, income, tax) VALUES (?, ?, ?)",
                (self.client_id, self.income, self.tax)
            )
            conn.commit()
            self.id = cursor.lastrowid

    @classmethod
    def all(cls):
        cls.create_table()
        with sqlite3.connect(cls.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, client_id, income, tax FROM tax_records")
            rows = cursor.fetchall()

        records = []
        for row in rows:
            client = Client.get_by_id(row[1])
            if client:
                record = cls(client, income=row[2], id=row[0])
                records.append(record)
        return records
