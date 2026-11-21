# Task 8 – Algorithm planning

Add pseudocode, a flowchart image and a hand trace for three entries.

Suggested pseudocode outline:

```text
START
SET ten_day_total TO 0
FOR each entry IN entries
    IF entry is valid THEN
        CALCULATE rate per litre
        CALCULATE payment
        SET ten_day_total TO ten_day_total + payment
    ELSE
        OUTPUT "Invalid entry"
    ENDIF
ENDFOR
OUTPUT ten_day_total
END
```
