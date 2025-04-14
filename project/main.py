from tkinter import *
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import json
import datetime as dt

python_score = 0
content = ["100 Days", "Pandas", "Numpy", "Matplot", "Seaborn", "Plotly", "Altair", "Scikit", "SQL", "Bonus"]
score = []

def update_data(vars):
    score.clear()  # Clear previous state

    for i, var in enumerate(vars):
        val = var.get()
        score.append(val)
        
    plt.bar(content,score,color="purple")
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.title("Todays Progress")
    plt.show()
    today = dt.datetime.now().strftime("%Y-%m-%d")
    data_to_dump={today: sum(score)}
    try:
        with open("data.json", "r") as f:
            existing_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = {}

    existing_data[today] = sum(score)  # Overwrite only today's entry

    with open("data.json", "w") as file:
        json.dump(existing_data, file, indent=4)

def all_analyze():
    with open("data.json","r") as f:
        val=json.load(f)
    print(val)
    keys=list(val.keys())
    values=list(val.values())

    plt.stem(keys,values)
    plt.xticks(rotation=45)
    plt.title("Overall Graph")
    plt.show()

def python_sylabus():
    window1 = Toplevel()
    window1.title("PYTHON SUB TOPICS")
    window1.config(height=500, width=500, bg="MistyRose3", padx=20, pady=20)

    # Store all IntVar variables
    vars = [IntVar() for _ in range(10)]

    Label(window1, text="Python Content (Select Completed Topics)", bg="MistyRose3", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

    # Checkbuttons
    Checkbutton(window1, text="100 Days Of Coding", variable=vars[0], bg="MistyRose3").grid(row=1, column=0, sticky="w", pady=2)

    Label(window1, text="Data Manipulation Tools:", bg="MistyRose3").grid(row=2, column=0, columnspan=2, pady=10, sticky="w")
    Checkbutton(window1, text="Pandas", variable=vars[1], bg="MistyRose3").grid(row=3, column=0, sticky="w", pady=2)
    Checkbutton(window1, text="Numpy", variable=vars[2], bg="MistyRose3").grid(row=4, column=0, sticky="w", pady=2)

    Label(window1, text="Data Visualization Tools:", bg="MistyRose3").grid(row=5, column=0, columnspan=2, pady=10, sticky="w")
    Checkbutton(window1, text="Matplotlib.pyplot", variable=vars[3], bg="MistyRose3").grid(row=6, column=0, sticky="w", pady=2)
    Checkbutton(window1, text="Seaborn", variable=vars[4], bg="MistyRose3").grid(row=7, column=0, sticky="w", pady=2)
    Checkbutton(window1, text="Plotly", variable=vars[5], bg="MistyRose3").grid(row=8, column=0, sticky="w", pady=2)
    Checkbutton(window1, text="Altair", variable=vars[6], bg="MistyRose3").grid(row=9, column=0, sticky="w", pady=2)

    Label(window1, text="Machine Learning:", bg="MistyRose3").grid(row=10, column=0, columnspan=2, pady=10, sticky="w")
    Checkbutton(window1, text="Scikit-learn", variable=vars[7], bg="MistyRose3").grid(row=11, column=0, sticky="w", pady=2)

    Checkbutton(window1, text="SQL Database", variable=vars[8], bg="MistyRose3").grid(row=12, column=0, sticky="w", pady=2)

    Checkbutton(window1, text="Bonus (Jupyter, GitHub, APIs, Web scraping)", variable=vars[9], bg="MistyRose3", wraplength=400).grid(row=13, column=0, columnspan=2, sticky="w", pady=5)

    Button(window1, text="Apply", command=lambda: update_data(vars), bg="lightgreen", width=15).grid(row=14, column=0, pady=15)

    python_button.config(state="disabled")


# MAIN UI
window = Tk()
window.title("TO DO LIST")
window.config(padx=20, pady=20, width=700, height=500, bg="purple4")

canvas = Canvas(height=300, width=600)
img = Image.open("images/imagess.png")
img = img.resize((650, 300), Image.Resampling.LANCZOS)
main_image = ImageTk.PhotoImage(img)
canvas.image = main_image
canvas.create_image(0, 0, image=main_image, anchor=NW)
canvas.grid(row=0, column=0, columnspan=3)

python_button = Button(text="Python", command=python_sylabus, width=15)
python_button.grid(row=1, column=0, pady=20)

overall=Button(text="Analyze",command=all_analyze,width=16)
overall.grid(row=1,column=2,pady=20)

window.mainloop()
