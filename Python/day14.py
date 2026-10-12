def greet():
    print("Namaste, Welcome to the KFC")
greet()

def calculate_bill(momo, noodles, kfc):
    momo_quantity = 1
    noodles_quantity = 2
    kfc_quantity = 1
    print(f"Momo={momo*momo_quantity}")
    print(f"Noodels={noodles*noodles_quantity}")
    print(f"KFC={kfc*kfc_quantity}")
    total = momo + (noodles*noodles_quantity) + kfc
    print(f"Total bill: {total}")
calculate_bill(150, 160, 900)
