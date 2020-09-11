from loader import Loader
from collect_manger import CollectManager


def main():
    loader = Loader()
    cm = CollectManager()

    mod1 = loader.load_schema('decryptor')
    mod2 = loader.load_schema('decryptor')
    mod3 = loader.load_schema('and')

    uid1 = cm.add(mod1)
    uid2 = cm.add(mod2)
    cm.connect({uid1: {0: [uid2, 0], 1: [uid2, 1], 2: [uid2, 2]}})

    uid3 = cm.add(mod3)
    cm.connect({uid2: {0: [uid3, 0], 1: [uid3, 1]}})

    ins = {0: 1, 1: 0, 2: 0}
    cm.execute(uid1, ins, True)


if __name__ == '__main__':
    main()
