from src.data_cleaning import (
    load_data,
    dataset_info,
    clean_data,
    validate_dataset,
    convert_data_types
)

from src.eda import (
    basic_match_analysis,
    team_wins_analysis,
    win_percentage_analysis,
    toss_winner_analysis,
    toss_decision_analysis,
    city_wise_matches,
    venue_wise_matches,
    top_run_scorers,
    top_six_hitters,
    top_four_hitters,
    top_wicket_takers,
    orange_cap_analysis,
    purple_cap_analysis,
    player_of_match_analysis,
    highest_team_score_analysis,
    lowest_team_score_analysis,
    season_runs_analysis,
    season_wickets_analysis,
    venue_average_score_analysis,
    head_to_head_analysis,
    powerplay_analysis,
    middle_overs_analysis,
    death_overs_analysis,
    chasing_vs_defending_analysis,
    economy_analysis,
    dot_ball_analysis,
    best_batting_team_analysis,
    best_bowling_team_analysis
)


def main():

    matches, ball = load_data()

    dataset_info(matches, "IPL Matches")
    dataset_info(ball, "IPL Ball By Ball")

    matches = clean_data(matches, "IPL Matches")
    ball = clean_data(ball, "IPL Ball By Ball")

    matches, ball = convert_data_types(matches, ball)

    validate_dataset(matches, "IPL Matches")
    validate_dataset(ball, "IPL Ball By Ball")

    basic_match_analysis(matches)

    team_wins_analysis(matches)
    win_percentage_analysis(matches)

    toss_winner_analysis(matches)
    toss_decision_analysis(matches)

    city_wise_matches(matches)
    venue_wise_matches(matches)
    venue_average_score_analysis(ball)

    top_run_scorers(ball)
    top_six_hitters(ball)
    top_four_hitters(ball)
    orange_cap_analysis(ball)

    top_wicket_takers(ball)
    purple_cap_analysis(ball)
    economy_analysis(ball)
    dot_ball_analysis(ball)

    player_of_match_analysis(matches)

    highest_team_score_analysis(ball)
    lowest_team_score_analysis(ball)

    season_runs_analysis(ball)
    season_wickets_analysis(ball)

    head_to_head_analysis(matches)
    chasing_vs_defending_analysis(matches)

    powerplay_analysis(ball)
    middle_overs_analysis(ball)
    death_overs_analysis(ball)

    best_batting_team_analysis(ball)
    best_bowling_team_analysis(ball)


if __name__ == "__main__":
    main()