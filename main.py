from googletrans import Translator
from tkinter import *

translator = Translator()


window = Tk()

selected_option = StringVar()
inputText = StringVar()

language_dict = {
    "English": "en",
    "Hindi": "hi",
    "French": " fr",
    "Spanish": "es",
    "German": "de",
    "Chinese": "zh",
    "Japanese": "ja",
    "Korean": "ko",
    "Russian": "ru",
    "Arabic": "ar",
}


def translateText(*args):
    selected_language = selected_option.get()
    text = inputText.get()
    
    if not text:
        label.config(text="Please Enter some Text First")
        return 

    tl = language_dict[selected_language]
    try:
        translation = translator.translate(text=text, dest=f"{tl}")
        label.config(text=translation.text)
        inputText.delete(0,END)
    except ModuleNotFoundError as err:
        print(f"There is Error:-{err}")
    else:
        print("You task is done!")


options = []


for key in language_dict.keys():
    options.append(key)


window.title("Translation Application")
window.config(padx=20, pady=20, bg="cyan")

inputText = Entry(width=50)
inputText.insert(END, "Enter your Text here")
inputText.grid(column=0, row=1, pady=20)

label = Label(text="Your Translated Text shown here", bg="red",width=50,height=3)
label.grid(column=0, row=3, pady=20)


selected_option.set(options[0])  # Set default value


def option_selected(*args):
    print("Selected option:", selected_option.get())


selected_option.trace("w", option_selected)
option_menu = OptionMenu(window, selected_option, *options)
option_menu.grid(column=0, row=0)


translate = Button(
    text="Translate", width=50, height=5, command=translateText, bg="blue"
)
translate.grid(column=0, row=2, pady=20)


window.mainloop()
