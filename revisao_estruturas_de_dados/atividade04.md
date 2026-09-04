# Atividade 04 — Desafios de Fundamentos

## Exercício 1 — O Simulador "Desfazer"

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    char acao[50];
    struct Node *proximo;
} Node;

// adiciona uma ação na pilha
void adicionar(Node **topo, char acao[]) {
    Node *novo = malloc(sizeof(Node));

    strcpy(novo->acao, acao);
    novo->proximo = *topo;
    *topo = novo;
}

// desfaz a última ação
void desfazer(Node **topo) {
    if (*topo == NULL) {
        printf("Nao tem acao para desfazer.\n");
        return;
    }

    Node *temp = *topo;

    printf("Desfazendo: %s\n", temp->acao);

    *topo = temp->proximo;
    free(temp);
}

void mostrar(Node *topo) {
    while (topo != NULL) {
        printf("- %s\n", topo->acao);
        topo = topo->proximo;
    }
}

int main() {
    Node *topo = NULL;

    adicionar(&topo, "Digitar");
    adicionar(&topo, "Apagar");
    adicionar(&topo, "Substituir");

    printf("Acoes:\n");
    mostrar(topo);

    desfazer(&topo);

    printf("\nDepois de desfazer:\n");
    mostrar(topo);

    return 0;
}
```

### Resultado

```text
Acoes:
- Substituir
- Apagar
- Digitar

Desfazendo: Substituir

Depois de desfazer:
- Apagar
- Digitar
```

### Resposta

Eu usei uma pilha porque a última ação que entrou é a primeira que precisa ser desfeita.

---

## Exercício 2 — Sistema de Impressão

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    char documento[50];
    struct Node *proximo;
} Node;

typedef struct {
    Node *inicio;
    Node *fim;
} Fila;

// inicia a fila
void inicializar(Fila *fila) {
    fila->inicio = NULL;
    fila->fim = NULL;
}

// coloca o documento no final
void adicionar(Fila *fila, char documento[]) {
    Node *novo = malloc(sizeof(Node));

    strcpy(novo->documento, documento);
    novo->proximo = NULL;

    if (fila->inicio == NULL) {
        fila->inicio = novo;
        fila->fim = novo;
    } else {
        fila->fim->proximo = novo;
        fila->fim = novo;
    }
}

// imprime o primeiro documento
void imprimir(Fila *fila) {
    if (fila->inicio == NULL) {
        printf("Fila vazia.\n");
        return;
    }

    Node *temp = fila->inicio;

    printf("Imprimindo: %s\n", temp->documento);

    fila->inicio = temp->proximo;

    if (fila->inicio == NULL) {
        fila->fim = NULL;
    }

    free(temp);
}

void mostrar(Fila *fila) {
    Node *atual = fila->inicio;

    while (atual != NULL) {
        printf("- %s\n", atual->documento);
        atual = atual->proximo;
    }
}

int main() {
    Fila fila;

    inicializar(&fila);

    adicionar(&fila, "Trabalho.pdf");
    adicionar(&fila, "Relatorio.pdf");
    adicionar(&fila, "Atividade.pdf");

    printf("Documentos:\n");
    mostrar(&fila);

    imprimir(&fila);

    printf("\nDepois da impressao:\n");
    mostrar(&fila);

    return 0;
}
```

### Resultado

```text
Documentos:
- Trabalho.pdf
- Relatorio.pdf
- Atividade.pdf

Imprimindo: Trabalho.pdf

Depois da impressao:
- Relatorio.pdf
- Atividade.pdf
```

### Resposta

Eu usei uma fila porque o documento mais antigo deve ser o primeiro a ser impresso.

---

# Desafio Master — Triagem Hospitalar

### Regras

- Paciente normal entra no final da fila.
- Paciente prioritário entra no começo da fila.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Paciente {
    char nome[50];
    int idade;
    char tipo[20];
} Paciente;

typedef struct Node {
    Paciente paciente;
    struct Node *proximo;
} Node;

typedef struct {
    Node *inicio;
    Node *fim;
} Fila;

// começa a fila vazia
void inicializar(Fila *fila) {
    fila->inicio = NULL;
    fila->fim = NULL;
}

// adiciona paciente normal no final
void adicionarNormal(Fila *fila, Paciente paciente) {
    Node *novo = malloc(sizeof(Node));

    novo->paciente = paciente;
    novo->proximo = NULL;

    if (fila->inicio == NULL) {
        fila->inicio = novo;
        fila->fim = novo;
    } else {
        fila->fim->proximo = novo;
        fila->fim = novo;
    }
}

// adiciona paciente prioritário no começo
void adicionarPrioridade(Fila *fila, Paciente paciente) {
    Node *novo = malloc(sizeof(Node));

    novo->paciente = paciente;

    // aponta para quem estava no começo
    novo->proximo = fila->inicio;

    // agora ele fica no começo
    fila->inicio = novo;

    if (fila->fim == NULL) {
        fila->fim = novo;
    }
}

// mostra a fila
void mostrar(Fila *fila) {
    Node *atual = fila->inicio;

    printf("\nFila de atendimento:\n");

    while (atual != NULL) {
        printf("Nome: %s\n", atual->paciente.nome);
        printf("Idade: %d\n", atual->paciente.idade);
        printf("Tipo: %s\n", atual->paciente.tipo);
        printf("------------------\n");

        atual = atual->proximo;
    }
}

// atende o primeiro paciente
void atender(Fila *fila) {
    if (fila->inicio == NULL) {
        printf("Fila vazia.\n");
        return;
    }

    Node *temp = fila->inicio;

    printf("\nAtendendo: %s\n", temp->paciente.nome);

    fila->inicio = temp->proximo;

    if (fila->inicio == NULL) {
        fila->fim = NULL;
    }

    free(temp);
}

int main() {
    Fila fila;

    inicializar(&fila);

    Paciente ana = {"Ana", 30, "Normal"};
    Paciente bruno = {"Bruno", 40, "Normal"};
    Paciente carlos = {"Carlos", 70, "Prioridade"};
    Paciente daniel = {"Daniel", 25, "Normal"};

    // normais entram no final
    adicionarNormal(&fila, ana);
    adicionarNormal(&fila, bruno);

    // prioridade entra no começo
    adicionarPrioridade(&fila, carlos);

    adicionarNormal(&fila, daniel);

    mostrar(&fila);

    atender(&fila);

    printf("\nDepois do atendimento:");
    mostrar(&fila);

    return 0;
}
```

### Resultado

```text
Fila de atendimento:

Nome: Carlos
Idade: 70
Tipo: Prioridade
------------------
Nome: Ana
Idade: 30
Tipo: Normal
------------------
Nome: Bruno
Idade: 40
Tipo: Normal
------------------
Nome: Daniel
Idade: 25
Tipo: Normal
------------------

Atendendo: Carlos
```

### Explicação

Eu fiz os pacientes normais entrarem no final da fila.

O paciente prioritário entra no começo porque precisa ser atendido primeiro.

A fila fica:

```text
Carlos → Ana → Bruno → Daniel → NULL
```

Depois que Carlos é atendido:

```text
Ana → Bruno → Daniel → NULL
```

---

# Conclusão

Eu entendi que a pilha funciona de um jeito que o último elemento colocado é o primeiro a sair.

A fila funciona na ordem em que os elementos entram.

No desafio do hospital, eu fiz uma exceção para os pacientes prioritários, colocando eles no começo da fila.

Também usei ponteiros para ligar os nós e `malloc()` para criar espaço na memória.
