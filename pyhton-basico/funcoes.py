#funções
#estruturas que possibilitam a separação da programação em blocos
# sintaxe: 
# def nome_da_função (parametros):
#          <instruções>
#       return "valor do retorno"

def mensagem1():
  print("Hello world")
  return mensagem1

texto = mensagem1()
print(texto)