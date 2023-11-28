
from sizeAwareControl import SizeAwareControl
import flet as ft


def main(page: ft.Page):
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
        
        page.update()

    button_style = ft.ButtonStyle(
        side={ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.CYAN_ACCENT_200)},
                                  shape={
                    ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=4),
                    ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=4),
                },)

    boton = ft.OutlinedButton(style=button_style,expand=5 ,text="                                                                  ")
    sound_controls = ft.Row(spacing=8, controls=[
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


    
    s1 = SizeAwareControl(ft.Container(content=sound_controls,alignment=ft.alignment.center), on_resize=handle_resize, expand=1)
    s2 = SizeAwareControl(ft.Container(content=sound_controls, alignment=ft.alignment.center), on_resize=handle_resize, expand=1)
    s3 = SizeAwareControl(ft.Container(content=sound_controls,alignment=ft.alignment.center), on_resize=handle_resize, expand=1)
    s4 = SizeAwareControl(ft.Container(content=sound_controls, alignment=ft.alignment.center), on_resize=handle_resize, expand=1)
    s5 = SizeAwareControl(ft.Container(content=sound_controls,alignment=ft.alignment.center), on_resize=handle_resize, expand=1)
    s6 = SizeAwareControl(ft.Container(content=sound_controls, alignment=ft.alignment.center), on_resize=handle_resize, expand=1)
    s7 = SizeAwareControl(ft.Container(content=sound_controls,alignment=ft.alignment.center), on_resize=handle_resize, expand=1)
    s8 = SizeAwareControl(ft.Container(content=sound_controls, alignment=ft.alignment.center), on_resize=handle_resize, expand=1)
    s9 = SizeAwareControl(ft.Container(content=sound_controls,alignment=ft.alignment.center), on_resize=handle_resize, expand=1)

    page.add(
        ft.Column([
            ft.Row(expand=1,controls=[s1, s2, s3]),
            ft.Row(expand=1,controls=[s4, s5, s6]),
            ft.Row(expand=1,controls=[s7, s8, s9]),            
            ], expand=True),
    )

ft.app(main)