from loader import Loader
from collect_manger import CollectManager
from mainwindow import MainWindow


def main():
    L = Loader('schemas/')
    cm = CollectManager()

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

    cm.add(decryptor)
    cm.add(matrix)
    cm.add(multiplexer)
    cm.add(and1)
    cm.add(and2)

    cm.set_ins(decryptor, {'A0': 1, 'A1': 1, 'A2': 1})
    cm.set_ins(multiplexer, {'A0': 0, 'A1': 1, 'A2': 1})
    cm.set_ins(and1, {'X1': 1, 'X2': 1})
    cm.execute(decryptor, True)

    mw = MainWindow()
    mw.draw_schema(decryptor, [50, 50])
    mw.draw_matrix(matrix, [200, 50])
    mw.draw_schema(multiplexer, [360, 250])
    mw.draw_schema(and1, [360, 460])
    mw.draw_schema(and2, [520, 420])
    mw.draw_connections()
    mw.execute()


if __name__ == '__main__':
    main()
