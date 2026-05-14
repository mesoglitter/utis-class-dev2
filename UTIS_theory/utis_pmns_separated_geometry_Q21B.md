# UTIS Separated PMNS Geometry Q-21B

## 1. Goal

Construct separated charged-lepton and neutrino branch geometries generating PMNS-like large mixing.

---

## 2. Core interpretation

```text
charged leptons -> localized/folded geometry
neutrinos       -> delocalized/unfolded geometry
```

---

## 3. Charged-lepton overlap matrix

```text
[[1.00000000e+00 1.29922608e-01 5.13137905e-05]
 [1.29922608e-01 1.00000000e+00 5.29305019e-02]
 [5.13137905e-05 5.29305019e-02 1.00000000e+00]]
```

Parameters:

```text
sigma_e = 0.35
positions = [0.0, 1.0, 2.2]
```

---

## 4. Neutrino overlap matrix

```text
[[1.         0.93941306 0.66148676]
 [0.93941306 1.         0.8569834 ]
 [0.66148676 0.8569834  1.        ]]
```

Parameters:

```text
sigma_nu = 1.4
positions = [0.0, 0.7, 1.8]
```

---

## 5. PMNS extraction

```text
V_PMNS = U_e^dagger U_nu
```

Extracted |V_PMNS|:

|     |      nu1 |      nu2 |       nu3 |
|:----|---------:|---------:|----------:|
| e   | 0.986807 | 0.136516 | 0.0870325 |
| mu  | 0.105681 | 0.950402 | 0.292518  |
| tau | 0.122649 | 0.279461 | 0.952291  |

---

## 6. Mixing-angle scales

```text
theta12 = 0.136516
theta23 = 0.292518
theta13 = 0.087032
```

Interpretation:

```text
non-identical branch geometries
→ nontrivial PMNS mixing structure
```

---

## 7. UTIS interpretation

```text
localized folded branch vacuum
→ charged-lepton hierarchy

delocalized unfolded branch vacuum
→ neutrino large mixing

mismatch of branch geometry
→ PMNS emergence
```

---

## 8. Unitary consistency

```text
[[1.00000000e+00 2.58420927e-16 3.93517029e-16]
 [2.58420927e-16 1.00000000e+00 6.51518947e-17]
 [3.93517029e-16 6.51518947e-17 1.00000000e+00]]
```

---

## 9. Important caution

```text
This remains a toy PMNS scaffold.
```

Still required:

```text
neutrino mass ordering
Majorana structure
oscillation fits
CP phase fit
global phenomenology
```

---

## 10. Long-term target

Desired chain:

```text
branch localization asymmetry
→ mismatch geometry
→ unitary PMNS structure
→ large lepton mixing
→ neutrino phenomenology
```
