from tqdm import tqdm
from ..monitor import Plotter

class Monitor:
    
    @staticmethod
    def run(dataset):
        plot_dir = Plotter.init()
        
        # List of all plotting tasks with their arguments
        tasks = [
            (Plotter.hitogram_plot, [dataset, 'Gender', plot_dir]),
            (Plotter.pie_chart_plot, [dataset, 'Gender', plot_dir]),
            (Plotter.scatteplot, [dataset, 'Age', 'Annual Income (k$)', plot_dir], {'hue': 'Gender'}),
            (Plotter.scatteplot, [dataset, 'Age', 'Spending Score (1-100)', plot_dir], {'hue': 'Gender'}),
            (Plotter.scatteplot, [dataset, 'Annual Income (k$)', 'Spending Score (1-100)', plot_dir], {'hue': 'Gender'}),
            (Plotter.categorical_boxplot, [dataset, 'Annual Income (k$)', 'Gender', plot_dir]),
            (Plotter.categorical_boxplot, [dataset, 'Spending Score (1-100)', 'Gender', plot_dir]),
            (Plotter.continuous_boxplot, [dataset, 'Age', plot_dir]),
            (Plotter.continuous_boxplot, [dataset, 'Annual Income (k$)', plot_dir]),
            (Plotter.continuous_boxplot, [dataset, 'Spending Score (1-100)', plot_dir]),
            (Plotter.normal_distribution_plot, [dataset, 'Age', plot_dir]),
            (Plotter.normal_distribution_plot, [dataset, 'Annual Income (k$)', plot_dir]),
            (Plotter.normal_distribution_plot, [dataset, 'Spending Score (1-100)', plot_dir]),
            (Plotter.violin_swarm_plot, [dataset, 'Age', 'Gender'], {'hue': 'Gender', 'plot_type': 'both', 'plot_dir': plot_dir}),
            (Plotter.violin_swarm_plot, [dataset, 'Annual Income (k$)', 'Gender'], {'hue': 'Gender', 'plot_type': 'both', 'plot_dir': plot_dir}),
            (Plotter.violin_swarm_plot, [dataset, 'Spending Score (1-100)', 'Gender'], {'hue': 'Gender', 'plot_type': 'both', 'plot_dir': plot_dir}),
            (Plotter.violin_swarm_plot, [dataset, 'Age', 'Gender'], {'hue': 'Gender', 'plot_type': 'swarm', 'plot_dir': plot_dir}),
            (Plotter.violin_swarm_plot, [dataset, 'Annual Income (k$)', 'Gender'], {'hue': 'Gender', 'plot_type': 'swarm', 'plot_dir': plot_dir}),
            (Plotter.violin_swarm_plot, [dataset, 'Spending Score (1-100)', 'Gender'], {'hue': 'Gender', 'plot_type': 'swarm', 'plot_dir': plot_dir}),
            (Plotter.violin_swarm_plot, [dataset, 'Age', 'Gender'], {'hue': 'Gender', 'plot_type': 'violin', 'plot_dir': plot_dir}),
            (Plotter.violin_swarm_plot, [dataset, 'Annual Income (k$)', 'Gender'], {'hue': 'Gender', 'plot_type': 'violin', 'plot_dir': plot_dir}),
            (Plotter.violin_swarm_plot, [dataset, 'Spending Score (1-100)', 'Gender'], {'hue': 'Gender', 'plot_type': 'violin', 'plot_dir': plot_dir}),
        ]
        
        # Execute tasks with progress tracking
        for task in tqdm(tasks, desc="Generating plots", unit="plot"):
            func = task[0]  # Extract the function
            args = task[1]  # Extract the positional arguments
            kwargs = task[2] if len(task) > 2 else {}  # Extract keyword arguments (if any)
            
            func(*args, **kwargs)
