"""
@auth Dhillyon

Features needed:
    Commands:

    - Get player stats
        - Goals (FWD, MF, DEF) 
        - Assists (FWD, MF, DEF) 
        - Clean sheets (MF, DEF, GK) 
        - Points (ALL),
        - Bonus points (ALL), 
        - Minuites (ALL), 
        - price (ALL)
    - Timespan metrics
        - Last 5 gameweeks
            - Follow stats from Get player stats, but price gain/loss over timeframe instead
            - Transfers in/out?
        - Last gameweek
    - Get team stats
        - Total points (?)
        - Highlight best assets
    - Get FPL team stats
        - Current gameweek
            - Points
            - Highest scorers
            - Option to compare with another team
        - Overall
            - Points/average per week
            - Wildcards used
            - Team value
            - Total transfers
        - Last 5 gameweeks
            - Overall average points vs last 5 gameweek average
            - Total transfers
            - Wildcards played
    
    Other:

    - Price change notifications
    - Injuries, suspensions, fixture changes
    - Live updates
    - Captaincy suggestions

    Longer term:
    
    - Visualisations
        - Team value over season
        - Rank over season


Useful links:
    - https://www.game-change.co.uk/2023/02/10/a-complete-guide-to-the-fantasy-premier-league-fpl-api/
"""

import requests 

API_URL = 'https://fantasy.premierleague.com/api/'