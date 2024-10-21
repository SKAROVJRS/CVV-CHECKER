import re

def validar_cartao(numero_cartao):
    """
    Valida um n�mero de cart�o e descobre o tipo de cart�o e o CVV.
    
    Args:
        numero_cartao (str): N�mero do cart�o.
    
    Returns:
        dict: Dicion�rio com informa��es sobre o cart�o.
    """
    
    # Remover espa�os e h�fen do n�mero do cart�o
    numero_cartao = re.sub(r'\D', '', numero_cartao)
    
    # Verificar se o n�mero do cart�o � v�lido (16 d�gitos)
    if len(numero_cartao) != 16:
        return {"erro": "N�mero do cart�o inv�lido"}
    
    # Descobrir o tipo de cart�o
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
    
    # Verificar se o CVV � v�lido (3 ou 4 d�gitos)
    cvv = input("Digite o CVV: ")
    if len(cvv) not in (3, 4):
        return {"erro": "CVV inv�lido"}
    
    # Retornar informa��es sobre o cart�o
    return {
        "tipo_cartao": tipo_cartao,
        "numero_cartao": numero_cartao,
        "cvv": cvv
    }

# Exemplo de uso
numero_cartao = input("Digite o n�mero do cart�o: ")
resultado = validar_cartao(numero_cartao)
print(resultado)
