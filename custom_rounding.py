def round_half_up_via_decimal(n, decimals):
    """
    See github issues 55 and 56 for context.
    """
    import decimal

    old_context = decimal.getcontext()

    decimal.setcontext(decimal.Context(rounding=decimal.ROUND_HALF_UP))

    first_quantize = "0." + "".join(["0"] * (decimals + 1))
    second_quantize = "0." + "".join(["0"] * (decimals))

    result = (
        decimal.Decimal(n)
        .quantize(decimal.Decimal(first_quantize))
        .quantize(decimal.Decimal(second_quantize))
    )

    decimal.setcontext(old_context)

    return result
