with open ('file.txt','r') as f:
            for line in f:
                line=line.split(',')
                line[5]=line[5][:-1]
                print(line)