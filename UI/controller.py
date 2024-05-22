import flet as ft
import datetime


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._sel_color = None
        self._sel_year = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []

    def fillDD(self):
        self._listYear = self._model.get_years()
        self._listColor = self._model.get_colors()
        for y in self._listYear:
            self._view._ddyear.options.append(ft.dropdown.Option(key=y, text=y))
        for c in self._listColor:
            self._view._ddcolor.options.append(ft.dropdown.Option(c))
        self._view.update_page()

    def handle_graph(self, e):
        self._view.txtOut.controls.clear()
        if self._sel_year == None or self._sel_color == None:
            self._view.txtOut.controls.append(ft.Text("Select an year and a color!"))
        else:
            self._model.build_graph(self._sel_year,self._sel_color)
            num_n = self._model.get_num_nodes()
            num_ed = self._model.get_num_edges()
            max_3, most_recurrent = self._model.get_max_edges()
            self._view.txtOut.controls.append(ft.Text(f'Number of nodes: {num_n} - Number of edges : {num_ed}'))
            for e in max_3:
                self._view.txtOut.controls.append(ft.Text(f'Edge from {e[0].Product_number} to {e[1].Product_number} - weight : {e[2]['weight']}'))
            self._view.txtOut.controls.append(ft.Text(f'The most recurrent nodes is {most_recurrent}'))
        self._view.update_page()

    def read_dd_year(self,e):
        self._sel_year = e.control.value

    def read_dd_color(self,e):
        self._sel_color = e.control.value

    def fillDDProduct(self):
        pass


    def handle_search(self, e):
        pass
