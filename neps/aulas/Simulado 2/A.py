# Leia os pesos dos cubos da entrada
x = [int(x) for x in input().split()]

# Calcule a soma dos pesos de todos os cubos
total_weight = sum(x)

# Verifique se a soma dos pesos é divisível por 3
if total_weight % 3 != 0:
  # Se não for, é impossível formar uma pirâmide equilibrada
  print("N")
else:
  # Ordene a lista de pesos em ordem crescente
  x.sort()

  # Verifique se o peso do cubo mais pesado é igual a um terço do peso total
  if x[5] != total_weight / 3:
    # Se não for, é impossível formar uma pirâmide equilibrada
    print("N")
  else:
    # Percorra a lista de pesos (excluindo o cubo mais pesado)
    for i in range(5):
      for j in range(i + 1, 5):
        # Encontre dois cubos cujo peso combinado seja igual a um terço do peso total
        if x[i] + x[j] == total_weight / 3:
          # Se tais cubos forem encontrados, é possível formar uma pirâmide equilibrada
          print("S")
          break
      else:
        continue
      break
    else:
      # Se não for encontrada tal par de cubos, é impossível formar uma pirâmide equilibrada
      print("N")

