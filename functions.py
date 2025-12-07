def vereficar(CPF):
    # VEREFICAÇÃO NA CONTAGEM
    if len(str(CPF)) != 11:
        return False

    else:
        # VEREFICAÇÃO NA IGUALDADE
        diferente = False
        for d in str(CPF):
            if d != str(CPF)[0]:
                diferente = True
                break
        if diferente == False:
            return False

        #CALCULOS MALDITOS
        Os_nines = str(CPF)[0:9]
        results_dv1 = []
        peso = 10
        for n in Os_nines:
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
        Os_ten = str(CPF)[0:10]
        results_dv2 = []
        peso = 11
        
        for n in Os_ten:
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

    if d2_vereficador == int(str(CPF)[10]) and d1_vereficador == int(str(CPF)[9]):
        return True
    else:
        return False
