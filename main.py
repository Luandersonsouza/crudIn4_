from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.uix.popup import Popup
from kivy.uix.image import Image

class Gerenciador(ScreenManager):
	pass

class Menu(Screen):
	def confirmacao(self, *args):
		box = BoxLayout(orientation='vertical')
		botoes = BoxLayout()

		sim = Button(text='Sim')
		nao = Button(text='Não')

		button.add_widget(sim)
		button.add_widget(nao)

		pop = Popup(title='Deseja mesmo sair?' , content =box)

		pop = Popup(title='Deseja mesmo sair?' , content= box, size_hint=(None, None), size =(300, 180))

		pop.open()


class Produtos(Screen):
	def __init__(self, produtos=[], **kwargs):
		super().__init__(**kwargs)

class Cadastro(Screen):
	def __init__(self, cadastro=[], **kwargs):
		super().__init__(**kwargs)

	def addWidget(self):
		textoc = self.ids.textoc.text
		self.ids.bom.add_widget(Cadastro(text=textoc))

class AtualizarC(Screen):
	def __init__(self, atualizarc=[], **kwargs):
		super().__init__(**kwargs)

class Excluir(Screen):
	def __init__(self, excluir=[], **kwargs):
		super().__init__(**kwargs)

										
class crud(App):
    def build(self):
    	return Gerenciador()
        
crud().run()	