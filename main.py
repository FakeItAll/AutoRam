from loader import Loader


def main():
    loader = Loader('')
    mod1 = loader.load('decryptor')
    mod2 = loader.load('decryptor')

    d = [mod1, mod2]
    d[0].ins = [1, 1, 1]
    d[0].f()
    print(d[0].outs)
    d[1].ins = d[0].outs[:3]
    d[1].f()
    print(d[1].outs)


main()
