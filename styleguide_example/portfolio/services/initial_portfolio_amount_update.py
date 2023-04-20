from django.db.models import Case, DecimalField, F, Sum, When

from styleguide_example.portfolio.constants import (
    INITIAL_DATE,
    INITIAL_PORTFOLIO_AMOUNT,
)
from styleguide_example.portfolio.models import PortfolioAsset


def initial_portfolio_amount_update():
    portfolio_assets = PortfolioAsset.objects.filter(date=INITIAL_DATE).annotate(
        price=Sum(
            Case(
                When(
                    asset__prices__date=INITIAL_DATE,
                    then=F("asset__prices__value"),
                ),
                default=0,
                output_field=DecimalField(),
            )
        )
    )

    for portfolio_asset in portfolio_assets:
        portfolio_asset.amount = (
            portfolio_asset.weight * INITIAL_PORTFOLIO_AMOUNT / portfolio_asset.price
        )
        portfolio_asset.save()