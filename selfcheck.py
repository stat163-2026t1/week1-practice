"""Self-check for STAT163 practice notebooks (Week 1).

Confirms only that an answer is *saved* and has the right *type* — NOT that
the value is correct. You do not need to edit this file.
"""
import numpy as np
import pandas as pd


def _filled(v):
    return not (v is ... or (isinstance(v, str) and v.strip() in ("", "?", "...")))


_KINDS = {
    "integer":   (lambda v: isinstance(v, (int, np.integer)) and not isinstance(v, (bool, np.bool_)), "an integer"),
    "number":    (lambda v: isinstance(v, (int, float, np.integer, np.floating)) and not isinstance(v, (bool, np.bool_)), "a number"),
    "text":      (lambda v: isinstance(v, str), "text"),
    "Series":    (lambda v: isinstance(v, pd.Series), "a Series"),
    "DataFrame": (lambda v: isinstance(v, pd.DataFrame), "a DataFrame"),
}


def check(name, value, kind):
    if not _filled(value):
        print(f"⏳ {name}: not filled in yet"); return
    ok, label = _KINDS[kind]
    print(f"✅ {name}: saved (type — {label}). Move on."
          if ok(value) else
          f"⚠️ {name}: expected {label}, got {type(value).__name__}.")


def check_col(df, col):
    if not isinstance(df, pd.DataFrame) or col not in df.columns:
        print(f"⏳ column \"{col}\" not created yet"); return
    try:
        if df[col].map(lambda v: v is ...).all():
            print(f"⏳ column \"{col}\" not filled in yet"); return
    except Exception:
        pass
    print(f'✅ ["{col}"]: column created. Move on.')


def check_choice(name, value, allowed):
    if not _filled(value):
        print(f"⏳ {name}: not filled in yet"); return
    print(f"✅ {name}: answer \"{value}\" saved — the check does not test whether it is right. Move on."
          if str(value).strip().upper() in allowed else
          f"⚠️ {name}: expected one of {sorted(allowed)}.")


_PLACEHOLDER_NAMES = {"", "...", "name surname", "your name"}


def _norm_name(s):
    return s.strip().lower().replace("ʼ", "'").replace("`", "'").replace("’", "'")


def check_identity(name):
    """Confirms the name is filled in and differs from the placeholder (not graded)."""
    if not isinstance(name, str) or _norm_name(name) in _PLACEHOLDER_NAMES:
        print("⏳ student_name: replace the placeholder with your real name"); return
    print(f"✅ student_name: \"{name.strip()}\" saved. Move on.")
