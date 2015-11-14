from gameoflife import Game

def test_init_10x10():
	game = Game(10, 10)
	assert game.width == 10
	assert game.height == 10

def test_create_world():
	world = Game.create_world(10, 5)
	assert len(world) == 10
	for col in world:
		assert len(col) == 5

def test_set():
	game = Game(10, 5)
	game.set(1, 1, True)
	assert game.get(1, 1) is True

def test_get():
	game = Game(10, 5)
	assert game.get(1, 1) is False

def test_will_die():
	game = Game(10, 5)
	game.set(2, 2, True)
	assert game.check_next_state(2, 2) is False

def test_will_live():
	game = Game()