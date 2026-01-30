# Implementação de Exemplo - ExternalLoggerNode

Esta é uma estrutura de exemplo demonstrando como implementar o novo nó `ExternalLoggerNode` conforme o plano técnico retornado pela ferramenta `get_architecture_plan`.

## Estrutura

```
example_implementation/
├── src/
│   ├── domain/
│   │   └── nodes/
│   │       └── ExternalLoggerNode.ts  (Novo arquivo criado)
│   └── infra/
│       └── mappers/
│           └── NodeDataMapper.ts     (Modificado para registrar o novo nó)
└── README.md
```

## Implementação

### 1. ExternalLoggerNode.ts
- Implementa a interface `ActionNode`
- Possui método `execute()` que recebe uma mensagem e a loga
- Possui método `getName()` que retorna o nome do nó

### 2. NodeDataMapper.ts
- Registra o novo nó `ExternalLoggerNode` no mapeador
- Inicializa automaticamente os nós ao carregar o módulo
- Fornece métodos para acessar e gerenciar os nós

## Como usar

```typescript
import { NodeDataMapper } from './src/infra/mappers/NodeDataMapper';

// Obter o nó ExternalLoggerNode
const loggerNode = NodeDataMapper.getNode('ExternalLoggerNode');

if (loggerNode) {
  // Executar o nó com uma mensagem
  await loggerNode.execute('Mensagem de teste');
}
```

## Nota

Esta é uma estrutura de exemplo. Para aplicar no código real do microserviço 'Cenário', você deve:
1. Localizar o diretório do projeto
2. Copiar/adaptar os arquivos conforme a estrutura real do projeto
3. Ajustar os imports e interfaces conforme necessário



