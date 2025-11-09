
# main.py
# Kivy app: two-button consent UI. Yes -> open mail client (mailto).
# Author: ChatGPT for Isa
# Notes: change RECIPIENT to your target email if needed.

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
import webbrowser
import urllib.parse

RECIPIENT = "isaxvillain@gmail.com"  # change if you want

class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=12, padding=20, **kwargs)
        Window.clearcolor = (0.04, 0.06, 0.08, 1)  # dark background
        title = Label(text="> Share contacts with Isa", size_hint=(1, None), height=50,
                      color=(0.0, 0.8, 1.0, 1), bold=True)
        desc = Label(text="Tap YES to open your mail app. You must attach/paste contacts and press Send.",
                     size_hint=(1, None), height=70, color=(0.6,0.7,0.8,1))
        btn_layout = BoxLayout(size_hint=(1, None), height=60, spacing=12)

        yes_btn = Button(text="YES — open mail", background_normal='', background_color=(0.0,0.47,0.9,1),
                         color=(0,0,0,1), font_size=16)
        no_btn  = Button(text="NO — do not share", background_normal='', background_color=(0.12,0.14,0.16,1),
                         color=(0.6,0.7,0.8,1), font_size=16)

        yes_btn.bind(on_release=self.on_yes)
        no_btn.bind(on_release=self.on_no)

        btn_layout.add_widget(yes_btn)
        btn_layout.add_widget(no_btn)

        self.add_widget(title)
        self.add_widget(desc)
        self.add_widget(btn_layout)

    def on_yes(self, instance):
        # Compose mailto URL
        subject = "Share contact with Isa"
        body = ("Salam Sir — please attach your vCard (.vcf) or paste contact details below:\n\n"
                "Name:\nPhone:\nEmail:\nOrg:\n\nThanks,")
        mailto = f"mailto:{RECIPIENT}?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"

        # Try Android Intent via pyjnius if available; else fallback to webbrowser
        try:
            # pyjnius import is only available on Android build
            from jnius import autoclass, cast
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')

            currentActivity = PythonActivity.mActivity
            intent = Intent(Intent.ACTION_SENDTO)
            intent.setData(Uri.parse(mailto))
            # startActivity may throw if no handler; wrap in try
            currentActivity.startActivity(intent)
        except Exception:
            # fallback: open default handler (desktop or web)
            try:
                webbrowser.open(mailto)
            except Exception:
                from kivy.uix.popup import Popup
                from kivy.uix.label import Label
                p = Popup(title='Error', content=Label(text='Unable to open mail client on this device.'),
                          size_hint=(0.8, 0.3))
                p.open()

    def on_no(self, instance):
        from kivy.uix.popup import Popup
        from kivy.uix.label import Label
        p = Popup(title='Cancelled', content=Label(text='No problem — nothing will be shared.'),
                  size_hint=(0.8, 0.3))
        p.open()


class ShareApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    ShareApp().run()
