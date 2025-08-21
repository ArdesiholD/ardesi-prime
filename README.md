# Ardesi Prime

Script/CLI per il **Pattern Binario Ardesi** come pre‑filtro ai test di primalità (Miller–Rabin).
Questo repository usa **il codice originale** fornito dall'autore in `ardesi_prime.py`
ed espone anche una *console script* `ardesi-prime` dopo l'installazione.

## Installazione (locale)

```bash
python -m pip install .
```

> Windows: se `python` apre il Microsoft Store, disattiva gli alias in
> **Impostazioni → App → Impostazioni avanzate app → Alias di esecuzione app**
> per `python.exe` e `python3.exe`. Aggiungi la cartella di Python al PATH.

## Utilizzo

Esecuzione diretta del file:

```bash
python ardesi_prime.py --range 10000000000 10000002000 --only-primes
```

Oppure, dopo l'installazione come pacchetto:

```bash
ardesi-prime --range 10000000000 10000002000 --only-primes
```

### Opzioni principali
- `--exp X Y`  : intervallo come potenze, da 10^X a 10^Y (inclusi)
- `--range A B`: intervallo esplicito [A, B]
- `-k INT`     : numero massimo di candidati per blocco (default: 3)
- `--only-primes` : stampa solo i **primi reali** (con confidenza Miller–Rabin)
- `--rounds INT`  : round di Miller–Rabin (default: 8)

### Output di riepilogo (esempio)
```
Numero primi previsti: 4
Primi 4 più probabili:
  10000000019  (Probabilità ≈ 0.999999996275)
  10000000033  (Probabilità ≈ 0.999999996275)
  10000000061  (Probabilità ≈ 0.999999996275)
  10000000069  (Probabilità ≈ 0.999999996275)
Tempo di calcolo: 0.412 secondi
```

## Consigli per intervalli grandi

Il file `ardesi_prime.py` accumula i risultati in memoria. Per **range enormi**,
esegui in **blocchi** (es.  /-range A A+10_000_000, poi A+10_000_001 .../ ) oppure
reindirizza l’output su file:

```bash
python ardesi_prime.py --range 10000000000 10000002000 --only-primes > primes.txt
```

## Licenza
MIT © Marco Ardesi
