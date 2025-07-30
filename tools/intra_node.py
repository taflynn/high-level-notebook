import matplotlib.pyplot as plt

class intra_node_perf():
    def __init__(self,serial_time,number_of_cores,time):
        ''' Calculate statistics about Intra Node Performance ss'''
        self.serial_time = serial_time
        self.number_of_cores = number_of_cores
        self.time = time
        # calculate amount of data
        self.amount_of_data = len(number_of_cores)
        
        # calculate speed up (mod)
        self.speed_up_mod = [serial_time / t for t in time]
        
        # calculate efficiency
        self.efficiency = [self.speed_up_mod[i] / number_of_cores[i] for i in range(self.amount_of_data)]

        # calculate Intra Node Proportion
        E_value,i = 1,0
        while E_value >= 0.8:
            E_value = serial_time/(time[i]*number_of_cores[i])
            i += 1
        p_critical = number_of_cores[i-1]
        self.intraNode_proportion = p_critical / max(number_of_cores)

    def plot_efficiency_graph(self):
        ''' Plot Efficiency against Number of Cores graph '''
        fig, ax = plt.subplots()
        ax.axhline(y=0.8, color="#ffc844", linestyle="--")
        ax.axhline(y=0.6, color="#e35555", linestyle="--")
        ax.set_title('Efficiency against Number of Cores')
        ax.set_xlabel('Number of Cores')
        ax.set_ylabel('Efficiency')
        ax.set_xticks(self.number_of_cores)
        ax.plot(self.number_of_cores, self.efficiency, '.-', color="black", linewidth=2)

        plt.show()

    def plot_time_graph(self):
        ''' Plot Time against Number of Cores graph '''
        fig, ax = plt.subplots()
        ax.set_title("Time against Number of Cores")
        ax.set_xlabel("Number of Cores")
        ax.set_ylabel("Time")
        ax.set_xticks(self.number_of_cores)
        plt.plot(self.number_of_cores, self.time, '.-', color = 'black', linewidth=2)
        plt.show()