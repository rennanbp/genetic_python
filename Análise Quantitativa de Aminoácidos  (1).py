#!/usr/bin/env python
# coding: utf-8

# # Análise Quantitativa de Aminoácidos da Proteína p53 (Homo sapiens)

# In[29]:


import pandas as pd


# In[30]:


# Uma list com a sequencia de aminoácidos da proteína p53

Proteína = pd.Series(list('MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGPDEAPRMPEAAPRVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAKSVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHERCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRNSFEVHVCACPGRDRRTEEENLRKKGEPHHELPPGSTKRALSNNTSSSPQPKKKPLDGEYFTLQIRGRERFEMFRELNEALELKDAQAGKEPGGSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD'))
Proteína


# In[31]:


Proteína.unique()


# In[32]:


series = Proteína.value_counts()
series.rename({'P': 'Prolina', 'S': 'Serina','L':'Leucina','E':'Glutamato', 'R': 'Arginina', 'A':'Alanina', 'G':'Glicina', 'T':'Treonina', 'D': 'Aspartato', 'K': 'Lisina', 'V': 'Valina', 'Q':'Glutamina', 'N':'Asparagina', 'H': 'Histidina', 'M': 'Metionina', 'F':'Fenilalanina', 'C':'Cisteina', 'Y':'Tirosina', 'I':'Isoleucina', 'W': 'Triptofano'})


# In[28]:


import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
py.init_notebook_mode(connected=True)


# In[9]:


trace = go.Bar(x = ['Prolina', 'Serina','Leucina','Glutamato', 'Arginina', 'Alanina', 'Glicina', 'Treonina', 'Aspartato', 'Lisina', 'Valina', 'Glutamina', 'Asparagina', 'Histidina', 'Metionina', 'Fenilalanina', 'Cisteina', 'Tirosina', 'Isoleucina', 'Triptofano'],
               y = [43,39,32,30,26,24,23,22,20,20,18,15,14,13,12,11,10,9,8,4])
data = [trace]
py.iplot(data)


# # Análise Quantitativa de Aminoácidos da Proteína p53 (Mus musculus)

# In[10]:


Proteina_2 = pd.Series(list('MTAMEESQSDISLELPLSQETFSGLWKLLPPEDILPSPHCMDDLLLPQDVEEFFEGPSEALRVSGAPAAQDPVTETPGPVAPAPATPWPLSSFVPSQKTYQGNYGFHLGFLQSGTAKSVMCTYSPPLNKLFCQLAKTCPVQLWVSATPPAGSRVRAMAIYKKSQHMTEVVRRCPHHERCSDGDGLAPPQHRIRVEGNLYPEYLEDRQTFRHSVVVPYEPPEAGSEYTTIHYKYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRDSFEVRVCACPGRDRRTEEENFRKKEVLCPELPPGSAKRALPTCTSASPPQKKKPLDGEYFTLKIRGRKRFEMFRELNEALELKDAHATEESGDSRAHSSYLKTKKGQSTSRHKKTMVKKVGPDSD'))
Proteina_2


# In[11]:


Proteina_2.unique()


# In[12]:


series = Proteina_2.value_counts()
series.rename({'P': 'Prolina', 'S': 'Serina','L':'Leucina','E':'Glutamato', 'R': 'Arginina', 'A':'Alanina', 'G':'Glicina', 'T':'Treonina', 'D': 'Aspartato', 'K': 'Lisina', 'V': 'Valina', 'Q':'Glutamina', 'N':'Asparagina', 'H': 'Histidina', 'M': 'Metionina', 'F':'Fenilalanina', 'C':'Cisteina', 'Y':'Tirosina', 'I':'Isoleucina', 'W': 'Triptofano'})


# In[13]:


trace = go.Bar(x = ['Prolina', 'Serina','Leucina','Glutamato', 'Arginina', 'Alanina', 'Glicina', 'Treonina', 'Aspartato', 'Lisina', 'Valina', 'Glutamina', 'Asparagina', 'Histidina', 'Metionina', 'Fenilalanina', 'Cisteina', 'Tirosina', 'Isoleucina', 'Triptofano'],
               y = [38,35,34,32,25,24,24,24,24,20,17,14,13,12,12,11,11,9,8,3])
data = [trace]
py.iplot(data)


