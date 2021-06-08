import pandas as pd
import numpy as np
import os
from os import path
import math
import sys


def main():
    coding_file = "./qualitative_codings.xlsx"
    all_factors_primary = "all_factors"
    all_factors_secondary = "all_factors-secondary"
    all_strategy_primary = "all_strategy"
    all_strategy_secondary = "all_strategy-secondary"

    factors_irr = irr_calc(coding_file, all_factors_primary, all_factors_secondary, 14)
    print(f'Cohen\'s Kappa for Q4 codebook: {factors_irr}')

    strategy_irr = irr_calc(coding_file, all_strategy_primary, all_strategy_secondary, 14)
    print(f'Cohen\'s Kappa for Q6 codebook: {strategy_irr}')

    
def read_xlsx(fname, sname):
    global keys
    l = []
    reader = pd.read_excel(fname, sheet_name=sname, header=None).replace(np.nan, '', regex=True)
    for _, row in reader.iterrows():
        row = row.values.tolist()
        if not keys: 
            keys=row
            continue
        l.append(dict(zip(keys,row)))
    return l


keys = []
def irr_calc(xlsx_file, primary_file, secondary_file, num_code_columns):
    global keys

    #if not path.exists(primary_file) or not path.exists(secondary_file):
    #    print(f'Either {primary_file} or {secondary_file} does not exist!')
    #    return
    
    pri_l = read_xlsx(xlsx_file, primary_file)
    sec_l = read_xlsx(xlsx_file, secondary_file)
    

    id_k = keys[0]
    q_k = keys[1]

    
    pri_d = {d[id_k]:d for d in read_xlsx(xlsx_file, primary_file)[1:]}
    sec_d = {d[id_k]:d for d in read_xlsx(xlsx_file, secondary_file)[1:]}

    overlap = {}
    
    pri_used = {}
    sec_used = {}
    codes = [f"Code {x}" for x in range (1, num_code_columns+1)]
    tot_pri = 0
    tot_sec = 0
    tot = 0
    for sk in sec_d:
      
        s = sec_d[sk]
        p = pri_d[s[id_k]] #get primary
        sec_codes = set(s[c].strip() for c in codes if
                        c in s and s[c] != ''
#                        and not "->" in s[c]
        )
        pri_codes = set(p[c].strip() for c in codes if
                        c in p and p[c] != '' 
#                        and not "->" in p[c]
        )
        if any(sec_codes) and any(pri_codes):
            tot_sec += len(sec_codes)
            tot_pri += len(pri_codes)

            #print(s[id_k])
            #print(textwrap.indent(textwrap.fill('"'+s[q_k]+'"'),"\t"))
            #print("pri_code:\t",pri_codes)
            #print("sec_cod:\t",sec_codes)
            #print()

            for c in sec_codes.intersection(pri_codes):
                overlap[c] = overlap.get(c,0)+1
                
            for sc in sec_codes:
                sec_used[sc] = sec_used.get(sc,0)+1

            for pc in pri_codes:
                pri_used[pc] = pri_used.get(pc,0)+1

    pri_used = {k:pri_used[k]/tot_pri for k in pri_used}
    sec_used = {k:sec_used[k]/tot_sec for k in sec_used}
    overlap = {k:overlap[k]/max(tot_pri,tot_sec) for k in overlap}

    for c in pri_used:
        if not c in overlap:
            overlap[c]=0.0
    
    for c in sec_used:
        if not c in overlap:
            overlap[c]=0.0

    #print("Primary Coders Usage")
    #pprint.pprint(pri_used)
    #print()
    #print("Secondary Coders Usage")
    #pprint.pprint(sec_used)
    #print()
    #print("Overlapping Usage")
    #pprint.pprint(overlap)

    #print()
    #print(f'primary len: {tot_pri}, secondary len: {tot_sec}')
    p_a = sum(overlap.values())
    p_c = sum(pri_used.get(c,0.0)*sec_used.get(c,0.0) for c in set(pri_used.keys()).union(set(sec_used.keys())))
    
    #irr = p_a/(1-p_c)    
    irr = 1 - (1-p_a)/(1-p_c)

    #print("p_a:",p_a)
    #print("p_c:",p_c)
    #print("irr:",irr)

    keys = [] #reset global keys back to empty

    return irr
    
if __name__ == '__main__':
    main()
