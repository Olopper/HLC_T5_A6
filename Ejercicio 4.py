def es_palindromo(n):
    if len(n) <= 1:
        return True
    if n[0] == n[-1]:
        return es_palindromo(n[1:-1])
    return False

entrada = "reconocer"
print(es_palindromo(entrada))