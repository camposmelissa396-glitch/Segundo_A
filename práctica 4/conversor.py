print("Bienvenido al conversor de millas a kilometros")

print("Escribe un numero de millas:")
millas = input()#string

print("Tipo de datos de millas", type(millas))
#Convertir su atring a numero
millas = float(millas)
print("Tipo de datos de millas", type(millas))

# 1 millas = 1.609 kms
kilometros = millas * 1.609

print("Millas ingresadas:",millas)
print("Kilometros:", kilometros)
