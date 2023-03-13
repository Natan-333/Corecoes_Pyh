tupla = ("São Paulo", "Rio de Janeiro", 105)


print("Rio de Janeiro" in tupla)
print(105 in tupla)
print("Espírito Santo" in tupla)


print(tupla.count("São Paulo"))
print(tupla.count("Espírito Santo"))


tupla_nomes = ('Maria', 'João', 'Paulo', 'Pedro', 'Maria', 'Sérgio')


print(tupla_nomes.index('Maria'))


# Pesquisa a partir do segundo elemento até o quinto elemento (opcional)
print(tupla_nomes.index('Maria', 2, 5))