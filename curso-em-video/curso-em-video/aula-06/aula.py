valor = input("Digite algo: ")

print(valor)
print(type(valor))

print("Só espaços?", valor.isspace())
print("É número?", valor.isnumeric())
print("É alfabético?", valor.isalpha())
print("É alfanumérico?", valor.isalnum())
print("Maiúsculo?", valor.isupper())
print("Minúsculo?", valor.islower())
print("Capitalizado?", valor.istitle())