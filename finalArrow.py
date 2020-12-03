import matplotlib.pyplot as plt
n=10 #this will be the user's input - this is just test data for now
list_ind=[(-0.9316248171795721, 0.363421518371063), (0.952835510258892, 0.30348721618822233), (-0.2516567939867145, -0.9678165415203072), (0.9634205191656435, -0.26799422242018933), (-0.9217345199815645, 0.38782144689838244), (-0.9217345199815645, 0.38782144689838244), (0.9634205191656435, -0.26799422242018933), (-0.2516567939867145, -0.9678165415203072), (0.952835510258892, 0.30348721618822233), (-0.9316248171795721, 0.363421518371063)]
#this is a test set for this list - there will be the same no. of tuples in this list as the variable n


#plt.plot(list_ind)
#plt.show()

list_x=list()
list_y=list()
for count_n in range(n-1): #this starts from 0 to n-1 (the first arrow is found at [0][0] and [0][1])
    list_x.append(list_ind[count_n][0])
    list_y.append(list_ind[count_n][1])

