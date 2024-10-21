import re

def validar_cartao(numero_cartao):
    """
    Valida um número de cartão e descobre o tipo de cartão e o CVV.
    
    Args:
        numero_cartao (str): Número do cartão.
    
    Returns:
        dict: Dicionário com informações sobre o cartão.
    """
    
    # Remover espaços e hífen do número do cartão
    numero_cartao = re.sub(r'\D', '', numero_cartao)
    
    # Verificar se o número do cartão é válido (16 dígitos)
    if len(numero_cartao) != 16:
        return {"erro": "Número do cartão inválido"}
    
    # Descobrir o tipo de cartão
    tipo_cartao = ""
    if numero_cartao.startswith(("34", "37")):
        tipo_cartao = "American Express"
    elif numero_cartao.startswith(("60", "64", "65")):
        tipo_cartao = "Discover"
    elif numero_cartao.startswith(("5018", "5020", "5038", "6304")):
        tipo_cartao = "Maestro"
    elif numero_cartao.startswith(("51", "52", "53", "54", "55")):
        tipo_cartao = "Mastercard"
    elif numero_cartao.startswith(("4",)):
        tipo_cartao = "Visa"
    
    # Verificar se o CVV é válido (3 ou 4 dígitos)
    cvv = input("Digite o CVV: ")
    if len(cvv) not in (3, 4):
        return {"erro": "CVV inválido"}
    
    # Retornar informações sobre o cartão
    return {
        "tipo_cartao": tipo_cartao,
        "numero_cartao": numero_cartao,
        "cvv": cvv
    }

# Exemplo de uso
numero_cartao = input("Digite o número do cartão: ")
resultado = validar_cartao(numero_cartao)
print(resultado)
