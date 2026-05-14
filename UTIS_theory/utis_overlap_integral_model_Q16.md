# UTIS Explicit Overlap Integral Model Q-16

## 1. Goal

Construct explicit branch-wavefunction overlap integrals for CKM/PMNS precursor structure.

---

## 2. Gaussian branch wavefunctions

```text
psi_i(x) ~ exp[-(x-x_i)^2/(2 sigma^2)]
```

Interpretation:

```text
x_i     = branch-vacuum center
sigma   = localization width
```

---

## 3. Overlap integrals

### O12

```text
sqrt(pi)*N_q**2*sigma_q*exp((-2*x1**2 + 4*x1*x2 - 2*x2**2 + (x1 - x2)**2)/(4*sigma_q**2))
```

### O23

```text
sqrt(pi)*N_q**2*sigma_q*exp((-2*x2**2 + 4*x2*x3 - 2*x3**2 + (x2 - x3)**2)/(4*sigma_q**2))
```

### O13

```text
sqrt(pi)*N_q**2*sigma_q*exp((-2*x1**2 + 4*x1*x3 - 2*x3**2 + (x1 - x3)**2)/(4*sigma_q**2))
```

---

## 4. Key hierarchy structure

```text
large separation -> exponentially suppressed overlap
```

Interpretation:

```text
Overlap ~ exp[-distance^2/(4 sigma^2)]
```

This naturally generates:

```text
hierarchical mixing angles
suppressed distant mixing
nearest-neighbor dominance
```

---

## 5. CKM-like branch geometry

```text
small sigma_q + separated branches
```

Interpretation:

```text
localized vacuum states
small overlap
hierarchical mixing
```

---

## 6. PMNS-like branch geometry

```text
large sigma_l + overlapping branches
```

Interpretation:

```text
broad vacuum support
large overlap
large flavor mixing
```

---

## 7. Physical interpretation map

### localized_state

```text
small width -> weak overlap
```

### delocalized_state

```text
large width -> broad overlap
```

### hierarchical_mixing

```text
exponential overlap suppression
```

### large_lepton_mixing

```text
extended overlap geometry
```

### folded_branch

```text
screened localized vacuum mode
```

### unfolded_branch

```text
extended propagation vacuum mode
```

---

## 8. Possible UTIS interpretation

```text
branch vacuum geometry
→ localized/delocalized states
→ overlap integrals
→ effective flavor mixing
→ CKM / PMNS hierarchy emergence
```

---

## 9. Important caution

At this stage:

```text
This is still a toy overlap scaffold.
```

Still required:

```text
unitary normalization
exact flavor basis
mass matrix derivation
CP phase emergence
fermion representation structure
gauge consistency
```

---

## 10. Long-term target

Desired chain:

```text
vacuum branch geometry
→ localized wavefunctions
→ overlap integrals
→ mixing matrices
→ CKM / PMNS structure
→ flavor phenomenology
```

---

## 11. Next step Q-17

Construct normalized unitary mixing scaffold:

```text
normalized overlap matrix
Gram-Schmidt/unitary structure
mixing-angle extraction
CP-phase scaffold
comparison to observed hierarchy
```
