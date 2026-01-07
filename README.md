# python-threads

Projeto em Python demonstrando o uso de **threads** para execução paralela, sincronização e controle de concorrência utilizando `threading`.

---

## Parte 1 — Execução paralela com herança de `Thread`

Nesta etapa, é criada uma classe que herda de `Thread`.

Cada instância representa uma thread independente, com seu próprio tempo de espera e execução.  
O método `run()` define o comportamento da thread.

Enquanto as threads dormem e executam em paralelo, o loop principal continua rodando normalmente, demonstrando concorrência entre tarefas.

**Conceitos aplicados:**
- Herança da classe `Thread`
- Execução paralela
- Não bloqueio da thread principal

---

## Parte 2 — Threads com função alvo e `join()`

Aqui, as threads são criadas a partir de uma **função**, utilizando o parâmetro `target`.

O método `join()` é utilizado para **bloquear a thread principal** até que a thread especificada finalize sua execução.

Isso garante controle explícito da ordem de execução quando necessário.

**Conceitos aplicados:**
- `Thread(target=...)`
- Passagem de argumentos
- Sincronização com `join()`
- Bloqueio controlado da execução principal

---

## Parte 3 — Concorrência, estado compartilhado e `Lock`

Nesta parte, múltiplas threads acessam e modificam um **recurso compartilhado** (`stock`).

Para evitar condições de corrida, é utilizado um `Lock` (cadeado), garantindo que apenas uma thread execute a operação crítica por vez.

Sem o `Lock`, o valor do estoque poderia se tornar inconsistente.

**Conceitos aplicados:**
- Estado compartilhado
- Condição de corrida
- Exclusão mútua com `Lock`
- Sincronização de acesso a recursos críticos

---

## Tecnologias

- Python
- `threading.Thread`
- `threading.Lock`
