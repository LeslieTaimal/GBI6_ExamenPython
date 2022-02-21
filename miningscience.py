from Bio import Entrez
import re

def download_pubmed(keyword):
    """Esta función sirve para la extracción y el conteo de los artículos que contienen una palabra en especial o conjunto de palabras , pues se puede definir si tienen que encontrarse en el título o en el abstract más comunmente"""
    Entrez.email = "leslie.taimal@est.ikiam.edu.ec"
    hd1 = Entrez.read(Entrez.esearch(db="pubmed", 
                        term=keyword,
                        usehistory="y"))
    webenv = record["WebEnv"]
    query_key = record["QueryKey"]
    hd1 = Entrez.efetch(db="pubmed",
                       retstart=0,
                       rettype="medline",
                       retmode="text",
                       retmax=543, webenv=webenv, query_key=query_key)
    out_hd1 = open("keyword.txt", "w")
    data = hd1.read()
    datos = re.sub(r'\n\s{6}', '', data)
    return datos
def mining_pubs(tipo):
    """Esta función en cambio nos proporciona datos específicos del texto utilizando el parametro tipo porejemplo:
    si el tipo es DP nos va a proporcionar el año de publicación del artículo 
    si el tipo es AU no imprime el número de autores por PMID
    si es AD en cambio nos ayuda con el conteo totales de cada país"""
    pass
    return
    