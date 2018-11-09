import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from tqdm import tqdm
import anogan

def main():
	(X_train, y_train), (X_test, y_test) = mnist.load_data()
	X_train = X_train.astype(np.float32)/255.
	X_train = X_train.reshape(60000, 28, 28, 1)


	Model_d, Model_g = anogan.train(32, X_train)

if __name__ == '__main__':
	main()