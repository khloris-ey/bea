import customtkinter as ctk
from rembg import remove
from PIL import Image, ImageTk
import os
from tkinter.filedialog import askopenfilename
from pathlib import Path
from collections import Counter
from tkinter import filedialog
import imageio
import cv2


class Main(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1000x600")
        self.title("Background Remover/Jpg to Png")
        self.configure(fg_color="#0d120e")
        self.resizable(False, False)
        self.cap = None
        self.attributes("-fullscreen", True)

        self.create_tabs()

    def create_tabs(self):
        tabs = ctk.CTkTabview(self, width=1300, height=1300)
        tabs.pack(pady=20)

        tabs.add("Camera")
        tabs.add("Background Remover")
        tabs.add("Jpg to Png")

        self.remover_tab(tabs.tab("Background Remover"))
        self.jpg_to_png_tab(tabs.tab("Jpg to Png"))
        self.camera(tabs.tab("Camera"))

    def camera(self, tab):
        frame = ctk.CTkFrame(tab, fg_color="#6d7e5f")
        frame.pack(fill="both", expand=True)

        self.cam = ctk.CTkLabel(frame, text=" ", corner_radius=20)
        self.cam.place(x=500, y=10)

        takepic = ctk.CTkButton(
            frame, width=80, height=20, fg_color='#E8e9e0', text="PIC", text_color="black", command=self.take_picture, )
        takepic.place(x=850, y=600)

        bgremovepic = ctk.CTkButton(frame, width=200, height=100, text="Remove Background", font=("serif", 15, "bold"), text_color="#E8e9e0",
                                    fg_color='#0d120e', command=lambda: self.set_choice("remove_bg"))
        bgremovepic.place(x=90, y=100)

        pngconvert = ctk.CTkButton(frame, width=200, height=100, text="To PNG",
                                   fg_color="#0d120e", font=("serif", 15, "bold"), text_color="#E8e9e0", command=lambda: self.set_choice("to_png"))
        pngconvert.place(x=90, y=250)

        whitebg_button = ctk.CTkButton(frame, width=200, height=100, text="White Background", font=("serif", 15, "bold"), text_color="#E8e9e0",
                                       fg_color='#0d120e', command=lambda: self.set_choice("replacebg_white"))
        whitebg_button.place(x=90, y=400)

        greenbg_button = ctk.CTkButton(frame, width=200, height=100, text="Green Background", font=("serif", 15, "bold"), text_color="#E8e9e0",
                                       fg_color='#0d120e', command=lambda: self.set_choice("replacebg_green"))
        greenbg_button.place(x=90, y=550)

        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            print("ERROR")
            return

        self.update_camera()

    def set_choice(self, choice):
        self.choice = choice
        print(f"User choice set to: {self.choice}")

    def update_camera(self):
        if self.cap is not None:

            ret, frame = self.cap.read()

        if ret:

            frame = cv2.resize(frame, (750, 570))

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            img = Image.fromarray(frame)

            imagetk = ImageTk.PhotoImage(image=img)

            self.cam.imagetk = imagetk
            self.cam.configure(image=imagetk)

        self.cam.after(100, self.update_camera)

    def take_picture(self):

        doc_path = Path.home()/"Pictures"

        self.png_folder = "Converted_to_Png"
        self.removebgfile = "Remove_Background"
        self.replacebgwhitefile = "White_Bg"
        self.replacebggreenfile = "Green_Bg"

        self.png_path = doc_path/self.png_folder
        self.removebg_path = doc_path/self.removebgfile
        self.replacebgwhite_path = doc_path/self.replacebgwhitefile
        self.replacebggreen_path = doc_path/self.replacebggreenfile

        os.makedirs(self.png_path, exist_ok=True)
        os.makedirs(self.removebg_path, exist_ok=True)
        os.makedirs(self.replacebgwhite_path, exist_ok=True)
        os.makedirs(self.replacebggreen_path, exist_ok=True)

        ret, frame = self.cap.read()

        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            if self.choice == "remove_bg":
                file_name = self.get_next_img(self.removebg_path, "image", "jpg")
                self.file_path = self.removebg_path / file_name
                img.save(self.file_path)
                print(f"Image saved in {self.file_path}")
                self.removebg2(self.removebg_path)

            elif self.choice == "to_png":
                file_name = self.get_next_img(self.png_path, "image", "jpg")
                self.file_path = self.png_path / file_name
                img.save(self.file_path)
                print(f"Image saved in {self.file_path}")
                self.to_png2(self.png_path)

            elif self.choice == "replacebg_white":
                file_name = self.get_next_img(
                    self.replacebgwhite_path, "image", "jpg")
                self.file_path = self.replacebgwhite_path / file_name
                img.save(self.file_path)
                print(f"Image saved in {self.file_path}")
                self.replacebg(self.replacebgwhite_path, bg_color="white")

            elif self.choice == "replacebg_green":
                file_name = self.get_next_img(
                    self.replacebggreen_path, "image", "jpg")
                self.file_path = self.replacebggreen_path / file_name
                img.save(self.file_path)
                print(f"Image saved in {self.file_path}")
                self.replacebg(self.replacebggreen_path, bg_color="green")

    def get_next_img(self, dir, bname, extension):

        if not os.path.exists(dir):
            os.makedirs(dir)
        file_exist = [f for f in os.listdir(dir) if f.startswith(
            bname) and f.endswith(f".{extension}")]

        num = []
        for file_name in file_exist:
            try:

                fname = int(file_name[len(bname):-len(f".{extension}")])
                num.append(fname)
            except ValueError:
                continue

        next_name = max(num, default=0) + 1

        return f"{bname}{next_name}.{extension}"

    def removebg2(self, fileselected):
        for file_name in os.listdir(fileselected):
            file_path = fileselected/file_name
            if file_path.suffix.lower() in ['.jpg', '.jpeg']:
                try:
                    orig_img = Image.open(file_path)
                    removebg_img = remove(orig_img)

                    save_path = file_path.with_suffix('.png')
                    removebg_img.save(save_path)

                    print(f"{file_name} saved!")

                except Exception as error:
                    print("ERROR")
        # os.remove(file_path)

    def to_png2(self, fileselected):
        for file_name in os.listdir(fileselected):
            file_path = fileselected/file_name
            if file_path.suffix.lower() in ['.jpg', '.jpeg']:
                try:
                    orig_img = Image.open(file_path)

                    save_path = file_path.with_suffix('.png')
                    orig_img.save(save_path, "PNG")

                    print("png image saved")
                except Exception as error:
                    print("ERROR")

    def replacebg(self, fileselected, bg_color="white"):
        for file_name in os.listdir(fileselected):
            file_path = fileselected / file_name
            if file_path.suffix.lower() in ['.jpg', '.jpeg']:
                try:
                    orig_img = Image.open(file_path)
                    removebg_img = remove(orig_img)

                    # Set the background color
                    if bg_color.lower() == "green":
                        background_color = (0, 255, 0, 255)
                    else:
                        # White background
                        background_color = (255, 255, 255, 255)

                    colored_bg = Image.new(
                        "RGBA", removebg_img.size, background_color)
                    final_img = Image.alpha_composite(
                        colored_bg, removebg_img.convert("RGBA"))

                    save_path = file_path.with_suffix('.png')
                    final_img.save(save_path)
                    print(f"Image with {bg_color} background saved!")
                except Exception as error:
                    print(f"ERROR: {error}")

    def closing(self):

        if self.cap is not None:

            self.cap.release()

        self.destroy()

    def remover_tab(self, tab):
        frame = ctk.CTkFrame(tab, fg_color="#6d7e5f")
        frame.pack(fill="both", expand=True)

        label = ctk.CTkLabel(
            frame, text="Background Remover", font=("Roboto Serif", 20, "bold"))
        label.pack(pady=10)

        info_label = ctk.CTkLabel(
            frame, text="Choose a picture. It should be Jpeg, Jpg, or Png only.\n \n !!note for the green and white background it should be png file!!", font=("Roboto Serif", 16))
        info_label.pack(pady=20)

        open_buttonrembg = ctk.CTkButton(
            frame, text="Choose a picture", font=("Roboto Serif", 16), command=self.open_filerembg)
        open_buttonrembg.pack(pady=30)

        open_buttonwhitebg = ctk.CTkButton(
            frame, text="Choose a picture (White Bg)", font=("Roboto Serif", 16), command=self.select_imagewhitebg)
        open_buttonwhitebg.pack(pady=30)

        open_buttongreenbg = ctk.CTkButton(
            frame, text="Choose a picture (Green Bg)", font=("Roboto Serif", 16), command=self.select_imagegreenbg)
        open_buttongreenbg.pack(pady=30)

        self.result_label = ctk.CTkLabel(frame, text="")
        self.result_label.pack(pady=20)

        self.save_directory_white_green_bg =  r"C:\Users\asus\Pictures\White and Green Bg"
        os.makedirs(self.save_directory_white_green_bg, exist_ok=True)

    def removebg(self, fileselected):
        file_folder = os.path.splitext(fileselected)[1][1:].lower()

        if file_folder not in ['jpg', 'jpeg', 'png']:
            print(
                f"Warning!! The file '{file_folder}' is unsupported. Make sure your file types are: jpg, jpeg, and png only.")
            return

        try:
            origImg = Image.open(fileselected)
            imgnoBg = remove(origImg)

            save_directory = "C:\\Users\\asus\\Pictures\\Removebg images"
            os.makedirs(save_directory, exist_ok=True)

            base_name = os.path.basename(os.path.splitext(fileselected)[0])
            filesave = os.path.join(save_directory, base_name + '.png')
            imgnoBg.save(filesave)

            print(f"Remove Background successfully. Saved as {filesave}")
            self.result_label.configure(text=f"Image saved as: {filesave}")
        except Exception as error:
            print(f"An error occurred: {error}")

    def open_filerembg(self):
        inputfile = askopenfilename(title="Select an image", filetypes=[
                                    ("Image Files", "*.jpg *.jpeg *.png")])
        if inputfile:
            self.removebg(inputfile)
        else:
            print("No file selected.")

    def select_imagewhitebg(self):
        file_path = askopenfilename(title="Select PNG Image", filetypes=[
                                    ("PNG files", "*.png")])
        if file_path:
            self.convert_image(file_path, (255, 255, 255))

    def select_imagegreenbg(self):
        file_path = askopenfilename(title="Select PNG Image", filetypes=[
                                    ("PNG files", "*.png")])
        if file_path:
            self.convert_image(file_path, (0, 255, 0))

    def convert_image(self, file_path, bg_color):
        outputfiles = self.pngtojpg(file_path, bg_color)
        self.result_label.configure(text=f"Image saved as: {outputfiles}")

    def pngtojpg(self, file_name: str, trans_color: tuple):
        try:
            with Image.open(file_name) as img:
                image = img.convert("RGBA")
                datas = image.getdata()

                newData = []
                for item in datas:
                    if item[3] == 0:
                        newData.append(trans_color)
                    else:
                        newData.append(tuple(item[:3]))

                image = Image.new("RGB", img.size)
                image.putdata(newData)

                base_name = os.path.basename(os.path.splitext(file_name)[0])
                output_file = os.path.join(
                    self.save_directory_white_green_bg, f'{base_name}.jpg')

                image.save(output_file)
                print(f"Saved {output_file}")

                return output_file
        except Exception as error:
            print(f"An error occurred: {error}")
            return None

    def jpg_to_png_tab(self, tab):
        frame = ctk.CTkFrame(tab, fg_color="#6d7e5f")
        frame.pack(fill="both", expand=True)

        label = ctk.CTkLabel(
            frame, text="Jpg to Png Converter", font=("Roboto Serif", 20, "bold"))
        label.pack(pady=10)

        image = Image.open(r"C:\Users\asus\Downloads\png.jpg")

        imresize = image.resize((300, 300))
        img = ImageTk.PhotoImage(imresize)
        self.canvas = ctk.CTkCanvas(frame, width=300, height=300)
        self.canvas.place(x=150, y=100)
        self.canvas.create_image(0, 0, anchor='nw', image=img)

        self.output = ctk.CTkCanvas(frame, width=300, height=300)
        self.output.place(x=580, y=100)
        self.output.create_image(0, 0, anchor='nw', image=img)

        upload_bttn = ctk.CTkButton(
            frame,  width=150, height=50, corner_radius=10, text="Upload", command=self.upload_image)
        upload_bttn.place(x=270, y=430)

        save_button = ctk.CTkButton(
            frame, width=150, height=50, text="Save", corner_radius=10, command=self.save_png)
        save_button.place(x=470, y=430)

        self.transparency_switch = ctk.CTkSwitch(
            frame, text="Transparent Background", command=self.transparent_bg_png)
        self.transparency_switch.place(x=270, y=500)

    def upload_image(self):
        self.file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg; *.jpeg; *.png")])

        if self.file_path:

            image1 = Image.open(self.file_path)
            rszimg = image1.resize((300, 300))
            fnl_img = ImageTk.PhotoImage(rszimg)

            self.canvas.create_image(0, 0, anchor='nw', image=fnl_img)
            self.canvas.fnl_img = fnl_img

            self.to_png()

    def to_png(self):

        unconverted = Image.open(self.file_path)
        self.convert = unconverted

        rsz = self.convert.resize((300, 300))
        cnvrt_img = ImageTk.PhotoImage(rsz)

        self.output.create_image(0, 0, anchor='nw', image=cnvrt_img)
        self.output.cnvrt_img = cnvrt_img

    def find_common_color(self, img):

        rgbimg = img.convert("RGB")

        colors = rgbimg.getdata()

        self.count_colors = Counter(colors).most_common(1)[0][0]

        return self.count_colors

    def transparent_bg_png(self):

        image = Image.open(self.file_path)

        self.rgbaimg = image.convert("RGBA")

        most_color = self.find_common_color(self.rgbaimg)

        data = self.rgbaimg.getdata()
        pixels = []

        for item in data:
            if item[:3] == most_color:
                pixels.append((255, 255, 255, 0))

            else:
                pixels.append(item)

        self.rgbaimg.putdata(pixels)

        rsz = self.rgbaimg.resize((300, 300))

        final = ImageTk.PhotoImage(rsz)

        self.output.create_image(0, 0, anchor='nw', image=final)
        self.output.final = final

    def save_png(self):

        if hasattr(self, 'rgbaimg'):

            save_img = self.rgbaimg

            msg = f" tPNG image is saved to"

        elif hasattr(self, 'convert'):
            save_img = self.convert
            msg = f"png image is saved to"
        else:
            print("NO image saved")
            return

        download_path = str(Path.home() / "Downloads")

        file_name = "download.png"

        save_file = os.path.join(download_path, file_name)

        save_img.save(save_file, "PNG")

        print(f"{msg} {save_file}")


if __name__ == "__main__":
    app = Main()
    app.protocol("WM_DELETE_WINDOW", app.closing)
    app.mainloop()
