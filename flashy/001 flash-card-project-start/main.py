
import tkinter,pandas as pd
import random
import time
BACKGROUND_COLOR = "#B1DDC6"
def pull_dict():

    new_dict={}
    with open("../translated_dict.csv","r") as data_file:

        df=pd.read_csv(data_file)

        count=0
        for key,value in df.iterrows():
            swa=value.iloc[0]
            eng=value.iloc[1]
            new_dict[swa]=eng

        return new_dict


dict1=pull_dict()

#print(f"key : {key} , value : {value}")

new_dictionary={}
#load the swahili word to canvas 1
#function to add known words to a new dict
is_in_eng=0

def generate_key_value():
    global dict1
    list_of_keys = list(dict1.keys())
    key = random.choice(list_of_keys)
    value = dict1[key]
    return key,value


(key,value)=generate_key_value()
def add_words():
    global is_in_eng
    global key
    global value
    time.sleep(0.3)
    global new_dictionary
    if is_in_eng==1:
        key_value={key:value}
        new_dictionary.update(key_value)
        with open(file="known_words.txt",mode="w") as data_file:
            data_file.write(str(new_dictionary))
            data_file.write("\n")
        print( new_dictionary)
        is_in_eng=0
        (key, value) = generate_key_value()
        #check if key is among words ticked correct
        while key in new_dictionary.keys():
            (key, value) = generate_key_value()

        display_swa()

# a mirror of the add words withot adding words for the x button

def next_words():
    global is_in_eng
    global key
    global value
    time.sleep(0.3)
    global new_dictionary
    if is_in_eng == 1:
        key_value = {key: value}

        print(new_dictionary)
        is_in_eng = 0
        (key, value) = generate_key_value()
        # check if key is among words ticked correct
        while key in new_dictionary.keys():
            (key, value) = generate_key_value()

        display_swa()








window=tkinter.Tk()
window.title("FLashy")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
canvas=tkinter.Canvas(width=800,height=526)
canvas.config(bg=BACKGROUND_COLOR)
#load images
card_back=tkinter.PhotoImage(file="images/card_back.png")
card_front=tkinter.PhotoImage(file="images/card_front.png")
tick_image=tkinter.PhotoImage(file="images/right.png")
wrong_image=tkinter.PhotoImage(file="images/wrong.png")



tick_button=tkinter.Button(image=tick_image,highlightthickness=0,command=add_words)
wrong_button=tkinter.Button(image=wrong_image,highlightthickness=0,command=next_words)

word_label=tkinter.Label()
#swahili=f" Swahili word \n\n {key}"

#flag to see if in eng or swa slide
def display_eng(key,value):
    global is_in_eng
    is_in_eng=1
    front_img = canvas.create_image(400, 264, image=card_front)
    eng_text = canvas.create_text(200, 132, text=value, font=("courier", 40))

def display_swa():
    global key
    global value


    back_img = canvas.create_image(400, 264, image=card_back)
    swa_text = canvas.create_text(200, 132, text=key, font=("courier", 40))
    window.after(3000,display_eng,key,value)
#TODO add button functionalities ,create a mirror dict with words exclusion





#front_img=canvas.create_image(400,263,image=card_front

#dummy rows
row1=tkinter.Label(text=" ")
row2=tkinter.Label(text=" ")
row3=tkinter.Label(text=" ")
row4=tkinter.Label(text=" ")

canvas.grid(column=0,row=0,columnspan=2)
(i,j)=(0,0)


tick_button.grid(row=3,column=0)
wrong_button.grid(row=3,column=1)

#pulling pairs from the file
display_swa()



window.mainloop()

