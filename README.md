# ShipSail Project

Welcome to the ShipSail project! This project is built using FastAPI, a modern, high-performance web framework for building APIs with Python. The API returns the guests' preferred ticket type based on their ranking responses.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Directory Structure](#directory-structure)
- [Authors](#authors)

## Getting Started

Follow these steps to get the project up and running on your local machine.

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 installed on your system.
- [Optional] Virtual Environment

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/crystaltys/aiap15-Crystal-Toh-Yi-Shan-747G.git

2. Navigate to the project directory:

   ```
   cd aiap15-Crystal-Toh-Yi-Shan-747G
   ```
   
3. Create a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate
   ```

4. Install project dependencies:
   ```
   pip install -r requirements.txt
   ```
   
5. Setup project configuration settings.
   Rename env file to .env and add .env file to the project directory.

6. Running the Development Server (Start the FastAPI development server):
   ```
   chmod +x run.sh
   ./run.sh
   ```
   After executing the above commands, the API will be available at http://0.0.0.0:8080/docs#.
   Configure the parameters for each response fields with its numeric value.
   <img width="1372" alt="image" src="https://github.com/crystaltys/aiap15-Crystal-Toh-Yi-Shan-747G/assets/51997682/39087817-dd7c-4253-a40f-89ffc8a7abef">
   Ticket type response is generated.
   <img width="1340" alt="image" src="https://github.com/crystaltys/aiap15-Crystal-Toh-Yi-Shan-747G/assets/51997682/077f6f5f-cfd0-4a71-98e4-1ea5839fa554">


8. Running the Exploratory Notebook:
   Add ./data/*.db files to project directory.


## Directory Structure
```
- aiap15-Crystal-Toh-Yi-Shan-747G
  - ./data
  - ./models
  - ./src
  - eda.ipynb
  - .env
  - requirements.txt
  - main.py
  - run.sh
  - app_config.yml
``` 
## Authors
| **Author**            | **Username** |
|-------------          |--------------|
| Crystal Toh Yi Shan   | tyscrystal@gmail.com   |
