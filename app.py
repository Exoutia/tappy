import subprocess
import tkinter as tk
from tkinter import filedialog

from PIL import ImageTk, Image


class ImageApp:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Image Theme Application")
        self.img_label = tk.Label(root)
        self.img_label.pack()

        self.upload_button = tk.Button(
            root, text="Upload Image", command=self.upload_image
        )
        self.upload_button.pack()

        self.upload_img = tk.Label(root)
        self.upload_img.pack()

        self.theme_listbox = tk.Listbox(root, height=5)
        themes = ['dark-decay', 'gruvbox-dark', 'tokyonight-storm', 'vulcan-base16']
        for theme in themes:
            self.theme_listbox.insert(tk.END, theme)
        self.theme_listbox.pack()

        self.apply_theme_button = tk.Button(root, text="Apply Theme", command=self.apply_theme)
        self.apply_theme_button.pack()

        self.result_image_label = tk.Label(root)
        self.result_image_label.pack()


    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image_path = file_path
            print(self.image_path)
            self.display_image(self.image_path, self.upload_img)

    def apply_theme(self):
        print("this ")
        if self.image_path:
            out_path = './custom/' + 'new_image_decay_' + self.image_path.split('/')[-1].replace(' ', '_')
            theme = self.theme_listbox.get(tk.ACTIVE)
            self.run_lutgen(self.image_path, out_path, theme)
            self.display_image(out_path, self.result_image_label)
            

    def run_lutgen(self, image_path, out_path, theme):
        subprocess.run('lutgen apply ' + '-o ' + out_path + ' -p '+ theme + ' ' + image_path, shell=True, capture_output=True)

    def display_image(self, img_path, label):
        img = Image.open(img_path)
        img.thumbnail((300, 300))
        img_tk = ImageTk.PhotoImage(img)
        label.config(image=img_tk)
        label.image = img_tk


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageApp(root)
    root.mainloop()
