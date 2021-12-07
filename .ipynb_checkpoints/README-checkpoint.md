# Ambiente Gerado

Requisitos

- Docker instalado

## Elyra Notebook 

``` bash

$ docker run  -e GRANT_SUDO=yes -it -p 8888:8888 elyra/elyra:dev jupyter lab --debug

```
!["Imagem ilustrativa"](elyra-pipelines.gif)

Fonte: https://github.com/elyra-ai/elyra

## Portainer CE


``` bash

$ docker volume create portainer_data

$ docker run -d -p 8000:8000 -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce

```
![Portainer](https://media-exp1.licdn.com/dms/image/C5112AQFrlut0AkEykw/article-inline_image-shrink_1000_1488/0/1541068458082?e=1642032000&v=beta&t=qQnplESdqvDpNccgiCBFI6ueUU8Zq4PPfiaWKxkBMXM)

Fonte: https://docs.portainer.io/v/ce-2.9/start/install/server/docker/linux


## Arquitetura de dados(Banco + Visualizador)

-> Metabase

``` bash

$ docker run -d -p 3000:3000 --name metabase metabase/metabase

```
-> MySQL


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


