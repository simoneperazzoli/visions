from collections import Counter

import pandas as pd

from tangled_up_in_unicode import script, block, category_alias, block_alias, category


def text_summary(series: pd.Series) -> dict:
    """

    Args:
        series:

    Returns:

    """
    # Distribution of length
    summary = {"length": series.map(lambda x: len(str(x))).value_counts().to_dict()}

    # Unicode Character Summaries (category and script name)
    character_counts = dict(Counter(series.str.cat()))

    summary["category_short_values"] = {
        key: category(key) for key in character_counts.keys()
    }
    summary["category_alias_values"] = {
        key: category_alias(key) for key in character_counts.keys()
    }
    summary["script_values"] = {key: script(key) for key in character_counts.keys()}
    summary["block_values"] = {key: block(key) for key in character_counts.keys()}
    summary["block_alias_values"] = {
        key: block_alias(key) for key in character_counts.keys()
    }

    return summary
