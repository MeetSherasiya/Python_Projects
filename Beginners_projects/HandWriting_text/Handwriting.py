# import pywhatkit as pw

# txt = """"Python is an interpreted high-level general-purpose programming.
# Its design philosophy emphasizes code readability with its use of significant."""

# pw.text_to_handwriting(txt, "demo1.pdf",[0,0,138])
# print("END ")


from PIL import Image
txt=open("dummy.txt")
# path of your text file#path of page(background)photo (I have used blank page)
BG=Image.open("bg.png")
sheet_width=BG.width
gap, ht = 0, 0
for i in txt.read().replace("\n",""):
    cases = Image.open("myfont/{}.png".format(str(ord(i))))
    BG.paste(cases, (gap, ht))
    size = cases.width
    height=cases.height
    #print(size)
    gap+=size
    if sheet_width < gap or len(i)*115 >(sheet_width-gap):
        gap,ht=0,ht+140
print(gap)
print(sheet_width)
BG.show()