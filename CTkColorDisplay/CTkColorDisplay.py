from typing import Optional, Tuple, Union
import customtkinter as ctk
import tkinter
from PIL import Image
import numpy as np
from os.path import basename
from .utilities import hex_to_rgb, verify_hex
from .exceptions import invalidHexException

class CTkColorDisplay(ctk.CTkFrame):
    def __init__(self, master: any, display_color:str = "#ffffff", variable:ctk.StringVar = None,display_image:str|Image.Image = __file__.replace(basename(__file__),"assets/colorsquare.png"),display_width: int = 32, display_height: int = 32, frame_width: int = 200, frame_height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = "transparent", border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        """
        a widget for displaying colors\n
        all defualt arguments of a frame stil apply\n
            (width & height have been renamed to frame_width & frame_height)\n
        the new ones for this widget are:\n
            display_color: str - hex code of the initial color to display\n
            display_image: str | Image.Image - a path to an image or an PIL.Image.Image object\n
                this image is used to display the color.\n
                white (#ffffff) in this image wil be replaced with the display color\n
            image_width: int - width of the display image in px\n
            image_height: int - height of the display image in px\n
        """
        super().__init__(master, frame_width, frame_height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self._master = master
        if variable != None:
            variable.trace_add("write",callback=self._set_color_trace)
        self._display_width = display_width
        self._display_height = display_height
        self.configure(fg_color=fg_color)
        self.columnconfigure((0),weight=1)
        self.rowconfigure((0),weight=1)
        self._display_color = display_color
        if not verify_hex(self._display_color):
            raise invalidHexException(f"{self._display_color} is not a valid hex color")
        if isinstance(display_image,str):
            self._original_image = Image.open(display_image)
        elif isinstance(display_image,Image.Image):
            self._original_image = display_image
        self._color_display = ctk.CTkLabel(self,text="error",text_color="#ffffff",fg_color="#ff0000")
        self._color_display.grid(row=0,column=0,sticky="nesw")
        self._update_color_display()

    def set_color(self, color:str):
        self._display_color=color
        if not verify_hex(self._display_color):
            raise invalidHexException(f"{self._display_color} is not a valid hex color")
        self._update_color_display()
    
    def _set_color_trace(self,*args):
        color = self.winfo_toplevel().getvar(args[0])
        self.set_color(color)

    def _update_color_display(self):
        self._color_display.destroy()
        self._colored_image = ctk.CTkImage(self._recolor_image(self._original_image,self._display_color).resize((self._display_width,self._display_height),resample=Image.NEAREST),size=(self._display_width,self._display_height))
        self._color_display = ctk.CTkLabel(self,text="",image=self._colored_image,fg_color="transparent")
        self._color_display.grid(row=0,column=0,sticky="nesw")
        
    def _recolor_image(self,image:Image.Image,new_color:str,replace_color: str = "#ffffff") -> Image.Image:
        data = np.array(image)
        new_color_rgb=hex_to_rgb(new_color)
        replace_color_rgb = hex_to_rgb(replace_color)
        red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
        mask = (red == replace_color_rgb[0]) & (green == replace_color_rgb[1]) & (blue == replace_color_rgb[2])
        data[:,:,:3][mask] = [new_color_rgb[0], new_color_rgb[1], new_color_rgb[2]]
        return Image.fromarray(data)
    
    def configure(self, require_redraw=False, **kwargs):
        if "display_width" in kwargs:
            self._display_width = kwargs.pop("display_width")
        if "display_height" in kwargs:
            self._display_height = kwargs.pop("display_height")
        if "display_image" in kwargs:
            temp = kwargs.pop("display_image")
            if isinstance(temp,str):
                self._original_image = Image.open(temp)
            elif isinstance(temp,Image.Image):
                self._original_image = temp
        super().configure(require_redraw, **kwargs)