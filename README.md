# BabyAI

BabyAI is an AI project designed to simulate how a baby learns in a Minecraft world. The AI can only "see" the world around it and must figure out how to interact with its environment (like moving, mining, etc.) through trial and error. The goal is to create an agent that can learn from its surroundings using reinforcement learning.

## Introduction
BabyAI is inspired by **Emergent Garden**, who has created a similar AI system in Minecraft using reinforcement learning. The goal of this project is to provide a foundational AI model that learns autonomously, with limited capabilities, and can interact with the Minecraft environment.

## Setup Guide
To get started with BabyAI, follow these steps:

**Clone the repository:**
   ```bash
   git clone https://github.com/SerSaumy/BabyAI.git
```
**Install dependencies:**
```bash
pip install -r requirements.txt
```
**Install Node.js and Mineflayer (for Minecraft interaction):**
copy code
```bash
npm install mineflayer
```
### Run the bot:
```bash
node bot.js
```
# Usage
BabyAI is designed to connect to a Minecraft world where it will attempt to learn from its environment. The bot will start, and the AI will make decisions based on its visual input (a 3x3 grid of blocks). To interact with the world, BabyAI uses no actions for now because I want it to figure out itself but if he cant then we'll add basic actions.

For now the bot only spawns in the world and stare does nothing but I and working

To run the AI, use the following commands:
``` 
bash
python main.py
```
# Contributing
I welcome contributions to BabyAI! If you want to help improve the project or add new features, please fork the repository and submit a pull request. Here's how you can contribute:

Fork the repository.
Make your changes in a new branch.
Write tests for any new functionality.
Ensure your code follows the project’s coding style.
Submit a pull request for review.
We appreciate all contributions, no matter how big or small!

# Acknowledgments
Special thanks to Emergent Garden (Kolbytn on GitHub) for inspiring the creation of this project. BabyAI is based on the principles from Emergent Garden's work and his approach to reinforcement learning in Minecraft. You can check out his projects:

[Emergent Garden's YouTube Channe](https://www.youtube.com/@EmergentGarden)

[Kolbytn's GitHub](https://www.github.com/koblynt)

Feel free to ask questions or report issues by opening an issue in the GitHub repository.

