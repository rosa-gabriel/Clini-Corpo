# Sistema de Gerenciamento de Estoque

Este projeto é um sistema de gerenciamento de estoque simples que utiliza uma estrutura de árvore binária para armazenar produtos e gerenciar suas quantidades. O sistema permite adicionar produtos, verificar estoques, processar pedidos, comprar produtos e exibir o estoque atual. Quando um produto atinge um nível crítico de estoque, o sistema automaticamente faz um pedido de reposição.

## Funcionalidades

- **Adicionar Produto**: Permite que o usuário adicione novos produtos ao estoque, especificando nome, quantidade e tempo de reposição.
- **Verificar Estoque**: O usuário pode verificar a quantidade disponível de um produto. Se a quantidade estiver abaixo do nível crítico, um pedido de reposição é automaticamente gerado.
- **Processar Pedido**: Permite que o usuário processe um pedido para um produto, aumentando sua quantidade no estoque.
- **Comprar Produto**: Os usuários podem comprar produtos, reduzindo a quantidade disponível.
- **Exibir Estoque**: Exibe a lista atual de produtos no estoque com suas quantidades e tempos de reposição.

# Estrutura do Código

## Classes Principais

- **Product**: Representa um produto, contendo atributos como nome, quantidade e tempo de reposição.
- **BinaryTree**: Implementa uma árvore binária para armazenar produtos, permitindo inserções, buscas e exibições em ordem.
- **InventoryManagementSystem**: Gerencia as operações do sistema, incluindo a adição de produtos, verificação de estoque, processamento de pedidos, compras e pedidos de reposição automáticos.

# Como Usar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/clini-corpo.git
```

2. Navegue até o diretório do projeto:

```bash
cd clini-corpo
```
3. Execute o script:

```bash
python main.py
```

Siga as instruções na tela para interagir com o sistema.
