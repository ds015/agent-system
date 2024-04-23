import numpy as np
import gym

env = gym.make('FrozenLake-v1', render_mode="human", is_slippery=False)

NUM_STATES  = env.observation_space.n
NUM_ACTIONS = env.action_space.n

print('States: {}'.format(NUM_STATES))
print('Actions: {}'.format(NUM_ACTIONS))

#Q = np.random.rand(NUM_STATES, NUM_ACTIONS)
Q = [
 [0, 0, 1, 0],  #0
 [0, 0, 1, 0],  #1
 [0, 1, 0, 0],  #2
 [0, 0, 0, 0],  #3
 [0, 0, 0, 0],  #4
 [0, 0, 0, 0],  #5
 [0, 1, 0, 0],  #6
 [0, 0, 0, 0],  #7
 [0, 0, 0, 0],  #8
 [0, 0, 0, 0],  #9
 [0, 1, 0, 0],  #10
 [0, 0, 0, 0],  #11
 [0, 0, 0, 0],  #12
 [0, 0, 0, 0],  #13
 [0, 0, 1, 0],  #14
 [0, 0, 1, 0]   #15
 ]

observation = env.reset()[0]

for i in range(10):
    
    a = np.argmax(Q[observation])
    observation, reward, terminated, truncated, info = env.step(a)
      
    if reward != 0:
        print('Reward = {}'.format(reward))

    if terminated or truncated:
        break

env.render()  