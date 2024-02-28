# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 16:26:46 2022

@author: Yu Wang
"""
l = [] 

with open('Nat2017PublicUS.c20180516.r20180808.txt') as f:
    while True: 
        contents = f.readline() 
        
        if not contents:
            break

        # Yu Wang start from here: 
        # smoking 
        CIG_0 = contents[252: 254] 
        CIG_1 = contents[254: 256] 
        CIG_2 = contents[256: 258]
        CIG_3 = contents[258: 260] 
        
        F_CIGS_0 = contents[264]    
        F_CIGS_1 = contents[265] 
        F_CIGS_2 = contents[266] 
        F_CIGS_3 = contents[267] 
        F_TOBACO = contents[269] 
        
        # maternal reproductive history 
        PRIORLIVE = contents[170: 172] 
        PRIORDEAD = contents[172: 174] 
        PRIORTERM = contents[174: 176] 
        ILLB_R = contents[197: 200] 
        ILOP_R = contents[205: 208] 
        ILP_R = contents[213: 216] 
        
        # infections 
        IP_GON = contents[342] 
        IP_SYPH = contents[343] 
        IP_CHLAM = contents[344] 
        IP_HEPB = contents[345] 
        IP_HEPC = contents[346] 
        
        # start from here 
        RF_PDIAB=contents[312]
        RF_GDIAB=contents[313]
        BMI=contents[282:286]
        PWgt_R=contents[291:294]
        DWgt_R =contents[298:301]
        WTGAIN =contents[303:305]
        RF_INFTR =contents[324]
        RF_FEDRG =contents[325] 
        
        
        # start from here
        FEDUC= contents[162] 
        MEDUC= contents[123]  
        FAGECOMB= contents[146:148] 
        MAGER= contents[74:76] 
        MRTERR= contents[88:90] 
        BFACIL= contents[31] 
        MRTERR= contents[88:90] 
        RESTATUS = contents[103]
        
        # target
        CA_ANEN = contents[536] 

        r = [CIG_0, CIG_1, CIG_2, CIG_3, F_CIGS_0, F_CIGS_1, F_CIGS_2, F_CIGS_3, F_TOBACO, PRIORLIVE, 
             PRIORDEAD, PRIORTERM, ILLB_R, ILOP_R, ILP_R, IP_GON, IP_SYPH, IP_CHLAM, IP_HEPB, IP_HEPC, 
             RF_PDIAB, RF_GDIAB, BMI, PWgt_R, DWgt_R, WTGAIN, RF_INFTR, RF_FEDRG, FEDUC, MEDUC, FAGECOMB, 
             MAGER, MRTERR, BFACIL, MRTERR, RESTATUS, CA_ANEN] 
        
        
        l.append(r) 
        
        
        
title = ["CIG_0", "CIG_1", "CIG_2", "CIG_3", "F_CIGS_0", "F_CIGS_1", "F_CIGS_2", "F_CIGS_3", "F_TOBACO", "PRIORLIVE", 
             "PRIORDEAD", "PRIORTERM", "ILLB_R", "ILOP_R", "ILP_R", "IP_GON", "IP_SYPH", "IP_CHLAM", "IP_HEPB", "IP_HEPC", 
             "RF_PDIAB", "RF_GDIAB", "BMI", "PWgt_R", "DWgt_R", "WTGAIN", "RF_INFTR", "RF_FEDRG", "FEDUC", "MEDUC", "FAGECOMB", 
             "MAGER", "MRTERR", "BFACIL", "MRTERR", "RESTATUS", "CA_ANEN"]



import csv  

with open('2017Anencephaly.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f, dialect='excel', lineterminator='\n')
    writer.writerow(title) 
    for i in range(len(l)): 
        #if l[i][-1] == 'Y': 
        writer.writerow(l[i]) 

