import matplotlib.pyplot as plt
import numpy as np

class intra_node_perf():
    def __init__(self, serial_runtime, core_count, parallel_runtimes):
        '''Raw inter-node performance data'''
        
        self.serial_runtime = serial_runtime
        self.core_count = np.array(core_count)
        self.parallel_runtimes = np.array(parallel_runtimes)
        
        self.speed_up = self.serial_runtime/self.parallel_runtimes 
        self.efficiency = self.speed_up/self.core_count

        self.p_crit_80 = self.core_count[(self.efficiency < 0.8) & (self.efficiency >= 0.6)][-1]
        self.p_crit_60 = self.core_count[(self.efficiency < 0.6) & (self.core_count > self.p_crit_80)][0]
        
        self.intra_node_prop_80 = self.p_crit_80 / max(self.core_count)
        self.intra_node_prop_60 = self.p_crit_60 / max(self.core_count)
    
    def parallel_efficiency_figure(self):
        '''Generates a figure of parallel efficiency against number of cores'''
        fig, ax = plt.subplots()
        ax.set_xlabel(r'$p$')
        ax.set_ylabel(r'$E(p)$')
        
        ax.axvline(x=self.p_crit_80, color="#ffc844", linestyle="--")
        ax.axvline(x=self.p_crit_60, color="#e35555", linestyle="--")
        ax.plot(self.core_count, self.efficiency, '.-', color="black", linewidth=2)

        plt.show()

    def runtimes_figure(self):
        '''Generates a figure of parallel efficiency against number of cores'''
        fig, ax = plt.subplots()
        ax.set_xlabel(r'$p$')
        ax.set_ylabel(r'$t(p)$')
        
        plt.plot(self.core_count, self.parallel_runtimes, '.-', color = 'black', linewidth=2)
        plt.plot(1, self.serial_runtime, 'r.')
        
        plt.show()

    def intra_node_perf_table(self):
        '''Generates a traffic-light table for the intra-node performance metric'''
        data = [[''], [''], ['']]
        column_headings = [r'Parallel efficiency metrics']
        row_headings = [r'$C_{\mathrm{intra}}^{80\%} \geq 0.8$', 
                        r'$C_{\mathrm{intra}}^{80\%} < 0.8 \wedge C_{\mathrm{intra}}^{60\%} \geq 0.6$', 
                        r'otherwise']

        perf_str = [r'$C_{\mathrm{intra}}^{80\%} \approx$' + f'{self.intra_node_prop_80:.3f}' 
                    + r', $C_{\mathrm{intra}}^{60\%} \approx$' + f'{self.intra_node_prop_60:.3f}']
        
        if self.intra_node_prop_80 >= 0.8:
            data[0] = perf_str
        elif self.intra_node_prop_80 < 0.8 and self.intra_node_prop_60 >= 0.6:
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