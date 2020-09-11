from loader import Loader
from collect_manger import CollectManager
from mainwindow import MainWindow


def main():
    loader = Loader()
    cm = CollectManager()

    mod1 = loader.load_schema('decryptor')
    mod2 = loader.load_schema('decryptor')
    mod3 = loader.load_schema('and')

    uid1 = cm.add(mod1)
    uid2 = cm.add(mod2)
    cm.connect({uid1: {'D0': [uid2, 'A'], 'D1': [uid2, 'B'], 'D2': [uid2, 'C']}})

    uid3 = cm.add(mod3)
    cm.connect({uid2: {'D0': [uid3, 'I1'], 'D1': [uid3, 'I2']}})

    ins = {'A': 1, 'B': 0, 'C': 0}
    cm.execute(uid1, ins, True)

    mw = MainWindow()
    mw.draw_schema(mod1, [360, 60])
    mw.execute()


if __name__ == '__main__':
    main()
