import pandas as pd 
import numpy as np
from datetime import datetime as dt 
from console_logging.console import Console
import dataset

console = Console()

db = dataset.connect('mysql://root:mysql@192.168.29.145:62614/mydatabase')
table = db['tlb_logs']

class Logs(object):
    def __init__(self, etapa):
        self.etapa = etapa
        
    def info(self,msg):
        console.info(self.etapa+ " | "+msg)
        table.insert(dict(etapa=self.etapa ,status=msg,dt=str(dt.now())))
        
    
class DataQuality(object):
    
    def __init__(self,df,ufs):
        self.df = pd.read_csv(df)
        self.ufs = pd.read_csv(ufs)
       
    def load_bases(self):
        return self.df,self.ufs 

    def rename_df(self):
        self.df.rename(columns={"state": "uf"},inplace=True)
        self.df.rename(columns={"uf": "uf_code"},inplace=True)
        
        return self.df 
    
    @staticmethod
    def inner_join(ufs,df,key):
        base_enriquecida = pd.merge(ufs, df, on=key, how='inner')
        return base_enriquecida
