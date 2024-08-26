import tkinter as tk

# Função para atualizar o valor na tela
def click_button(value):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + value)

# Função para calcular o resultado
def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Função para limpar a tela
def clear_display():
    display.delete(0, tk.END)

# Configuração da janela principal
window = tk.Tk()
window.title("Calculadora")
window.geometry("350x450")
window.configure(bg="#282C34")

# Configuração da tela de exibição
display = tk.Entry(window, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, bg="#ABB2BF", fg="#282C34")
display.grid(row=0, column=0, columnspan=4)

# Lista de botões e suas posições
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Adicionando os botões na janela
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(window, text=text, padx=30, pady=20, font=("Arial", 14), bg="#98C379", fg="white",
                           command=calculate)
    else:
        button = tk.Button(window, text=text, padx=30, pady=20, font=("Arial", 14), bg="#61AFEF", fg="white",
                           command=lambda t=text: click_button(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Botão de limpar
clear_button = tk.Button(window, text="C", padx=30, pady=20, font=("Arial", 14), bg="#E06C75", fg="white",
                         command=clear_display)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Botão de sair
exit_button = tk.Button(window, text="Sair", padx=30, pady=20, font=("Arial", 14), bg="#C678DD", fg="white",
                        command=window.quit)
exit_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

# Inicia a aplicação
window.mainloop()
