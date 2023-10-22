######################################################
#################Inductivo###########################
#####################################################
# Encontrar la suma de los primeros n números naturales
def suma_numeros_naturales(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

n = 5
resultado = suma_numeros_naturales(n)
print(f"La suma de los primeros {n} números naturales es {resultado}.")

######################################################
#################Deductivo###########################
#####################################################

# Razonamiento deductivo: Silogismo
# Premisa 1: Todos los hombres son mortales.
# Premisa 2: Sócrates es un hombre.
# Conclusión: Sócrates es mortal.

def razonamiento_deductivo(hombre, socrates):
    premisa1 = "Todos los hombres son mortales."
    premisa2 = "Sócrates es un hombre."

    if hombre and socrates:
        return "Sócrates es mortal."
    else:
        return "No se puede concluir."

print(razonamiento_deductivo(True, True))


######################################################
#################Abductivo###########################
#####################################################

# Razonamiento abductivo: Inferir la causa de un síntoma
def razonamiento_abductivo(sintoma):
    if sintoma == "fiebre" or sintoma == "dolor de garganta":
        return "Podría ser un resfriado."
    elif sintoma == "fiebre" or sintoma == "dolor de cabeza":
        return "Podría ser una gripe."
    else:
        return "No se puede concluir la causa del síntoma."

sintoma = "fiebre"
causa = razonamiento_abductivo(sintoma)
print(f"El síntoma {sintoma} podría deberse a: {causa}")
