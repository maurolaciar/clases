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

1. Run main.py script:
    ```sh
    python main.py
    ```

### Google Cloud deployment

1. Create a new project in Google Cloud Platform.

2. Go to compute engine and create a new VM instance.

   #### VM basics:

   a. Name the instance: `instance-reglineal`

   b. Select the region and zone: `us-central (Iowa)` `Any`
   
   c. VM provisioning model: `Spot`

   #### Machine configuration:

   a. Series: `E1`

   b. Machine type: `e2-micro`

   #### OS and storage:

   Name `instance-reglineal`

   Type `New balanced persistent disk`
   
   Size `10 GB`
   
   Snapshot schedule `No schedule selected`
   
   Licence type `Free`
   
   Image `Debian GNU/Linux 12 (bookworm)`

   #### Firewall:

   a. Allow HTTP traffic

   b. Allow HTTPS traffic

   #### Advanced:

   a. Automation: startup script (optional)

3. Firewall rules

   a. Go to the VPC network > Firewall rules.

   b. Create a new firewall rule with the following settings:
   
   Name: `allow-8000`
   
   Targets: `All instances in the network`
   
   Source IP ranges: `0.0.0.0/0`

   Protocols and ports: Allow all

4. Connect to the VM instance using SSH.

5. Update the package list and install the required packages:
    ```sh
    sudo apt update
    sudo apt install python3 pip
    sudo apt install git
    sudo apt -y install python3.11-venv
    ```

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

6. Clone the repository and install the required packages.

   git clone https://github.com/maurolaciar/clases.git


7. Move to the folder, install reqs and run the main.py script.
   ```sh
   cd clases/deploy_model_mvp
   pip install -r requirements.txt
   python3 main.py
   ```

8. Go to the external IP address of the VM instance to access the web application on port 8000.

   e.g. `http://externalipaddress:8000/`
