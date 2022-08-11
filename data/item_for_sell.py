from aiogram import types
from aiogram.types import LabeledPrice

from utils.misc.item import Item

Tesla_S = Item(
    title="Tesla Model S",
    description="Model S is built from the ground up as an electric"
                " vehicle, with a high-strength architecture and " 
                "floor-mounted battery pack for incredible occupant" 
                " protection and low rollover risk.",
    currency="RUB",
    prices=[
        LabeledPrice(
            label="Tesla Model S",
            amount=1_000_000_00
        )
    ],
    start_parameter='create_invoice_tesla_model_s',
    photo_url="https://upload.wikimedia.org/wikipedia/commons/4/4f/Tesla_Model_S_02_2013.jpg"
)

Tesla_X = Item(
    title="Tesla Model X",
    description="Model X is the best SUV to drive, and the best SUV to be driven in. "
                "Clean, powerful yet invisible cabin conditioning. Tri-zone temperature controls,"
                " ventilated front seats and HEPA filtration come standard. Model X offers a "
                "spacious cabin with the world's largest panoramic windshield and seating for up to seven.",
    currency="RUB",
    prices=[
        LabeledPrice(
            label="Tesla Model X",
            amount=1_000_000_00
        ),
        LabeledPrice(
            label="Delivery",
            amount=10_000_00
        ),
        LabeledPrice(
            label="Discount",
            amount=-500_000_00
        ),
        LabeledPrice(
            label="Tax",
            amount=200_000_00
        ),
    ],
    start_parameter='create_invoice_tesla_model_x',
    photo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/"
              "2017_Tesla_Model_X_100D_Front.jpg/1920px-2017_Tesla_Model_X_100D_Front.jpg",
    need_shipping_address=True,
    is_flexible=True
)

POST_REGULAR_SHIPPING = types.ShippingOption(
    id="post_reg",
    title="Simple_delivery",
    prices=[
        types.LabeledPrice(
            "Simple box", 0
        ),
        types.LabeledPrice(
            "Plastic box", 1000_00
        )
    ]
)

POST_FAST_SHIPPING = types.ShippingOption(
    id="post_fast",
    title="Important_delivery",
    prices=[
        types.LabeledPrice(
            "Strong metal docker", 10_000_00
        ),
        types.LabeledPrice(
            "DHL - (3 days)", 10_000_00
        )
    ]
)

PICKUP_FROM_SHOP = types.ShippingOption(
    id="post_office",
    title="Pickup",
    prices=[
        types.LabeledPrice(
            "Pickup from shop", -1_000_00
        )
    ]
)
