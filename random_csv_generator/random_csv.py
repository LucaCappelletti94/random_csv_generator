from random_italian_person import RandomItalianPerson
import pandas as pd
import locale
import random

locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')


def money_amount():
    total = random.randrange(0, 100000)
    payed = random.randrange(0, total)
    return {
        "total_debit": locale.currency(total, grouping=True),
        "payed_debit": locale.currency(payed, grouping=True)
    }


def random_csv(number: int = 500) -> pd.DataFrame:
    """Return random well-formed CSV."""
    return pd.DataFrame([
        {
            **RandomItalianPerson().data,
            **money_amount()
        }
        for _ in range(number)
    ])
