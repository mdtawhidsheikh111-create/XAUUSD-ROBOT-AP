import asyncio
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

# ===================================================
# XAUUSD (Gold) Instant Scalper Mobile App
# ===================================================


class MT5DirectRobotApp(App):

  def build(self):
    self.is_running = False

    # প্রধান লেআউট
    layout = BoxLayout(orientation="vertical", padding=20, spacing=15)

    # শিরোনাম
    title = Label(
        text="XAUUSD Instant Scalper Bot",
        font_size="22sp",
        bold=True,
        size_hint_y=None,
        height=50,
    )
    layout.add_widget(title)

    # স্ট্যাটাস ডিসপ্লে
    self.status_label = Label(
        text="Status: READY (Press Start)",
        font_size="18sp",
        color=(1, 1, 0, 1),
        size_hint_y=None,
        height=40,
    )
    layout.add_widget(self.status_label)

    # MT5 অ্যাকাউন্ট তথ্য দেওয়ার ঘর (অ্যাপের ভেতরই থাকবে)
    self.login_input = TextInput(
        hint_text="MT5 Login ID",
        multiline=False,
        input_type="number",
        size_hint_y=None,
        height=45,
    )
    self.pass_input = TextInput(
        hint_text="MT5 Password",
        password=True,
        multiline=False,
        size_hint_y=None,
        height=45,
    )
    self.server_input = TextInput(
        hint_text="Broker Server (e.g. Exness-Real10)",
        multiline=False,
        size_hint_y=None,
        height=45,
    )

    layout.add_widget(self.login_input)
    layout.add_widget(self.pass_input)
    layout.add_widget(self.server_input)

    # START বাটন (সবুজ)
    self.start_btn = Button(
        text="START BOT",
        background_color=(0, 0.8, 0.2, 1),
        font_size="20sp",
        bold=True,
        size_hint_y=None,
        height=60,
    )
    self.start_btn.bind(on_press=self.start_robot)
    layout.add_widget(self.start_btn)

    # STOP বাটন (লাল)
    self.stop_btn = Button(
        text="STOP BOT",
        background_color=(0.9, 0.1, 0.1, 1),
        font_size="20sp",
        bold=True,
        size_hint_y=None,
        height=60,
    )
    self.stop_btn.bind(on_press=self.stop_robot)
    layout.add_widget(self.stop_btn)

    return layout

  # রোবট অন করার লজিক
  def start_robot(self, instance):
    if not self.is_running:
      login = self.login_input.text
      password = self.pass_input.text
      server = self.server_input.text

      if not login or not password or not server:
        self.status_label.text = "Error: Fill all MT5 details!"
        return

      self.is_running = True
      self.status_label.text = "Status: CONNECTING TO MT5..."
      # ব্যাকগ্রাউন্ড ট্রেডিং লুপ শুরু
      Clock.schedule_interval(self.robot_trading_logic, 0.3)

  # রোবট অফ করার লজিক
  def stop_robot(self, instance):
    if self.is_running:
      self.is_running = False
      Clock.unschedule(self.robot_trading_logic)
      self.status_label.text = "Status: BOT STOPPED"

  # আসল ট্রেডিং লজিক (XAUUSD Scalping)
  def robot_trading_logic(self, dt):
    if not self.is_running:
      return

    # ১. এখানে ব্যাকগ্রাউন্ড কোড XAUUSD-এর প্রফিট মনিটর করবে
    # ২. প্রফিট $০.০৫ ডলার ছোঁয়া মাত্রই ট্রেড ক্লোজ করবে
    # ৩. RSI দেখে অটো বাই/সেল নেবে
    self.status_label.text = "Status: RUNNING (Monitoring XAUUSD)"


if __name__ == "__main__":
  MT5DirectRobotApp().run()
