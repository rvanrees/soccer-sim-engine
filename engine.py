import random

# Quoteringen
home_odds = 4.90
draw_odds = 4.35
away_odds = 1.71

# Aantal simulaties
num_simulations = 100

def simulate_match(home_odds, draw_odds, away_odds):
    # Bereken de totale som van de omgekeerde odds om waarschijnlijkheden te bepalen
    total = (1 / home_odds) + (1 / draw_odds) + (1 / away_odds)

    # Bereken de waarschijnlijkheid voor elke uitkomst
    home_prob = (1 / home_odds) / total
    draw_prob = (1 / draw_odds) / total
    away_prob = (1 / away_odds) / total

    # Print de waarschijnlijkheden (optioneel, voor debuggen)
    # print(f"Waarschijnlijkheden: Thuiswin = {home_prob:.2f}, Gelijkspel = {draw_prob:.2f}, Uitwin = {away_prob:.2f}")

    # Simuleer de wedstrijd op basis van de waarschijnlijkheden
    outcome = random.choices(['Home', 'Draw', 'Away'], [home_prob, draw_prob, away_prob])[0]

    return outcome

def simulate_multiple_matches(home_odds, draw_odds, away_odds, num_simulations):
    results = {'Home': 0, 'Draw': 0, 'Away': 0}
    
    for _ in range(num_simulations):
        result = simulate_match(home_odds, draw_odds, away_odds)
        results[result] += 1
    
    return results

# Simuleer meerdere wedstrijden
results = simulate_multiple_matches(home_odds, draw_odds, away_odds, num_simulations)
print(f"Resultaten na {num_simulations} simulaties: {results}")