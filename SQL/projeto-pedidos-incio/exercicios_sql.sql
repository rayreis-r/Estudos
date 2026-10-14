CREATE DATABASE estudos;
USE estudos;

-- CRIANDO TABELAS 
CREATE TABLE Cliente(
id_cliente INT,
nome VARCHAR(40),
email VARCHAR(40),
telefone VARCHAR (40),
data_cadastro DATE,
CONSTRAINT pk_cliente PRIMARY KEY (id_cliente)
);

CREATE TABLE Produto (
id_produto INT,
nome_produto VARCHAR(50),
categoria VARCHAR(50),
preco DOUBLE(15,2),
CONSTRAINT fk_produto PRIMARY KEY (id_produto)
);

CREATE TABLE Pedido (
id_pedido INT,
fk_cliente INT,
data_pedido DATE,
valor_total DOUBLE(15,2),
status VARCHAR(40),
CONSTRAINT fk_pedido PRIMARY KEY (id_pedido),
CONSTRAINT fk_cliente FOREIGN KEY (fk_cliente) REFERENCES Cliente (id_cliente)
);

CREATE TABLE ItensPedido(
id_item INT,
fk_pedido INT,
fk_produto INT,
quantidade INT,
preco_unitario DOUBLE(15,2),
CONSTRAINT pk_item PRIMARY KEY (id_item),
CONSTRAINT fk_pedido FOREIGN KEY (fk_pedido) REFERENCES Pedido(id_pedido),
CONSTRAINT fk_produto FOREIGN KEY (fk_produto) REFERENCES Produto(id_produto)
);

-- 1. INSERINDO CLIENTES
INSERT INTO Cliente (id_cliente, nome, email, telefone, data_cadastro) VALUES
(1, 'Ana Silva', 'ana.silva@email.com', '(11) 98765-4321', '2025-01-15'),
(2, 'Bruno Costa', 'bruno.costa@email.com', '(21) 97654-3210', '2025-02-01'),
(3, 'Carla Souza', 'carla.souza@email.com', '(31) 96543-2109', '2025-02-10'),
(4, 'Diego Oliveira', 'diego.oliveira@email.com', '(41) 95432-1098', '2025-03-05');

-- 2. INSERINDO PRODUTOS
INSERT INTO Produto (id_produto, nome_produto, categoria, preco) VALUES
(1, 'Smartphone Galaxy', 'Eletrônicos', 1999.90),
(2, 'Notebook Dell', 'Informática', 3500.00),
(3, 'Cadeira Ergonômica', 'Móveis', 850.50),
(4, 'Teclado Mecânico', 'Informática', 250.00),
(5, 'Mouse Sem Fio', 'Informática', 99.90);

-- 3. INSERINDO PEDIDOS
INSERT INTO Pedido (id_pedido, fk_cliente, data_pedido, valor_total, status) VALUES
(1, 1, '2025-03-10', 2099.80, 'Concluído'),
(2, 2, '2025-03-12', 3500.00, 'Processando'),
(3, 1, '2025-03-15', 850.50, 'Concluído'),
(4, 3, '2025-03-18', 349.90, 'Cancelado');

-- 4. INSERINDO ITENS DO PEDIDO
INSERT INTO ItensPedido (id_item, fk_pedido, fk_produto, quantidade, preco_unitario) VALUES
-- Itens do Pedido 1 (Ana Silva: Smartphone + Mouse)
(1, 1, 1, 1, 1999.90),
(2, 1, 5, 1, 99.90),

-- Itens do Pedido 2 (Bruno Costa: Notebook)
(3, 2, 2, 1, 3500.00),

-- Itens do Pedido 3 (Ana Silva: Cadeira)
(4, 3, 3, 1, 850.50),

-- Itens do Pedido 4 (Carla Souza: Teclado + Mouse)
(5, 4, 4, 1, 250.00),
(6, 4, 5, 1, 99.90);

SELECT * FROM Cliente;
SELECT * FROM Produto;
SELECT * FROM Pedido;
SELECT * FROM ItensPedido;

-- COMEÇANDO OS DESAFIOS
-- Seleção de Colunas: Liste o nome e o email de todos os clientes cadastrados
SELECT nome, email FROM estudos.Cliente;

