---
name: typed-holes
description: Use when designing a system's slots before its parts exist, so a type checker, not a reviewer, decides whether each part fits its slot.
---

# Typed holes

## Inputs
- The goal as a list of slots (terms), each with what it consumes and produces.
- A checker with sections or holes (Coq, Agda, Idris, Lean, or a typed language).

## Steps
1. Write each slot as a declared hole with its type: in Coq, a `Variable name : Type.` inside a `Section`; in Agda or Idris, a hole `?name`.
2. Write the whole as one definition that uses every hole (the harness).
3. Closure check: compile, then confirm every declared hole is a binder of the closed definition after the section ends (Coq silently drops a section Variable that nothing uses). Print one line: CLOSED or FAIL naming the unconsumed holes.
4. Plant: remove one use of a hole in a copy; the closure check must print FAIL. Keep the plant in the check script.
5. Fill a hole by giving a term; it fits iff the checker accepts it there. Keep a table: hole, owner, check, what it is not, cost.
6. For pieces with no type (prose, config), fall back to a removal or ledger check and say so in the table.

## Done test
A piece fits iff the checker accepts it in its hole; the closure check prints CLOSED, and its plant prints FAIL.

## Evidence
- A 13-hole harness (32 Variables, coqc 8.18) read MESH CLOSED; dropping one hole's use read MESH FAIL; later 16 holes / 35 Variables stayed CLOSED (VERIFY/MESH/FINDINGS.md:3, VERIFY/MESH/check.sh).
- Chosen over five alternatives (refinement calculus, Parnas criteria, wiring-diagram operads, design structure matrix, axiomatic design) because it alone makes fit mechanical (MESH-METHOD/PRIOR-ART.md, citations opened).

## Where it failed
- A type decides fit only as far as it states the slot: an under-stated type is the new underdefinition (inferred).
- Not compared head to head against the untyped ledger on the same target.

## Not for
- Auditing an artifact that already exists (use mesh-ledger).
- Prose or config pieces with no type.
