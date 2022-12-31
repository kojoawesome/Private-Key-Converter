from bit import Key

count = 0
#grabing file content
file = 'private-keys.txt'
with open (file, 'r', encoding='utf-8', errors='ignore') as reader:
    for keys in reader.readlines():
        private_key = keys.strip('\n').strip()
        prv = Key.from_hex(private_key)

        addr = prv.address
        print(f'{private_key}:{addr}\n')
        # balance = prv.get_balance('usd')
        # writing files locally
        with open ('Results by Codejoe.txt', 'a') as writer:
            writer.write(f'{private_key}:{addr}\n')
        # count =+ 1
        # if count == 100000:
            writer.close()



    
