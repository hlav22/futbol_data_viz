import pandas as pd
import numpy as np


def main():
    csv_file = 'S2122-laliga-santander.csv'
    position = 'Forward'
    # print_santander(csv_file)
    print_santander_by_position(csv_file, position)


def print_santander(csv_file):
    # Reading the CSV file
    try:
        data = pd.read_csv(csv_file, header=0,
                           usecols=['competition', 'name', 'team', 'position', 'weight', 'height', 'country',
                                    'aerial_duels',
                                    'aerial_duels_lost', 'aerial_duels_won', 'appearances', 'assists_intentional',
                                    'attempts_from_set_pieces',
                                    'away_goals', 'backward_passes', 'blocked_shots', 'blocks', 'catches',
                                    'clean_sheets',
                                    'clearances_off_the_line', 'corners_taken_incl_short_corners', 'corners_won',
                                    'crosses_not_claimed', 'drops', 'duels', 'duels_lost', 'duels_won', 'fifty_fifty',
                                    'forward_passes',
                                    'foul_attempted_tackle', 'foul_won_penalty', 'games_played',
                                    'gk_successful_distribution', 'gk_unsuccessful_distribution',
                                    'goal_assists', 'goalkeeper_smother', 'goals', 'goals_conceded',
                                    'goals_conceded_inside_box', 'goals_conceded_outside_box',
                                    'goals_from_inside_box', 'goals_from_outside_box', 'ground_duels',
                                    'ground_duels_lost', 'ground_duels_won',
                                    'handballs_conceded', 'headed_goals', 'headed_goals', 'hit_woodwork', 'home_goals',
                                    'index', 'interceptions',
                                    'key_passes_attempt_assists', 'last_man_tackle', 'left_foot_goals',
                                    'leftside_passes', 'offsides', 'open_play_passes', 'other_goals', 'own_goal_scored',
                                    'penalties_conceded', 'penalties_faced', 'penalties_off_target', 'penalties_saved',
                                    'penalties_taken', 'penalty_goals', 'penalty_goals_conceded', 'punches',
                                    'putthrough_blocked_distribution',
                                    'putthrough_blocked_distribution_won', 'recoveries', 'red_cards_2nd_yellow',
                                    'right_foot_goals',
                                    'rightside_passes', 'saves_from_penalty', 'saves_made', 'saves_made_caught',
                                    'saves_made_from_inside_box', 'saves_made_from_outside_box', 'saves_made_parried',
                                    'second_goal_assists',
                                    'set_pieces_goals', 'shots_off_target_inc_woodwork', 'shots_on_target_inc_goals',
                                    'starts', 'straight_red_cards', 'substitute_off', 'substitute_on',
                                    'successful_corners_into_box',
                                    'successful_crosses_corners', 'successful_crosses_open_play', 'successful_dribbles',
                                    'successful_fifty_fifty', 'successful_launches', 'successful_layoffs',
                                    'successful_long_passes', 'successful_open_play_passes',
                                    'successful_passes_opposition_half',
                                    'successful_passes_own_half', 'successful_short_passes', 'tackles_lost',
                                    'tackles_won',
                                    'team_games_played', 'through_balls', 'throw_ins_to_opposition_player',
                                    'throw_ins_to_own_player', 'time_played', 'times_tackled', 'total_clearances',
                                    'total_fouls_conceded',
                                    'total_fouls_won', 'total_losses_of_possession', 'total_passes', 'total_red_cards',
                                    'total_shots', 'total_successful_passes_excl_crosses_corners', 'total_tackles',
                                    'total_touches_in_opposition_box',
                                    'total_unsuccessful_passes_excl_crosses_corners', 'unsuccessful_corners_into_box',
                                    'unsuccessful_crosses_corners', 'unsuccessful_crosses_open_play',
                                    'unsuccessful_dribbles', 'unsuccessful_launches',
                                    'unsuccessful_layoffs', 'unsuccessful_long_passes',
                                    'unsuccessful_passes_opposition_half', 'unsuccessful_passes_own_half',
                                    'unsuccessful_short_passes', 'winning_goal', 'yellow_cards'])
        if data.empty:
            print("ERROR: CSV file is empty.")
        else:
            print(data)
    except FileNotFoundError:
        print(f"ERROR: CSV file '{csv_file}' not found.")
    except pd.errors.EmptyDataError:
        print(f"ERROR: CSV file '{csv_file}' is empty.")
    except pd.errors.ParserError:
        print(f"ERROR: Unable to parse CSV file '{csv_file}'.")


def print_santander_by_position(csv_file, position):
    pd.set_option('display.width', 5000)
    pd.set_option('display.max_columns', 100)
    pd.set_option('display.max_rows', 200)

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
            # Group the rows by the position column
            position_groups = data.groupby('position')
            # Iterate over each unique position and create a new DataFrame for it
            for pos, group in position_groups:
                if pos == position:
                    print(f"--- {pos} ---")
                    print(group)
    except FileNotFoundError:
        print(f"ERROR: CSV file '{csv_file}' not found.")
    except pd.errors.EmptyDataError:
        print(f"ERROR: CSV file '{csv_file}' is empty.")
    except pd.errors.ParserError:
        print(f"ERROR: Unable to parse CSV file '{csv_file}'.")


if __name__ == '__main__':
    main()
