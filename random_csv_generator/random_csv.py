"""Module to generate random CSV files."""

import locale
import random
from typing import Optional
from random_italian_person import RandomItalianPerson
import pandas as pd
import numpy as np
from tqdm.auto import trange


def money_amount(
    minimum_value: int = 0,
    maximum_value: int = 10_000,
    localization: Optional[str] = "it_IT.UTF-8",
    random_state: int = 42,
):
    """Returns a random total and payed debit.

    Parameters
    ----------
    minimum_value: int,
        The minimum value of the total debit, by default 0
    maximum_value: int,
        The maximum value of the total debit, by default 10_000
    localization: str, optional
        The locale to use, by default "it_IT.UTF-8"
    random_state: int,
        The random state to use, by default 42
    """
    if locale is not None:
        locale.setlocale(locale.LC_ALL, localization)
    state = random.Random(random_state)
    total = state.randrange(minimum_value, maximum_value)
    if total > 0:
        payed = state.randrange(0, total)
    else:
        payed = 0
    return {
        "total_debit": locale.currency(total, grouping=True),
        "payed_debit": locale.currency(payed, grouping=True),
    }


def random_csv(
    number_of_rows: int = 500,
    minimum_money_amount: int = 0,
    maximum_money_amount: int = 10_000,
    localization: Optional[str] = "it_IT.UTF-8",
    verbose: bool = False,
    random_state: int = 42,
) -> pd.DataFrame:
    """Return random well-formed CSV.

    Parameters
    ----------
    number_of_rows: int
        The number of rows to generate, by default 500
    minimum_money_amount: int
        The minimum value of the total debit, by default 0
    maximum_money_amount: int
        The maximum value of the total debit, by default 10_000
    localization: str, optional
        The locale to use, by default "it_IT.UTF-8"
    verbose: bool
        Whether to show the progress bar, by default False
    random_state: int
        The random state to use, by default 42
    """
    # We set the random state for numpy, pandas, and random
    random.seed(random_state)
    np.random.seed(random_state)

    return pd.DataFrame(
        [
            {
                **RandomItalianPerson().data,
                **money_amount(
                    minimum_money_amount,
                    maximum_money_amount,
                    localization,
                    random_state,
                ),
            }
            for _ in trange(
                number_of_rows,
                desc="Generating random CSV",
                disable=not verbose or number_of_rows <= 1,
                leave=False,
                dynamic_ncols=True,
            )
        ]
    )
