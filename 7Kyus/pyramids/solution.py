def pyramid(n):
    p = ""
    fill = " "
    for i in range(0, n - 1):
        for _ in range(0, n - i - 1):
            p += fill
        p += "/"
        for _ in range(0, i * 2):
            p += fill
        p += "\\\n"
    last_line = "/"
    last_line += "".join("_" for _ in range(0, (n - 1) * 2)) + "\\\n"
    p += last_line
    return p


# ---------------------------------------------------------------------------
# Résultats attendus (tirés directement de l'énoncé)
# ---------------------------------------------------------------------------
EXPECTED = {
    4: (
        "   /\\\n"
        "  /  \\\n"
        " /    \\\n"
        "/______\\\n"
    ),
    6: (
        "     /\\\n"
        "    /  \\\n"
        "   /    \\\n"
        "  /      \\\n"
        " /        \\\n"
        "/__________\\\n"
    ),
    10: (
        "         /\\\n"
        "        /  \\\n"
        "       /    \\\n"
        "      /      \\\n"
        "     /        \\\n"
        "    /          \\\n"
        "   /            \\\n"
        "  /              \\\n"
        " /                \\\n"
        "/__________________\\\n"
    ),
}


# ---------------------------------------------------------------------------
# Couleurs ANSI pour un affichage lisible
# ---------------------------------------------------------------------------
GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
GRAY   = "\033[90m"
BOLD   = "\033[1m"
RESET  = "\033[0m"


def visible(text):
    """
    Rend visibles les espaces et les sauts de ligne.
    - Espaces      -> '·'
    - Saut de ligne -> '⏎' suivi d'un vrai \n
    Très utile pour repérer un \n final manquant ou un espace en trop.
    """
    if text is None:
        return f"{RED}<None>{RESET}"
    return (
        text.replace(" ", f"{GRAY}·{RESET}")
            .replace("\n", f"{GRAY}⏎{RESET}\n")
    )


def diff_report(actual, expected):
    """Retourne une liste de messages décrivant les différences principales."""
    issues = []
    if actual is None:
        issues.append("La fonction a retourné None.")
        return issues
    if not isinstance(actual, str):
        issues.append(f"Type retourné incorrect: {type(actual).__name__} (attendu: str).")
        return issues
    if actual == expected:
        return issues

    # Différence de longueur
    if len(actual) != len(expected):
        issues.append(
            f"Longueur différente: obtenu {len(actual)} caractères, "
            f"attendu {len(expected)}."
        )

    # \n final manquant ?
    if not actual.endswith("\n"):
        issues.append("Il manque le saut de ligne final ('\\n').")

    # Nombre de lignes
    a_lines = actual.split("\n")
    e_lines = expected.split("\n")
    if len(a_lines) != len(e_lines):
        issues.append(
            f"Nombre de lignes différent: obtenu {len(a_lines)}, "
            f"attendu {len(e_lines)}."
        )

    # Première ligne qui diverge
    for i, (a, e) in enumerate(zip(a_lines, e_lines)):
        if a != e:
            issues.append(
                f"Ligne {i + 1} différente:\n"
                f"    obtenu : {repr(a)}\n"
                f"    attendu: {repr(e)}"
            )
            break

    return issues


def run_test(n, expected):
    print(f"{BOLD}{CYAN}── Test n = {n} {'─' * 40}{RESET}")
    try:
        actual = pyramid(n)
    except Exception as exc:
        print(f"{RED}EXCEPTION: {type(exc).__name__}: {exc}{RESET}\n")
        return False

    ok = (actual == expected)

    print(f"{BOLD}Attendu:{RESET}")
    print(visible(expected))
    print(f"{BOLD}Obtenu:{RESET}")
    print(visible(actual))

    if ok:
        print(f"{GREEN}{BOLD}✓ OK{RESET}\n")
    else:
        print(f"{RED}{BOLD}✗ ÉCHEC{RESET}")
        for issue in diff_report(actual, expected):
            print(f"  {YELLOW}• {issue}{RESET}")
        print()
    return ok


def main():
    print(f"\n{BOLD}Légende:{RESET} {GRAY}·{RESET} = espace, "
          f"{GRAY}⏎{RESET} = saut de ligne\n")

    results = []
    for n, expected in EXPECTED.items():
        results.append(run_test(n, expected))

    # Bonus: vérifie aussi des cas limites simples
    print(f"{BOLD}{CYAN}── Cas limites ─────────────────────────────────{RESET}")
    for n in (1, 2):
        try:
            out = pyramid(n)
            print(f"pyramid({n}) =")
            print(visible(out))
        except Exception as exc:
            print(f"{RED}pyramid({n}) a levé {type(exc).__name__}: {exc}{RESET}")
    print()

    total = len(results)
    passed = sum(results)
    color = GREEN if passed == total else RED
    print(f"{BOLD}{color}Résultat: {passed}/{total} tests réussis.{RESET}\n")


if __name__ == "__main__":
    # print(pyramid(4))
    main()
