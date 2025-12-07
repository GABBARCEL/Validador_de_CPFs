from functions import *


print("=" * 42)
print("VEREFICADOR DE CPF")
print("=" * 42)


while True:
    try:
        CPF = int(input("Digite o CPF SEM FORMATAÇÃO: "))
    
    except (ValueError):
        print("[ERRO] CPF com caracter não numérico")
        continue

    except Exception as e:
        print(f"[ERRO] {e}")
        continue

    else:
        validacao = vereficar(CPF)
        if validacao:
            print(f"O CPF {CPF}. É Válido!")
            break
        else:
            print(f"O CPF {CPF}. É Inválido!")

        break
            