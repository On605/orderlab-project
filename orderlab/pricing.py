# orderlab/pricing.py

a = 100


def subtotal(unit_price: int, quantity: int) -> int:
    # 단가와 수량으로 부분합을 계산한다. 음수는 허용하지 않는다.
    if unit_price < 0 or quantity < 0:
        raise ValueError("negative input")
    return unit_price * quantity


def final_total(price: int, qty: int, discount: int) -> int:
    if not 0 <= discount <= 100:
        raise ValueError("invalid discount")
    amount = subtotal(price, qty)
    amount -= amount * discount // 100
    shipping = 3_000 if 0 < amount <= 50_000 else 0
    return amount + shipping
