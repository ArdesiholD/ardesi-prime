# Ardesi Prime

Script/CLI for the **Ardesi Binary Pattern** as a pre‑filter for primality tests (Miller–Rabin).  
This repository uses the **original code** provided by the author in `ardesi_prime.py`  
and also exposes a console script `ardesi-prime` after installation.

---

## Installation (local)

```bash
python -m pip install .
```

> Windows: if `python` opens the Microsoft Store, disable aliases in  
> **Settings → Apps → Advanced app settings → App execution aliases**  
> for `python.exe` and `python3.exe`. Add the Python folder to the PATH.

---

## Usage

Run the file directly:

```bash
python ardesi_prime.py --range 10000000000 10000002000 --only-primes
```

Or, after installation as a package:

```bash
ardesi-prime --range 10000000000 10000002000 --only-primes
```

### Main Options
- `--exp X Y`  : interval as powers, from 10^X to 10^Y (inclusive)
- `--range A B`: explicit interval [A, B]
- `-k INT`     : maximum number of candidates per block (default: 3)
- `--only-primes` : print only the **actual primes** (with Miller–Rabin confidence)
- `--rounds INT`  : Miller–Rabin rounds (default: 8)

---

## Example output (summary)
```
Number of expected primes: 4
Top 4 most probable:
  10000000019  (Probability ≈ 0.999999996275)
  10000000033  (Probability ≈ 0.999999996275)
  10000000061  (Probability ≈ 0.999999996275)
  10000000069  (Probability ≈ 0.999999996275)
Computation time: 0.412 seconds
```

---

## Tips for large ranges

The `ardesi_prime.py` file stores results in memory. For **huge ranges**,  
run in **blocks** (e.g. `--range A A+10_000_000`, then `A+10_000_001 ...`) or  
redirect output to a file:

```bash
python ardesi_prime.py --range 10000000000 10000002000 --only-primes > primes.txt
```

---

## License
MIT © Marco Ardesi
