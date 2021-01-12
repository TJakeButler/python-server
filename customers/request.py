CUSTOMERS = [
    {
      "email": "jake@gmail.com",
      "password": "pw",
      "name": "Jake B",
      "id": 1
    },
    {
      "email": "Randy@gmail.com",
      "password": "pw",
      "name": "Randy  Travis",
      "id": 2
    }
]


def get_all_customers():
    return CUSTOMERS

    # Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found animal, if it exists
    requested_customer = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer