import matplotlib.pyplot as plt
import numpy as np

class inter_node_perf():
    def __init__(self, serial_runtime, node_count, parallel_runtimes):
        '''Raw inter-node performance data'''

        self.serial_runtime = serial_runtime
        self.node_count = np.array(node_count)
        self.parallel_runtimes = np.array(parallel_runtimes)
        
        self.efficiency = self.serial_runtime/self.parallel_runtimes

        self.p_crit_80 = self.node_count[(self.efficiency < 0.8) & (self.efficiency >= 0.6)][-1]
        self.p_crit_60 = self.node_count[(self.efficiency < 0.6) & (self.node_count > self.p_crit_80)][0]
        
        self.inter_node_prop_80 = self.p_crit_80 / max(self.node_count)
        self.inter_node_prop_60 = self.p_crit_60 / max(self.node_count)

    def parallel_efficiency_figure(self):
        '''Generates a figure of parallel efficiency against number of nodes'''
        
        fig, ax = plt.subplots()
        ax.set_xlabel(r'$n$')
        ax.set_ylabel(r'$E(n)$')
        
        ax.axvline(x=self.p_crit_80, color="#ffc844", linestyle="--")
        ax.axvline(x=self.p_crit_60, color="#e35555", linestyle="--")    
        ax.plot(self.node_count, self.efficiency, '.-', color="black", linewidth=2)
        
        plt.show()

    def runtimes_figure(self):
        '''Generates a figure of parallel efficiency against number of nodes'''
        
        fig, ax = plt.subplots()
        ax.set_xlabel(r'$n$')
        ax.set_ylabel(r'$t(n)$')
        
        plt.plot(self.node_count, self.parallel_runtimes, '.-', color = 'black', linewidth=2)
        
        plt.show()

    def inter_node_perf_table(self):
        '''Generates a traffic-light table for the inter-node performance metric'''
        data = [[''], [''], ['']]
        column_headings = [r'Parallel efficiency metrics']
        row_headings = [r'$C_{\mathrm{inter}}^{80\%} \geq 0.8$',
                        r'$C_{\mathrm{inter}}^{80\%} < 0.8 \wedge C_{\mathrm{inter}}^{60\%} \geq 0.6$', 
                        r'otherwise']

        perf_str = [r'$C_{\mathrm{inter}}^{80\%} =$' + f'{self.inter_node_prop_80:.3f}' 
                    + r', $C_{\mathrm{inter}}^{60\%} =$' + f'{self.inter_node_prop_60:.3f}']
        
        if self.inter_node_prop_80 >= 0.8:
            data[0] = perf_str
        elif self.inter_node_prop_80 < 0.8 and self.inter_node_prop_60 >= 0.6:
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