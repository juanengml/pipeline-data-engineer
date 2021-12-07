import pandas as pd 
import numpy as np
from datetime import datetime as dt 

class DataQuality(object):
    
    def __init__(self,df,ufs):
        self.df = pd.read_csv(df)
        self.ufs = pd.read_csv(ufs)
       
    def load_bases(self):
        return self.df,self.ufs 

    def rename_df(self):
        self.df.rename(columns={"estado": "uf"},inplace=True)
        self.df.rename(columns={"uf": "uf_code"},inplace=True)
        
        return self.df 
    
    @staticmethod
    def inner_join(ufs,df,key):
        base_enriquecida = pd.merge(ufs, df, on=key, how='inner')
        return base_enriquecida    
 
def main():  
  inicio = dt.now()  

  quality = DataQuality(df="base_gerada/base_limpinha.csv",
                   ufs="https://raw.githubusercontent.com/mapaslivres/municipios-br/main/tabelas/ufs.csv")

  df, ufs = quality.load_bases() 
    
  df = quality.rename_df()

  base_enriquecida = quality.inner_join(ufs=ufs[['timezone','no_accents','macroregion','uf_code']], df=df,key='uf_code')
  base_enriquecida.to_csv("base_gerada/base_enriquecida_dados_cadastrados.csv",index=False)
  
  print("Tempo de Execução: ",dt.now()-inicio)
    
if __name__ == "__main__":
    main()