-- Filtro de Texto: Encontre todos os clientes que moram na cidade de "São Paulo"
-- ADICIONANDO NOVO CAMPO A TABELA CLIENTE CHAMADO 'CIDADE' 
ALTER TABLE Cliente ADD COLUMN cidade VARCHAR(45);

-- ATUALIZANDO REGISTROS
UPDATE Cliente SET cidade = 'São Paulo' where id_cliente = 1;
UPDATE Cliente SET cidade = 'Floripa' WHERE id_cliente = 2;
UPDATE Cliente SET cidade = 'Ceará' WHERE id_cliente = 3;
UPDATE Cliente SET cidade = 'São Paulo' WHERE id_cliente = 4;

-- QUERY PARA SELECIONAR OS CLIENTES QUE MORAM EM SP
SELECT * FROM Cliente WHERE cidade = 'São Paulo';

-- Busca por Padrão (LIKE): Selecione todos os produtos cujo nome comece com a palavra "Smartphone".
SELECT * FROM Produto WHERE nome_produto like 'Smartphone%';

-- Filtro numérico e Ordenação: Liste os produtos com preço maior que R$ 500,00, ordenados do mais caro para o mais barato.
SELECT * FROM Produto where preco > 500.00 order by preco desc;

-- Busca por Faixa (BETWEEN): Retorne os pedidos realizados entre '2025-03-10' e '2025-03-15'
SELECT * FROM Pedido WHERE data_pedido BETWEEN '2025-03-10' and '2025-03-15';

-- Remoção de Duplicatas: Exiba uma lista com todas as categorias de produtos únicas cadastradas, sem repetições.
SELECT DISTINCT categoria FROM Produto;

-- Contagem Simples: Quantos clientes estão cadastrados no banco de dados?
SELECT COUNT(id_cliente) FROM Cliente;

-- Soma e Média: Qual é o valor total arrecadado em vendas e qual é o ticket médio (média do valor_total) dos pedidos?
SELECT SUM(valor_total) as valor_total, AVG(valor_total) as ticket_médio FROM Pedido;

-- Agrupamento (GROUP BY): Exiba a quantidade total de produtos em estoque agrupada por categoria.
SELECT count(id_produto) as qtd_produto, categoria as categoria FROM Produto GROUP BY categoria;

-- Contagem com Agrupamento: Mostre o total de pedidos realizados por cada status (ex: Pendente, Enviado, Cancelado).
SELECT count(id_pedido) as total_pedido, status FROM Pedido GROUP BY status;

-- Filtro pós-agrupamento (HAVING): Identifique as cidades que possuem mais de 1 clientes cadastrados.
SELECT cidade as cidade, count(id_cliente) as total_cliente FROM Cliente group by cidade HAVING COUNT(id_cliente) > 1;


-- RELACIONAMENTOS - JOINS 
-- Inner Join: Liste o id_pedido, data_pedido, nome do cliente e o valor_total de todos os pedidos.
SELECT p.id_pedido, p.data_pedido, c.nome, p.valor_total
FROM Pedido p INNER JOIN Cliente c
ON c.id_cliente = p.fk_cliente;

-- Left Join: Liste todos os clientes cadastrados e, caso tenham efetuado algum pedido, mostre o id_pedido. Inclua também os clientes que nunca compraram nada.
SELECT c.nome, p.id_pedido FROM Cliente c LEFT JOIN Pedido p
ON c.id_cliente = p.fk_cliente;

-- Join com Múltiplas Tabelas: Exiba o id_pedido, o nome do cliente e o nome_produto de todos os itens comprados no pedido #101
SELECT pedido.id_pedido, c.nome, produto.nome_produto FROM Cliente c 
JOIN Pedido pedido 
ON c.id_cliente = pedido.fk_cliente
JOIN ItensPedido ip 
ON ip.fk_pedido = pedido.id_pedido
JOIN Produto produto 
ON ip.fk_produto = produto.id_produto; 

-- Agregação com Join: Calcule o total gasto em compras por cada cliente, exibindo o nome do cliente e o total_gasto.
