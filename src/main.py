import gym
import mineflayer
from ai.agent import Agent
from environment.minecraft_env import MinecraftEnv

def main():
    # Set up the Minecraft environment for the AI
    env = MinecraftEnv()

    # Initialize the AI agent
    agent = Agent(env)

    # Run the training process (AI learning)
    agent.train()

if __name__ == "__main__":
    main()
