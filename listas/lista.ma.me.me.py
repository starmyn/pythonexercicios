nums = []
iteracao = 1
while iteracao<=5:
    num = int(input(f"Digite {iteracao}º numero inteiro: "))
    nums.append(num)
    iteracao+=1

somar_nota = sum (nums)
menor_nota = min (nums)
maior_nota = max (nums)
media_notas = somar_nota / len (nums)
print(nums)
print(f"A soma nota é {somar_nota}.")
print (f"A menor nota é {menor_nota}.")
print (f"A maior nota é {maior_nota}.")
print (f"A média das notas é {media_notas}.")