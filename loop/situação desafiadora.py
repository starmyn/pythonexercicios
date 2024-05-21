print("Olá,bem vindo ao smilebank")
tentativa=3
senha=123456
while tentativa>0:
    resposta = int(input("Digite sua senha"))
    if resposta != senha:
        tentativa-=1
        print(f"Sua senha está incorreta, você tem {tentativa} tentativa.")
        if tentativa==0:
            print('Your key is incorrect')
    
    else:
       print(f'Welcome, to your account!!!')
       break

    
