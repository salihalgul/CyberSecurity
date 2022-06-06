"""
Bu ödevde size verilecek bir string içerisindeki sesli harfleri sayıp bunları bir dict olarak kaydedeceksiniz.
dict objeniz aşağıdaki gibi olacaktır:
{
    'a': 7,
    'e': 9,
    'i': 4,
    ........
}

Sonrasinda bu dict objesini aşağıdaki formatta ekrana yazdıracaksınız:

a = 7
-----
e = 9
-----
i = 4
-----
..........


Örnek stringiniz de:
Başım köpük köpük bulut
İçim dışım deniz
Ben bir ceviz ağacıyım Gülhane Parkı’nda
Budak budak, şerham şerham ihtiyar bir ceviz
Ne sen bunun farkındasın ne polis farkında

Ben bir ceviz ağacıyım Gülhane Parkı’nda
Ne sen bunun farkındasın ne de polis farkında
"""


sesli_harfler = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']
ornek_string = "Başım köpük köpük bulut İçim dışım deniz Ben bir ceviz ağacıyım Gülhane Parkı’nda Budak budak, " \
        "şerham şerham ihtiyar bir ceviz Ne sen bunun farkındasın ne polis farkında Ben bir ceviz ağacıyım" \
        " Gülhane Parkı’nda Ne sen bunun farkındasın ne de polis farkında"
ornek_sonucu = []
for i in ornek_string:
        if i == sesli_harfler:
                ornek_sonucu.count(i)
print(ornek_sonucu)
