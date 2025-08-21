import argparse
import random
import time
from typing import List

ARDESI_RESIDUES = (1, 7, 11, 13, 17, 19, 23, 29)

def is_probable_prime(n: int, rounds: int = 8) -> bool:
    if n < 2:
        return False
    small = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for p in small:
        if n % p == 0:
            return n == p

    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(rounds):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def candidati_ardesi(n: int, k: int = 3) -> List[int]:
    base = n - (n % 30)
    out = []
    for r in ARDESI_RESIDUES:
        c = base + r
        if c >= n:
            out.append(c)
            if len(out) >= k:
                break
    return out

def parse_args():
    p = argparse.ArgumentParser()
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--exp", nargs=2, type=int, metavar=("X", "Y"))
    g.add_argument("--range", nargs=2, type=int, metavar=("START", "STOP"))
    p.add_argument("-k", type=int, default=3)
    p.add_argument("--only-primes", action="store_true")
    p.add_argument("--rounds", type=int, default=8)
    return p.parse_args()

def main():
    args = parse_args()
    if args.exp:
        X, Y = args.exp
        start = 10 ** min(X, Y)
        stop  = 10 ** max(X, Y)
    else:
        s, t = args.range
        start, stop = (s, t) if s <= t else (t, s)

    t0 = time.perf_counter()
    results = []
    first4 = []
    n = max(2, start)
    n -= (n % 30)

    while n <= stop:
        cand_list = candidati_ardesi(max(n, start), args.k)
        for c in cand_list:
            if c > stop:
                break
            if args.only_primes:
                if is_probable_prime(c, rounds=args.rounds):
                    results.append(c)
                    if len(first4) < 4:
                        first4.append(c)
            else:
                results.append(c)
                if len(first4) < 4:
                    first4.append(c)
        n += 30

    t1 = time.perf_counter()

    # --- riepilogo pulito ---
    print(f"Numero primi previsti: {len(results)}")
    if first4:
        print("Primi 4 più probabili:")
        # calcola probabilità teorica Miller–Rabin
        prob = 1 - 1/(4**args.rounds)
        for x in first4:
            print(f"  {x}  (Probabilità ≈ {prob:.12f})")
    else:
        print("Primi 4 più probabili: (nessuno trovato)")
    print(f"Tempo di calcolo: {t1 - t0:.3f} secondi")

if __name__ == "__main__":
    main()
