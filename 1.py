import argparse
import secrets
import random
import string
parser = argparse.ArgumentParser(
    prog = 'Password Generation',
    )
parser.add_argument('-c','--count', 
                    type=int, 
                    help="Количество паролей",
                    choices=range(1,11),
                    required=False
                    )
parser.add_argument('-s','--size',
                    type=int, 
                    choices=range(5,11),
                    help="Длинна пароля",
                    required=False
                    )
parser.add_argument('-a','--alphabet',  
                    choices=['ascii_lowercase', 'ascii_uppercase', 'digits'], 
                    help="Алфавит для составления пароля",
                    required=False
                    )
args = parser.parse_args()

if args.alphabet == None and args.count == None and args.size == None:
    print("Please, enter -h for look help")
    exit(1)

if args.alphabet == "ascii_lowercase":
    alpha = string.ascii_lowercase
elif args.alphabet == "ascii_uppercase":
    alpha = string.ascii_uppercase
elif args.alphabet == "digits":
    alpha = string.digits

class Password:
    def __init__(self,alphabet, pas_size = 10, count = 1):
        self.pas_size = pas_size
        self.alphabet = alphabet
        self.count = count
    def new_pass(self):
        all_pass = []
        for k in range(self.count):
            result = []
            for i in range(self.pas_size):
                rand = (secrets.randbelow(len(self.alphabet)))
                result.append((self.alphabet)[rand])
            random.shuffle(result)
            body = ''.join(result)
            all_pass.append(body)  
        return all_pass

print(*Password(alphabet=alpha, count=args.count, pas_size=args.size).new_pass(), sep='\n')