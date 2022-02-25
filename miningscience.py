def download_pubmed(keyword):
    """Esta función sirve para la extracción y el conteo de los artículos que contienen una
    palabra en especial o keyword llamado en la función, pues se puede definir si tienen que encontrarse en el
    título la palabra o en el abstract más comunmunte, cabe destacar que esta función en el examen proporcionara
    información acerca del número de artículos y el PMID del primer artículo """
    from Bio import Entrez
    import re
    Entrez.email = "leslie.taimal@est.ikiam.edu.ec"
    x=Entrez.read(Entrez.esearch(db="pubmed",
                        term= keyword,
                        usehistory="y"))
    
    webenv=x["WebEnv"]
    query_key=x["QueryKey"]
    hd1=Entrez.efetch(db="pubmed",
                      rettype='medline',
                      retmode="text",
                      retstart=0,
                      retmax=543, webenv=webenv, query_key=query_key)
    out_hd1 = open(keyword+".txt", "w")
    m=hd1.read()
    out_hd1.write(m)
    out_hd1.close()
    hd1.close()
    return m



def mining_pubs(tipo, keyword):
    """Esta funcion nos ayuda a la extraccion de datos según nos indique pued tipo hace realcion a DP,AU,AD, en cambio keyword hace relacion a las mismas palabras usadas en el ejercicio 1, pues de esta manera se realizo una función en general, cabe destacar tambien que:
    DP recupera el año de publicación del artículo
    AU recupera el número de autores por PMID
    AD recupera el conteo de autores por país."""
        

    import csv
    import re
    import pandas as pd
    from collections import Counter
    with open(keyword+".txt", errors="ignore") as f: 
        my_text = f.read() 
    if tipo == "DP":
        PMID = re.findall("PMID-\s\d{8}", my_text)
        PMID = "".join(PMID)
        PMID = PMID.split("PMID- ")
        year = re.findall("DP\s{2}-\s(\d{4})", my_text)
        pmid_year = pd.DataFrame()
        pmid_year["Año de publicación"] = year
        pmid_year["PMID"] = PMID 
        return (pmid_year)
    elif tipo == "AU": 
        PMID = re.findall("PMID- (\d*)", my_text) 
        autors = my_text.split("PMID- ")
        autors.pop(0)
        num_autors = []
        for i in range(len(autors)):
            num_total = re.findall("AU -", autors[i])
            n = (len(num_total))
            num_autors.append(n)
        PMID_autors = pd.DataFrame()
        PMID_autors["PMID"] = PMID 
        PMID_autors["Numero de autores"] = num_autors
        return (PMID_autors)
    elif tipo == "AD": 
        text = re.sub(r" [A-Z]{1}\.","", my_text)
        text = re.sub(r"Av\.","", my_text)
        text = re.sub(r"Vic\.","", my_text)
        text = re.sub(r"Tas\.","", my_text)
        AD = text.split("AD  - ")
        n_country = []
        for i in range(len(AD)): 
            country = re.findall("\S, ([A-Za-z]*)\.", AD[i])
            if not country == []: 
                if not len(country) >= 2:  
                    if re.findall("^[A-Z]", country[0]): 
                        n_country.append(country[0])
        count=Counter(n_country)
        result = {}
        for clave in count:
            valor = count[clave]
            if valor != 1: 
                result[clave] = valor 
        count_pais = pd.DataFrame()
        count_pais["pais"] = result.keys()
        count_pais["numero de autores"] = result.values()
        return (count_pais)