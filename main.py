import dicionarios as d

def fazPergunta(estado):
  if estado == 0: print(d.textos.get("e0p0"))
  if estado == 1.0: print(d.textos.get("e1p0"))
  if estado == 1.1: print(d.textos.get("e1p1"))
  if estado == 1.2: print(d.textos.get("e1p2"))
  if estado == 1.3: print(d.textos.get("e1p3"))
  if estado == 1.4: print(d.textos.get("e1p4"))
  if estado == 1.5: print(d.textos.get("e1p5"))
  if estado == 1.6: print(d.textos.get("e1p6"))
  if estado == 2.0: print(d.textos.get("e2p0"))
  if estado == 3.0: print(d.textos.get("e3p0"))
  if estado == 3.1: print(d.textos.get("e3p1"))
  
  if estado in (1.3, 1.4, 1.5, 3.0):
    trataResposta(estado, (input()))
  elif estado in (1.6, 2.0, 3.1): pass
  else: trataResposta(estado, int(input()))

def trataResposta(estado, resposta):
  if estado == 0:
    if resposta == 1: fazPergunta(1.0)
    if resposta == 2: fazPergunta(2.0)
    if resposta == 3: fazPergunta(3.0)
  if estado == 1.0: fazPergunta(1.1)
  if estado == 1.1:
    if resposta == 1: fazPergunta(1.2)
    if resposta == 2: print("Até Logo!")
  if estado == 1.2:
    if resposta == 1: fazPergunta(1.3)
    if resposta == 2: print("Até Logo!")
  if estado == 1.3: fazPergunta(1.4)
  if estado == 1.4: fazPergunta(1.5)
  if estado == 1.5: fazPergunta(1.6)
  if estado == 3.0: fazPergunta(3.1)
  if estado == 3.1:
    pass
    
print("Seja bem vindo!\n")
fazPergunta(0)