import gym

def policy(s):
    a = env.action_space.sample() # случайная стратегия
    return a

#'Pong-v4'
#'Assault-v4'
#'CarRacing-v4'
env = gym.make('Assault-v4', render_mode="human")

STATE_SHAPE = env.observation_space.shape
NUM_ACTIONS = env.action_space.n
ACTION_MEANING = env.unwrapped.get_action_meanings()

print('States shape: {}'.format(STATE_SHAPE))
print('Actions: {}'.format(NUM_ACTIONS))
print('Actions: {}'.format(ACTION_MEANING))

observation = env.reset()

for i in range(1000):
  a = policy(observation)
  observation, reward, terminated, truncated, info = env.step(a)
  
  if reward != 0:
    print('Reward = {}'.format(reward))

  if terminated or truncated:
    break
    
env.close()