import re
from time import sleep 

import docker
from console_logging.console import Console


client = docker.from_env()

console = Console()


def create_portainer():
   console.log("....UP PORTAINER....")    

   console.info("CREATE VOLUME portainer_data_01")

   volume = client.volumes.create(name='portainer_data_01')
   
   console.info("----UP PORTAINER----")

   portainer = client.containers.run("portainer/portainer-ce", 
                         name="portainer",
                         ports={"8000/tcp":8000,"9000/tcp":9000},
                         restart_policy={"Name": "always"},
                         volumes=['/var/run/docker.sock:/var/run/docker.sock','portainer_data_01:/data'],            
                         detach=True)
    
   sleep(5)

   console.info(portainer.logs())
    
def create_metabase():
   console.log("....UP METABASE....")    

   metabase = client.containers.run("metabase/metabase", 
                         name="metabase",
                         ports={"3000/tcp":3000},
                         detach=True)
    
   console.info(metabase.attrs['Config']['Image'])
    
def create_elyra():
   console.log("....UP ELYRA....") 

   elyra = client.containers.run("elyra/elyra:dev", 
                         user="root",
                         environment=["GRANT_SUDO=yes"],
                         command="jupyter lab --debug --allow-root",
                         name="elyra",
                         ports={"8888/tcp":8888},
                         detach=True)

   sleep(5)

def endpoint_elyra():
    containers_list = client.containers.list()
    result = ""
    for pod in containers_list:
        if pod.attrs['Config']['Image'] == "elyra/elyra:dev":
            log = str(pod.logs())
            fim = re.search(r"http://127.0.0.1:8888/lab?",log).end()
            pos = re.search(r"http://127.0.0.1:8888/lab?",log).start()
            result = "http://0.0.0.0:8888/lab"+log[fim:fim+54]

    return result

def main():
    create_portainer()
    create_metabase()
    
    create_elyra()
    console.info("PORTAINER ENDPOINT - http://0.0.0.0:9000/")
    console.info("ELYRA ENDPOINT - "+ endpoint_elyra())
    console.info("METABASE ENDPOINT - http://0.0.0.0:3000/")
    console.success("....INFRA UP....")

if __name__ == "__main__":
    main()
    
    
