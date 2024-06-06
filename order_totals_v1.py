import pandas as pd

order_flavours = ["a", "b", "c"]
order_cost = ["1", "2", "3"]

final_order_dict = {
    "Flavours": order_flavours,
    "Cost": order_cost
}

order_frame = pd.DataFrame(final_order_dict)


