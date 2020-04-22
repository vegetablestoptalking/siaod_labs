from tkinter import *
from tkinter import scrolledtext


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value: str) -> None:
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, cost):
        self._add_edge(from_node, to_node, cost)
        self._add_edge(to_node, from_node, cost)

    def _add_edge(self, from_node, to_node, cost):
        self.edges.setdefault(from_node, [])
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = cost

    def print_graph(self) -> list:
        return [str(self.edges), str(self.distances)]


def find_min_road(graph: Graph, init: str) -> (dict, dict):  

    costs = {init: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in costs:
                if min_node is None:
                    min_node = node
                elif costs[node] < costs[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        cur_wt = costs[min_node]

        for edge in graph.edges[min_node]:
            wt = cur_wt + graph.distances[(min_node, edge)]
            if edge not in costs or wt < costs[edge]:
                costs[edge] = wt
                path[edge] = min_node

    return costs, path


def get_road(path: dict, from_node: str, to_node: str) -> str:
    result = to_node + ' '
    cur_node = to_node
    while path[cur_node] != from_node:
        cur_node = path[cur_node]
        result += cur_node + ' '
    result += from_node
    result = result[::-1].replace(' ', '->')
    return result


graph = Graph()


# GUI

def btn_print_graph() -> None:
    global graph
    scr.insert(INSERT, "Вершины: " + str(graph.print_graph()[0])+"\n")
    scr.insert(INSERT, "Путь: " + str(graph.print_graph()[1])+"\n")

def btn_add_node() -> None:
    graph.add_node(txt1.get())


def btn_add_edge() -> None:
    graph.add_edge(txt1.get(), txt2.get(), int(txt3.get()))


def btn_clear_graph() -> None:
    global graph
    graph = Graph()


def btn_road() -> None:
    from_node = txt1.get()
    to_node = txt2.get()
    vis, path = find_min_road(graph, from_node)
    if to_node in vis.keys() and from_node in vis.keys():
        scr.insert(INSERT, "Минимальная стоимость: " + str(vis[to_node]) + '\n')
        scr.insert(INSERT, "Путь: " + get_road(path, from_node, to_node) + '\n')
    else:
        scr.insert(INSERT, "Пути нет\n")

window = Tk()
window.title("Лабораторная работа 1")
window.geometry('500x350')

txt1 = Entry(window, width=30)
txt1.grid(column=2, row=2)

txt2 = Entry(window, width=30)
txt2.grid(column=2, row=3)

txt3 = Entry(window, width=30)
txt3.grid(column=2, row=4)

scr = scrolledtext.ScrolledText(window, width=40, height=10)
scr.grid(column=1, row=0)
btn_append_node = Button(window, text="Добавить вершину(1-ый)", command=btn_add_node)
btn_append_node.grid(column=1, row=1)
btn_clear_edge = Button(window, text="Добавить путь от 1->2(1-ый, 2-ой)", command=btn_add_edge)
btn_clear_edge.grid(column=1, row=2)
btn_clear = Button(window, text="Очистить граф", command=btn_clear_graph)
btn_clear.grid(column=1, row=3)
btn_get_road = Button(window, text="Вычислить путь до пункта(1-ый, 2-ой)", command=btn_road)
btn_get_road.grid(column=1, row=4)
btn_print = Button(window, text="Напечатать граф", command=btn_print_graph)
btn_print.grid(column=1, row=5)


window.mainloop()
