#!/usr/bin/env python

import math
import random
import string
import decimal

random.seed(0)

td = []
inputlayer =0
outputlayer=0
hiddenlayer=0

def appendInputMatrix(mat):
    matt=mat[:]
    return matt[:]

def getTopology():
    f = open("trainingdata.txt",'r')
    data=f.readline()
    
    number=0
    patern = [[[]]]
    x=0
    temp =0
    im = []
    om = []
    global inputlayer
    global outputlayer
    global hiddenlayer
    if(data!= 'network:'):
        inputlayer=int(f.readline())
        hiddenlayer=int(f.readline())
        outputlayer=int(f.readline())
        number=int(f.readline())
        print 'Input : ',inputlayer,' Hidden : ',hiddenlayer,' Output : ',outputlayer,' Number : ',number,'<br><br>'

        for x in range(0,number):
            globals()["InputVar{0}".format(x)]=[]
        for x in range(0,number):
            globals()["OutputVar{0}".format(x)]=[]
        varcount=0
        countline=0
        while True:
            if(f.readline()!=''):
                im[:] = []
                om[:] = []
                for j in range(inputlayer):
                    tempdata=f.readline()
                    im.append(float(tempdata))
                globals()["InputVar{0}".format(countline)]=im[:] 
                for k in range(outputlayer):
                    tempdata=f.readline()
                    om.append(int(tempdata))
                globals()["OutputVar{0}".format(countline)]=om[:]
                td.append([globals()["InputVar{0}".format(countline)],globals()["OutputVar{0}".format(countline)]])
                countline+=1
            else:
                break
        print countline,' Training Data Obtained!<br>'
    f.close()
    return td
    
    
def rand(a, b):
    return (b-a)*random.random() + a

def matr(I, J, fill=0.0):
    m = []
    for i in range(I):
        m.append([fill]*J)
    return m

def transferFxn(x):
    return math.tanh(x)


def dtransferFxn(y):
    return 1.0 - y**2

class NeuralNet:
    def __init__(self, ni, nh, no):
        self.ni = ni + 1 
        self.nh = nh
        self.no = no
        self.ai = [1.0]*self.ni
        self.ah = [1.0]*self.nh
        self.ao = [1.0]*self.no

        self.wi = matr(self.ni, self.nh)
        self.wo = matr(self.nh, self.no)

        for i in range(self.ni):
            for j in range(self.nh):
                self.wi[i][j] = rand(-0.2, 0.2)
        for j in range(self.nh):
            for k in range(self.no):
                self.wo[j][k] = rand(-1.0, 1.0)
  
        self.ci = matr(self.ni, self.nh)
        self.co = matr(self.nh, self.no)

    def forwardProp(self, inputs,roundoff=20):
        if len(inputs) != self.ni-1:
            raise ValueError('Invalid Input Number.')

        for i in range(self.ni-1):
            self.ai[i] = inputs[i]

        for j in range(self.nh):
            sum = 0.0
            for i in range(self.ni):
                sum = sum + self.ai[i] * self.wi[i][j]
            self.ah[j] = transferFxn(sum)

        for k in range(self.no):
            sum = 0.0
            for j in range(self.nh):
                sum = sum + self.ah[j] * self.wo[j][k]
            self.ao[k] = round(transferFxn(sum),roundoff)

        return self.ao[:]


    def backProp(self, targets, N, M):
        if len(targets) != self.no:
            raise ValueError('wrong number of target values')


        output_deltas = [0.0] * self.no
        for k in range(self.no):
            error = targets[k]-self.ao[k]
            output_deltas[k] = dtransferFxn(self.ao[k]) * error

        hidden_deltas = [0.0] * self.nh
        for j in range(self.nh):
            error = 0.0
            for k in range(self.no):
                error = error + output_deltas[k]*self.wo[j][k]
            hidden_deltas[j] = dtransferFxn(self.ah[j]) * error

        for j in range(self.nh):
            for k in range(self.no):
                change = output_deltas[k]*self.ah[j]
                self.wo[j][k] = self.wo[j][k] + N*change + M*self.co[j][k]
                self.co[j][k] = change

        for i in range(self.ni):
            for j in range(self.nh):
                change = hidden_deltas[j]*self.ai[i]
                self.wi[i][j] = self.wi[i][j] + N*change + M*self.ci[i][j]
                self.ci[i][j] = change


        error = 0.0
        for k in range(len(targets)):
            error = error + 0.5*(targets[k]-self.ao[k])**2
        return error

    def train(self, patterns, iterations=1000, N=0.2, M=0.1):
        Itmax=999999
        ItError=0.0001
        for i in range(Itmax):
            error = 0.0
            for p in patterns:
                inputs = p[0]
                targets = p[1]
                self.forwardProp(inputs)
                error = error + self.backProp(targets, N, M)
            if(error<=ItError):
                print '<h2>Training Completed at ',i,'th Itterations</h2><br>'
                break
                
    def saveWeights(self,filename = 'weights.txt'):
        f = open(filename,'w')

        for j in range(self.nh):
            for i in range(self.ni):
                temp = round(self.wi[i][j],9)
                f.write(repr(temp))
                f.write('\n')

        for k in range(self.no):
            for j in range(self.nh):
                temp = round(self.wo[j][k],9)
                f.write(repr(temp))
                f.write('\n')
        f.close()
        
if __name__ == '__main__':
    print 'Content-type: text/html\r\n\r\n'
    print '<html>'
    print '<head>'
    print '<title>Train AI</title>'
    print '<link rel="stylesheet" type="text/css" href="css/style.css">'
    print '</head>'
    print '<h1>Training</h1>'
    trainingpatern=getTopology()
    n = NeuralNet(inputlayer, hiddenlayer, outputlayer)
    n.train(trainingpatern,2000)
    n.saveWeights()
    print '</html>'

