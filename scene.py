import mysql.connector
import matplotlib.pyplot as plt

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='$£Jeixn32£',
    database='qeddatabase'
)
if mydb.cursor:
    print("done")
else:
    print("connection failed")
#creating cursor object to traverse resultset
cur=mydb.cursor()
# cur.execute("SHOW DATABASES")
# for row in cur:
#     print(row)
# mydb.close()
height = 100
constant_source_x = -50
constant_detector_x = 50
red=0.1888693526133274
green=1.0
blue=0.686159189832137
#will take colour values from main global variables when added onto combined
n=10
n_query=str(n)
# query="select * from path_table where id_n="+n_query
# try:
#     cur.execute(query)
#     print("Query Executed Successfully")
#     list=list()
#     for row in cur:
#         print(row)
# except Exception as e:
#     print("Invalid Query")
#     print(e)
# mydb.close()
list=list()
for count in range(1,n+1):
    count_n=str(count)
    query_2 = "select path_"+count_n+" from path_table where id_n="+n_query
    try:
        cur.execute(query_2)
        for row in cur:
            row=str(row)
            row=row.replace('(','')
            row=row.replace(')','')
            row=row.replace(',','')
            row=float(row)
            list.append(row)
    except Exception as e:
        print("Invalid Query")
        print(e)
mydb.close()
# print(list)

scene_img=plt.imread("scene.png")
fig, ax = plt.subplots()
ax.imshow(scene_img, extent=[-65,65,-10,120])
for count in range(0,n):
    plt.plot([constant_source_x,list[count],constant_detector_x],[height,0,height], color=(red, green,
                                    blue))#value 0 is reflection y value
    plt.xlim(-65, 65)
    plt.ylim(-10, 120)
    plt.tick_params(axis='x', which='both', bottom=False, top=False,
                    labelbottom=False)  # taken from pythonmatplotlibtips.blogspot.com, see references for link
    plt.tick_params(axis='y', which='both', right=False, left=False,
                    labelleft=False)  # removes axis labels, lines and ticks
    for pos in ['right', 'top', 'bottom', 'left']:
        plt.gca().spines[pos].set_visible(False)
    plt.tight_layout()
    plt.savefig('graph_scene.png')
# plt.show()
plt.clf()
