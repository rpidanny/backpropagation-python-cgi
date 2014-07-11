#!/usr/bin/env python

import math
import random
import string
import decimal

import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage() 
in1 = float(form.getvalue('ip1'))
in2  = float(form.getvalue('ip2'))
in3  = float(form.getvalue('ip3'))

inputlayer =0
outputlayer=0
hiddenlayer=0

random.seed(0)

def getTopology():
    f = open("trainingdata.txt",'r')
    data=f.readline()
    global inputlayer
    global outputlayer
    global hiddenlayer
    if(data!= 'network:'):
        inputlayer=int(f.readline())
        hiddenlayer=int(f.readline())
        outputlayer=int(f.readline())
        number=int(f.readline())
    else:
        print '<h2>Wrong Config file.</h2>'
    f.close()

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
                self.wo[j][k] = rand(-2.0, 2.0)
        self.ci = matr(self.ni, self.nh)
        self.co = matr(self.nh, self.no)

    def forwardProp(self, inputs,roundoff=10):
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
            print (self.ao[k])
        return self.ao[:]

    def test(self, patterns):
        for p in patterns:
            print ('The Output is')
            self.forwardProp(p[0],1)

    def loadWeights(self,filename = 'weights.txt'):
        f = open(filename,'r')
        for j in range(self.nh):
            for i in range(self.ni):
                self.wi[i][j] = float(f.readline())

        for k in range(self.no):
            for j in range(self.nh):
                self.wo[j][k]=float(f.readline())
        f.close()
        
if __name__ == '__main__':
    print 'Content-type: text/html\r\n\r'
    print '<head>'
    print '<title>Result</title>'
    print '<link rel="stylesheet" type="text/css" href="css/style.css">'
    print '</head>'
    print '<html>'
    print '<h1>Result : </h1>'
    getTopology()
    patern=[[[in1,in2,in3],[0.0]]]
    net1 = NeuralNet(inputlayer, hiddenlayer, outputlayer)
    net1.loadWeights()
    net1.test(patern)
    print '</html>'
