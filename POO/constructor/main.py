from Auto import Auto

auto1 = Auto("Rojo","Ford","Mustang",130,8)
auto2 = Auto("Gris", "BMW", "abc", 100, 4)
auto3 = Auto("Amarillo","Chevrolet","Camaro",140,8)

#auto3.frenar()
auto3.acelerar()

print(auto1.getInfo())
print(auto2.getInfo())
print(auto3.getInfo())

print(auto1)