# Tunisian Card Game Simulator User Manual

Conduct a Monte Carlo simulation in Python to assess six Tunisian card games, determining winning probabilities and expected earnings. Results presented in a concise table.

>## Running the Simulator
1. Download the simulator script "CardGame.py"
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the command: python CardGame.py

>## Configuration Options
* Number of Plays: The simulator defaults to 100,000 plays per game. You can change this in the main call for the monte_carlo function.
    <br>exemple : monte_carlo(100)

* Seed: The seed is set to 619. If you wish to change it, modify the seed value in the script.
>## Understanding Results
Results are displayed in a table with the following columns:

* Game: Name of the card game.
* Probability of Winning: Estimated probability of winning based on simulations.
* Expected Winnings per Play: Average winnings per play in Tunisian dinars.
* Total Money Earned : Total Money won for each game .

>## Results 

| Game              | Probability of Winning  | Expected Winnings per Play    | Total Money Earned              |
| ----------------- | ----------------------- | ----------------------------- | ------------------------------- |
| Sahara Ace        | 7.5%                   | 0.75  Tunisian dinars         | 75280 Tunisian dinars        |
| Tunisian Twins    | 30.9%                   | 15.47  Tunisian dinars         | 1546900 Tunisian dinars        |
| Medina Biggie     | 46.2%                   | 0.92  Tunisian dinars         | 92310 Tunisian dinars        |
| Desert Hearts     | 57.9%                   | 0.75  Tunisian dinars         | 74980 Tunisian dinars        |
| Oasis Runny       | 25.8%                   | 1.29  Tunisian dinars         | 129070 Tunisian dinars        |
| El Haia Card      | 0.3%                   | 0.27  Tunisian dinars         | 27200 Tunisian dinars        |

>* Observation:
1. The most winnable game is "Desert Hearts"
2. The least winnable game is "El Haia Card"

>* New Game Description :

<u>El Haia Card:</u> The player draws three cards. If there is the card of 7 Diamond, and the sum of all three cards equals to 10. Otherwise, the player loses.

>## Troubleshooting
* I couldn't find the difference between the single deck card game and the infinite deck card dealer. 
