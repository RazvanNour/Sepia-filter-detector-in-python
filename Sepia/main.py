import numpy as np
import subprocess

exe = "C:/Users/PycharmProjects/exiftool.exe"
def obtainData(input_file, exe):
    metadata=[]
    process=subprocess.Popen([exe,input_file], stdout=subprocess.PIPE,stderr=subprocess.STDOUT, universal_newlines=True)
    for output in process.stdout:
        info={}
        line=output.strip().split(":")
        info[line[0].strip()]=line[1]
        metadata.append(info)
    for e in metadata:
        print(e)

def readData():
    inputs1 = []
    inputs2 = []
    outputs = []
    f=open("sepia.data", "r")
    c=f.readline()
    while (c!=""):
        v = c.split(", ")
        inputs1.append(float(v[0]))
        inputs2.append(float(v[1]))
        outputs.append(int(v[2]))
        c=f.readline()
    return inputs1, inputs2, outputs
inputs1, inputs2, out=readData()
class NeuralNetwork():
    def __init__(self):
        np.random.seed(1)
        self.synaptic_weights =  2*np.random.random((2, 1)) - 1
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    def sigmoid_derivative(self, x):
        return x * (1 - x)
    def train(self, training_inputs, training_outputs, epochs):
        for iteration in range(epochs):
            # Pass training set through the neural network
            output = self.calculate(training_inputs)
            # Calculate the error rate
            error = training_outputs - output
            error*=np.exp(-40)
            #print (error)
            # Multiply error by input and gradient of the sigmoid function
            # Less confident weights are adjusted more through the nature of the function
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))
            # Adjust synaptic weights
            self.synaptic_weights += adjustments
    def calculate(self, inputs):
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output


np.random.seed(6)
indexes = [i for i in range(len(inputs1))]
trainSample1 = np.random.choice(indexes, int(0.8 * len(inputs1)), replace = False)
testSample1 = [i for i in indexes  if not i in trainSample1]
trainInputs1 = [inputs1[i] for i in trainSample1]
testInputs1 = [inputs1[i] for i in testSample1]
np.random.seed(6)
indexes = [i for i in range(len(inputs2))]
trainSample2 = np.random.choice(indexes, int(0.8 * len(inputs1)), replace = False)
testSample2 = [i for i in indexes  if not i in trainSample2]
trainInputs2 = [inputs2[i] for i in trainSample2]
testInputs2 = [inputs2[i] for i in testSample2]

trainOutputs = [out[i] for i in trainSample1]
testOutputs = [out[i] for i in testSample1]
# Initialize the single neuron neural network
neural_network = NeuralNetwork()
print("Valoarea conexiunilor sinaptice la inceput: ")
print(neural_network.synaptic_weights)

ar=[]
for i in range(len(trainInputs1)):
    ar.append([trainInputs1[i],trainInputs2[i]])
training_inputs = np.array(ar)
print(trainOutputs)
training_outputs = np.array([trainOutputs]).T
# Train the neural network
neural_network.train(training_inputs, training_outputs, 10000)
print("Valoarea conexiunilor sinaptice dupa training: ")
print(neural_network.synaptic_weights)
rez=[]
arra=[]
for i in range(len(testInputs1)):
    arra.append([testInputs1[i],testInputs2[i]])
print("Output data: ")
for i in arra:
    print (float(neural_network.calculate(np.array(i))))
    if float(neural_network.calculate(i))<0.2:
        print(0)
        rez.append(0)
    else:
        print(1)
        rez.append(1)
print (testOutputs)
#print (arra)
z=0
for i in range(len(testOutputs)):
    if testOutputs[i]==rez[i]:
        z+=1
acc=z/len(testOutputs)*100
print ("Acuratetea este: ", acc, "%")

