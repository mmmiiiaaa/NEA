import tkinter as tk
from PIL import ImageTk

root = tk.Tk()
root.title("QED Calculations")

main_frame=tk.Frame(root) #width=1000, height=600
final_canvas=tk.Canvas(main_frame, width=640, height=480, bg="yellow")
scrolling_frame=tk.Frame(main_frame, width=1600, height=160, bg="red")
scene_canvas=tk.Canvas(main_frame,width=640, height=480, bg="green")
controls_frame=tk.Frame(main_frame, width=320, height=480, bg="blue")

frequency_canvas=tk.Canvas(controls_frame, width=100, height=10, bg='purple')

final_image=ImageTk.PhotoImage(file="finalArrow.png")
final_canvas.create_image(640,480, image=final_image, anchor='se')

# final_img=ImageTk.PhotoImage(Image.open("finalArrow.png"))
# final_canvas.create_image(640,480, anchor='n', image=final_img)

scene_image=ImageTk.PhotoImage(file="graph_scene.png")
scene_canvas.create_image(640,480, image=scene_image, anchor='se')

# controls_frame.columnconfigure(0,weight=1)
# controls_frame.columnconfigure(0,weight=3)
calculate_button= tk.Button(controls_frame, text="CALCULATE")
frequency_spinbox=tk.Spinbox(controls_frame)
#requency_image= TODO: make a frequency image that updates
n_spinbox=tk.Spinbox(controls_frame)
save_button=tk.Button(controls_frame, text="SAVE")
retrieve_button=tk.Button(controls_frame, text="RETRIEVE")

main_frame.grid(column=0,row=0)
final_canvas.grid(column=6,row=0, columnspan=4,rowspan=3)
scrolling_frame.grid(column=0, row=5, columnspan=10, rowspan=1)
scene_canvas.grid(column=2, row=0, columnspan=4, rowspan=3)
controls_frame.grid(column=0,row=0, columnspan=2,rowspan=5)

frequency_canvas.grid(column=0,row=1)

calculate_button.grid(column=0, row=4)
frequency_spinbox.grid(column=0, row=0)
n_spinbox.grid(column=0, row=2)
save_button.grid(column=0, row=5)
retrieve_button.grid(column=0, row=6)

# #packing placing and grid are all different
# frame=tk.Frame(root, bg='#e5e5e5')
# frame.place(relx=0.1, rely=0.1,relwidth=0.8,relheight=0.8)#relative width and height will change size in relation to parent
#
#
# label = tk.Label(frame, text="label", bg="yellow")
# label.pack(side='left')
#
# button=tk.Button(frame, text="Button", bg='grey', fg='red') #nested structure
# button.pack(side="left")
#
# entry=tk.Entry(frame,bg='green')
# entry.pack(side='right', fill='both')

root.mainloop()