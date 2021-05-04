# Get Started
docker-compose up

# APIs and examples

### Auth
##### POST /auth/register
Request: `{
    "username": "",
    "password": "",
    "password_confirm": ""
}`

##### POST /auth/login/
Request: `{
    "login": "",
    "password": ""
}`

#####
Response Example: `{
    "detail": "Login successful",
    "token": "..."
}`
#####
Make sure to add the following header to make authenticated requets: `{"Authorization": "Token <token>"}`


##### POST /auth/logout/
Request: `{
    "revoke_token": true
}`

### Game
##### GET /game/
Response Example: `
{
    "winner_state": "PLAYER",
    "game_state": "FINISHED",
    "board_state": [...],
    "board_visual": "..."
}`

##### POST /game/start/
Response Example: `
{
    "winner_state": "NONE",
    "game_state": "ONGOING",
    "board_state": [...],
    "board_visual": "..."
}`


##### POST /game/start/
Response Example: `
{
    "winner_state": "NONE",
    "game_state": "NOT_STARTED",
    "board_state": null,
    "board_visual": ""
}`

##### POST /game/move/
Request `{"move_index": 0-8}`
######
 Response 200 Example: `
{
    "winner_state": "NONE",
    "game_state": "ONGOING",
    "board_state": [...],
    "board_visual": "..."
}`
