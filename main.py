from loader import Loader
from collect_manger import CollectManager
from mainwindow import MainWindow


def main():
    L = Loader('schemas/')

    decryptor = L.load_schema('decryptor')
    matrix = L.load_schema('storage_matrix')
    multiplexer = L.load_schema('multiplexer')
    and1 = L.load_schema('and')
    and2 = L.load_schema('and')

    decryptor.connector.add(matrix,
                            {'Y0': 'Y0',
                             'Y1': 'Y1',
                             'Y2': 'Y2',
                             'Y3': 'Y3',
                             'Y4': 'Y4',
                             'Y5': 'Y5',
                             'Y6': 'Y6',
                             'Y7': 'Y7'})
    matrix.connector.add(multiplexer,
                         {'X0': 'X0',
                          'X1': 'X1',
                          'X2': 'X2',
                          'X3': 'X3',
                          'X4': 'X4',
                          'X5': 'X5',
                          'X6': 'X6',
                          'X7': 'X7'})
    multiplexer.connector.add(and2, {'Y': 'X1'})
    and1.connector.add(and2, {'Y': 'X2'})

    cm = CollectManager(decryptor)
    cm.add(matrix)
    cm.add(multiplexer)
    cm.add(and1)
    cm.add(and2)

    mw = MainWindow(cm)
    mw.canvas.schema(decryptor, [50, 50]).draw()
    mw.canvas.matrix(matrix, [200, 50]).draw()
    mw.canvas.schema(multiplexer, [360, 250]).draw()
    mw.canvas.schema(and1, [360, 460]).draw()
    mw.canvas.schema(and2, [520, 420]).draw()
    connections = mw.canvas.connections()
    for connection in connections:
        connection.draw()

    mw.execute()


if __name__ == '__main__':
    main()
