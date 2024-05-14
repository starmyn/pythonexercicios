print("Cálculode Grandezas Elétricas")
print("1-Tensão")
print("2-Resistência")
print("3-Corrente")
resposta=input("Fale qual das tês grandezas voce quer?")
if resposta=="1":
    Resistência=float(input("Informe o valor da sua Resistência "))
    Corrente=float(input("Informe o valor da sua Corrente "))
    Resultado=Resistência*Corrente
    print(f"A sua resposta é {Resultado} v ")
elif resposta=="2":
    Tensão=float(input("Informe o valor da sua Tensão " ohm))
    Corrente=float(input("Informe o valor da sua Corrente "))
    Resultado=Tensão/Corrente
    print(f"A sua resposta é  {Resultado} ")
elif resposta=="3":
    Tensão=float(input("Informe o valor da sua Tensão " ampér))
    Resistência=float(input("Informe o valor da sua Resistência "))
    Resultado=Tensão/Resistência
    print(f"A sua resposta é {Resultado} ")
else:
    print("Por favor informe um número válido")