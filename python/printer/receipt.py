from escpos import printer
esc = printer.Usb(0x0416, 0x5011, in_ep=0x81, out_ep=0x03)

def pr(*msg):
    print(msg)
#def foo():
    esc.set(align="center", custom_size=True, width=2, height=2)
    for m in msg:
        esc.block_text("{}\n".format(m), font="b", columns=16)
        esc.ln()
    esc.print_and_feed(2)

LBL = """
Soup Dec 2022
Foo

Bar
""".strip().split('\n')

print(LBL)


if __name__ == '__main__':
    pr(LBL)
#    pr('Chili', 'Sep 2022')
 


