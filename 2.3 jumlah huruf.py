#!/usr/bin/env python
# coding: utf-8

# In[1]:


nama = "Alia Dewanto" 
vokal = 'aiueoAIUEO' 
huruf = len(nama) - nama.count(' ') 
print ("Jumlah Huruf : ", huruf) 
jml_vo = 0
jml_ko = 0
for i in nama: 
    if i in vokal: 
        jml_vo += 1
    else : 
        jml_ko += 1 
print("Jumlah huruf vokal : ", jml_vo) 
print("Jumlah huruf konsonan : ", jml_ko)


# In[ ]:




