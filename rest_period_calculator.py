from datetime import datetime, timedelta


def calculate_rest_period(on_call_ends, office_start):
    """
    Calculate the rest period based on on-call end times and office start time.

    :param on_call_ends: List of datetime objects representing on-call end times.
    :param office_start: Datetime object representing the start time of the office.
    :return: Tuple containing a boolean indicating if the rest period is respected and a message.
    """
    if not on_call_ends:
        return False, "No on-call end times provided."

    latest_end = max(on_call_ends)
    is_weekend = any(
        end.weekday() >= 5 for end in on_call_ends
    )  # 5 and 6 are Saturday and Sunday

    required_rest = timedelta(hours=35 if is_weekend else 11)
    actual_rest = office_start - latest_end

    if actual_rest >= required_rest:
        return (
            True,
            f"Required rest period is respected. You can start at {office_start}.",
        )
    else:
        new_start_time = latest_end + required_rest
        return (
            False,
            f"Rest period is not respected. You should start at {new_start_time}.",
        )


# Example usage
if __name__ == "__main__":
    # Example on-call end times and office start time - Rest period is not respected
    on_call_ends = [datetime(2023, 1, 1, 17, 0), datetime(2023, 1, 2, 17, 0)]
    office_start = datetime(2023, 1, 3, 9, 0)

    respected, message = calculate_rest_period(on_call_ends, office_start)
    assert not respected  # nosec - ✅ not respected example
    # https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement
    print(on_call_ends, office_start)
    print(message)

    # Example on-call end times and office start time - Rest period is respected
    on_call_ends = [datetime(2024, 1, 1, 18, 0), datetime(2024, 1, 1, 20, 45)]
    office_start = datetime(2024, 1, 2, 9, 0)

    respected, message = calculate_rest_period(on_call_ends, office_start)
    assert respected  # nosec - ✅ respected example
    print(on_call_ends, office_start)
    print(message)
