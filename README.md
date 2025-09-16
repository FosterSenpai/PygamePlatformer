# Pygame Platformer

A 2D platformer built with Pygame CE for a personal exercise. It currently includes a basic menu, a play screen, animated player sprites, and the foundation for a physics-based movement system (forces, impulses, gravity) designed to scale.

## Features
- Screen system: Main Menu → Play Screen
- Player sprite loading from sprite sheets (idle, walk/run, jump start/transition/fall, attacks, etc.)
- Early physics architecture:
	- `PhysicsBody` (position, velocity, forces, inverse mass, gravity, damping)
	- `PlayerController` (input → forces/impulses)
	- Planned `CollisionSystem` for tile/static colliders
- Simple pause overlay

## Project Structure
```
assets/
	sprites/
		player/               # All player sprite sheets (PNG)
src/
	config.py               # Global config (window size, paths)
	main.py                 # Entry point
	classes/
		game.py               # Game loop & manager integration
		managers/
			game_manager.py
			screen_manager.py
		screens/
			main_menu_screen.py
			play_screen.py
			gui_components/button.py
		creatures/
			player.py
		controllers/
			player_controller.py
		physics/
			physics_body.py
			collision_system.py # TODO
requirements.txt          # Python dependencies for venv
```

## Requirements
- Windows 10/11
- Python 3.11+ (built & tested with Python 3.13)
- Pygame CE

Install dependencies (PowerShell):
```powershell
# From repo root
python -m venv .venv
./.venv/Scripts/Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run
```powershell
# From repo root with venv activated
python .\src\main.py
```

## Controls (current)
All are currently placeholders and tests.
- `ESC` — Toggle Pause
- `A / D` — Face/move left or right
- `SPACE` — Jump Start animation
- `S` — Jump Fall animation
- `Left Shift` — Dash animation
- `V` — Attack 1 animation

## Physics Design (Overview)
- `PhysicsBody` handles motion only:
	- Fields: `position`, `velocity`, `forces`, `mass`, `inverse_mass`, `gravity`, `linear_damping`, `on_ground`
	- Methods: `add_force`, `apply_impulse`, `apply_force`, `clamp_velocity`, setters
	- Uses inverse mass so static/kinematic bodies (moving platforms etc.) are just `inverse_mass = 0.0`
- `PlayerController` converts input → forces/impulses
- `CollisionSystem` (planned) resolves against tiles/platforms, sets `on_ground`, and clamps position/velocity

## Roadmap
- Wire `Player` to `PhysicsBody` + `PlayerController`
- Implement `CollisionSystem` with tile AABB and one-way platforms
- Test level for testing basic movements
- Add coyote time, jump buffer, fast fall, wall slide/jump
- Add first enemy, implement basic attack

### Plans
#### Animation Plan (Jump)
- One-shot `JUMP START` → hold last frame while ascending
- At apex (vertical velocity crosses ~0): `JUMP TRANSITION` (one-shot)
- Descending: One-shot `JUMP FALL` → hold last frame while descending
- On landing: return to `IDLE` or `WALK` based on input
- May need to do in a way where just being in air handles the animation for things like falling off ledges etc (falling but not having jumped)


## Assets & Credits
- Player sprites: © Mattz Art — used under a purchased license.
- These art assets are not covered by the project’s code license. Do not reuse, redistribute, or resell without permission from the creator.
- Creator: Mattz Art — Itch.io: https://itch.io/profile/xzany

## License
- Code: MIT (see `LICENSE`)
- Art: Licensed separately (see “Assets & Credits”)


