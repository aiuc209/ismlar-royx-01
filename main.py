def teskari_ismlar(ismlar):
    yangi_ismlar = []
    for ism in ismlar:
        harflar = list(ism)
        harflar.sort(reverse=True)
        yangi_ism = ''.join(harflar)
        yangi_ismlar.append(yangi_ism)
    return yangi_ismlar

ismlar = ["ali", "bobur", "javohir"]
print(teskari_ismlar(ismlar))
