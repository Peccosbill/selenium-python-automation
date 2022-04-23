# Crear y escribir
my_file = open('data.txt', 'w+')
my_file.write('Pablo\nAna\nJorge\nNatalia')
my_file.close()


# Leer
def read_file(filename):
    my_file = open(filename, 'r')
    print(my_file.read())
    my_file.close()


# Añadir algo al final del archivo
my_file = open('data.txt', 'a')  # append
my_file.write('\nAldo\nRomina\nFernando')
my_file.close()

read_file('data.txt')

my_file = open('data.txt', 'r')
names = my_file.readlines()
for name in names:
    print(name)
my_file.close()
