def calculate_tax(income):
    """
    Calculates tax based on income.
    Currently a flat 20% tax rate.
    """
    if not isinstance(income, (int, float)):
        raise TypeError("Income must be a number.")
    if income < 0:
        raise ValueError("Income cannot be negative.")

    return round(income * 0.2, 2)
