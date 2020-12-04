import matplotlib.pyplot as plt

r=48/255#this will come from frequency sub section
g=255/255
b=177/255
n = 10  # this will be the user's input - this is just test data for now
list_ind = [(-0.9316248171795721, 0.363421518371063), (0.952835510258892, 0.30348721618822233),
            (-0.2516567939867145, -0.9678165415203072), (0.9634205191656435, -0.26799422242018933),
            (-0.9217345199815645, 0.38782144689838244), (-0.9217345199815645, 0.38782144689838244),
            (0.9634205191656435, -0.26799422242018933), (-0.2516567939867145, -0.9678165415203072),
            (0.952835510258892, 0.30348721618822233), (-0.9316248171795721, 0.363421518371063)]
# this is a test set for this list - there will be the same no. of tuples in this list as the variable n

list_x = list()
list_y = list()
list_x.append(list_ind[0][0])
list_y.append(list_ind[0][1])
for count_n in range(1, n):  # this starts from 0 to n-1 (the first arrow is found at [0][0] and [0][1])
    list_x.append(list_ind[count_n][0] + list_x[count_n - 1])  # these lists have been formatted for final arrow
    list_y.append(list_ind[count_n][1] + list_y[(
                                                    count_n) - 1])  # each value is their original value from
    # list_ind plus all of the corresponding values summed before it

plt.plot(list_x, list_y, color=(r,g,b))
plt.plot([list_x[0],list_x[n-1]],[list_y[0],list_y[n-1]], color=(0,0,0))
plt.tick_params(axis='x', which='both',bottom=False, top=False, labelbottom=False)
plt.tick_params(axis='y', which='both', right=False, left=False, labelleft=False)
for pos in['right','top','bottom','left']:
    plt.gca().spines[pos].set_visible(False)
plt.show()
