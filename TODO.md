# Bugs
- Fix duplicate edge creation in graph wrapper constructor, it should be as simple as checking if an edge already exists before adding it
- Need a way to prevent infinite games in demo game, maybe a sudden death mode?
- Check win doesn't always work right
- Need to handle no movable vertices left during turn case
# Features
- Could use some automated testing code, maybe a random move making bot?
# Ideas
- More graph wrapper functionality would not hurt, functions like IsAdjacent(vertex1,vertex2) and ConnectedEdges(vertex) for example
- Need more ideas for other games
- Need a way to organize code better per game
- How do we want to separate out game specific code and generic engine code?
- Do we want to use dot or the built in plotting functionality for display?
	- If we use dot we will probably need to process the dot files we generate, sed grep bash and etc could probably make this process pretty easy.
- Should probably come up with and implement a consistent style
