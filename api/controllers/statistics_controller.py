from ..app import app
from flask import jsonify

from ..services.statistics import (
    get_top_selling_products,
    get_worst_selling_products,
    get_orders_last_weeks,
)


@app.get("/statistics")
def get_stats():
    return jsonify(
        {
            "top_products": get_top_selling_products(),
            "worst_products": get_worst_selling_products(),
            "orders_last_weeks": get_orders_last_weeks(),
        }
    )
