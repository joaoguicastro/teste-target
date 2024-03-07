#primeiro desafio
indice = 13
soma = 0
k = 0
while k < indice:
    k = k + 1
    soma = soma + k
print(soma)

#segundo desafio
n = 10

sequencia_fibonacci = [0, 1]

while len(sequencia_fibonacci) < n:
    sequencia_fibonacci.append(sequencia_fibonacci[-1] + sequencia_fibonacci[-2])

print(sequencia_fibonacci)

#terceiro desafio
sequencia_a = [1,3,5,7]
prox_a = sequencia_a[-1] + 2

sequencia_b = [2,4,8,16,32,64]
prox_b = sequencia_b[-1] * 2

sequencia_c = [0,1,4,9,16,25,36]
prox_c = len(sequencia_c)**2

sequencia_d = [4,16,36,64]
prox_d = ((len(sequencia_d) + 1) * 2) ** 2

sequencia_e = [1,1,2,3,5,8]
prox_e = sequencia_e[-1] + sequencia_e[-2]

sequencia_f = [2,10,12,16,17,18,19]
prox_f = sequencia_f[-1] + 1

print("Proximos Elementos:")
print(f"a) {prox_a}")
print(f"a) {prox_b}")
print(f"a) {prox_c}")
print(f"a) {prox_d}")
print(f"a) {prox_e}")
print(f"a) {prox_f}")

#quarto desafio

interruptores = [0,0,0]

interruptores[0] = -1

interruptores[1] = 1

print("Após verificar as lampadas:")
for i, estado in enumerate(interruptores):
    if estado == -1:
        print(f"Interruptores {i + 1} esta conectado a lampada quente (ligada a mais tempo)")
    elif estado == 1:
        print(f"Interruptores {i + 1} esta conectado a lampada nao quente (ligada a menos tempo)")
    else:
        print(f"Interruptores {i + 1} esta desconectado da lampada")

#quinto desafio
def inverter_string(s):
    string_invertida = ""
    for caracteres in s:
        string_invertida = caracteres + string_invertida
    return string_invertida

string_original = "exemplo"
string_invertida = inverter_string(string_original)
print(string_invertida)