# Atividade — Aula 03: Ponteiros e Estruturas Dinâmicas em C

## Exercício 1 — Ponteiros

```c
#include <stdio.h>

int main() {
    int idade = 20;

    // p guarda o endereço da idade
    int *p = &idade;

    printf("Idade: %d\n", idade);
    printf("Valor apontado: %d\n", *p);

    return 0;
}
```

### Resposta

O `&` pega o endereço da variável e o `*` mostra o valor que está nesse endereço.

---

## Exercício 2 — Criando uma cadeia de nós

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    char valor;
    struct Node *proximo;
} Node;

int main() {

    // criando os nós
    Node *n1 = malloc(sizeof(Node));
    Node *n2 = malloc(sizeof(Node));
    Node *n3 = malloc(sizeof(Node));

    n1->valor = 'A';
    n2->valor = 'B';
    n3->valor = 'C';

    // ligando os nós
    n1->proximo = n2;
    n2->proximo = n3;
    n3->proximo = NULL;

    Node *atual = n1;

    while (atual != NULL) {
        printf("%c\n", atual->valor);

        // passa para o próximo nó
        atual = atual->proximo;
    }

    free(n1);
    free(n2);
    free(n3);

    return 0;
}
```

### Saída

```text
A
B
C
```

Eu fiz os três nós e depois usei o ponteiro `proximo` para ligar um no outro.

---

## Exercício 3 — Depuração

O problema é que o `atual` não estava mudando.

### Código corrigido

```c
while (atual != NULL) {
    printf("%d\n", atual->valor);

    // vai para o próximo
    atual = atual->proximo;
}
```

### Respostas

**1. Qual é o problema?**

O ponteiro `atual` não estava sendo atualizado.

**2. Por que não termina?**

Porque ele fica sempre no mesmo nó.

**3. Qual linha foi acrescentada?**

```c
atual = atual->proximo;
```

**4. Saída:**

```text
10
20
30
```

---

## Exercício 4 — Lista encadeada

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int valor;
    struct Node *proximo;
} Node;

void adicionar(Node **inicio, int valor) {

    // criando um novo nó
    Node *novo = malloc(sizeof(Node));

    novo->valor = valor;

    // ligando o novo nó
    novo->proximo = *inicio;

    // o novo nó vira o primeiro
    *inicio = novo;
}

void exibir(Node *inicio) {

    Node *atual = inicio;

    while (atual != NULL) {
        printf("%d\n", atual->valor);

        atual = atual->proximo;
    }
}

int main() {

    Node *inicio = NULL;

    adicionar(&inicio, 10);
    adicionar(&inicio, 20);
    adicionar(&inicio, 30);

    exibir(inicio);

    return 0;
}
```

### Saída

```text
30
20
10
```

Como eu adiciono sempre no começo, o último número colocado aparece primeiro.

---

# Exercício 5 — Sistema de atendimento

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Paciente {
    char nome[50];
    int idade;
    char prioridade[20];
} Paciente;

typedef struct Node {
    Paciente paciente;
    struct Node *proximo;
} Node;

typedef struct {
    Node *inicio;
    Node *fim;
    int quantidade;
} Fila;

// inicia a fila
void inicializar(Fila *fila) {
    fila->inicio = NULL;
    fila->fim = NULL;
    fila->quantidade = 0;
}

// verifica se está vazia
int estaVazia(Fila *fila) {
    return fila->inicio == NULL;
}

// adiciona paciente
void adicionar(Fila *fila, Paciente paciente) {

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

    fila->quantidade++;
}

// mostra os pacientes
void listar(Fila *fila) {

    if (estaVazia(fila)) {
        printf("Fila vazia.\n");
        return;
    }

    Node *atual = fila->inicio;

    while (atual != NULL) {
        printf("Nome: %s\n", atual->paciente.nome);
        printf("Idade: %d\n", atual->paciente.idade);
        printf("Prioridade: %s\n", atual->paciente.prioridade);
        printf("------------------\n");

        atual = atual->proximo;
    }
}

