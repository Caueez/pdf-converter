# Conversion Service Architecture TODO

- [ ] **Caso 1 - Composition root consistente**
  - [ ] Corrigir injeção de dependências do `CreateConversionJobUseCase` no container para casar com a assinatura completa (repo de conversão, repo de usuário, cache, bus, storage).
  - [ ] Evitar construir use cases antes de inicializar recursos necessários (ex.: `bus`).

- [ ] **Caso 2 - Dependências da application (inversão de dependência)**
  - [x] Remover imports de classes concretas da infraestrutura em use cases.
  - [x] Definir/usar ports no limite da application (ex.: `application/ports/...`) e injetar adapters concretos apenas no container.
  - [x] Ajustar `GetConversionJobUseCase` para usar interface/port ao invés de repositório concreto.

- [ ] **Caso 3 - Fronteira de portas/adapters padronizada**
  - [ ] Unificar a estratégia de interfaces (repos, storage, cache, bus) em um local arquitetural único e coerente.
  - [ ] Garantir que todos os use cases dependam de ports, não de implementação.

- [ ] **Caso 4 - Container usando adapters corretos**
  - [ ] Instanciar e injetar também o adapter de `storage`.
  - [ ] Garantir que os objetos injetados no container respeitem exatamente os contratos esperados pelos use cases.

- [ ] **Caso 6 - Contrato API -> Application**
  - [ ] Substituir payload genérico (`dict`) por schemas explícitos de request/response.
  - [ ] Centralizar e corrigir o mapper de entrada/saída entre API e DTOs da application.
  - [ ] Revisar tratamento de erros para exceções de domínio/aplicação com respostas HTTP adequadas.

