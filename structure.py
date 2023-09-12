import os

# Define the project root directory
project_root = "TradeAnalytica"

# Define the directory structure
directories = [
    "data/raw_data",
    "data/processed_data",
    "analysis",
    "machine_learning",
    "gradio",
    "deployment/aws_deploy",
    "deployment/heroku_deploy",
    "deployment/docker",
    "tests/unit_tests",
    "tests/integration_tests",
    "docs",
    "assets/images"
]

# Create directories
for directory in directories:
    path = os.path.join(project_root, directory)
    os.makedirs(path, exist_ok=True)

# Create empty files
files = ["data/data_preparation.ipynb",
         "analysis/exploratory_data_analysis.ipynb",
         "analysis/trade_insights.ipynb",
         "gradio/gradio_app.py",
         "README.md",
         "LICENSE",
         ".gitignore"]

for file in files:
    path = os.path.join(project_root, file)
    open(path, 'a').close()

print(f"Project file structure created in '{project_root}' directory.")
