target_companies = ["MSFT", "ADP", "ATOS",
                    "TSLA", "AAPL",
                    "AIR", "OR"]
#"PARRO", "UBI", "LVMH",
simulation_time = 40
timelapse = 0.1
simulation_date = "2020-01-01"


selected_strategy = "naive"

# "classic"

# strategy_naive : valeurs des bornes supérieur et inférieur
# pour une variation moyenne des gains supérieurs à upper, on achète, pour une
# variation moyenne des gains inférieurs à lower on vends
lower = -2
upper = 2
moving_window = 30
