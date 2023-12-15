import json
from matplotlib.cbook import get_sample_data
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import json
import datetime

# Carregar dados do JSON
with open('RIPE-Atlas-measurement-64470119.json') as f:
    data = json.load(f)
with open('forecast.txt', 'w') as file:
    df = pd.DataFrame(data)
    rtt = []
    hops = []  # List to store the number of hops for each probe
    for i in range(len(df['result'])):
        try:
            for c in range(len(df['result'][i][-1]['result'])):
                rtt.append(df['result'][i][-1]['result'][c]['rtt'])
            rtt.sort()
            file.write(f"prob_id = {df['prb_id'][i]} | rtt = {rtt[1]} | hop = {df['result'][i][-1]['hop']} | timestamp = {df['timestamp'][i]}\n")
            rtt = []
            hops.append(df['result'][i][-1]['hop'])  # Store the number of hops for each probe
        except:
            pass

# Leitura do arquivo forecast.txt
with open('forecast.txt', 'r') as file:
    lines = file.readlines()

# Criar dicionário para armazenar os valores de rtt e hops por prob_id
rtt_dict = {}
hops_dict = {}  # Dictionary to store the number of hops for each probe
for line in lines:
    prob_id, rtt, hop, timestamp = line.split('|')
    prob_id = prob_id.strip().split('=')[1].strip()
    rtt = float(rtt.strip().split('=')[1].strip())
    hop = int(hop.strip().split('=')[1].strip())
    timestamp = timestamp.strip().split('=')[1].strip()
    if prob_id not in rtt_dict:
        rtt_dict[prob_id] = {'rtt': [], 'timestamp': []}
    rtt_dict[prob_id]['rtt'].append(rtt)
    rtt_dict[prob_id]['timestamp'].append(timestamp)
    if prob_id not in hops_dict:
        hops_dict[prob_id] = {'hops': []}
    hops_dict[prob_id]['hops'].append(hop)

# Load country data from country.json
with open('country.json') as f:
    country_data = json.load(f)

# # Plotar um gráfico de linha para cada prob_id relacionando o rtt ao longo do tempo
# for prob_id, values in rtt_dict.items():
#     country_code = country_data['prob_id'][prob_id]['country']
#     plt.plot(values['timestamp'], values['rtt'], label=f'{country_code}')
#     plt.xlabel('Timestamp')
#     plt.ylabel('RTT')
#     plt.title('Variation of RTT over Time')
#     plt.legend()
#     plt.show()


# Adicionar o país ao rtt_dict
for prob_id, values in rtt_dict.items():
    country_code = country_data['prob_id'][prob_id]['country']
    values['country'] = country_code



countries = ['brazil', 'canada', 'chile','denmark','fiji','germany','india','japan','russia','spain','usa']

# Count the number of unique prob_ids for each country
num_probes_per_country = {country: sum(1 for values in rtt_dict.values() if values['country'] == country) for country in countries}

for country in countries:
    print("Pais: ", country)
    fig, ax = plt.subplots(figsize=(10, 5))
    # counter = 0
    for prob_id, values in rtt_dict.items():
        if values['country'] == country:
            # if counter == 2:
            m = min(values['timestamp'])
            v = [int(i) - int(m) for i in values['timestamp']]
            ax.plot( values['rtt'], label=f'prob_id: {prob_id}')
            # counter += 1
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('RTT')
    ax.set_title(f'Variation of RTT over Time for {country}')
    ax.legend()
    plt.tight_layout()
    plt.show()

# #plotar o grafico relacionando o rtt ao longo do tempo para cada pais, onde cada prob_id do pais é uma linha
# countries = ['brazil', 'canada', 'chile','denmark','fiji','germany','india','japan','russia','spain','usa']
# for country in countries:
#     print("Pais: ", country)
#     # print(rtt_dict.items())
#     for prob_id, values in rtt_dict.items():
#         # print(values['rtt'])
#         if values['country'] == country:
#             # print("timestamp: ", values['timestamp'])
#             # print("rtt: ", values['rtt'])

#             #verify with timestamp  is in order
#             flag = False
#             for i in range(len(values['timestamp'])-1):
#                 if values['timestamp'][i] > values['timestamp'][i+1]:
#                     flag = True
#                     break
#             if flag:
#                 print("timestamp is not in order")
#                 #order timestamp and rtt,
#                 # values['timestamp'], values['rtt'] = zip(*sorted(zip(values['timestamp'], values['rtt'])))
#                 # print("timestamp: ", values['timestamp'])
#                 # print("rtt: ", values['rtt'])

#             plt.plot(values['timestamp'], values['rtt'], label=f'{prob_id}')
#     plt.xlabel('Timestamp')
#     plt.ylabel('RTT')
#     plt.title('Variation of RTT over Time')
#     plt.legend()
#     plt.show()

    

    


# Plotar gráfico de linhas para cada prob_id
# for prob_id, values in rtt_dict.items():
#     plt.plot(values['timestamp'], values['rtt'], label=f'prob_id {prob_id}')

# plt.xlabel('Timestamp')
# plt.ylabel('RTT')
# plt.title('Variation of RTT over Time')
# plt.legend()
# plt.show()

# Plotar gráfico de barras comparando a quantidade de saltos das probes para um mesmo destino
plt.figure()
plt.bar(hops_dict.keys(), [max(hops_dict[prob_id]['hops']) for prob_id in hops_dict])
plt.xlabel('Probe ID')
plt.ylabel('Number of Hops')
plt.title('Number of Hops for Each Probe')
plt.show()

# # Plotar gráfico de dispersão
plt.figure()
plt.scatter([max(hops_dict[prob_id]['hops']) for prob_id in hops_dict], [np.mean(rtt_dict[prob_id]['rtt']) for prob_id in rtt_dict])
plt.xlabel('Number of Hops')
plt.ylabel('Mean RTT')
plt.title('Mean RTT x Number of Hops')
plt.show()

