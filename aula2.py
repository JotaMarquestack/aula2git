def calcular_preco_final(preco_original, valor_desconto):
    """
    BUG RELATADO: Clientes reclamam que o preço aumenta ao aplicar o cupom.
    """
    if valor_desconto > preco_original:
        return 0

    # ERRO VISÍVEL PARA O REVIEWER: O operador está somando (+) em vez de subtrair (-)
    preco_final = preco_original + valor_desconto
    return preco_final

print("Preço final (esperado 80):", calcular_preco_final(100, 20))