# UTIS Einstein / FRW Limit Recovery Q-13

## 1. Goal

Check whether the emergent geometric-flow equations recover Einstein/FRW-like behavior in weak-flow limits.

---

## 2. Weak-flow assumptions

### small_gradient

```text
|∂Phi| << 1
```

### small_curvature

```text
|R| << 1
```

### near_uniform_density

```text
rho(x,t) ~ rho0 + epsilon*delta_rho
```

### slow_metric_evolution

```text
|∂t g| << 1
```

---

## 3. Geometric-flow equation

```text
alpha*R(x, t) - beta*rho(x, t) + Derivative(g(x, t), t) = 0
```

Equivalent form:

```text
∂t g ~ -alpha R + beta rho
```

---

## 4. Curvature relation

```text
R(x, t) - Derivative(Phi(x, t), (x, 2)) = 0
```

Equivalent form:

```text
R ~ ∂x²Phi
```

---

## 5. Einstein-like weak-flow limit

Assume:

```text
∂t g -> small
```

Then:

```text
alpha*R(x, t) - beta*rho(x, t) ~ 0
```

Equivalent form:

```text
R ~ (beta/alpha) rho
```

Interpretation:

```text
effective curvature sourced by branch density
```

---

## 6. Homogeneous FRW-like reduction

Assume:

```text
rho(x,t) -> rho0(t)
```

Then:

```text
alpha*R(x, t) - beta*rho0 ~ 0
```

Equivalent form:

```text
R ~ rho0
```

Possible cosmological interpretation:

```text
H^2 ~ rho_eff
```

---

## 7. Correspondence map

### rho_branch

```text
effective matter-density source
```

### Phi_curvature

```text
effective curvature potential
```

### metric_flow

```text
large-scale spacetime evolution
```

### weak_flow_limit

```text
Einstein-like smooth geometry regime
```

### homogeneous_limit

```text
FRW-like cosmological sector
```

---

## 8. Possible UTIS interpretation

```text
branch-density flow
→ effective curvature sourcing
→ smooth geometric regime
→ Einstein-like limit
→ FRW-like cosmological evolution
```

---

## 9. Important caution

At this stage:

```text
This is a correspondence scaffold,
not a full derivation of Einstein gravity.
```

Still required:

```text
full covariant derivation
tensor structure recovery
exact Einstein equations
full FRW perturbation sector
Boltzmann consistency
```

---

## 10. Long-term interpretation

Current UTIS picture resembles:

```text
cyclic branch medium
→ directed vacuum flow
→ emergent curvature sourcing
→ screened/unfolded geometry
→ Einstein-like smooth limit
→ cosmological large-scale structure
```

---

## 11. Next step Q-14

Construct perturbation-sector emergence:

```text
linearized geometric flow
scalar perturbations
effective Poisson equation
screened growth sector
connection to CLASS observables
```
