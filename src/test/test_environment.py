from src.environment.minecraft_env import MinecraftEnv

def test_environment():
    # Create environment
    env = MinecraftEnv()

    # Test environment: Get random visual observation
    observation = env.get_observation()
    print("Initial Observation:", observation)

    env.close()  # Close the environment after testing

if __name__ == "__main__":
    test_environment()
