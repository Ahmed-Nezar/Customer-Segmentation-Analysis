import os


class Utils:
    @classmethod    
    def create_directories(self, run_dir: str):
        self.log_path = os.path.join(run_dir, "logs")
        self.data_path = os.path.join(run_dir, "data")
        self.model_path = os.path.join(self.log_path, "models")
        self.plot_path = os.path.join(self.log_path, "plots")
        os.makedirs(self.log_path, exist_ok=True)
        os.makedirs(self.data_path, exist_ok=True)
        os.makedirs(self.model_path, exist_ok=True)
        os.makedirs(self.plot_path, exist_ok=True)
        print(f"Created directories: {self.log_path}, {self.data_path}, {self.model_path}")
        # Any other directories you want to create can be added here