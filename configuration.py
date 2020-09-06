target_companies = ["MSFT", "ADP", "ATOS",
                    "TSLA", "AAPL",
                    "AIR", "OR"]
#"PARRO", "UBI", "LVMH",
simulation_time = 30
timelapse = 0.1
simulation_date = "2020-01-01"  # year - month - day


selected_strategy = "classic"  # "naive"

# "classic"

# strategy_naive : valeurs des bornes supérieur et inférieur
# pour une variation moyenne des gains supérieurs à upper, on achète, pour une
# variation moyenne des gains inférieurs à lower on vends
lower = -2
upper = 2
moving_window = 30