// atende o primeiro
void atender(Fila *fila) {

    if (estaVazia(fila)) {
        printf("Nao tem paciente na fila.\n");
        return;
    }

    Node *temp = fila->inicio;

    printf("Atendendo: %s\n", temp->paciente.nome);

    fila->inicio = temp->proximo;

    if (fila->inicio == NULL) {
        fila->fim = NULL;
    }

    fila->quantidade--;

    free(temp);
}

int tamanho(Fila *fila) {
    return fila->quantidade;
}

int main() {

    Fila fila;

    inicializar(&fila);

    Paciente p1 = {"Ana", 32, "Normal"};
    Paciente p2 = {"Bruno", 70, "Prioridade"};
    Paciente p3 = {"Carlos", 45, "Normal"};
    Paciente p4 = {"Daniela", 28, "Normal"};
    Paciente p5 = {"Eduardo", 65, "Prioridade"};

    adicionar(&fila, p1);
    adicionar(&fila, p2);
    adicionar(&fila, p3);
    adicionar(&fila, p4);
    adicionar(&fila, p5);

    printf("Pacientes:\n");
    listar(&fila);

    printf("Quantidade: %d\n", tamanho(&fila));

    atender(&fila);

    printf("\nDepois do atendimento:\n");
    listar(&fila);

    printf("Quantidade: %d\n", tamanho(&fila));

    return 0;
}
```

### O que eu fiz

Criei uma estrutura para o paciente e outra para o nó.

O nó guarda o paciente e um ponteiro para o próximo nó.

A fila tem um `inicio` e um `fim`, para saber onde começa e termina.

---

# Exercício 6 — Prioridade

Para colocar o paciente prioritário na frente, fiz uma função simples:

```c
void adicionarPrioridade(Fila *fila, Paciente paciente) {

    Node *novo = malloc(sizeof(Node));

    novo->paciente = paciente;

    // aponta para quem estava no começo
    novo->proximo = fila->inicio;

    // agora ele é o primeiro
    fila->inicio = novo;

    if (fila->fim == NULL) {
        fila->fim = novo;
    }

    fila->quantidade++;
}
```

Exemplo:

```text
Antes:

Ana → Bruno → NULL

Depois de adicionar Carlos como prioridade:

Carlos → Ana → Bruno → NULL
```

Assim o paciente prioritário será atendido primeiro.

---

# Testes

Eu testei:

- fila vazia;
- um paciente;
- vários pacientes;
- atendimento;
- remoção do paciente;
- paciente prioritário.

### Exemplo

```text
Quantidade: 5

Atendendo: Ana

Quantidade: 4
```

---

# Erro que encontrei

Um erro que encontrei foi esquecer de passar para o próximo nó.

Eu tinha feito assim:

```c
while (atual != NULL) {
    printf("%d\n", atual->valor);
}
```

O programa ficava repetindo o mesmo valor.

Depois coloquei:

```c
atual = atual->proximo;
```

Aí funcionou normalmente.

---

# Reflexão final

### O que é um ponteiro em C?

É uma variável que guarda o endereço de outra variável.

### Por que uma lista encadeada usa ponteiros?

Porque os ponteiros servem para ligar um nó ao outro.

### Qual a diferença entre uma variável e um ponteiro?

A variável guarda um valor e o ponteiro guarda um endereço.

### Qual erro encontrei?

Esqueci de atualizar o `atual`, então o programa ficava em loop.

### Como os ponteiros ajudam?

Eles ajudam a ligar os elementos da estrutura, formando listas e filas.

---

# Conclusão

Eu entendi que os ponteiros são importantes para trabalhar com estruturas dinâmicas em C.

Também entendi como criar nós e ligar eles usando ponteiros.

A parte que achei mais importante foi aprender que preciso cuidar da memória usando `malloc()` e `free()`.
