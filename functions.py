def limpar(CPF):
    CPF_limpo = ""
    for i in str(CPF):
        if i.isdigit():
            CPF_limpo += i
    return CPF_limpo
def verificar(CPF):
    # VEREFICAÇÃO NA CONTAGEM
    if len(CPF) != 11:
        print(f"Não passou no teste de quantidade de caracteres, {len( CPF)} digitos") # Teste e controle
        saida = "[ERRO] O CPF digitado não possuí 11 digitos!"
        return saida

    else:
        print("Passou no teste de quantidade de caracteres") # Teste e controle
        # VEREFICAÇÃO NA IGUALDADE
        diferente = False
        for d in CPF:
            if d !=  CPF[0]:
                print("Passou no teste de igualdade") # Teste e controle
                diferente = True
                break

        if diferente == False:
            print("Não passou no teste de igualdade") # Teste e controle
            saida = "[ERRO] O CPF digitado possuí digitos repetidos!"
            return saida
            

        #CALCULOS MALDITOS
        calculo_dv1 =  CPF[0:9]
        results_dv1 = []
        peso = 10
        for n in calculo_dv1:
            local_result = int(n) * peso
            results_dv1.append(local_result)
            peso -= 1
        results_dv1 = sum(results_dv1)
        results_dv1 *= 10
        results_dv1 %= 11

        if results_dv1 == 10:
            d1_vereficador = 0
        
        else:
            d1_vereficador = results_dv1

        #MAIS CALCULOS PARA ME DEIXAR MALUKO!!!!
        calculo_dv2 =  CPF[0:10]
        results_dv2 = []
        peso = 11
        
        for n in calculo_dv2:
            local_result = int(n) * peso
            results_dv2.append(local_result)
            peso -= 1
        results_dv2 = sum(results_dv2)
        results_dv2 *= 10
        results_dv2 %= 11

        if results_dv2 == 10:
            d2_vereficador = 0
        
        else:
            d2_vereficador = results_dv2

    if d2_vereficador == int( CPF[10]) and d1_vereficador == int( CPF[9]):
        print("válido") # Teste e controle
        saida = "O CPF é VÁLIDO!"
        return saida
    else:
        print("inválido") # Teste e controle
        saida = "O CPF é INVÁLIDO"
        return saida