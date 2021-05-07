
# coding: utf-8

# In[2]:


import numpy as np


# In[162]:


def run_trial(ability, ability_trial, cutoff):
    ability_trial=ability_trial-1
    ind = np.random.uniform(); 
    if ind<=cutoff:
        ability = ability+1; 
        cutoff = np.max((0.25, cutoff-0.1)); 
    else:
        cutoff=np.min((0.75, cutoff+0.1));
    return ability, ability_trial, cutoff

def case1(ability1, ability1_trial, ability2, ability2_trial, ability3, ability3_trial, cutoff):
    if cutoff>=0.65:  #First rule 
        ability1, ability1_trial, cutoff = run_trial(ability1, ability1_trial, cutoff); 
    elif cutoff>=0.55 and cutoff<0.65: #second rule 
        ability2, ability2_trial, cutoff = run_trial(ability2, ability2_trial, cutoff); 
    else: 
        ability3, ability3_trial, cutoff = run_trial(ability3, ability3_trial, cutoff);     
    return ability1, ability1_trial, ability2, ability2_trial, ability3, ability3_trial, cutoff

def case2(ability1, ability1_trial, ability2, ability2_trial, ability3, ability3_trial, cutoff):
    #only 1,2, possible. 
    if cutoff>=0.55:
        ability1, ability1_trial, cutoff = run_trial(ability1, ability1_trial, cutoff); 
    else: 
        ability2, ability2_trial, cutoff = run_trial(ability2, ability2_trial, cutoff); 
    return ability1, ability1_trial, ability2, ability2_trial, ability3, ability3_trial, cutoff

def case3(ability1, ability1_trial, ability2, ability2_trial, ability3, ability3_trial, cutoff):
    #1,3 possible 
    if cutoff>=0.55: 
        ability1, ability1_trial, cutoff = run_trial(ability1, ability1_trial, cutoff); 
    else: 
        ability3, ability3_trial, cutoff = run_trial(ability3, ability3_trial, cutoff);     
    return ability1, ability1_trial, ability2, ability2_trial, ability3, ability3_trial, cutoff
    
def case4(ability1, ability1_trial, ability2, ability2_trial, ability3, ability3_trial, cutoff):
    #2,3 possible 
    if cutoff>=0.55:
        ability2, ability2_trial, cutoff = run_trial(ability2, ability2_trial, cutoff); 
    else: 
        ability3, ability3_trial, cutoff = run_trial(ability3, ability3_trial, cutoff);     
    return ability1, ability1_trial, ability2, ability2_trial, ability3, ability3_trial, cutoff

def case5(ability1, ability1_trial, ability2, ability2_trial, ability3, ability3_trial, cutoff):
    #only 1 possible 
    ability1, ability1_trial, cutoff = run_trial(ability1, ability1_trial, cutoff); 
    return ability1, ability1_trial, ability2, ability2_trial, ability3, ability3_trial, cutoff

def case6(ability1, ability1_trial, ability2, ability2_trial, ability3, ability3_trial, cutoff):
    #only 2 possible 
    ability2, ability2_trial, cutoff = run_trial(ability2, ability2_trial, cutoff); 
    return ability1, ability1_trial, ability2, ability2_trial, ability3, ability3_trial, cutoff

def case7(ability1, ability1_trial, ability2, ability2_trial, ability3, ability3_trial, cutoff):
    #only 3 possible 
    ability3, ability3_trial, cutoff = run_trial(ability3, ability3_trial, cutoff);     
    return ability1, ability1_trial, ability2, ability2_trial, ability3, ability3_trial, cutoff

def ability_stone_simulator(N):
    final_output = np.zeros((3,N)); 
    successes = np.zeros(N); 
    failures = np.zeros(N); 
    dol_97 = np.zeros(N); 
    dol_77 = np.zeros(N); 
    for t in range(N):
        ability1 = 0; 
        ability2 = 0; 
        ability3 = 0; 
        ability1_trial = 10; 
        ability2_trial = 10; 
        ability3_trial = 10; 
        cutoff = 0.75; 
        for i in range(30):
            if ability1_trial>0 and ability2_trial>0 and ability3_trial>0:
#                 print("case_1 running")
                ability1, ability1_trial, ability2, ability2_trial, ability3, ability3_trial, cutoff = case1(ability1, ability1_trial, ability2, ability2_trial, ability3, ability3_trial, cutoff)
            elif ability1_trial>0 and ability2_trial>0 and ability3_trial<=0: 
#                 print("case_2 running")
                ability1, ability1_trial, ability2, ability2_trial, ability3, ability3_trial, cutoff = case2(ability1, ability1_trial, ability2, ability2_trial, ability3, ability3_trial, cutoff)
            elif ability1_trial>0 and ability2_trial<=0 and ability3_trial>0: 
#                 print("case_3 running")
                ability1, ability1_trial, ability2, ability2_trial, ability3, ability3_trial, cutoff = case3(ability1, ability1_trial, ability2, ability2_trial, ability3, ability3_trial, cutoff)
            elif ability1_trial<=0 and ability2_trial>0 and ability3_trial>0: 
#                 print("case_4 running")
                ability1, ability1_trial, ability2, ability2_trial, ability3, ability3_trial, cutoff = case4(ability1, ability1_trial, ability2, ability2_trial, ability3, ability3_trial, cutoff)
            elif ability1_trial>0 and ability2_trial<=0 and ability3_trial<=0: 
#                 print("case_5 running")
                ability1, ability1_trial, ability2, ability2_trial, ability3, ability3_trial, cutoff = case5(ability1, ability1_trial, ability2, ability2_trial, ability3, ability3_trial, cutoff)
            elif ability1_trial<=0 and ability2_trial>0 and ability3_trial<=0: 
#                 print("case_6 running")
                ability1, ability1_trial, ability2, ability2_trial, ability3, ability3_trial, cutoff = case6(ability1, ability1_trial, ability2, ability2_trial, ability3, ability3_trial, cutoff)
            elif ability1_trial<=0 and ability2_trial<=0 and ability3_trial>0: 
#                 print("case_7 running")
                ability1, ability1_trial, ability2, ability2_trial, ability3, ability3_trial, cutoff = case7(ability1, ability1_trial, ability2, ability2_trial, ability3, ability3_trial, cutoff)
        final_output[0,t] = ability1
        final_output[1,t] = ability2
        final_output[2,t] = ability3
        successes[t] = ability1+ability2
        failures[t] = ability3
        if ability1>=7 and ability2>=7:
            dol_77[t] = 1
        if (ability1>=9 and ability2>=7) or (ability1>=7 and ability2>=9):
            dol_97[t] = 1 
    return final_output, successes, failures, dol_77, dol_97

        



            



# In[164]:


final_output, successes, failures, dol_77, dol_97 = ability_stone_simulator(10000);


# In[165]:


sum(successes>16)/10000


# In[167]:


sum(dol_77)/10000

