from bit import Key
import sys

print ('''

██╗░░██╗███████╗██╗░░░██╗░█████╗░░█████╗░███╗░░██╗
██║░██╔╝██╔════╝╚██╗░██╔╝██╔══██╗██╔══██╗████╗░██║
█████═╝░█████╗░░░╚████╔╝░██║░░╚═╝██║░░██║██╔██╗██║
██╔═██╗░██╔══╝░░░░╚██╔╝░░██║░░██╗██║░░██║██║╚████║
██║░╚██╗███████╗░░░██║░░░╚█████╔╝╚█████╔╝██║░╚███║
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░░╚════╝░░╚════╝░╚═╝░░╚══╝

    BTC Private Key Converter written by Codejoe
========================================================    
     \n''')


#grabing file content
file = input('Enter file with .txt: \n')
amount = int(input('No. of keys to convert: '))
# file = 'Results by Codejoe.txt'
with open (file, 'r', encoding='utf-8', errors='ignore') as reader:
    # lines = reader.readlines()
    for keys in reader.readlines():
        private_key = keys.strip('\n').strip()
        prv = Key.from_hex(private_key)

        addr = prv.address
        # print(f'{private_key}:{addr}\n')
        # balance = prv.get_balance('usd')
        count = 0
        count += 1
        # writing files locally
        with open ('Results by Codejoe.txt', 'a') as writer:
            writer.write(f'{private_key}:{addr}\n')
        if count == amount:
                writer.close()
                sys.exit()

print(count)

    
