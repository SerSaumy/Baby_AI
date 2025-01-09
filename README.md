# BabyAI

**BabyAI** is a reinforcement learning project that simulates the learning process of an AI in the Minecraft world. The goal is to create an AI that starts with the ability to **see** its environment, and through exploration, learns to interact with the world (e.g., mining, moving, placing blocks) without prior knowledge of its surroundings. The project focuses on **visual perception** and **learning through trial and error**.

## Project Structure

The project is structured as follows:

```
BabyAI/
├── README.md                # Project overview and instructions
├── requirements.txt         # List of dependencies
├── docs/                    # Documentation (optional)
├── src/                     # Source code
│   ├── main.py              # Main entry point for the project
```

## Requirements

- Python 3.x
- **Mineflayer**: A Minecraft bot for interacting with the game
- **Gym**: A toolkit for developing reinforcement learning environments
- **NumPy**: For handling arrays and basic calculations

To set up the project, follow the steps below.

## Setup Instructions

### 1. Clone the repository:

```bash
git clone https://github.com/<your-username>/BabyAI.git
cd BabyAI
```

### 2. Create a virtual environment:

```bash
python -m venv venv
```

### 3. Activate the virtual environment:
- On **Windows**:
  ```bash
  venv\Scripts\Activate
  ```
- On **Mac/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 5. Run the main program:

```bash
python src/main.py
```

## Contributing

Feel free to fork the repository, make changes, and submit pull requests. Contributions are welcome!

## License

This project is open-source and available under the [MIT License](LICENSE).

Copyright

© 2025 SerSaumy. All rights reserved.