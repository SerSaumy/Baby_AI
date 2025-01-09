import random
import numpy as np

class Agent:
    def __init__(self, environment):
        self.environment = environment
        self.actions = ["move", "mine", "place_block"]  # List of actions AI can perform

    def train(self):
        for episode in range(100):  # Run for 100 episodes (or more)
            state = self.environment.reset()  # Reset the environment
            done = False

            while not done:
                action = self.choose_action(state)  # Choose an action
                next_state, reward, done, _ = self.environment.step(action)  # Take the action
                state = next_state  # Update state

    def choose_action(self, state):
        # Choose a random action for simplicity (can be replaced with a better strategy)
        return random.choice(self.actions)
