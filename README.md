### NAME
TTmTDB - Difference between the TT and TDB time scale in seconds.

### SYNOPSIS
TTmTDB returns the difference between the TT time scale (terrestrial time, proper time on the earth's geoid at sea level) and the TDB time scale (barycentric dynamical time, taking into account time dilatation in the solar system). Other time scales are connected to TT and TDB via simple scalings but TT-TDB depends on the position of the bodies in the solar system and must be evaluated by ephemeris theories.

TTmTDB tests against INPOP21 with an error of 200ns over 2 centuries (it is in fact used for Inpop unit testing). TTmTDB uses 127 periodic terms given by Fairhead & Bretagnon 

For the past and next centuries the TTmTDB correction has a maximum value of less than 2 ms so it is only required for high precision applications.

#### REQUIREMENTS
TTmTDB depends on Numpy. Numba is not required but will result in a significant speedup.

#### PROVIDES
A single function, TTmTDB.

### DESCRIPTION
The Python module is called ttmtdb:

```python
from ttmtdb import TTmTDB

JD2000 = 2451545.0

dt = TTmTDB(JD2000)
print(dt)
9.930573125973422e-05  # seconds
```
It is possible to pass a second time argument, typically containing a day fraction:

```python
dt2 = TTmTDB(JD2000, 1/12)
print(dt2)
9.689409358933716e-05  # seconds
```

### AUTHOR
TTmTDB is written by Marcel Hesselberth.

### REPORTING BUGS
Inpop online help: https://github.com/hesselberth/TTmTDB/issues

### COPYRIGHT
Marcel Hesselberth.

TTmTDB is released under GPLv3. The text of the license can be found at https://www.gnu.org/licenses/gpl-3.0.txt .
This is free software: you are free to change and redistribute it. There is NO WARRANTY.

### SEE ALSO
Fairhead & Bretagnon (A&A 229, 240-247, 1990).
