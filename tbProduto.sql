CREATE TABLE tbProduto (
    codigo int NOT NULL AUTO_INCREMENT,
    descricao varchar(200),
    quantidade int,
    precoVenda float(18, 2),
    PRIMARY KEY(codigo)
);
 
CREATE TABLE tbVenda (
    numero int NOT NULL AUTO_INCREMENT,
    data DATE,
    quantidade int,
    precoVenda float,
    PRIMARY KEY(numero)
);
 
CREATE TABLE tbVendaProduto (
    numeroVenda int NOT NULL,
    codigoProduto int NOT NULL,
    quantidade int,
    precoVenda float(18, 2),
    PRIMARY KEY(numeroVenda, codigoProduto),
    FOREIGN KEY (numeroVenda) REFERENCES tbVenda(numero),
    FOREIGN KEY (codigoProduto) REFERENCES tbProduto(codigo)
);