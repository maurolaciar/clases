# Deploy Model MVP

This directory contains the code and resources for deploying a Machine Learning model as a Minimum Viable Product (MVP).

## Structure

- `templates/`: Contains the HTML templates for the web application.
- `main.py`: The main script for running the web application.
- `model.pkl`: The trained model saved as a pickle file.
- `requirements.txt`: A list of required Python packages.
- `README.md`: This file.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Required Python packages listed in `requirements.txt`

### Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd caece/deploy_model_mvp
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Usage

1. Run the data preprocessing script:
    ```sh
    python scripts/preprocess_data.py
    ```

2. Train the model:
    ```sh
    python scripts/train_model.py
    ```

3. Evaluate the model:
    ```sh
    python scripts/evaluate_model.py
    ```