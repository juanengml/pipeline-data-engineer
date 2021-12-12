# ⚙️ Infraestrutura Dockerizada 

# Ambiente 

Requisitos

- 🐳 Docker instalado


## Montando infra 
``` bash
$ virtualenv env --python=python3

$ source env/bin/activate  

(env) $ pip install -r requirements.txt 

(env) $ python src/infra.py 

```
## Configurando Banco de dados e Orquestrador 

#### Subindo banco de dados no Portainer (MySQL)

![](https://juanengml-github.s3.amazonaws.com/UP+DATABASE+PORTAINER.gif)  

#### Configurar Acesso do MySQL no Metabase 

![](https://juanengml-github.s3.amazonaws.com/Configure+Metabase.gif)


## Fonte - Ferramentas Utilizadas 

### Portainer CE (orquestração de microserviços) 

![Portainer](https://media-exp1.licdn.com/dms/image/C5112AQFrlut0AkEykw/article-inline_image-shrink_1000_1488/0/1541068458082?e=1642032000&v=beta&t=qQnplESdqvDpNccgiCBFI6ueUU8Zq4PPfiaWKxkBMXM)

Fonte: https://docs.portainer.io/v/ce-2.9/start/install/server/docker/linux


### Metabase (orquestração de banco)

Ferramenta para monitoramento de dados.

![Metabase](https://www.metabase.com/images/posts/metabase-0.40/editing-dashboard.gif)

Fonte: https://www.metabase.com/




---
