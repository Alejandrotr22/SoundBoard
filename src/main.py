import flet as ft
from core import *
import math
from sizeAwareControl import SizeAwareControl




def main(page: ft.Page):
    
    #s1 = SoundController(index=1)
    sounds = []
    
    #sounds.append(s1)
    
    
    page.theme = ft.Theme()
    button_style = ft.ButtonStyle(
        side={ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.CYAN_ACCENT_200)},
                                  shape={
                    ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=4),
                    ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=4),
                },)
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
        # instead of e.width for example, you can use the e.control.size namedtuple (e.control.size.width or e.control.size[0])

        if e.width < e.height:
           sound_controls.width = e.width
           sound_controls.height = sound_controls.width
        else:
           sound_controls.height = e.height
           sound_controls.width = sound_controls.height

        page.update()
    


    boton = ft.OutlinedButton(style=button_style,expand=5 ,text="                                                                  ")
    sound_controls = ft.Row(width=250,height=250,spacing=8, controls=[
        ft.Column(expand = 1,alignment=ft.MainAxisAlignment.CENTER ,horizontal_alignment=ft.CrossAxisAlignment.CENTER ,controls=[
            ft.IconButton(style=button_style,icon=ft.icons.ARROW_DROP_UP,expand=1),
            ft.Text(0.0,text_align=ft.CrossAxisAlignment.CENTER),
            ft.IconButton(style=button_style,icon=ft.icons.ARROW_DROP_DOWN,expand=1),
            ft.IconButton(style=button_style,icon=ft.icons.ADD,expand=1),
        ]),
        ft.Column(run_spacing=0, expand=4 , horizontal_alignment=ft.CrossAxisAlignment.CENTER,controls=[
            ft.Slider(expand=1,min=0,max=100),
            boton, 
            ft.Row(expand=2,controls=[
                ft.IconButton(style=button_style,expand =1, icon=ft.icons.LOOP,icon_size=10),
                ft.IconButton(style=button_style,expand =1, icon=ft.icons.PAUSE,icon_size=10),
                ft.IconButton(style=button_style,expand =1, icon=ft.icons.DRIVE_FOLDER_UPLOAD_SHARP,icon_size=10),
            ]),
            ft.Slider(expand=1,min=0,max=100),
        ]),
        ft.Column(expand = 1, horizontal_alignment=ft.CrossAxisAlignment.CENTER ,controls=[
            ft.IconButton(style=button_style,icon=ft.icons.ARROW_DROP_UP,expand=3),
            ft.Text(0.0),
            ft.IconButton(style=button_style,icon=ft.icons.ARROW_DROP_DOWN,expand=3),
            ft.IconButton(style=button_style,icon=ft.icons.REMOVE,expand=3),
        ]),
    ])
    
    sound_cage = SizeAwareControl(content=ft.Column([
        ft.Row([
            sound_controls,
            sound_controls,
            sound_controls,
        ]),
        ft.Row([
            sound_controls,
            sound_controls,
            sound_controls,
        ]),
        ft.Row([
            sound_controls,
            sound_controls,
            sound_controls,
        ]),
        ]),on_resize=handle_resize,expand = 1)
    

        
    

    page.add(SizeAwareControl(content=ft.Column(expand=True,controls=[
        
    ]),on_resize=handle_resize)
    )
    
    

    page.update()

ft.app(main)
