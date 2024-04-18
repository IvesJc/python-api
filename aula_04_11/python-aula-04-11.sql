create table alunos (alunis_id number generated always as identity primary key,
                    alunos_rm number,
                    alunos_nome varchar(50),
                    alunos_curso varchar(30),
                    alunos_idade number);
                    
create table clientes (clie_id number generated always as identity primary key,
                        clie_nome varchar(50),
                        clie_logra varchar(70),
                        clie_bairro varchar(40),
                        clie_cidade varchar(50),
                        clie_idade number,
                        clie_limit_cred number);

