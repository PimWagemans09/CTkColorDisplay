## CTkColorDisplay
CTkColorDisplay is a customtkinter extension that adds a new widget to display colors

**NOTE: i made this for one of my own projects and decided to upload it,<br/>
there are probably better way to display colors but i needed it this way**

![picture of widget](README_images/CTkColorDisplay.png?raw=true)

**code for above window**
```python
import CTkColorDisplay
import customtkinter 

root = customtkinter.CTk()

a = CTkColorDisplay.CTkColorDisplay(root,display_width=100,display_height=100,display_color="#00ff00")
a.grid(row=0,column=0,padx=10,pady=10)

root.mainloop()
```

## Arguments
| Parameter | Description |type|optional|
|-----------| ------------| ------------| ------------|
|master|the master widget or window|any|mandatory|
|display_color|a hex code for the color to display|str|optional|
|variable|a variable to trace the display color wil be set to this|customtkinter.StringVar|optional|
|display_image|the image used to display the color al white(#ffffff) pixels will be replaced with the display_color|str OR PIL.Image.Image|optional|
|display_width|the width of the display in px|int|optional|
|display_height|the height of the display in px|int|optional|
|frame_width|the width of the entire widget(replaces "width" from customtkinter.CTkFrame)|int|optional|
|frame_height|the height of the entire widget(replaces "height" from  customtkinter.CTkFrame)|int|optional|
|*other parameters|other parameters of  customtkinter.CTkFrame can also be passed|*-depends-*|optional|

## Methods
### .set_color(color:str)
    change the display color
### .configure(**kwargs)
    change:
        display_width: int
        display_height: int
        display_image: str | PIL.Image.Image
        all confirurable args of customtkinter.CTkFrame

## Instalation*
*for windows i dont know about other operating systems
- download `CTkColorDisplay.zip` from Releases
- right click on the downloaded file and select "extract all"
- click "browse" and select the folder your project is stored in OR `C:/users/<username>/appdata/local/programs/python/python<version>/lib/site-packages`
