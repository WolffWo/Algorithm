## Implemention of the algorithms

###Literature:

<<<<<<< HEAD
- ['Das Sieb des Eratosthenes: Wie schnell kann man eine Primzahlentabelle berechnen?'](
https://prof.beuth-hochschule.de/fileadmin/user/oellrich/eratosthenes.pdf)
    by *Rolf Möhring und Martin Oellrich
    *Institut für Mathematik, Technische Universität Berlin*
=======
- ['Das Sieb des Eratosthenes: Wie schnell kann man eine Primzahlentabelle berechnen?'](https://prof.beuth-hochschule.de/fileadmin/user/oellrich/eratosthenes.pdf)

    by *Rolf Möhring und Martin Oellrich Institut für Mathematik, Technische Universität Berlin*
>>>>>>> origin/master

- Useful for testing http://www.arndt-bruenner.de/mathe/scripts/primzahlen.htm

### List of algorithms

`eratosthenes.py`
  - Calc a table of prime numbers from 2 to n and the run time. Using the algorithm of eratosthenes. Be careful with n!

| n    | time  | # prime numbers  |
|------:|-------|------------------:|
| 10 | 5.19752502441e-05 | 4 |
| 100 | 0.00389409065247 | 25 |
| 1000 | 1.91667890549 | 168 |

`eratosthenesBetter.py`

 - Better algorithms

| n    | time  | # prime numbers  |
|------:|-------|------------------:|
| 10 | 3.60012054443e-05 | 4 |
| 100 | 0.000226020812988 | 25 |
| 1000 | 0.0174708366394 | 168 |

 `eratosthenesEvenBetter.py`
  - Even better algorithms

| n    | time  | # prime numbers  |
|------:|-------|------------------:|
| 10 | 6.07967376709e-05 | 4 |
| 100 | 0.000262975692749 | 25 |
| 1000 | 0.0124711990356 | 168 |


 `eratosthenesEndVersion.py`
  - End version of the algorithms


| n    | time  | # prime numbers  |
|------:|-------|------------------:|
| 10 | 4.41074371338e-05 | 4 |
| 100 | 0.000207185745239 | 25 |
| 1000 | 0.0142419338226 | 168 |
