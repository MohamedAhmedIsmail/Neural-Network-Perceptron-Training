import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
class Perceptron(object):
   def __init__(self, rate = 0.01, niter = 10):
      self.rate = rate
      self.niter = niter

   def fit(self, X, y):
      self.weight = np.zeros(1 + X.shape[1])
      self.errors = [] 
      for i in range(self.niter):
         err = 0
         for xi, target in zip(X, y):
            delta_w = self.rate * (target - self.predict(xi))
            self.weight[1:] += delta_w * xi
            self.weight[0] += delta_w
            
            err += int(delta_w != 0.0)
         self.errors.append(err)
      return self

   def net_input(self, X):
    
      return np.dot(X, self.weight[1:]) + self.weight[0]

   def predict(self, X):
     
      return np.where(self.net_input(X) >= 0.0, 1, -1)
    
def plot(X, y, classifier, resolution=0.02):
   # setup marker generator and color map
   markers = ('s', 'x', 'o', '^', 'v')
   colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
   cmap = ListedColormap(colors[:len(np.unique(y))])

   # plot the decision surface
   x1_min, x1_max = X[:,  0].min() - 1, X[:, 0].max() + 1
   x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
   xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
   np.arange(x2_min, x2_max, resolution))
   Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
   Z = Z.reshape(xx1.shape)
   plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
   plt.xlim(xx1.min(), xx1.max())
   plt.ylim(xx2.min(), xx2.max())

   
   for idx, cl in enumerate(np.unique(y)):
      plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],
      alpha=0.8, c=cmap(idx),
      marker=markers[idx], label=cl)
      





df = pd.read_csv('N.csv')
y = df.iloc[:100, 4].values
y=np.where(y=='Iris-setosa',-1,1)
X = df.iloc[:100, [0, 1]].values

x1=int(input("Enter the first Number: "))
x2=int(input("Enter the second Number: "))

B = df.iloc[0:150, [x1, x2]].values
plt.scatter(B[:50, 0], B[:50, 1], color='red', marker='o', label='setosa')
plt.scatter(B[50:100,0],B[50:100,1],color='blue',marker='x',label='versicolor')
plt.scatter(B[100:150,0],B[100:150,1],color='green',marker='+',label='verginica')

plt.xlabel('Petal Length')
plt.ylabel('Sepal Length')
plt.legend(loc='upper left')
plt.show()




pn = Perceptron(0.1, 10)
pn.fit(X, y)
plt.plot(range(1, len(pn.errors) + 1), pn.errors, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Number of misclassifications')
plt.show()
plot(X, y, classifier=pn)
plt.xlabel('sepal length')
plt.ylabel('petal length')
plt.legend(loc='upper left')
plt.show()