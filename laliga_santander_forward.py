import pandas as pd


def save_santander_forward(csv_file, output_file):
    pd.set_option('display.width', 10)
    pd.set_option('display.max_columns', 100)
   # pd.set_option('display.max_rows', 200)

    try:
        data = pd.read_csv(csv_file, header=0,
                           usecols=['competition', 'name', 'team', 'position', 'weight', 'height', 'country',
                                    'position', 'aerial_duels', 'aerial_duels_lost', 'aerial_duels_won',
                                    'appearances', 'assists_intentional', 'attempts_from_set_pieces',
                                    'away_goals', 'backward_passes', 'blocked_shots', 'blocks', 'catches',
                                    'forward_passes', 'foul_attempted_tackle', 'foul_won_penalty', 'games_played',
                                    'goal_assists', 'goalkeeper_smother', 'goals', 'goals_from_inside_box',
                                    'goals_from_outside_box', 'headed_goals', 'hit_woodwork', 'home_goals',
                                    'index', 'interceptions', 'key_passes_attempt_assists', 'left_foot_goals',
                                    'leftside_passes', 'offsides', 'open_play_passes', 'other_goals', 'own_goal_scored',
                                    'penalties_off_target', 'penalties_taken', 'penalty_goals',
                                    'penalty_goals_conceded',
                                    'recoveries', 'red_cards_2nd_yellow', 'right_foot_goals', 'rightside_passes',
                                    'second_goal_assists', 'set_pieces_goals', 'shots_off_target_inc_woodwork',
                                    'shots_on_target_inc_goals', 'starts', 'straight_red_cards', 'substitute_off',
                                    'substitute_on', 'team_games_played', 'through_balls',
                                    'throw_ins_to_opposition_player',
                                    'throw_ins_to_own_player', 'time_played', 'times_tackled', 'total_clearances',
                                    'total_fouls_conceded', 'total_fouls_won', 'total_losses_of_possession',
                                    'total_passes', 'total_red_cards', 'total_shots',
                                    'total_successful_passes_excl_crosses_corners', 'total_tackles',
                                    'total_touches_in_opposition_box', 'winning_goal', 'yellow_cards'])
        if data.empty:
            print("ERROR: CSV file is empty.")
        else:
            # Print only the rows where the position is "Forward"
            forwards = data[data['position'] == 'Forward']
            # Write filtered data to a new csv file
            forwards.to_csv(output_file, index=False)
            print(f"Filtered data saved to '{output_file}' successfully.")

    except FileNotFoundError:
        print(f"ERROR: CSV file '{csv_file}' not found.")
    except pd.errors.EmptyDataError:
        print(f"ERROR: CSV file '{csv_file}' is empty.")
    except pd.errors.ParserError:
        print(f"ERROR: Unable to parse CSV file '{csv_file}'.")
