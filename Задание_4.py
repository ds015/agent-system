import numpy as np
import gym
import matplotlib.pyplot as plt
 
env = gym.make('FrozenLake-v1', is_slippery=False, render_mode='human')
 
NUM_STATES = env.observation_space.n
NUM_ACTIONS = env.action_space.n
 
print('States: {}'.format(NUM_STATES))
print('Actions: {}'.format(NUM_ACTIONS))
 
lr     = 0.8       # learning rate
gamma  = 0.95      # параметр дисконтирования

NUM_EPISODES    = 50   # число эпизодов для обучения
MAX_STEPS       = 100  # максимальное число шагов в эпизоде 

pathLenList = []     # длины траекторий по эпизодам
totalRewardList = [] # суммарные награды по эпизодам

# Инициализация Q-функции (таблицы)
Q = np.random.rand(NUM_STATES, NUM_ACTIONS)

for i in range(NUM_EPISODES):

    observation = env.reset()[0]
    
    totalReward = 0
    step        = 0
    
    while step < MAX_STEPS:
        step += 1
        
        # Выбор действия по текущей политике
        a = np.argmax(Q[observation,:])
        
        # Сделать шаг
        ob_1, reward, terminated, truncated, info = env.step(a)
        
        # Новое целевое значение функции
        if terminated:
            Q_target = reward
        else:
            Q_target = reward + gamma * np.max(Q[ob_1, :])
            
        # Обновление Q-функции
        Q[observation, a] = (1 - lr) * Q[observation, a] + lr * Q_target
        
        totalReward += reward
        observation = ob_1
        
        #Если конец эпизода
        if terminated or truncated:
            break
            
    pathLenList.append(step)
    totalRewardList.append(totalReward)
    print('Episod {}: Total reward = {}'.format(i, totalReward))

#Отобразим длины траекторий    
plt.plot(pathLenList)
plt.grid()

# Отобразим график суммарных наград
plt.plot(totalRewardList)
plt.grid()