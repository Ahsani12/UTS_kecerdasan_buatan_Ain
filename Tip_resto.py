def triangular(x, a, b, c):
    if x <= a or x >= c:
        return 0.0
    if x <= b:
        return (x - a) / (b - a)
    else:
        return (c - x) / (c - b)

# Membership functions
def food_bad(x):        return triangular(x, 0, 0, 5)
def food_good(x):       return triangular(x, 5, 10, 10)
def service_poor(x):    return triangular(x, 0, 0, 5)
def service_excellent(x): return triangular(x, 5, 10, 10)
def tip_low(x):         return triangular(x, 0, 0, 10)
def tip_high(x):        return triangular(x, 10, 20, 20)

def hitung_tip(food, service):
    # 1. Fuzzification
    f_bad  = food_bad(food)
    f_good = food_good(food)
    s_poor = service_poor(service)
    s_exc  = service_excellent(service)

    # 2. Rule Inference
    alpha_low  = max(s_poor, f_bad)        # Rule 1
    alpha_high = min(s_exc, f_good)        # Rule 2

    # 3. Defuzzifikasi Centroid
    n = 2000
    dx = 20.0 / n
    x = 0.0
    numerator = 0.0   # Σ (x × μ(x))
    denominator = 0.0 # Σ μ(x)

    for i in range(n + 1):
        tip_val = x

        # Clipping
        mu_low  = min(alpha_low,  tip_low(tip_val))
        mu_high = min(alpha_high, tip_high(tip_val))
        mu_agg  = max(mu_low, mu_high)

        # Integral approximation: f(x) * dx
        numerator   += tip_val * mu_agg * dx
        denominator += mu_agg * dx

        x += dx

    tip_akhir = numerator / denominator if denominator > 0 else 0.0

    # Output
    print("\n" + "="*65)
    print("           SISTEM TIP RESTAURANT")
    print("="*65)
    print(f"Food Quality    : {food:5.1f}  → Bad = {f_bad:5.3f} | Good = {f_good:5.3f}")
    print(f"Service Quality : {service:5.1f}  → Poor = {s_poor:5.3f} | Excellent = {s_exc:5.3f}")
    print("-"*65)
    print(f"Rule 1 (Low)    α = {alpha_low:.3f}")
    print(f"Rule 2 (High)   α = {alpha_high:.3f}")
    print("-"*65)
    print(f"       TIP YANG DISARANKAN: {tip_akhir:6.2f}%")
    print("="*65 + "\n")

# PROGRAM UTAMA
print("SISTEM TIP RESTAURANT")
print("Masukkan nilai 0-10 | ketik 'exit' untuk keluar\n")

while True:
    try:
        inp = input("Food Quality (0-10): ").strip()
        if inp.lower() in ["exit", "quit", "q"]: 
            print("Terima kasih!")
            break
        food = float(inp)

        inp = input("Service Quality (0-10): ").strip()
        if inp.lower() in ["exit", "quit", "q"]: 
            print("Terima kasih!")
            break
        service = float(inp)

        if not (0 <= food <= 10 and 0 <= service <= 10):
            print("Error: Nilai harus 0 sampai 10!\n")
            continue

        hitung_tip(food, service)

    except ValueError:
        print("Error: Masukkan angka!\n")