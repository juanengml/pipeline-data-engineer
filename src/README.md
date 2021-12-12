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

![](https://github.com/juanengml/talent-data-analyst-lv4/raw/main/src/2021-12-12-14-28-21.gif)

## Configurando Banco de dados e Orquestrador 

#### Subindo banco de dados no Portainer (MySQL)





#### Configurar Acesso do MySQL no Metabase 

![](https://github.com/juanengml/talent-data-analyst-lv4/raw/main/src/2021-12-12-14-36-19.gif)




## Fonte - Ferramentas Utilizadas 


| Portainer  | Metabase |  
|----------|-------|
| ![Portainer](https://media-exp1.licdn.com/dms/image/C5112AQFrlut0AkEykw/article-inline_image-shrink_1000_1488/0/1541068458082?e=1642032000&v=beta&t=qQnplESdqvDpNccgiCBFI6ueUU8Zq4PPfiaWKxkBMXM) | ![Metabase](https://www.metabase.com/images/posts/metabase-0.40/editing-dashboard.gif)
  | Fonte: https://docs.portainer.io/v/ce-2.9/start/install/server/docker/linux      | Fonte: https://www.metabase.com/           

