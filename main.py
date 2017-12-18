# voeg de huidige structuur toe aan path
import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

# importeer de gebruikte structuur
from datastructuur import DataStructuur
from bruteforce import randomize
from hillclimber import hill_climber
from breadthfirst import breadth_first
from genetic import genetic
from score import score

def main():
    A = DataStructuur("voorbeeld.csv")

    # probeer verschillende algoritmes
    # brute force
    B = randomize(A)

    # iteratief
    C = hill_climber(A)

    # constructief
    D = breadth_first(A)

    # evolutionair
    E = genetic(A)

    print("score van random:                {}\n"
          "score van hill_climber:          {}\n"
          "score van breadth_first:         {}\n"
          "score van genetisch algoritme1:  {}\n".format(
        score(B), score(C), score(D), score(E)
    ))

if __name__ == "__main__":
    main()