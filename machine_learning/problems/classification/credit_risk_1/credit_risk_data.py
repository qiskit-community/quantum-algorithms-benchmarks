from qiskit.circuit.library import ZZFeatureMap
from qiskit.circuit.library import RealAmplitudes
from qiskit.algorithms.optimizers import COBYLA
from qiskit_machine_learning.algorithms.classifiers import VQC
from qiskit_aer import AerSimulator

import numpy as np
from sklearn.metrics import accuracy_score, recall_score, precision_score

import time
import csv
import _pickle as cPickle
import bz2

#Load Data
train_data = cPickle.load(bz2.BZ2File('../../../datasets/credit_risk_data/train.pbz2', 'rb'))
test_data = cPickle.load(bz2.BZ2File('../../../datasets/credit_risk_data/test.pbz2', 'rb'))
X_train, y_train = train_data.iloc[:, 0:len(train_data.columns)-1], train_data.iloc[:, len(train_data.columns)-1]
X_test, y_test = test_data.iloc[:, 0:len(test_data.columns)-1], test_data.iloc[:, len(test_data.columns)-1]
# Constract Ansatz

num_features = len(X_train.columns)

feature_map = ZZFeatureMap(feature_dimension=num_features, reps=2, entanglement='linear')
ansatz = RealAmplitudes(num_qubits=num_features, reps=5, entanglement='linear')

optimizer = COBYLA(maxiter=0) #100

params = np.load('trained_params.npy')

# print(params.tolist())

header = ['loss', 'params']

with open('training_progress.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)

def callback(params, loss):
    with open('training_progress.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        # write the data
        writer.writerow([loss, params])
    return

vqc = VQC(
    quantum_instance=AerSimulator(method='matrix_product_state'),
    feature_map=feature_map,
    ansatz=ansatz,
    initial_point=params,
    optimizer=optimizer,
    callback = callback
)
t0 = time.time()
vqc.fit(X_train.to_numpy(), y_train.to_numpy())
print('Time to train ', time.time()-t0)

print('Fit result ', vqc._fit_result)
print('Loss ', vqc._fit_result[0])

# print('Train Score', vqc.score(X_train.to_numpy(), y_train.to_numpy()))
# print('Test Score',  vqc.score(X_test.to_numpy(), y_test.to_numpy()))

# print('Train Accuracy', accuracy_score(y_train.to_numpy(), vqc.predict(X_train.to_numpy())))
# print('Test Accuracy', accuracy_score(y_test.to_numpy(), vqc.predict(X_test.to_numpy())))

print('Train Recall', recall_score(y_train.to_numpy(), vqc.predict(X_train.to_numpy())))
print('Test Recall', recall_score(y_test.to_numpy(), vqc.predict(X_test.to_numpy())))

print('Train Precision', precision_score(y_train.to_numpy(), vqc.predict(X_train.to_numpy())))
print('Test Precision', precision_score(y_test.to_numpy(), vqc.predict(X_test.to_numpy())))


trained_params = vqc.weights
print(trained_params)
# np.save('trained_params.npy', trained_params)

