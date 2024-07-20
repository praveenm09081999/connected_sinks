# connected_sinks
Complex 2D puzzle for flow between sink and source: Solved in python

#QUESTION:
We have a network of interconnected water paths built on a grid. Special markers help us navigate:

Source (✳️): The starting point, where water originates.
Drains (A, B, C...): Endpoints where water flows out.
Pipes (═, ║, etc.): Channels that connect different parts of the network.
Some pipes have openings on multiple sides, allowing water to flow in different directions.  Imagine elbows, turns, and junctions!

The key question: Which drains can be reached by water flowing from the source?

This challenge involves analyzing a text file that describes the layout of the water channels. The file tells us where sources, drains, and pipes are located on the grid.

Your job is to write a Python function that takes this file path as input. The function should then figure out which drains are connected to the source and return a string listing these drains in alphabetical order (e.g., "ABC" if drains A, B, and C are connected).
