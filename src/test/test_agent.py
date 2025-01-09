from ai.agent import Agent
from environment.minecraft_env import MinecraftEnv

def test_agent():
    # Create environment and agent
    env = MinecraftEnv()
    agent = Agent(env)

    # Train agent for a few episodes to test
    agent.train(episodes=10)

    # Clean up
    agent.close()

if __name__ == "__main__":
    test_agent()
