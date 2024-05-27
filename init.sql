-- public.alembic_version definition

-- Drop table

-- DROP TABLE public.alembic_version;

CREATE TABLE public.alembic_version (
	version_num varchar(32) NOT NULL,
	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);


-- public.banco definition

-- Drop table

-- DROP TABLE public.banco;

CREATE TABLE public.banco (
	id serial4 NOT NULL,
	nome varchar(50) NULL,
	cnpj varchar(30) NULL,
	CONSTRAINT banco_pkey PRIMARY KEY (id)
);


-- public.cliente definition

-- Drop table

-- DROP TABLE public.cliente;

CREATE TABLE public.cliente (
	id serial4 NOT NULL,
	nome varchar(40) NULL,
	cpfcnpj varchar(50) NOT NULL,
	auth bool NULL,
	CONSTRAINT cliente_cpfcnpj_key UNIQUE (cpfcnpj),
	CONSTRAINT cliente_pkey PRIMARY KEY (id)
);


-- public.tipos definition

-- Drop table

-- DROP TABLE public.tipos;

CREATE TABLE public.tipos (
	id serial4 NOT NULL,
	tipo varchar(50) NULL,
	CONSTRAINT tipos_pkey PRIMARY KEY (id)
);


-- public.leilao definition

-- Drop table

-- DROP TABLE public.leilao;

CREATE TABLE public.leilao (
	id serial4 NOT NULL,
	id_tipo int4 NOT NULL,
	id_banco int4 NOT NULL,
	id_cliente int4 NOT NULL,
	nome varchar(20) NULL,
	data_abertura date NOT NULL,
	data_fechamento date NOT NULL,
	endereco varchar(50) NULL,
	cidade varchar(50) NULL,
	estado varchar(50) NULL,
	link varchar(50) NULL,
	CONSTRAINT leilao_pkey PRIMARY KEY (id),
	CONSTRAINT leilao_banco_fk FOREIGN KEY (id_banco) REFERENCES public.banco(id),
	CONSTRAINT leilao_cliente_fk FOREIGN KEY (id_cliente) REFERENCES public.cliente(id),
	CONSTRAINT leilao_tipos_fk FOREIGN KEY (id_tipo) REFERENCES public.tipos(id)
);


-- public.entidade definition

-- Drop table

-- DROP TABLE public.entidade;

CREATE TABLE public.entidade (
	id serial4 NOT NULL,
	id_tipo int4 NOT NULL,
	id_leilao int4 NOT NULL,
	nome varchar(20) NULL,
	modelo varchar(30) NULL,
	endereco varchar(50) NULL,
	descricao varchar(50) NULL,
	min_lance money NOT NULL,
	min_incremento money NOT NULL,
	CONSTRAINT entidade_pkey PRIMARY KEY (id),
	CONSTRAINT entidade_leilao_fk FOREIGN KEY (id_leilao) REFERENCES public.leilao(id),
	CONSTRAINT entidade_tipos_fk FOREIGN KEY (id_tipo) REFERENCES public.tipos(id)
);


-- public.entidade_cliente definition

-- Drop table

-- DROP TABLE public.entidade_cliente;

CREATE TABLE public.entidade_cliente (
	id_cliente int4 NOT NULL,
	id_entidade int4 NOT NULL,
	lance money NOT NULL,
	data_lance date NULL,
	CONSTRAINT entidade_cliente_cliente_fk FOREIGN KEY (id_cliente) REFERENCES public.cliente(id),
	CONSTRAINT entidade_cliente_entidade_fk FOREIGN KEY (id_entidade) REFERENCES public.entidade(id)
);