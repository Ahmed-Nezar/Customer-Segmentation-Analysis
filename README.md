# Customer-Segmentation-Analysis
This project provides a comprehensive framework for analyzing customer data to derive meaningful insights and perform segmentation. It includes scripts for preprocessing raw data, training machine learning models, and generating visualizations. The structure is modular, with separate components for preprocessing, utilities, and runtime logs. The project is ideal for marketing analysis, customer behavior understanding, and predictive analytics. Its clear organization ensures easy extensibility for new data or features.

# Table of Contents
- [Project Overview](#project-overview)
- [Team Members](#team-members)
- [Datasets](#datasets)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [License](#license)


## Project Overview
Customer segmentation is a powerful tool for enhancing business strategies by identifying unique customer groups with similar attributes. This project leverages clustering algorithms to classify customers based on demographic and behavioral data. It enables companies to develop tailored marketing campaigns, optimize resource allocation, and improve customer satisfaction.

The project is structured into modules, including data preprocessing, clustering implementation, and visualization of results. Logs and saved models are systematically organized, ensuring a clean workflow for experimentation and scalability.

## Team Members
> - [Ahmed Nezar](https://github.com/Ahmed-Nezar)
> - [Seif Yasser](https://github.com/Seif-Yasser-Ahmed)
> - [Kirollos Ehab](https://github.com/KirollosEMH)
> - [Mohamed Yasser](https://github.com/mohammedYasser11)
> - [Omar Ahmed](https://github.com/Omarbayom)
> - [AbdulRahman Hesham](https://github.com/AHKSASE2002)

## Datasets

We used the [Mall Customers](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python) dataset in our experiments.

## Project Structure

```bash
├───main.py                   # Main script to run the analysis
├───run_dir                   # Directory for runtime or experiment-related files
│   ├───data                  # Stores input datasets and processed data
│   └───logs                  # Directory to log runtime information
│       ├───models            # Saved machine learning models and checkpoints
│       └───plots             # Generated visualizations and plots for analysis
└───src                       # Source code for data processing and analysis
    ├───__init__.py              # Marks this directory as a Python package
    ├───preprocessing            # Directory for data preprocessing logic
    │   ├───__init__.py          # Marks this subdirectory as a Python package
    │   └───preprocessor.py      # Script containing functions to preprocess the data
    └───utils                    # Utility scripts for various helper functions and configurations
        ├───__init__.py          # Marks this subdirectory as a Python package
        └───utils.py             # Contains helper functions for file handling, logging, and configuration
  ```

## Installation

1. Clone the Code Repository

```bash
git clone https://github.com/Ahmed-Nezar/Customer-Segmentation-Analysis.git
```
2. Navigate to the project directory
   
```bash
cd Customer-Segmentation-Analysis
```
3. Install Denpendencies

```bash
pip install -r requirements.txt
```
4. Run the Project
   
```bash
python main.py
```

## License
This project is licensed under the MIT LICENSE. See the [`LISENCE`](LICENSE) file for more details.
