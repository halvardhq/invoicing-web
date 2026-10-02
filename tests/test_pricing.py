from decimal import Decimal

from halvard_invoicing.pricing import total_with_tax


def test_total_with_tax() -> None:
    assert total_with_tax(Decimal("100")) == Decimal("123.00")
