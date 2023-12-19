# Internet Performance Analysis Project

This project was developed by Pedro Edom (149349) and Eduardo Evangelista (149382). The objective is to analyze the performance of the Internet for a series of destinations, using the RIPE Atlas platform.

## Code Description

The Python code performs the following tasks:

1. Loads latency and hop count measurement data from a JSON file.
2. Processes the data and stores the results in a text file.
3. Reads the text file and creates dictionaries to store latency and hop count values for each probe.
4. Loads country data from a JSON file and adds it to the latency dictionary.
5. Generates graphs of latency and hop count variation over time, by country and continent.
6. Generates graphs of correlation between latency and hop count.

## Analysis

It is possible to check all the graphs in the "graphs" folder where all the analyses extracted from the data are made.
It is possible to check the probs id list in the file "country.json", when each prob is related with their respective country, continent and city. Some prob don't have city related because we can't find the city from IP adress.

## License

This project is licensed under the MIT license.