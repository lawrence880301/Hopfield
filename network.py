import numpy as np

class Hopfield:
    def __init__(self,train_list):
        self.weight, self.theta = self.train(train_list)

    def train(self,train_list):
        data_dim = len(train_list[0]) 
        data_count = len(train_list) 
        sum_of_w = np.zeros([data_dim, data_dim])

        for i in range(data_count):
            a = np.array([train_list[i]])
            b = a.transpose()
            sum_of_w = sum_of_w + (b.dot(a))
        fore = (1 / data_dim) * sum_of_w
        back = (data_count / data_dim) * np.eye(data_dim)
        w = fore - back
        theta = []
        for i in range(data_dim):
            theta.append(sum(w[i]))
        return w, theta

    def test(self, iterate, data):
        for i in range(iterate):
            for j in range(len(data)):
                current_bit = np.sign(self.weight[j].dot(data)-self.theta[j])
                if current_bit==1:
                    data[j][0]=1
                elif current_bit==-1:
                    data[j][0]=-1
            index=(data==-1) #where matrix element is -1 -> 0
            data[index]=0
        return data