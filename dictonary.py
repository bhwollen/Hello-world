customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
customer["name"] = "jack smith"
print(customer["name"])
print(customer.get("birthdate", "jan 1 1980"))
