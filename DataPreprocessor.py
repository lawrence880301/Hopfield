import random
class Datapreprocessor():
    def __init__(self) -> None:
        pass

    def readfile(url):
        read = open(url)
        file = read.readlines()
        read.close()
        return file

    def generate_list(file):
        data_list=[]
        data=[]
        num_per_line=0
        for line in file:
            if len(line) != 1: #if line!=empty
                num_per_line = len(line)
                for c in line:
                    # print(c)
                    if c!='\n':
                        if c=='1':
                            data.append(int(c))
                        else:
                            data.append(-1)

            else:
                data_list.append(data)
                data=[]

        data_list.append(data)
        data=[]
        return data_list,num_per_line



