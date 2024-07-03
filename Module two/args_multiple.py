def full_name(first,last,**krgs):
    name = f'{first} {last}'
    for val in args:
        print(val)
    for key, value in krgs.items():
        print(key , value);
name = full_name(last='alu',first='kodu',truth_s='man is mortal',fauls='man is kamla')
print(name)