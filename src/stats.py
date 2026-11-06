"""stats.py – Lab 3: functions that compute numbers from your data."""


# Your code from Lab 3 goes below.
def mean(values, digits=2):
    """The mean of a list of numbers, rounded to `digits` decimals.
    Example: mean([1, 2, 4]) -> 2.33  ·  mean([1, 2, 4], digits=0) -> 2.0
    """
    if not values:
        return 0.0
    return round(sum(values) / len(values), digits)


def median(values):
    """The middle value of a list of numbers.
    Example: median([3, 1, 2]) -> 2  ·  median([4, 1, 3, 2]) -> 2.5
    """
    ...  # 🔵 your code
    new_list = sorted(values)
    mid_value = len(new_list) // 2

    if len(new_list) % 2 == 1:
        return new_list[mid_value]
    else:
        return (new_list[mid_value - 1] + new_list[mid_value]) / 2


def count_by(rows, key):
    """How many rows have each value of the column `key`.
    Example: count_by(rows, "type1") -> {"Grass": 2, "Fire": 2, "Water": 2}
    """
    ...  # 🔵 your code
    counts = {}

    for r in rows:
        value = r[key]
        if value not in counts:
            counts[value] = 0
        counts[value] = counts.get(value, 0) + 1
    return counts


def group_stat(rows, group, value, how="mean"):
    """One number per group: the mean / median / count / max of `value` in every group of `group`.
    Example: group_stat(rows, "type1", "attack") -> {"Grass": 55.5, "Fire": 58.0, "Water": 48.0}
    """
    groups = {}

    for r in rows:
        v = r[value]
        if v is None:
            continue

        g = r[group]
        if g not in groups:
            groups[g] = []
        groups[g].append(v)

    def one_number(values):
        if how == "mean":
            return mean(values)
        elif how == "median":
            return median(values)
        elif how == "count":
            return len(values)
        elif how == "max":
            return max(values)
        else:
            raise ValueError(f"Unknown 'how' value: {how}")

    return {g: one_number(v) for g, v in groups.items()}


def top(result, n=5):
    """The n biggest (key, number) pairs of a dictionary, biggest first – a ranking.
    Example: top({"a": 1, "b": 3, "c": 2}, n=2) -> [("b", 3), ("c", 2)]
    """
    sorted_items = sorted(result.items(), key=lambda pair: pair[1], reverse=True)
    return sorted_items[:n]


def summary_by(rows, group, value):
    """A table: for every group the number of values and their mean, the biggest mean first.
    Example: summary_by(rows, "type1", "attack") -> [{"group": "Fire", "count": 2, "mean": 58.0}, ...]
    """
    counts = group_stat(rows, group, value, how="count")
    means = group_stat(rows, group, value, how="mean")
    summary = [{"group": g, "count": counts[g], "mean": means[g]} for g in counts]
    return sorted(summary, key=lambda x: x["mean"], reverse=True)
