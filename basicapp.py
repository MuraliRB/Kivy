import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button 

class MyGridLayout(GridLayout):
	def __init__(self, **kwargs):
		super(MyGridLayout, self).__init__(**kwargs)

		self.cols = 1
		self.row_force_default=True
		self.row_default_height=85
		self.col_force_default=True
		self.col_default_width=100

		self.top_grid = GridLayout(
			row_force_default=True,
			row_default_height=40,
			col_force_default=True,
			col_default_width=100
			)
		self.top_grid.cols = 2

		self.top_grid.add_widget(Label(text="Name: "))

		self.name = TextInput(multiline=False)
		self.top_grid.add_widget(self.name)

		self.top_grid.add_widget(Label(text="Age: "))

		self.age = TextInput(multiline=False)
		self.top_grid.add_widget(self.age)

		self.top_grid.add_widget(Label(text="Gender: "))

		self.gender = TextInput(multiline=False)
		self.top_grid.add_widget(self.gender)

		self.add_widget(self.top_grid)

		self.submit = Button(text="Submit", 
			font_size=32,
			size_hint_y=None,
			height=50,
			size_hint_x=None,
			width=200
			)

		self.submit.bind(on_press=self.press)
		self.add_widget(self.submit)

	def press(self, instance):
		name = self.name.text
		age =  self.age.text	
		gender = self.gender.text 

		if(self.name.text == "" or self.age.text == "" or self.gender.text == "" ):
			self.add_widget(Label(text="All Fields are required"))
		else:	
		#print(f'Hello {name} your age is {age} and you are {gender}')
			self.add_widget(Label(text=f'Hello {name} your age is {age} and you are {gender}'))			

			self.name.text = ""
			self.age.text = ""
			self.gender.text = ""

class Myapp(App):
	def build(self):
		return MyGridLayout()


if __name__ == '__main__':
	Myapp().run()
