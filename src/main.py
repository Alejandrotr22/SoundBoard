import flet as ft
from core import *
import math
from sizeAwareControl import SizeAwareControl




def main(page: ft.Page):
    
    #s1 = SoundController(index=1)
    sounds = []
    
    #sounds.append(s1)
    
    
    page.theme = ft.Theme()
    #ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=2)
    for sound in sounds:
        pass
    
    def handle_resize(e: ft.canvas.CanvasResizeEvent):
        """
        The handle_resize function is a callback function that will be called when
        the control that triggered this event is resized (ex: through window resize).
        The CanvasResizeEvent object has several useful attributes:
            - control: The control that triggered the event (SizeAwareControl)
            - width: The new width of the control in pixels (after resize)
            - height: The new height of the control in pixels (after resize)
        """
        # grab the content of the SizeAwareControl
        c = e.control.content
        # grab the text in its content
        t = c.content
        # instead of e.width for example, you can use the e.control.size namedtuple (e.control.size.width or e.control.size[0])
        t.value = f"{e.width} x {e.height}"
        page.update()
    
    sound_controls = ft.Row( width=300,height=300, controls= [
        ft.Column(expand = 1, horizontal_alignment=ft.CrossAxisAlignment.CENTER ,controls=[
            ft.IconButton(icon=ft.icons.ARROW_DROP_UP,expand=3),
            ft.Text(0.0,expand=1),
            ft.IconButton(icon=ft.icons.ARROW_DROP_DOWN,expand=3),
            ft.IconButton(icon=ft.icons.ADD,expand=3),
        ]),
        ft.Column( expand=1 , horizontal_alignment=ft.CrossAxisAlignment.CENTER,controls=[
            ft.Slider(min=0,max=100),
            ft.OutlinedButton(expand=1, text="texto" ,),
            ft.Row([
                ft.IconButton(expand =True, icon=ft.icons.LOOP),
                ft.IconButton(expand =True, icon=ft.icons.PAUSE),
                ft.IconButton(expand =True, icon=ft.icons.DRIVE_FOLDER_UPLOAD_SHARP),
            ])
        ])
    ])
    
    sound_cage = SizeAwareControl(content=sound_controls,on_resize=handle_resize,expand = 1)
    
    page.add(sound_controls)

    page.update()

ft.app(main)