# ## Análise comparativa entre as duas espécies

# In[14]:


trace1 = go.Bar(x = ['Prolina', 'Serina','Leucina','Glutamato', 'Arginina', 'Alanina', 'Glicina', 'Treonina', 'Aspartato', 'Lisina', 'Valina', 'Glutamina', 'Asparagina', 'Histidina', 'Metionina', 'Fenilalanina', 'Cisteina', 'Tirosina', 'Isoleucina', 'Triptofano'],
                y = [43,39,32,30,26,24,23,22,20,20,18,15,14,13,12,11,10,9,8,4],
                name = 'Gráfico 1',
                marker = {'color': '#feca57'})
trace2 = go.Bar(x = ['Prolina', 'Serina','Leucina','Glutamato', 'Arginina', 'Alanina', 'Glicina', 'Treonina', 'Aspartato', 'Lisina', 'Valina', 'Glutamina', 'Asparagina', 'Histidina', 'Metionina', 'Fenilalanina', 'Cisteina', 'Tirosina', 'Isoleucina', 'Triptofano'],
                y = [38,35,34,32,25,24,24,24,24,20,17,14,13,12,12,11,11,9,8,3],
                name = 'Gráfico 2',
                marker = {'color': '#ff9f43'})
data = [trace1, trace2]
py.iplot(data)


# In[15]:


trace1 = go.Bar(x = ['Prolina', 'Serina','Leucina','Glutamato', 'Arginina', 'Alanina', 'Glicina', 'Treonina', 'Aspartato', 'Lisina', 'Valina', 'Glutamina', 'Asparagina', 'Histidina', 'Metionina', 'Fenilalanina', 'Cisteina', 'Tirosina', 'Isoleucina', 'Triptofano'],
                y = [43,39,32,30,26,24,23,22,20,20,18,15,14,13,12,11,10,9,8,4],
                name = 'Gráfico 1',
                marker = {'color': '#feca57'})
trace2 = go.Bar(x = ['Prolina', 'Serina','Leucina','Glutamato', 'Arginina', 'Alanina', 'Glicina', 'Treonina', 'Aspartato', 'Lisina', 'Valina', 'Glutamina', 'Asparagina', 'Histidina', 'Metionina', 'Fenilalanina', 'Cisteina', 'Tirosina', 'Isoleucina', 'Triptofano'],
                y = [38,35,34,32,25,24,24,24,24,20,17,14,13,12,12,11,11,9,8,3],
                name = 'Gráfico 2',
                marker = {'color': '#ff9f43'})
data = [trace1, trace2]
layout = go.Layout(title = 'Gráfico de barras do <a href=\'https://plot.ly/\'>Plotly</a>',
                   xaxis = {'title': 'Aminoácidos'},
                   yaxis = {'title': 'Quantidade'},
                   barmode = 'stack')
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# In[16]:


# Gráfico usando apenas marcadores
trace1 = go.Scatter(x = ['Prolina', 'Serina','Leucina','Glutamato', 'Arginina', 'Alanina', 'Glicina', 'Treonina', 'Aspartato', 'Lisina', 'Valina', 'Glutamina', 'Asparagina', 'Histidina', 'Metionina', 'Fenilalanina', 'Cisteina', 'Tirosina', 'Isoleucina', 'Triptofano'],
                    y = [43,39,32,30,26,24,23,22,20,20,18,15,14,13,12,11,10,9,8,4],
                    mode = 'lines',
                    name = 'Gráfico com linhas tracejadas',
                    line = {'color': '#ee5253',
                            'dash': 'dash'})
# Gráfico de apenas linhas
trace2 = go.Scatter(x = ['Prolina', 'Serina','Leucina','Glutamato', 'Arginina', 'Alanina', 'Glicina', 'Treonina', 'Aspartato', 'Lisina', 'Valina', 'Glutamina', 'Asparagina', 'Histidina', 'Metionina', 'Fenilalanina', 'Cisteina', 'Tirosina', 'Isoleucina', 'Triptofano'],
                    y = [38,35,34,32,25,24,24,24,24,20,17,14,13,12,12,11,11,9,8,3],
                    mode = 'lines',
                    name = 'Gráfico com linha pontilhada',
                    line = {'color': '#341f97',
                            'dash': 'dot'})
