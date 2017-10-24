import sys
from numpy import *


def rss_data(error, iteration):
    with open("rss.csv", "a+") as rss:
        rss.write(str(error) + ',' + str(iteration) + '\n')
        print(str(error) + ',' + str(iteration))
    rss.close() 


def compute_error_for_points(b, m, points):
    # error, loss
    # sum of the squared errors sse
    
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (m * x + b)) **2
        
    averageError = totalError/float(len(points))
    return averageError


def step_gradient(b_current, m_current, points, learning_rate):
    # how gradient descent works
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    
    for i in range(0, len(points)):
        x = points[i,0]
        y = points[i,1]
        
        b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
        
    new_b = b_current - (learning_rate * b_gradient)
    new_m = m_current - (learning_rate * m_gradient)
    
    return [new_b, new_m]


def gradient_descent_runner(points, starting_b, starting_m, learning_rate, iterations):
    b = starting_b
    m = starting_m
    
    for i in range(iterations):
        b,m = step_gradient(b, m, array(points), learning_rate)
        error = compute_error_for_points(b, m, points)
        #print("RSS: ", error)
        rss_data(error, i)
    return [b,m]


def run(learningRate, numIterations):
    points = genfromtxt('data/income.csv', delimiter = ",")
    
    learning_rate = learningRate 
    initial_b = 0 # y = mx + b
    initial_m = 0
    iterations = numIterations
    
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, iterations)
    
    #print("RSS : ", compute_error_for_points(b, m, points))
    print("Equation: y = ", m, "x + ", b)
    

if __name__ == "__main__":
    run(0.001, 1000)