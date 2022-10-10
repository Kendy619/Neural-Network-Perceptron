import random

SIZE = 3
BIAS = 0.4
LEARNING_RATE = 0.3
W=[]
INPUTS = [] 
Y=[0,1]
D=[-1,1]
TRESHOLD = 0 #CASO SEJA IGUAL OU MAIOR QUE O LIMEAR, O VALOR SERÁ 1. CASO CONTRÁRIO -1
EXPECT = [-1,1]
N = SIZE * SIZE

W.append(BIAS)

INPUTT = [[1,1,1],[0,1,0],[0,1,0]]
INPUTH = [[1,0,1],[1,1,1],[1,0,1]]

INPUTS.append([i for element in INPUTT for i in element])
INPUTS[0].insert(0,BIAS)

INPUTS.append([i for element in INPUTH for i in element])
INPUTS[1].insert(0,BIAS)

def W_inicialize(): 
    for i in range(1,N):
        W.append(random.uniform(-1,1))

def signalY(somatoria):
    if somatoria >= TRESHOLD:
        return 1
    else:
        return -1

def calc_y(x):
  v =  W[0]
  for i in range(0, N):
    v += x[i] * W[i] 
  return signalY(v)

def adjustW(input,y):
  W[0] = W[0] + LEARNING_RATE * BIAS * (EXPECT[input] - y)
  for i in range(1,N):
    W[i] = W[i] + LEARNING_RATE * INPUTS[input][i] * (EXPECT[input] - y)

def train():
  epoch = 100
  while epoch > 0:
    for i in range(len(INPUTS)):
        y = calc_y(INPUTS[i])
        if y == EXPECT[i]:
          epoch -= 1
          print("Epoch: ", epoch)
        else:
          adjustW(i,y)
          epoch = len(INPUTS)
  print(('*' * 10) + ' FIM ' + ('*' * 10))

def test(x):
    y = calc_y(x)
    if y == 1:
        return "T"
    else:
        return "H"
  
W_inicialize()
for i in range(0,len(W)):
  print(f' Weight: ({[i]}): {W[i]}')
  print('\n')


print(('-' * 10) + 'Treinamento' + ('-' * 10))
train()


print(('-' * 10) + 'Testes' + ('-' * 10))
print(f'Test Result For T is: {test([1,1,1,0,1,0,0,1,0])}')
print(f'Test Result for H is: {test([1,0,1,1,1,1,1,0,1])}')
print(f'Test Result for T is: ({test([1,1,1,0,1,1,0,1,0])})')
print(f'Test Result for T is: ({test([1,1,1,1,1,0,0,1,0])})')
print(f'Test Result for H is: ({test([1,0,1,1,0,1,1,0,1])})')
print(f'Test Result for H is: ({test([1,0,1,1,1,0,1,0,1])})')
