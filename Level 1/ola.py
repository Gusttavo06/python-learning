while True:
    nome = input("qual é o seu nome?");
   
    if nome.strip() !="":
        print(f"ola {nome}");
        break
    else:
        print("digite um nome válido");