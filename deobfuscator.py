import re
from entity_store import get_all_mappings
from config import settings

# Matches [[COP:8.270,03]] or [[USD:28.078,96]]
_COP_TAG = re.compile(r'\[\[COP:([\d.,]+)\]\]')
_USD_TAG = re.compile(r'\[\[USD:([\d.,]+)\]\]')


def _parse_latin(s: str) -> float:
    """Parse a Latin American formatted number (dot=thousands, comma=decimal)."""
    return float(s.replace(".", "").replace(",", "."))


def _format_latin(value: float) -> str:
    """Format a float as a Latin American number (dot=thousands, comma=decimal)."""
    formatted = f"{value:,.2f}"                          # "8,270,030,000.03"
    formatted = formatted.replace(",", "X").replace(".", ",").replace("X", ".")  # "8.270.030.000,03"
    if formatted.endswith(",00"):
        formatted = formatted[:-3]
    return formatted


def _replace_monetary(text: str, pattern: re.Pattern, factor: float) -> str:
    def replacer(match: re.Match) -> str:
        scaled = _parse_latin(match.group(1))
        real = scaled / factor
        return _format_latin(real)
    return pattern.sub(replacer, text)


def deobfuscate(text: str) -> str:
    # Step 1: replace entity pseudonyms with real values
    mappings = get_all_mappings()  # already sorted by pseudonym length DESC
    for pseudonym, original_value in mappings:
        text = text.replace(pseudonym, original_value)

    # Step 2: de-scale tagged monetary values
    text = _replace_monetary(text, _COP_TAG, settings.cop_factor)
    text = _replace_monetary(text, _USD_TAG, settings.usd_factor)

    return text
