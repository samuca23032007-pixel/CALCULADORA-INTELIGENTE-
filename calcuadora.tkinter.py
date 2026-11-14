import tkinter as tk
from tkinter import messagebox

# ---------- Cores (tema escuro) ----------
BG = "#1e1e2e"
CARD = "#2a2a3d"
TEXTO = "#cdd6f4"
TEXTO_SUAVE = "#9399b2"
CAMPO = "#313244"
DESTAQUE = "#89b4fa"
VERDE = "#a6e3a1"
VERMELHO = "#f38ba8"
AMARELO = "#f9e2af"
ROXO = "#cba6f7"


def calcular(opcao):
    """Lê os dois números, faz o cálculo com match/case e mostra o resultado."""
    try:
        a = float(entrada_a.get().replace(",", "."))
        b = float(entrada_b.get().replace(",", "."))
    except ValueError:
        resultado.set("⚠️ Digite números válidos")
        label_resultado.config(fg=AMARELO)
        return

    match opcao:
        case 1:
            texto = f"➕ Soma: {a + b:g}"
            cor = VERDE
        case 2:
            texto = f"➖ Subtração: {a - b:g}"
            cor = DESTAQUE
        case 3:
            texto = f"✖️ Multiplicação: {a * b:g}"
            cor = ROXO
        case 4:
            if b == 0:
                texto = "❌ Erro: divisão por zero"
                cor = VERMELHO
            else:
                texto = f"➗ Divisão: {a / b:g}"
                cor = AMARELO
        case _:
            texto = "Opção inválida!"
            cor = VERMELHO

    resultado.set(texto)
    label_resultado.config(fg=cor)


def limpar():
    entrada_a.delete(0, tk.END)
    entrada_b.delete(0, tk.END)
    resultado.set("Resultado aparece aqui")
    label_resultado.config(fg=TEXTO_SUAVE)
    entrada_a.focus()


def sair():
    if messagebox.askyesno("Sair", "Saindo do sistema...\nDeseja realmente sair?"):
        janela.destroy()


def criar_botao(pai, texto, cor, comando):
    botao = tk.Button(
        pai,
        text=texto,
        command=comando,
        bg=cor,
        fg=BG,
        activebackground=TEXTO,
        activeforeground=BG,
        font=("Segoe UI", 12, "bold"),
        relief="flat",
        bd=0,
        cursor="hand2",
        height=2,
    )
    return botao


# ---------- Janela ----------
janela = tk.Tk()
janela.title("Calculadora Inteligente")
janela.geometry("380x540")
janela.bind("<F11>", lambda e: janela.attributes("-fullscreen", not janela.attributes("-fullscreen")))
janela.bind("<Escape>", lambda e: janela.attributes("-fullscreen", False))
janela.configure(bg=BG)

# Título
tk.Label(
    janela, text="🧮 CALCULADORA", bg=BG, fg=DESTAQUE, font=("Segoe UI", 20, "bold")
).pack(pady=(25, 0))
tk.Label(
    janela, text="INTELIGENTE", bg=BG, fg=TEXTO_SUAVE, font=("Segoe UI", 11, "bold")
).pack(pady=(0, 15))

# Card dos campos
card = tk.Frame(janela, bg=CARD, padx=20, pady=15)
card.pack(padx=25, fill="x")

tk.Label(
    card, text="Primeiro número", bg=CARD, fg=TEXTO_SUAVE, font=("Segoe UI", 10)
).pack(anchor="w")
entrada_a = tk.Entry(
    card,
    bg=CAMPO,
    fg=TEXTO,
    insertbackground=TEXTO,
    relief="flat",
    font=("Segoe UI", 14),
    justify="center",
)
entrada_a.pack(fill="x", ipady=6, pady=(2, 10))

tk.Label(
    card, text="Segundo número", bg=CARD, fg=TEXTO_SUAVE, font=("Segoe UI", 10)
).pack(anchor="w")
entrada_b = tk.Entry(
    card,
    bg=CAMPO,
    fg=TEXTO,
    insertbackground=TEXTO,
    relief="flat",
    font=("Segoe UI", 14),
    justify="center",
)
entrada_b.pack(fill="x", ipady=6, pady=(2, 0))

# Botões das operações (grade 2x2)
grade = tk.Frame(janela, bg=BG)
grade.pack(padx=25, pady=15, fill="x")
grade.columnconfigure((0, 1), weight=1, uniform="col")

criar_botao(grade, "➕ Soma", VERDE, lambda: calcular(1)).grid(
    row=0, column=0, padx=4, pady=4, sticky="ew"
)
criar_botao(grade, "➖ Subtração", DESTAQUE, lambda: calcular(2)).grid(
    row=0, column=1, padx=4, pady=4, sticky="ew"
)
criar_botao(grade, "✖️ Multiplicação", ROXO, lambda: calcular(3)).grid(
    row=1, column=0, padx=4, pady=4, sticky="ew"
)
criar_botao(grade, "➗ Divisão", AMARELO, lambda: calcular(4)).grid(
    row=1, column=1, padx=4, pady=4, sticky="ew"
)

# Resultado
resultado = tk.StringVar(value="Resultado aparece aqui")
caixa_resultado = tk.Frame(janela, bg=CARD, pady=12)
caixa_resultado.pack(padx=25, fill="x")
label_resultado = tk.Label(
    caixa_resultado,
    textvariable=resultado,
    bg=CARD,
    fg=TEXTO_SUAVE,
    font=("Segoe UI", 14, "bold"),
    wraplength=300,
)
label_resultado.pack()

# Limpar e Sair
rodape = tk.Frame(janela, bg=BG)
rodape.pack(padx=25, pady=15, fill="x")
rodape.columnconfigure((0, 1), weight=1, uniform="col")

criar_botao(rodape, "🧹 Limpar", CAMPO, limpar).grid(
    row=0, column=0, padx=4, sticky="ew"
)
criar_botao(rodape, "🚪 Sair", VERMELHO, sair).grid(
    row=0, column=1, padx=4, sticky="ew"
)

# Atalho: Enter não faz nada sozinho, então deixamos o foco no primeiro campo
entrada_a.focus()

janela.mainloop()