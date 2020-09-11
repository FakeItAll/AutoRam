from loader import Loader
from collect_manger import CollectManager
from mainwindow import MainWindow


def main():
    loader = Loader()
    cm = CollectManager()

    mod1 = loader.load_schema('decryptor')
    mod2 = loader.load_schema('multiplexer')
    mod3 = loader.load_schema('and')

    mod1.connector.add(mod2, {'Y0': 'A1', 'Y1': 'A2', 'Y2': 'X0'})
    mod2.connector.add(mod3, {'Y': 'I1', 'Y': 'I2'})

    cm.add(mod1)
    cm.add(mod2)
    cm.add(mod3)

    ins = {'A1': 1, 'A2': 0, 'A3': 0}
    cm.execute(mod1, ins, True)

    mw = MainWindow()
    mw.draw_schema(mod1, [100, 300])
    mw.draw_schema(mod2, [50, 150])
    mw.draw_schema(mod3, [60, 40])
    mw.execute()

"Тест"
if __name__ == '__main__':
    main()