data = [trace1, trace2]
py.iplot(data)


# ### Análise Quantitativa de Aminoácidos da Proteína p53 (Penaeus japonicus)

# In[17]:


Proteina_3 = pd.Series(list('MQQGGMQRSDSELLFGEDEYHLLRDDSLLQRFGSANFHTLLDGPDVEPPVTEQEVEDQQQQQQQQQQQPQPQQQQQQIQQQQPGQQPAPQIAYPIQNIDNQLILTNSHIHGEIFQTVQVQQQPQQQQIQQLQPGQPIPWDSLQTLDTENVEVLPNNNVPVGGVSAAITLIEGSATSCLADSTLAHSVPSLQPWAGRHKFGISLPTGNKDRNKWCYSQDLGKLYLCPNVAVPVNVMLEDWVNATITMTPVFKQSCHRTEPVNRCYNCKSIQNCDPNLAEHVVQIEGEGCEYSFINDRYLVTVPLRPPPPGEVPSTLLIKIMCLTSCVGGPNRRPFCIVLTLRNSVTGEEIGRQILDIKCCKCPSRDLTNDEKSRTPTAPSTPSVDEEKRTKVRKLANEIAVGQKRKRPKIKLEPGTDSRMVNIAVPVEYEAEVKSYINKLIAADLIKKWQPDALMYPEEESN'))
Proteina_3


# In[18]:


Proteina_3.unique()


# In[19]:


series = Proteina_3.value_counts()
series.rename({'P': 'Prolina', 'S': 'Serina','L':'Leucina','E':'Glutamato', 'R': 'Arginina', 'A':'Alanina', 'G':'Glicina', 'T':'Treonina', 'D': 'Aspartato', 'K': 'Lisina', 'V': 'Valina', 'Q':'Glutamina', 'N':'Asparagina', 'H': 'Histidina', 'M': 'Metionina', 'F':'Fenilalanina', 'C':'Cisteina', 'Y':'Tirosina', 'I':'Isoleucina', 'W': 'Triptofano'})


# In[20]:


# Gráfico usando apenas marcadores
trace1 = go.Scatter(x = ['Prolina', 'Serina','Leucina','Glutamato', 'Arginina', 'Alanina', 'Glicina', 'Treonina', 'Aspartato', 'Lisina', 'Valina', 'Glutamina', 'Asparagina', 'Histidina', 'Metionina', 'Fenilalanina', 'Cisteina', 'Tirosina', 'Isoleucina', 'Triptofano'],
                    y = [43,39,32,30,26,24,23,22,20,20,18,15,14,13,12,11,10,9,8,4],
                    mode = 'lines',
                    name = 'Gráfico com linhas tracejadas',
                    line = {'color': '#ee5253',
                            'dash': 'dash'})
# Gráfico de apenas linhas
trace2 = go.Scatter(x = ['Prolina', 'Serina','Leucina','Glutamato', 'Arginina', 'Alanina', 'Glicina', 'Treonina', 'Aspartato', 'Lisina', 'Valina', 'Glutamina', 'Asparagina', 'Histidina', 'Metionina', 'Fenilalanina', 'Cisteina', 'Tirosina', 'Isoleucina', 'Triptofano'],
                    y = [38,35,34,32,25,24,24,24,24,20,17,14,13,12,12,11,11,9,8,3],
                    mode = 'lines',
                    name = 'Gráfico com linha pontilhada',
                    line = {'color': '#341f97',
                            'dash': 'dot'})

# Gráfico de apenas linhas
trace3 = go.Scatter(x = ['Prolina', 'Serina','Leucina','Glutamato', 'Arginina', 'Alanina', 'Glicina', 'Treonina', 'Aspartato', 'Lisina', 'Valina', 'Glutamina', 'Asparagina', 'Histidina', 'Metionina', 'Fenilalanina', 'Cisteina', 'Tirosina', 'Isoleucina', 'Triptofano'],
                    y = [54,40,38,33,31,28,27,25,25,24,23,21,20,20,14,10,8,8,7,5],
                    mode = 'lines',
                    name = 'Gráfico com linha continua',
                    line = {'color': '#7f7f7f',
                            'dash': 'dot'})

data = [trace1, trace2, trace3]
py.iplot(data)


# In[ ]:





# In[ ]:




