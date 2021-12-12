# Arquitetura de dados (End to End)

![](https://github.com/juanengml/talent-data-analyst-lv4/raw/main/src/Arquitetura%20de%20Dados.png)

## Requisitos 

PS: Siga o passo a passo no linka abaixo

* LINK - https://github.com/juanengml/talent-data-analyst-lv4/blob/main/src/README.md

  
## Rodar Pipeline
  - Clocar Repo 

#### ✔️ Rodar pipeline Etapa 1

![](https://github.com/juanengml/talent-data-analyst-lv4/raw/main/Etapa%201/2021-12-11-23-43-07.gif)
  
#### Resultados Etapa 1 (perguntas)
![](https://github.com/juanengml/talent-data-analyst-lv4/raw/main/Etapa%201/Resultados%20Etapa%201.PNG)


#### ✔️ Rodar pipeline Etapa 2
![](https://github.com/juanengml/talent-data-analyst-lv4/raw/main/Etapa%202/Etapa%202%20-%20Running.gif)


#### Resultados Etapa 2 (perguntas)
![](https://github.com/juanengml/talent-data-analyst-lv4/raw/main/Etapa%202/Resultado%20Etapa%202.gif)

``` sql 
- --Qual é o valor de gasto médio por estado (`state`)?
select uf_code, avg(totalSpent) from tlb_users_prod group by uf_code order by  uf_code desc;

--- Qual é o valor de gasto médio por `jobArea`?
select jobArea, avg(totalSpent) from tlb_users_prod group by jobArea ;,

---Qual é a PF que gastou menos (`totalSpent`)?
select name,document,pessoa,totalSpent from tlb_users_prod where pessoa = 'FISICA' order by totalSpent asc limit 1;

--- Quantos nomes e documentos repetidos existem nesse dataset?
SELECT  name, document, COUNT(*) FROM    tlb_users_prod GROUP BY     name, document HAVING      COUNT(*) > 1

---Quantas linhas existem nesse dataset?
select count(*) from tlb_users_prod

```
--- 


# Fontes 

Docker: https://www.docker.com/

Portainer: https://www.portainer.io/

Elyra: https://github.com/elyra-ai/elyra

Metabase: https://www.metabase.com/




---

# Quem é a ST IT?

Uma empresa que utiliza o que há de mais recente em termos de tecnologia de desenvolvimento de softwares e ferramentas de gestão de projetos, através de profissionais certificados e com experiência no mercado.

Trabalhamos em parceria com nossos clientes para oferecer todo suporte necessário, cumprindo prazos e resultados que o mundo corporativo exige.

Inovar no negócio, nas estratégias, na tecnologia, nos processos traz resultados, isso é o que a ST IT Data tem realizado juntamente com seus clientes, investir com Inteligência e eficiência.




# Porque trabalhar na ST IT?

Somos uma empresa colaborativa, com equipes multidisciplinares, que trabalham bem em equipe, mas com autonomia, somos um empresa formadora de líderes e que tem foco na gestão de pessoas, não apenas gestão técnica.


# O Desafio

Faça um fork do projeto para um repositório publico do seu Github.

No repositório contém o arquivo DataAnalytics_test.ipynb que contém todas as questões a serem resolvidas, teóricas e práticas, siga todos os passos do arquivo.

Depois de todos os passos do teste realizado envie o link para o contato do RH para que possa ser avaliado (rh@stitcloud.com).



