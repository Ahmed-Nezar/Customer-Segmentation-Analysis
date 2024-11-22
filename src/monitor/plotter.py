import matplotlib.pyplot as plt
import seaborn as sns
import os
from ..utils import Utils

class Plotter:
    
    @staticmethod
    def init():
        Plotter.seaborn_palette()
        _, _, _, plot_dir = Utils.get_dir()
        return plot_dir
    
    @staticmethod
    def seaborn_palette(palette: str = 'Set2'):
        sns.set_palette(palette)

    @staticmethod
    def hitogram_plot(data, key, plot_dir):
        plt.figure(figsize=(10, 6))
        sns.histplot(data, x=key, bins=3, hue=key, multiple="stack")
        plt.title(f"Distribution of {key}")
        plt.xlabel(key)
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.savefig(os.path.join(plot_dir, f"hitogram_plot_{key}.png"))
        plt.close() 
        
    @staticmethod
    def pie_chart_plot(data, key, plot_dir):
        plt.figure(figsize=(10, 6))
        data[key].value_counts().plot.pie(autopct='%1.1f%%')
        plt.title(f"Distribution of {key}")
        plt.tight_layout()
        plt.savefig(os.path.join(plot_dir, f"pie_chart_plot_{key}.png"))
        plt.close()
    
    @staticmethod
    def scatteplot(df, x, y, plot_dir, hue = None):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x=x, y=y, hue=hue)
        plt.title(f"{x} vs {y}")
        plt.tight_layout()
        plt.savefig(os.path.join(plot_dir, f"scatterplot_{x}_{y}.png"))
        plt.close()
    
    @staticmethod
    def categorical_boxplot(df, x, y, plot_dir):
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df, x=x, y=y, hue=y)
        plt.title(f"{x} vs {y}")
        plt.tight_layout()
        plt.savefig(os.path.join(plot_dir, f"categorical_boxplot_{x}_{y}.png"))
        plt.close()

    @staticmethod 
    def continuous_boxplot(df, key, plot_dir):
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=df[key])
        plt.title(f"Box plot of {key}")
        plt.tight_layout()
        plt.savefig(os.path.join(plot_dir, f"continuous_boxplot_{key}.png"))
        plt.close()
    
    @staticmethod
    def normal_distribution_plot(df, key, plot_dir):
        plt.figure(figsize=(10, 6))
        sns.kdeplot(df[key], fill=True, color='blue')
        plt.grid(True)
        plt.title(f"Normal distribution of {key}")
        plt.tight_layout()
        plt.savefig(os.path.join(plot_dir, f"normal_distribution_plot_{key}.png")) 
        plt.close()
    
    @staticmethod
    def violin_swarm_plot(df, x, y, hue, plot_dir, plot_type='violin'):
        plt.figure(figsize=(10, 6))
        if plot_type == 'violin':
            sns.violinplot(data=df, x=x, y=y, hue=hue)
        elif plot_type == 'swarm':
            sns.swarmplot(data=df, x=x, y=y, hue=hue)
        elif plot_type == 'both':
            sns.violinplot(data=df, x=x, y=y, hue=hue)
            sns.swarmplot(data=df, x=x, y=y, hue=hue, palette='dark:black')
        else:
            raise ValueError("Invalid plot type")
        plt.title(f"Violin Plot for {x}")
        plt.tight_layout()
        plt.savefig(os.path.join(plot_dir, f"violin_swarm_plot{x}_{y}_{plot_type}.png"))
        plt.close()
    
    

