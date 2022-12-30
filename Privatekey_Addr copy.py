from bit import Key

private_key = "e48f9b56af0e3c0cb0f05f34a5b20e1b6c5cd6b0f8a0ceb2dcc6f5e1dbf8c44d"
prv = Key.from_hex(private_key)

addr = prv.address
balance = prv.get_balance('usd')
print(addr)
print(balance)

