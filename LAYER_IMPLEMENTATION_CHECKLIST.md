# Conversion Service - Checklist por Camada

Use este guia sempre que for adicionar uma nova funcionalidade no serviço.

## 1. Domain (`domain/`)

### O que lembrar
- Colocar aqui apenas regra de negócio e invariantes.
- Entidades e value objects não devem depender de FastAPI, DB, cache, fila ou libs de infraestrutura.
- Estados/transições devem ser validados dentro da entidade.

### Checklist
- [ ] A regra é de negócio (não é detalhe técnico)?
- [ ] A entidade/value object impede estado inválido?
- [ ] Não há import de `infrastructure`, `api` ou libs de framework?

### Erros comuns
- Colocar acesso a banco dentro da entidade.
- Resolver erro HTTP diretamente no domínio.

## 2. Application (`application/`)

### O que lembrar
- Use case orquestra fluxo; não implementa detalhe de infra.
- Use case depende de **ports/interfaces** em `application/ports`.
- DTO/mappers da application fazem fronteira entre domínio e camadas externas.

### Checklist
- [ ] Use case recebe dependências por interface (ports)?
- [ ] Nenhum import de implementação concreta de `infrastructure`?
- [ ] Retorno do use case está em DTO ou tipo estável para API?
- [ ] Regras de domínio ficaram no `domain`, não no use case?

### Erros comuns
- Importar `Repository` concreto diretamente no use case.
- Misturar validação de negócio com validação de transporte HTTP.

## 3. API (`api/`)

### O que lembrar
- API só traduz HTTP <-> application.
- Request/response devem ser explícitos (evitar `dict` genérico).
- Tratamento de erro deve mapear exceções para status code correto.

### Checklist
- [ ] Schema de entrada e saída está explícito?
- [ ] Endpoint só chama use case e mapeia resposta?
- [ ] Erros de domínio/aplicação viram respostas HTTP adequadas?
- [ ] Endpoint não conhece detalhe de banco, cache ou fila?

### Erros comuns
- Colocar regra de negócio na rota.
- Retornar exceção bruta no JSON.

## 4. Infrastructure (`infrastructure/`)

### O que lembrar
- Implementa ports definidos em `application/ports`.
- Converte dados externos (DB row, provider response) para tipos internos.
- Não deve empurrar detalhes de infra para dentro da application.

### Checklist
- [ ] Adapter implementa a interface correta do `application/ports`?
- [ ] SQL/SDK/provider ficou isolado no adapter?
- [ ] Mapper de infra converte corretamente para entidade/VO/DTO esperado?
- [ ] Erros de infra são tratados/traduzidos de forma consistente?

### Erros comuns
- Retornar formato cru do banco para use case.
- Colocar dependência circular entre infraestrutura e application/use case.

## 5. Container / Composition Root (`container.py`, `lifespan.py`)

### O que lembrar
- O container é o único lugar para montar implementações concretas.
- Todos os use cases devem ser criados com dependências completas.
- Ordem de startup/shutdown importa.

### Checklist
- [ ] Recursos são inicializados antes de construir use cases que dependem deles?
- [ ] Todo construtor de use case recebeu todos os parâmetros exigidos?
- [ ] Não existe uso de atributo ainda não inicializado?

### Erros comuns
- Construir use case com dependência faltando (ex.: `storage`).
- Criar use case antes do `bus`/db/cache estar pronto.

## 6. Regra de Dependência (resumo rápido)

- `domain` -> não depende de ninguém.
- `application` -> depende de `domain` e de `application/ports`.
- `infrastructure` -> depende de `application/ports` e `domain`.
- `api` -> depende de `application` (use cases + DTOs/schemas).
- `container` -> depende de todas para fazer wiring.

Se quebrar essa direção, a arquitetura começa a degradar.

