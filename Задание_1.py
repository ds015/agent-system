import gym

# Стратегия движения
def policy(s):
    #a = env.action_space.sample() # случайная стратегия
    
    if s == 0:
      a = 1
    elif s == 4:
      a = 1
    elif s == 8:
      a = 2
    elif s == 9:
      a = 2
    elif s == 10:
      a = 1
    elif s == 14:
      a = 2

    return a

env = gym.make('FrozenLake-v1', render_mode='single_rgb_array', new_step_api=True, is_slippery=False)

NUM_STATES = env.observation_space.n
NUM_ACTIONS = env.action_space.n

print('States: {}'.format(NUM_STATES))
print('Actions: {}'.format(NUM_ACTIONS))

observation = env.reset()[0]

for i in range(10):
  a = policy(observation)
  observation, reward, terminated, truncated, info = env.step(a)
  
  if reward != 0:
    print('Reward = {}'.format(reward))

  if terminated or truncated:
    break

env.render()        