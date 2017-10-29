from random import randint
from sys import argv

script, filename = argv

#loading data from the text file#
with open(filename) as txt:
    mincut_data = []
    for line in txt:
        line = line.split()
        if line:
            num = [int(i) for i in line.split("\t")]
            mincut_data.append(num)

#extracting edges from the data #            
edgelist = []
nodelist = []
for every_list in mincut_data:
    nodelist.append(every_list[0])
    temp_list = []
    for temp in range(1,len(every_list)):
        temp_list = [every_list[0], every_list[temp]]
        flag = 0
        for ad in edgelist:
            if set(ad) == set(temp_list):
                flag = 1
        if flag == 0 :
            edgelist.append([every_list[0],every_list[temp]])


#karger min cut algorithm#
while(len(nodelist) > 2):
    val = randint(0,(len(edgelist)-1))
    print val
    target_edge = edgelist[val]
    replace_with = target_edge[0]
    should_replace = target_edge[1]
    for edge in edgelist:
        if(edge[0] == should_replace):
            edge[0] = replace_with
        if(edge[1] == should_replace):
            edge[1] = replace_with
    edgelist.remove(target_edge)
    nodelist.remove(should_replace)
    for edge in edgelist:
        if edge[0] == edge[1]:
            edgelist.remove(edge)

print ('edgelist remaining: ',edgelist)
print ('nodelist remaining: ',nodelist)