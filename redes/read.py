import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

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

# Plotar gráfico de linhas para cada prob_id
for prob_id, values in rtt_dict.items():
    plt.plot(values['timestamp'], values['rtt'], label=f'prob_id {prob_id}')

plt.xlabel('Timestamp')
plt.ylabel('RTT')
plt.title('Variation of RTT over Time')
plt.legend()
plt.show()

# Plotar gráfico de barras comparando a quantidade de saltos das probes para um mesmo destino
plt.figure()
plt.bar(hops_dict.keys(), [len(hops_dict[prob_id]['hops']) for prob_id in hops_dict])
plt.xlabel('Probe ID')
plt.ylabel('Number of Hops')
plt.title('Number of Hops for Each Probe')
plt.show()

# Plotar gráfico de dispersão
plt.figure()
plt.scatter([len(hops_dict[prob_id]['hops']) for prob_id in hops_dict], [np.mean(rtt_dict[prob_id]['rtt']) for prob_id in rtt_dict])
plt.xlabel('Number of Hops')
plt.ylabel('Mean RTT')
plt.title('Mean RTT x Number of Hops')
plt.show()

