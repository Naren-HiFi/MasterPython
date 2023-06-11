                                        # Nesting

capitals_dictionary = {
  "France": "Paris",
  "Germany": "Berlin"
}

# Nesting a list in a dictionary

travel_log_dictionary = {
    "France": ["Paris","Lille","Dijon"],
    "Germany": ["Berlin","Hamburg","Stuttgart"],
}

# Nesting a dictionary in a dictionary

travel_vlog_dictionary = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"],"total_visits": 12},
    "Germany": {"cities_visited":["Berlin", "Hamburg", "Stuttgart"],"total_visits": 5}
}

# Nesting a dictionary in a list

travel_vlog_list = [
    {"country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visits": 12
     },
    {"country": "Germany",
     "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
     "total_visits": 5
     }
]

#