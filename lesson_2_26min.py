#value: int | str | float = input('Введите что-нибудь: ')
#print(f'type - {type(value)}, адрес - {id(value)}, хеш - {hash(value)}')

#help("hello world!")
#help(selp()
#help()


text = input('text:')
if text.isdigit():
    print(bin(int(text)))
    print(oct(int(text)))
    print(hex(int(text)))
elif text.isascii():
    print("Text ASCII")
