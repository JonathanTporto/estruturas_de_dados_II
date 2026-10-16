"""Projeto ConectaUDF: redes sociais com grafos."""

##Integrantes: Herik Acioly, Herbert Paulo, Jean Teófilo Porto, Jonathan Teófilo Porto e Kauã Alves.
# ---------------------------------------------------------------
# PARTE 1: rede original (secao 8 do caderno)
# ---------------------------------------------------------------
rede = {
    "Ana": ["Bruno", "Carla"],
    "Bruno": ["Ana", "Carla", "Diego"],
    "Carla": ["Ana", "Bruno", "Elisa"],
    "Diego": ["Bruno", "Elisa", "Felipe"],
    "Elisa": ["Carla", "Diego", "Felipe"],
    "Felipe": ["Diego", "Elisa"],
}


def analisar(rede, titulo):
    """Mostra graus, total de usuarios, arestas e densidade."""
    print(f"=== {titulo} ===")
    n = len(rede)

    for usuario, amigos in rede.items():
        print(usuario, "tem", len(amigos), "conexoes")

    soma_graus = sum(len(amigos) for amigos in rede.values())
    arestas = soma_graus // 2
    densidade = (2 * arestas) / (n * (n - 1))

    print("Total de usuarios:", n)
    print("Total de amizades:", arestas)
    print(f"Densidade: {densidade:.2%}")

    maior_grau = max(len(a) for a in rede.values())
    mais_conectados = [u for u, a in rede.items() if len(a) == maior_grau]
    print("Mais conexoes:", ", ".join(mais_conectados), f"(grau {maior_grau})")
    print()
    return densidade


densidade_antes = analisar(rede, "Rede original")


# ---------------------------------------------------------------
# PARTE 2: desafio em grupo (secao 10)
# ---------------------------------------------------------------
def adicionar_amizade(rede, a, b):
    """Cria a amizade nos dois sentidos (grafo nao direcionado)."""
    rede.setdefault(a, [])
    rede.setdefault(b, [])
    if b not in rede[a]:
        rede[a].append(b)
    if a not in rede[b]:
        rede[b].append(a)


# Novos usuarios ficticios: Gabi, Hugo, Iris e Joao
novas_amizades = [
    ("Felipe", "Gabi"),
    ("Gabi", "Hugo"),
    ("Hugo", "Iris"),
    ("Iris", "Joao"),
    ("Ana", "Joao"),
    ("Carla", "Hugo"),
]

for a, b in novas_amizades:
    adicionar_amizade(rede, a, b)

densidade_depois = analisar(rede, "Rede ampliada")

print("Comparacao de densidade:")
print(f"  Antes:  {densidade_antes:.2%}")
print(f"  Depois: {densidade_depois:.2%}")
print()


# ---------------------------------------------------------------
# PARTE 3: recomendacao de amizades (amigos em comum)
# ---------------------------------------------------------------
def recomendar(rede, usuario):
    """Sugere usuarios que ainda nao sao amigos, ordenados por
    quantidade de amigos em comum."""
    meus_amigos = set(rede[usuario])
    sugestoes = []

    for outro, amigos in rede.items():
        if outro == usuario or outro in meus_amigos:
            continue
        em_comum = meus_amigos & set(amigos)
        if em_comum:
            sugestoes.append((outro, sorted(em_comum)))

    sugestoes.sort(key=lambda s: len(s[1]), reverse=True)
    return sugestoes


print("Sugestoes de amizade:")
for usuario in rede:
    for outro, em_comum in recomendar(rede, usuario):
        print(f"  {usuario} -> {outro} "
              f"({len(em_comum)} em comum: {', '.join(em_comum)})")


# ---------------------------------------------------------------
# PARTE 4: caminho mais curto entre dois usuarios (busca em largura)
# ---------------------------------------------------------------
def menor_caminho(rede, origem, destino):
    fila = [[origem]]
    visitados = {origem}

    while fila:
        caminho = fila.pop(0)
        atual = caminho[-1]
        if atual == destino:
            return caminho
        for vizinho in rede[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(caminho + [vizinho])
    return None


print()
caminho = menor_caminho(rede, "Ana", "Felipe")
print("Menor caminho Ana -> Felipe:", " -> ".join(caminho))
print("Arestas no caminho:", len(caminho) - 1)
