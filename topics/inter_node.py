import matplotlib.pyplot as plt

class inter_node_perf():
    def __init__(self, serial_time, node_count, runtime):
        '''Calculate statistics about inter-node performance'''

        self.serial_time = serial_time
        self.node_count = node_count
        self.runtime = runtime
        
        # amount of data
        self.amount_of_data = len(node_count)
        
        # calculate speed up (mod)
        self.speed_up_mod = [self.serial_time / t for t in self.runtime]
        
        # calculate efficiency
        self.efficiency = [self.speed_up_mod[i] / self.node_count[i] for i in range(self.amount_of_data)]

        # calculate Intra Node Proportion
        E_value, i = 1, 0
        while E_value >= 0.8:
            i += 1
            E_value = self.serial_time/(self.runtime[i]*self.node_count[i])
        self.p_critical_80 = self.node_count[i-1]
        self.interNode_proportion_80 = self.p_critical_80 / max(self.node_count)

        E_value, i = 1, 0
        while E_value >= 0.6:
            i += 1
            E_value = self.serial_time/(self.runtime[i]*self.node_count[i])
        self.p_critical_60 = self.node_count[i-1]
        self.interNode_proportion_60 = self.p_critical_60 / max(self.node_count)

    def plot_efficiency_graph(self):
        '''Plot Efficiency against Number of Nodes'''
        
        fig, ax = plt.subplots()
        ax.set_xlabel(r'$n$')
        ax.set_ylabel(r'$E(n)$')
        
        ax.axvline(x=self.p_critical_80, color="#ffc844", linestyle="--")
        ax.axvline(x=self.p_critical_60, color="#e35555", linestyle="--")    
        ax.plot(self.node_count, self.efficiency, '.-', color="black", linewidth=2)
        
        plt.show()

    def plot_time_graph(self):
        '''Plot Time against Number of Nodes'''
        
        fig, ax = plt.subplots()
        ax.set_xlabel(r'$n$')
        ax.set_ylabel(r'$t(n)$')
        
        plt.plot(self.node_count, self.runtime, '.-', color = 'black', linewidth=2)
        
        plt.show()

    def inter_perf_table(self):
        ''' Draw a table indicating flaws in code '''
        data = [[''], [''], ['']]
        column_headings = [r'Parallel efficiency metrics']
        row_headings = [r'$C_{\mathrm{inter}}^{80\%} \geq 0.8$',
                        r'$C_{\mathrm{inter}}^{80\%} < 0.8 \wedge C_{\mathrm{inter}}^{60\%} \geq 0.6$',r'otherwise']

        perf_str = [r'$C_{\mathrm{inter}}^{80\%} =$' + f'{self.interNode_proportion_80:.3f}' + r', $C_{\mathrm{inter}}^{60\%} =$' + f'{self.interNode_proportion_60:.3f}']
        
        if self.interNode_proportion_80 >= 0.8:
            data[0] = perf_str
        elif self.interNode_proportion_80 < 0.8 and self.interNode_proportion_60 >= 0.6:
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