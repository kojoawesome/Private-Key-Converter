from bit import Key

#grabing file content
file = "private keys.txt"
with open (file, 'r', encoding='utf-8', errors='ignore') as reader:
    for keys in reader:
        private_key = keys
        prv = Key.from_hex(private_key)

        addr = prv.address
        print(addr)
        # balance = prv.get_balance('usd')
        # writing files locally
        with open ('Results by Codejoe.txt', 'a') as writer:
            writer.write(f'{private_key}:{addr}')
            writer.close()

    
