import matplotlib.pyplot as plt

class intra_node_perf():
    def __init__(self, serial_time, number_of_cores, time):
        ''' Calculate statistics about Intra Node Performance ss'''
        self.serial_time = serial_time
        self.number_of_cores = number_of_cores
        self.time = time
        # calculate amount of data
        self.amount_of_data = len(self.number_of_cores)
        
        # calculate speed up (mod)
        self.speed_up_mod = [self.serial_time / t for t in self.time]
        
        # calculate efficiency
        self.efficiency = [self.speed_up_mod[i] / self.number_of_cores[i] for i in range(self.amount_of_data)]

        # calculate Intra Node Proportion
        E_value, i = 1, 0
        while E_value >= 0.8:
            i += 1
            E_value = self.serial_time/(self.time[i]*self.number_of_cores[i])
        self.p_critical_80 = self.number_of_cores[i-1]
        self.intraNode_proportion_80 = self.p_critical_80 / max(self.number_of_cores)

        E_value, i = 1, 0
        while E_value >= 0.6:
            i += 1
            E_value = self.serial_time/(self.time[i]*self.number_of_cores[i])
        self.p_critical_60 = self.number_of_cores[i-1]
        self.intraNode_proportion_60 = self.p_critical_60 / max(self.number_of_cores)

    def plot_efficiency_graph(self):
        ''' Plot Efficiency against Number of Cores graph '''
        fig, ax = plt.subplots()
        ax.set_xlabel(r'$p$')
        ax.set_ylabel(r'$E(p)$')
        
        ax.axvline(x=self.p_critical_80, color="#ffc844", linestyle="--")
        ax.axvline(x=self.p_critical_60, color="#e35555", linestyle="--")
        ax.plot(self.number_of_cores, self.efficiency, '.-', color="black", linewidth=2)

        plt.show()

    def plot_time_graph(self):
        ''' Plot Time against Number of Cores graph '''
        fig, ax = plt.subplots()
        ax.set_xlabel(r'$p$')
        ax.set_ylabel(r'$t(p)$')
        
        plt.plot(self.number_of_cores, self.time, '.-', color = 'black', linewidth=2)
        
        plt.show()

    def intra_perf_table(self):
        ''' Draw a table indicating flaws in code '''
        data = [[''], [''], ['']]
        column_headings = [r'Parallel efficiency metrics']
        row_headings = [r'$C_{\mathrm{intra}}^{80\%} \geq 0.8$',r'$C_{\mathrm{intra}}^{80\%} < 0.8 \wedge C_{\mathrm{intra}}^{60\%} \geq 0.6$',r'otherwise']

        perf_str = [r'$C_{\mathrm{intra}}^{80\%} \approx$' + f'{self.intraNode_proportion_80:.3f}' + r', $C_{\mathrm{intra}}^{60\%} \approx$' + f'{self.intraNode_proportion_60:.3f}']
        
        if self.intraNode_proportion_80 >= 0.8:
            data[0] = perf_str
        elif self.intraNode_proportion_80 < 0.8 and self.intraNode_proportion_60 >= 0.6:
            data[1] = perf_str
        else:
            data[2] = perf_str
        
        fig, ax = plt.subplots()
        ax.set_axis_off()
        
        cell_colours = [['#0fa83480'], ['#ffc84480'], ['#e3555580']]

        plt.rcParams.update({'font.size': 18}) 

        table = plt.table(cellText = data,
                          rowLabels = row_headings,
                          colLabels = column_headings,
                          loc = 'center',
                          colLoc = 'center',
                          cellLoc = 'center',
                          rowLoc = 'center',
                          cellColours = cell_colours)

        table.scale(1.5,3)
        plt.show()