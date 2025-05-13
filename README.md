*🎮 2048 AI Solver*
This project implements and compares three AI algorithms—Expectimax, Greedy Search, and Monte Carlo Simulation—to play the game 2048. The goal is to evaluate how well each approach can perform under the same conditions.

🧠 Algorithms Implemented
1. Expectimax
A probabilistic decision tree algorithm that assumes the worst case on random tile generation. It models:

Max nodes (player moves)

Chance nodes (tile spawns: 2 or 4)

✅ Strength: Strong performance in deeper searches
❌ Weakness: Slower due to computational overhead

2. Greedy Search
Chooses the move that gives the highest immediate score without simulating further outcomes.

✅ Strength: Very fast
❌ Weakness: Shortsighted, often gets stuck

3. Monte Carlo Simulation
Simulates a large number of random games for each possible move and selects the move with the best average outcome.

✅ Strength: Simple and flexible
❌ Weakness: Requires many simulations for accuracy

