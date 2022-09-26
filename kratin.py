import joblib
filename = 'finalized_model.sav'
# loaded_model = joblib.load(filename)
# result = loaded_model.predict([[-0.0010777]])
# print(result)



#MODEL TRAIN IN GOOGLE COLAB

# WITH LINEAR REGRESSION ALGORITHM
############################################################################################
############################################################################################
# from sklearn.datasets import load_diabetes
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error,accuracy_score

# import numpy as np
# import matplotlib.pyplot as plt
# import joblib
# data = load_diabetes()
# print(data.DESCR)
# diabetes_x = data.data[:,np.newaxis,9]
# diabetes_x_train =  diabetes_x[:-420]
# diabetes_x_test = diabetes_x[-30:]
# diabetes_y_train = data.target[:-420]
# diabetes_y_test =  data.target[-30:]

# print(diabetes_x_test)

# model = LinearRegression().fit(diabetes_x_train,diabetes_y_train)
# p=model.predict(diabetes_x_test)
# print(p)
# print(diabetes_y_test)
# print(mean_squared_error(diabetes_y_test,p))
# filename = 'finalized_model.sav'
# joblib.dump(model, filename)



import tkinter
from tkinter import messagebox


win = tkinter.Tk()
win.title("SUGAR LEVEL")
win.geometry('440x440')
win.configure(bg='#333333')
def sig():
    loaded_model = joblib.load(filename)
    result = loaded_model.predict([[float(username_e.get())]])
    label.config(text=""+str(result))
   



username_label = tkinter.Label(
        win, text="ENTER THE SUGAR LEVEL", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_e = tkinter.Entry(win,font=("Arial", 16))

button1=tkinter.Button(win,text="Enter", command=sig)
username_label.pack()
username_e.pack()
button1.pack()
label=tkinter.Label(win, text="", font=('Calibri 15'))
label.pack()


win.mainloop()