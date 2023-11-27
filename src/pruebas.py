
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
    
    s1 = SizeAwareControl(ft.Container(content=sound_controls, bgcolor=ft.colors.RED, alignment=ft.alignment.center), on_resize=handle_resize, expand=2)
    s2 = SizeAwareControl(ft.Container(content=ft.Text("W x H"), bgcolor=ft.colors.BLUE, alignment=ft.alignment.center), on_resize=handle_resize, expand=3)

    page.add(
        ft.Row([s1, s2], expand=True),
    )

ft.app(main)