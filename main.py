from customtkinter import CTk, set_appearance_mode, CTkLabel, CTkEntry, CTkButton
import functions as fnc
# import tkinter

texto_area_retorno = ""
cor_retorno = "white"

# TRATAMENTO DA SAÍDA
def Tratamento():
    inp = CPF_input.get()
    CPF_filtrado = fnc.limpar(inp)
    resultado = fnc.verificar(CPF_filtrado)
    
    if resultado == "[ERRO] O CPF digitado não possuí 11 digitos!":
        area_retorno.configure(text=resultado, text_color="red")

    elif resultado == "[ERRO] O CPF digitado possuí digitos repetidos!":
        area_retorno.configure(text=resultado, text_color="red")
        
    elif resultado == "O CPF é INVÁLIDO":
        area_retorno.configure(text=resultado, text_color="yellow")

    elif resultado == "O CPF é VÁLIDO!":
        area_retorno.configure(text=resultado, text_color="green")



# CONFIG DA JANELA
window = CTk()
window.title("Vereficador de CPF")
window.geometry("350x200")
set_appearance_mode("dark")


# Titulo principal da pagina
lbl_titulo = CTkLabel(window, text="Fica fácil vereficar o CPF!", font=("Arial", 15))
lbl_titulo.pack(pady=15)

# Texto acima da caixa de entrada
lbl_texto1 = CTkLabel(window, text="Após enviar o CPF, clique em vereficar", font=("Arial", 13))
lbl_texto1.pack()

# Caixa de entrada
CPF_input = lbl_input = CTkEntry(window, placeholder_text="Digite CPF", font=("Arial", 10))
CPF_input.pack(pady=2, padx=120)

# Área de saída (erros e mensagens da validação)
area_retorno = CTkLabel(window, text=texto_area_retorno, font=("Arial", 14), text_color=cor_retorno)
area_retorno.pack()

# Botão para chamar a função "vereficar CPF"
botão_vereficar = CTkButton(window, text="Vereficar", command=Tratamento)
botão_vereficar.pack()

window.mainloop()