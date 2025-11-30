-- Cria o banco
CREATE DATABASE acoesdb;

\connect acoesdb;

-- Cria a tabela de ações
CREATE TABLE IF NOT EXISTS acoes (
    id SERIAL PRIMARY KEY,
    ticker VARCHAR(10) NOT NULL,
    empresa VARCHAR(100) NOT NULL,
    preco NUMERIC(10,2) NOT NULL
);

-- Insere algumas ações brasileiras
INSERT INTO acoes (ticker, empresa, preco) VALUES
('VALE3', 'Vale S.A.', 68.50),
('KLBN4', 'Klabin S.A.', 3.60),
('BBAS3', 'Banco do Brasil S.A.', 22.75);