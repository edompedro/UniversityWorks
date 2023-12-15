import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados do JSON
with open('RIPE-Atlas-measurement-64470117.json') as f:
    data = json.load(f)

df = pd.DataFrame(data)

error = 0
with open('output.txt', 'w') as file:
    for i in range(df['result'].count()):
        file.write("{\n")
        file.write("  \"src_addr\": \"" + str(df['src_addr'][i]) + "\",\n")
        file.write("  \"endtime\": " + str(df['endtime'][i]) + ",\n")
        file.write("  \"from\": \"" + str(df['from'][i]) + "\",\n")
        file.write("  \"fw\": " + str(df['fw'][i]) + ",\n")
        file.write("  \"proto\": \"" + str(df['proto'][i]) + "\",\n")
        file.write("  \"msm_id\": " + str(df['msm_id'][i]) + ",\n")
        file.write("  \"dst_name\": \"" + str(df['dst_name'][i]) + "\",\n")
        file.write("  \"paris_id\": " + str(df['paris_id'][i]) + ",\n")
        file.write("  \"prb_id\": " + str(df['prb_id'][i]) + ",\n")
        file.write("  \"result\": [\n")
        
        for c in range(len(df['result'][i])):
            try:
                file.write("    {\n")
                file.write("      \"hop\": " + str(df['result'][i][c]['hop']) + ",\n")
                file.write("      \"result\": [\n")
            except:
                try:
                    file.write("    {\n")
                    file.write("      \"error\": " + str(df['result'][i][c]['error']) + ",\n")
                    file.write("      \"result\": [\n")
                    error = 1
                except:
                    print("ALGO QUEBROU")
            if error == 0:
                
                for counter in range(len(df['result'][i][c]['result'])):
                    try:
                        file.write("        {\n")
                        file.write("          \"from\": \"" + str(df['result'][i][c]['result'][counter]['from']) + "\",\n")
                        file.write("          \"rtt\": " + str(df['result'][i][c]['result'][counter]['rtt']) + ",\n")
                        file.write("          \"size\": " + str(df['result'][i][c]['result'][counter]['size']) + ",\n")
                        file.write("          \"ttl\": " + str(df['result'][i][c]['result'][counter]['ttl']) + "\n")
                        file.write("        },\n")
                    except:
                        file.write("        NO DATA RETURN\n")
                    

            file.write("      ]\n")
            file.write("    },\n")
            error = 0

        file.write("  ],\n")
        file.write("  \"size\": " + str(df['size'][i]) + ",\n")
        file.write("  \"src_addr\": \"" + str(df['src_addr'][i]) + "\",\n")
        file.write("  \"timestamp\": " + str(df['timestamp'][i]) + "\n")
        file.write("}\n")
