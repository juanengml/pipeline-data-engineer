from os import listdir
from datetime import  datetime as dt 
import pandas as pd 
from console_logging.console import Console
import dataset
from Enriquecimento_UF import Logs


console = Console()


db = dataset.connect('mysql://root:mysql@192.168.15.66:58631/mydatabase')

bases = listdir("base_gerada")

table = db['tlb_users_prod']

etapa = "Etapa 2 - Data Load"

console_log = Logs(etapa)


def main():  
  
  console_log.info("Carregando dados para Database")
  for csv in bases:
    if csv.split(".")[0].isnumeric() != False:
        inicio = dt.now()   
    
        print("base_gerada/"+csv)
        
        path = "base_gerada/"+csv
    
        console.info("INICIO PROCESSO INGESTÃO")
        inicio = dt.now()
        
        df = pd.read_csv(path)
        df.fillna(0,inplace=True)
        for row in df.values.tolist():
            row = [str(item) for item in row]
            table.insert(dict(timezone=str(row[0]),
                              no_accents=str(row[1]),
                              macroregion=str(row[2]),
                              uf_code=str(row[3]),
                              document=str(row[4]),
                              name=str(row[5]),
                              job=str(row[6]),
                              jobArea=str(row[7]),
                              jobType=str(row[8]),
                              phoneNumber=str(row[9]),
                              birthDate=str(row[10]),
                              city=str(row[11]),
                              totalSpent=str(row[12]),
                              pessoa=str(row[13]),
                              ano=str(row[14]),
                              datahora= str(dt.now()).split(".")[0]))

        console.success("FIM PROCESSO")
        console.log("Tempo Exec: "+str(dt.now() - inicio))
        del df   
        console.info("Tempo de Execução: " + str(dt.now()-inicio))
        
  console_log.info("Fim do processo")
    
      
      
if __name__ == "__main__":
    main()