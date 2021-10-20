#https://www.geeksforgeeks.org/building-an-undirected-graph-and-finding-shortest-path-using-dictionaries-in-python/
import pandas as pd

class Trip:
    def __init__(self, df):
        self.df = df
        self.df = self.df.query("Energy != '0' & Time != '0'")
        self.cities = self.df['Start'].unique()
        self.ordered = self.df.sort_values(by=['Time', 'Energy'], ascending=True)
        self.force()

    def force(self):
        max_energy = 58000
        max_time = 515 + 135
        cities = self.cities.tolist()
        control = False
        path = {}

        for city in cities:
            possibilities = self.ordered.query('Start == "' + city + '"')
            possibilities = possibilities['Finish'].tolist()
            path[city] = possibilities
            print(path)
        
        visited = []
        energy = 0
        time = 0
        
        for a in path:
            p2 =  path[a]
            visited, energy, time = self.instructions(a, visited, energy, time)
            for b in p2:
                p3 =  path[b]
                visited, energy, time = self.instructions(b, visited, energy, time)
                for c in p3:
                    p4 =  path[c]
                    visited, energy, time = self.instructions(c, visited, energy, time)
                    for d in p4:
                        p5 =  path[d]
                        visited, energy, time = self.instructions(d, visited, energy, time)
                        for e in p5:
                            p6 =  path[e]
                            visited, energy, time = self.instructions(e, visited, energy, time)
                            for f in p6:
                                p7 =  path[f]
                                visited, energy, time = self.instructions(f, visited, energy, time)
                                for g in p7:
                                    p8 =  path[g]
                                    visited, energy, time = self.instructions(g, visited, energy, time)
                                    for h in p8:
                                        p9 =  path[h]
                                        visited, energy, time = self.instructions(h, visited, energy, time)
                                        for i in p9:
                                            p10 =  path[i]
                                            visited, energy, time = self.instructions(i, visited, energy, time)
                                            for j in p10:
                                                p11 =  path[j]
                                                visited, energy, time = self.instructions(j, visited, energy, time)
                                                for k in p11:
                                                    p12 =  path[k]
                                                    visited, energy, time = self.instructions(k, visited, energy, time)
                                                    for l in p12:
                                                        p13 =  path[l]
                                                        visited, energy, time = self.instructions(l, visited, energy, time)
                                                        for m in p13:
                                                            p14 =  path[m]
                                                            visited, energy, time = self.instructions(m, visited, energy, time)
                                                            for n in p14:
                                                                visited, energy, time = self.instructions(n, visited, energy, time)
                                                                print(len(visited))
                                                                if n == city and energy <= max_energy and time <= max_time:
                                                                    print([a, b, c, d, e, f, g, h, i, j, k, l, m, n])

    def instructions(self, city, visited, energy, time):
        visited.append(city)
        energy += 
        time += city['Time']

        return visited, energy, time

        # for i, city1 in self.ordered.iterrows():
        #     path[0] = city1['Start']
        #     if not control:
        #         energy = 0
        #         time = 0
        #         arrive = city1['Finish']
        #         cities.remove(city1['Start'])
        #         print(cities)

        #         while energy <= max_energy and time <= max_time:
        #             if len(cities) > 0:
        #                 city2 = self.ordered.query('Start == "' + arrive + '"')
        #                 city2 = city2.loc[city2['Start'].isin(cities)]
        #                 city2 = city2.sort_values(by=['Energy'], ascending=True)[0]
        #                 print(city2)
        #                 time += int(city2['Time'])
        #                 energy += int(city2['Energy'])
        #                 arrive = city2['Finish']
        #                 cities.remove(city2['Start'])
        #                 print(city1, city2, energy, time)
        #             else:
        #                 print("SHORT: ")
        #                 print(city1, city2, energy, time)
        #                 control = True
        #                 break
        #     else:
        #         break


with open('file.txt', 'r') as input_file:
    lines = input_file.readlines()
    paths = [line[:-1] for line in lines]
    data = []
    for line in paths:
        tmp = line.split("=")
        cities = tmp[0].split("-")
        energies = tmp[1].split(",")
        data.append([cities[0], cities[1], energies[0], energies[1]])
    df = pd.DataFrame(data, columns=['Start', 'Finish', 'Time', 'Energy'])
    solve = Trip(df)