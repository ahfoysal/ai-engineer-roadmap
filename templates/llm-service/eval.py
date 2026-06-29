"""Tiny eval harness — your 'tests' for a non-deterministic service.

You don't assert exact strings against an LLM. You score behavior over a
dataset and gate on the score. Expand EVAL_SET as you learn what matters.

Run:  python eval.py   (requires the service running, or import & call directly)
"""
from __future__ import annotations

from app import ExtractRequest, extract

# (input text, things that MUST appear in the structured result)
EVAL_SET = [
    ("Hi, I'm Dana Lee from Acme Corp, reach me at dana@acme.io", {"email": "dana@acme.io", "company": "Acme"}),
    ("Contact: sam@startup.dev — Sam, founder", {"email": "sam@startup.dev", "name": "Sam"}),
]


def score() -> float:
    passed = 0
    for text, expectations in EVAL_SET:
        result = extract(ExtractRequest(text=text)).model_dump()
        ok = all(
            str(v).lower() in str(result.get(k, "")).lower()
            for k, v in expectations.items()
        )
        print(f"[{'PASS' if ok else 'FAIL'}] {text[:40]!r} -> {result}")
        passed += ok
    pct = passed / len(EVAL_SET)
    print(f"\nScore: {passed}/{len(EVAL_SET)} = {pct:.0%}")
    return pct


if __name__ == "__main__":
    score()
