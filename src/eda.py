import pandas as pd  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
from matplotlib import pyplot as plt # type: ignore

import seaborn as sns  # type: ignore
import os 


def basic_match_analysis(matches):

    print("\n" + "=" * 60)
    print("BASIC MATCH ANALYSIS")
    print("=" * 60)

    total_matches = matches["match_id"].nunique()
    print(f"\nTotal Matches : {total_matches}")

    total_seasons = matches["season"].nunique()
    print(f"Total Seasons : {total_seasons}")

    total_teams = len(set(matches["team1"]).union(set(matches["team2"])))
    print(f"Total Teams : {total_teams}")

    total_cities = matches["city"].nunique()
    print(f"Total Cities : {total_cities}")

    total_venues = matches["venue"].nunique()
    print(f"Total Venues : {total_venues}")


def team_wins_analysis(matches):

    print("\n" + "=" * 60)
    print("TEAM WINS ANALYSIS")
    print("=" * 60)

    team_wins = matches["winner"].value_counts()
    team_wins = team_wins.drop("No Result", errors="ignore")

    print(team_wins)

    plt.figure(figsize=(12, 7))

    sns.barplot(
        x=team_wins.values,
        y=team_wins.index
    )

    for index, value in enumerate(team_wins.values):
        plt.text(value + 1, index, str(value), va="center")

    plt.title("IPL Team Wins (2008-2026)")
    plt.xlabel("Wins")
    plt.ylabel("Teams")

    plt.grid(axis="x", linestyle="--", alpha=0.3)

    plt.tight_layout()

    os.makedirs("output/charts", exist_ok=True)

    plt.savefig("output/charts/team_wins.png", dpi=300)

    plt.show(block=False)
    plt.pause(2)
    plt.close()


def win_percentage_analysis(matches):

    print("\n" + "=" * 60)
    print("TEAM WIN PERCENTAGE")
    print("=" * 60)

    team_wins = matches["winner"].value_counts()
    team_wins = team_wins.drop("No Result", errors="ignore")

    total_matches = team_wins.sum()

    win_percentage = ((team_wins / total_matches) * 100).round(2)

    result = pd.DataFrame({
        "Team": team_wins.index,
        "Wins": team_wins.values,
        "Win Percentage": win_percentage.values
    })

    print(result)

    plt.figure(figsize=(12, 7))

    sns.barplot(
        data=result,
        x="Win Percentage",
        y="Team"
    )

    for index, value in enumerate(result["Win Percentage"]):
        plt.text(value + 0.2, index, f"{value}%", va="center")

    plt.title("IPL Team Winning Percentage (2008-2026)")
    plt.xlabel("Winning Percentage")
    plt.ylabel("Teams")

    plt.grid(axis="x", linestyle="--", alpha=0.3)

    plt.tight_layout()

    plt.savefig("output/charts/team_win_percentage.png", dpi=300)

    plt.show(block=False)
    plt.pause(2)
    plt.close()


def toss_winner_analysis(matches):

    print("\n" + "=" * 60)
    print("TOSS WINNER ANALYSIS")
    print("=" * 60)

    toss = matches["toss_winner"].value_counts()

    print(toss)

    plt.figure(figsize=(12, 7))

    sns.barplot(
        x=toss.values,
        y=toss.index
    )

    for index, value in enumerate(toss.values):
        plt.text(value + 1, index, str(value), va="center")

    plt.title("Toss Wins By Teams")
    plt.xlabel("Toss Wins")
    plt.ylabel("Teams")

    plt.grid(axis="x", linestyle="--", alpha=0.3)

    plt.tight_layout()

    plt.savefig("output/charts/toss_winner_analysis.png", dpi=300)

    plt.show(block=False)
    plt.pause(2)
    plt.close()


def toss_decision_analysis(matches):

    print("\n" + "=" * 60)
    print("TOSS DECISION ANALYSIS")
    print("=" * 60)

    toss_decision = matches["toss_decision"].value_counts()

    print(toss_decision)

    plt.figure(figsize=(7, 7))

    plt.pie(
        toss_decision.values,
        labels=toss_decision.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Toss Decision Distribution")

    plt.tight_layout()

    plt.savefig("output/charts/toss_decision_analysis.png", dpi=300)

    plt.show(block=False)
    plt.pause(2)
    plt.close()


def city_wise_matches(matches):

    print("\n" + "=" * 60)
    print("CITY WISE MATCHES")
    print("=" * 60)

    city_matches = matches["city"].value_counts().head(10)

    print(city_matches)

    plt.figure(figsize=(12, 7))

    sns.barplot(
        x=city_matches.values,
        y=city_matches.index
    )

    for index, value in enumerate(city_matches.values):
        plt.text(value + 1, index, str(value), va="center")

    plt.title("Top 10 Cities By Number Of IPL Matches")
    plt.xlabel("Matches")
    plt.ylabel("City")

    plt.grid(axis="x", linestyle="--", alpha=0.3)

    plt.tight_layout()

    plt.savefig("output/charts/city_wise_matches.png", dpi=300)

    plt.show(block=False)
    plt.pause(2)
    plt.close()


def venue_wise_matches(matches):

    print("\n" + "=" * 60)
    print("VENUE WISE MATCHES")
    print("=" * 60)

    venue_matches = matches["venue"].value_counts().head(10)

    print(venue_matches)

    plt.figure(figsize=(12, 7))

    sns.barplot(
        x=venue_matches.values,
        y=venue_matches.index
    )

    for index, value in enumerate(venue_matches.values):
        plt.text(value + 1, index, str(value), va="center")

    plt.title("Top 10 IPL Venues")
    plt.xlabel("Matches")
    plt.ylabel("Venue")

    plt.grid(axis="x", linestyle="--", alpha=0.3)

    plt.tight_layout()

    plt.savefig("output/charts/venue_wise_matches.png", dpi=300)

    plt.show(block=False)
    plt.pause(2)
    plt.close()


def top_run_scorers(ball):

    print("\n" + "=" * 60)
    print("TOP 10 RUN SCORERS")
    print("=" * 60)

    top_batters = (
        ball.groupby("batter")["batter_runs"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print(top_batters)

    plt.figure(figsize=(12, 7))

    sns.barplot(
        x=top_batters.values,
        y=top_batters.index
    )

    for index, value in enumerate(top_batters.values):
        plt.text(value + 20, index, str(value), va="center")

    plt.title("Top 10 Run Scorers")
    plt.xlabel("Runs")
    plt.ylabel("Batter")

    plt.grid(axis="x", linestyle="--", alpha=0.3)

    plt.tight_layout()

    plt.savefig("output/charts/top_run_scorers.png", dpi=300)

    plt.show(block=False)
    plt.pause(2)
    plt.close()

def top_six_hitters(ball):

    print("\n" + "=" * 60)
    print("TOP 10 SIX HITTERS")
    print("=" * 60)

    sixes = (
        ball[ball["batter_runs"] == 6]
        .groupby("batter")
        .size()
        .sort_values(ascending=False)
        .head(10)
    )

    print(sixes)

    plt.figure(figsize=(12, 7))

    sns.barplot(
        x=sixes.values,
        y=sixes.index
    )

    for index, value in enumerate(sixes.values):
        plt.text(value + 1, index, str(value), va="center")

    plt.title("Top 10 Six Hitters")
    plt.xlabel("Sixes")
    plt.ylabel("Batter")

    plt.grid(axis="x", linestyle="--", alpha=0.3)

    plt.tight_layout()

    plt.savefig("output/charts/top_six_hitters.png", dpi=300)

    plt.show(block=False)
    plt.pause(2)
    plt.close()


def top_four_hitters(ball):

    print("\n" + "=" * 60)
    print("TOP 10 FOUR HITTERS")
    print("=" * 60)

    fours = (
        ball[ball["batter_runs"] == 4]
        .groupby("batter")
        .size()
        .sort_values(ascending=False)
        .head(10)
    )

    print(fours)

    plt.figure(figsize=(12, 7))

    sns.barplot(
        x=fours.values,
        y=fours.index
    )

    for index, value in enumerate(fours.values):
        plt.text(value + 1, index, str(value), va="center")

    plt.title("Top 10 Four Hitters")
    plt.xlabel("Fours")
    plt.ylabel("Batter")

    plt.grid(axis="x", linestyle="--", alpha=0.3)

    plt.tight_layout()

    plt.savefig("output/charts/top_four_hitters.png", dpi=300)

    plt.show(block=False)
    plt.pause(2)
    plt.close()


def top_wicket_takers(ball):

    print("\n" + "=" * 60)
    print("TOP 10 WICKET TAKERS")
    print("=" * 60)

    wickets = (
        ball[ball["is_wicket"] == 1]
        .groupby("bowler")
        .size()
        .sort_values(ascending=False)
        .head(10)
    )

    print(wickets)

    plt.figure(figsize=(12, 7))

    sns.barplot(
        x=wickets.values,
        y=wickets.index
    )

    for index, value in enumerate(wickets.values):
        plt.text(value + 1, index, str(value), va="center")

    plt.title("Top 10 Wicket Takers")
    plt.xlabel("Wickets")
    plt.ylabel("Bowler")

    plt.grid(axis="x", linestyle="--", alpha=0.3)

    plt.tight_layout()

    plt.savefig("output/charts/top_wicket_takers.png", dpi=300)

    plt.show(block=False)
    plt.pause(2)
    plt.close()

def orange_cap_analysis(ball):

    print("\n" + "=" * 60)
    print("ORANGE CAP ANALYSIS")
    print("=" * 60)

    orange_cap = (
        ball.groupby("batter")["batter_runs"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print(orange_cap)

    plt.figure(figsize=(12, 7))

    sns.barplot(
        x=orange_cap.values,
        y=orange_cap.index
    )

    for index, value in enumerate(orange_cap.values):
        plt.text(value + 20, index, str(value), va="center")

    plt.title("Orange Cap Contenders")
    plt.xlabel("Runs")
    plt.ylabel("Batter")

    plt.grid(axis="x", linestyle="--", alpha=0.3)

    plt.tight_layout()

    plt.savefig("output/charts/orange_cap.png", dpi=300)

    plt.show(block=False)
    plt.pause(2)
    plt.close()


def purple_cap_analysis(ball):

    print("\n" + "=" * 60)
    print("PURPLE CAP ANALYSIS")
    print("=" * 60)

    purple_cap = (
        ball[ball["is_wicket"] == 1]
        .groupby("bowler")
        .size()
        .sort_values(ascending=False)
        .head(10)
    )

    print(purple_cap)

    plt.figure(figsize=(12, 7))

    sns.barplot(
        x=purple_cap.values,
        y=purple_cap.index
    )

    for index, value in enumerate(purple_cap.values):
        plt.text(value + 1, index, str(value), va="center")

    plt.title("Purple Cap Contenders")
    plt.xlabel("Wickets")
    plt.ylabel("Bowler")

    plt.grid(axis="x", linestyle="--", alpha=0.3)

    plt.tight_layout()

    plt.savefig("output/charts/purple_cap.png", dpi=300)

    plt.show(block=False)
    plt.pause(2)
    plt.close()


def player_of_match_analysis(matches):

    print("\n" + "=" * 60)
    print("PLAYER OF THE MATCH ANALYSIS")
    print("=" * 60)

    player = (
        matches["player_of_match"]
        .value_counts()
        .head(10)
    )

    print(player)

    plt.figure(figsize=(12, 7))

    sns.barplot(
        x=player.values,
        y=player.index
    )

    for index, value in enumerate(player.values):
        plt.text(value + 0.5, index, str(value), va="center")

    plt.title("Top 10 Player of the Match Awards")
    plt.xlabel("Awards")
    plt.ylabel("Player")

    plt.grid(axis="x", linestyle="--", alpha=0.3)

    plt.tight_layout()

    plt.savefig("output/charts/player_of_match.png", dpi=300)

    plt.show(block=False)
    plt.pause(2)
    plt.close()

def highest_team_score_analysis(ball):

    print("\n" + "=" * 60)
    print("HIGHEST TEAM SCORE")
    print("=" * 60)

    highest_score = (
        ball.groupby(["match_id", "batting_team"])["total_runs"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print(highest_score)

    highest_score = highest_score.reset_index()

    plt.figure(figsize=(12, 7))

    sns.barplot(
        data=highest_score,
        x="total_runs",
        y="batting_team"
    )

    for index, value in enumerate(highest_score["total_runs"]):
        plt.text(value + 2, index, str(value), va="center")

    plt.title("Top 10 Highest Team Scores")
    plt.xlabel("Runs")
    plt.ylabel("Team")

    plt.grid(axis="x", linestyle="--", alpha=0.3)

    plt.tight_layout()

    plt.savefig("output/charts/highest_team_score.png", dpi=300)

    plt.show(block=False)
    plt.pause(2)
    plt.close()


def lowest_team_score_analysis(ball):

    print("\n" + "=" * 60)
    print("LOWEST TEAM SCORE")
    print("=" * 60)

    lowest_score = (
        ball.groupby(["match_id", "batting_team"])["total_runs"]
        .sum()
    )

    lowest_score = lowest_score[lowest_score > 0]

    lowest_score = (
        lowest_score
        .sort_values()
        .head(10)
    )

    print(lowest_score)

    lowest_score = lowest_score.reset_index()

    plt.figure(figsize=(12, 7))

    sns.barplot(
        data=lowest_score,
        x="total_runs",
        y="batting_team"
    )

    for index, value in enumerate(lowest_score["total_runs"]):
        plt.text(value + 2, index, str(value), va="center")

    plt.title("Lowest Team Scores")
    plt.xlabel("Runs")
    plt.ylabel("Team")

    plt.grid(axis="x", linestyle="--", alpha=0.3)

    plt.tight_layout()

    plt.savefig("output/charts/lowest_team_score.png", dpi=300)

    plt.show(block=False)
    plt.pause(2)
    plt.close()


def season_runs_analysis(ball):

    print("\n" + "=" * 60)
    print("SEASON WISE RUNS")
    print("=" * 60)

    ball = ball.copy()

    ball["season"] = pd.to_numeric(ball["season"], errors="coerce")

    ball = ball.dropna(subset=["season"])

    ball["season"] = ball["season"].astype(int)

    season_runs = (
        ball.groupby("season")["total_runs"]
        .sum()
        .sort_index()
    )

    print(season_runs)

    plt.figure(figsize=(13, 6))

    sns.lineplot(
        x=season_runs.index,
        y=season_runs.values,
        marker="o"
    )

    plt.title("Season Wise Total Runs")
    plt.xlabel("Season")
    plt.ylabel("Runs")

    plt.grid(alpha=0.3)

    plt.tight_layout()

    plt.savefig("output/charts/season_runs.png", dpi=300)

    plt.show(block=False)
    plt.pause(2)
    plt.close()


def season_wickets_analysis(ball):

    print("\n" + "=" * 60)
    print("SEASON WISE WICKETS")
    print("=" * 60)

    ball = ball.copy()

    ball["season"] = pd.to_numeric(ball["season"], errors="coerce")

    ball = ball.dropna(subset=["season"])

    ball["season"] = ball["season"].astype(int)

    wickets = (
        ball.groupby("season")["is_wicket"]
        .sum()
        .sort_index()
    )

    print(wickets)

    plt.figure(figsize=(13, 6))

    sns.lineplot(
        x=wickets.index,
        y=wickets.values,
        marker="o"
    )

    plt.title("Season Wise Wickets")
    plt.xlabel("Season")
    plt.ylabel("Wickets")

    plt.grid(alpha=0.3)

    plt.tight_layout()

    plt.savefig("output/charts/season_wickets.png", dpi=300)

    plt.show(block=False)
    plt.pause(2)
    plt.close()

def venue_average_score_analysis(ball):

    print("\n" + "=" * 60)
    print("VENUE AVERAGE SCORE")
    print("=" * 60)

    venue = (
        ball.groupby("venue")["total_runs"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    print(venue)

    plt.figure(figsize=(12, 7))

    sns.barplot(
        x=venue.values,
        y=venue.index
    )

    for index, value in enumerate(venue.values):
        plt.text(value + 0.02, index, f"{value:.2f}", va="center")

    plt.title("Top 10 Highest Scoring Venues")
    plt.xlabel("Average Runs Per Ball")
    plt.ylabel("Venue")

    plt.grid(axis="x", linestyle="--", alpha=0.3)

    plt.tight_layout()

    plt.savefig("output/charts/venue_average_score.png", dpi=300)

    plt.show(block=False)
    plt.pause(2)
    plt.close()


def head_to_head_analysis(matches):

    print("\n" + "=" * 60)
    print("HEAD TO HEAD ANALYSIS")
    print("=" * 60)

    head_to_head = (
        matches.groupby(["team1", "team2"])
        .size()
        .reset_index(name="Matches")
        .sort_values("Matches", ascending=False)
        .head(10)
    )

    print(head_to_head)

    plt.figure(figsize=(12, 7))

    sns.barplot(
        data=head_to_head,
        x="Matches",
        y="team1"
    )

    for index, value in enumerate(head_to_head["Matches"]):
        plt.text(value + 0.5, index, str(value), va="center")

    plt.title("Top Head-to-Head Matchups")
    plt.xlabel("Matches")
    plt.ylabel("Team")

    plt.grid(axis="x", linestyle="--", alpha=0.3)

    plt.tight_layout()

    plt.savefig("output/charts/head_to_head.png", dpi=300)

    plt.show(block=False)
    plt.pause(2)
    plt.close()


def powerplay_analysis(ball):

    print("\n" + "=" * 60)
    print("POWERPLAY ANALYSIS")
    print("=" * 60)

    powerplay = (
        ball[ball["phase"] == "Powerplay"]
        .groupby("batting_team")["total_runs"]
        .sum()
        .sort_values(ascending=False)
    )

    print(powerplay)

    plt.figure(figsize=(12, 7))

    sns.barplot(
        x=powerplay.values,
        y=powerplay.index
    )

    for index, value in enumerate(powerplay.values):
        plt.text(value + 20, index, str(value), va="center")

    plt.title("Powerplay Runs")
    plt.xlabel("Runs")
    plt.ylabel("Team")

    plt.grid(axis="x", linestyle="--", alpha=0.3)

    plt.tight_layout()

    plt.savefig("output/charts/powerplay.png", dpi=300)

    plt.show(block=False)
    plt.pause(2)
    plt.close()

def middle_overs_analysis(ball):

    print("\n" + "=" * 60)
    print("MIDDLE OVERS ANALYSIS")
    print("=" * 60)

    middle = (
        ball[ball["phase"] == "Middle Overs"]
        .groupby("batting_team")["total_runs"]
        .sum()
        .sort_values(ascending=False)
    )

    if middle.empty:
        print("No Middle Overs data found.")
        return

    print(middle)

    plt.figure(figsize=(12, 7))

    sns.barplot(
        x=middle.values,
        y=middle.index
    )

    for index, value in enumerate(middle.values):
        plt.text(value + 20, index, str(value), va="center")

    plt.title("Middle Overs Runs")
    plt.xlabel("Runs")
    plt.ylabel("Team")

    plt.grid(axis="x", linestyle="--", alpha=0.3)

    plt.tight_layout()

    plt.savefig("output/charts/middle_overs.png", dpi=300)

    plt.show(block=False)
    plt.pause(2)
    plt.close()

def death_overs_analysis(ball):

    print("\n" + "=" * 60)
    print("DEATH OVERS ANALYSIS")
    print("=" * 60)

    death = (
        ball[ball["phase"] == "Death Overs"]
        .groupby("batting_team")["total_runs"]
        .sum()
        .sort_values(ascending=False)
    )

    if death.empty:
        print("No Death Overs data found.")
        return

    print(death)

    plt.figure(figsize=(12, 7))

    sns.barplot(
        x=death.values,
        y=death.index
    )

    for index, value in enumerate(death.values):
        plt.text(value + 20, index, str(value), va="center")

    plt.title("Death Overs Runs")
    plt.xlabel("Runs")
    plt.ylabel("Team")

    plt.grid(axis="x", linestyle="--", alpha=0.3)

    plt.tight_layout()

    plt.savefig("output/charts/death_overs.png", dpi=300)

    plt.show(block=False)
    plt.pause(2)
    plt.close()


def chasing_vs_defending_analysis(matches):

    print("\n" + "=" * 60)
    print("CHASING VS DEFENDING")
    print("=" * 60)

    chase = matches["toss_decision"].value_counts()

    print(chase)

    plt.figure(figsize=(7, 7))

    plt.pie(
        chase.values,
        labels=chase.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Bat First vs Field First")

    plt.tight_layout()

    plt.savefig("output/charts/chasing_vs_defending.png", dpi=300)

    plt.show(block=False)
    plt.pause(2)
    plt.close()


def economy_analysis(ball):

    print("\n" + "=" * 60)
    print("TOP 10 BEST ECONOMY")
    print("=" * 60)

    economy = (
        ball.groupby("bowler")
        .agg(
            Runs=("total_runs", "sum"),
            Balls=("legal_ball", "sum")
        )
    )

    economy = economy[economy["Balls"] >= 120]

    economy["Overs"] = economy["Balls"] / 6

    economy["Economy"] = (
        economy["Runs"] / economy["Overs"]
    ).round(2)

    economy = economy.sort_values("Economy").head(10)

    print(economy)

    plt.figure(figsize=(12, 7))

    sns.barplot(
        x=economy["Economy"],
        y=economy.index
    )

    for index, value in enumerate(economy["Economy"]):
        plt.text(value + 0.05, index, str(value), va="center")

    plt.title("Top 10 Best Economy Bowlers")
    plt.xlabel("Economy")
    plt.ylabel("Bowler")

    plt.grid(axis="x", linestyle="--", alpha=0.3)

    plt.tight_layout()

    plt.savefig("output/charts/economy.png", dpi=300)

    plt.show(block=False)
    plt.pause(2)
    plt.close()


def dot_ball_analysis(ball):

    print("\n" + "=" * 60)
    print("DOT BALL ANALYSIS")
    print("=" * 60)

    dot = (
        ball[ball["is_dot_ball"] == 1]
        .groupby("bowler")
        .size()
        .sort_values(ascending=False)
        .head(10)
    )

    print(dot)

    plt.figure(figsize=(12, 7))

    sns.barplot(
        x=dot.values,
        y=dot.index
    )

    for index, value in enumerate(dot.values):
        plt.text(value + 5, index, str(value), va="center")

    plt.title("Most Dot Balls")
    plt.xlabel("Dot Balls")
    plt.ylabel("Bowler")

    plt.grid(axis="x", linestyle="--", alpha=0.3)

    plt.tight_layout()

    plt.savefig("output/charts/dot_balls.png", dpi=300)

    plt.show(block=False)
    plt.pause(2)
    plt.close()


def best_batting_team_analysis(ball):

    print("\n" + "=" * 60)
    print("BEST BATTING TEAM")
    print("=" * 60)

    batting = (
        ball.groupby("batting_team")["total_runs"]
        .sum()
        .sort_values(ascending=False)
    )

    print(batting)

    plt.figure(figsize=(12, 7))

    sns.barplot(
        x=batting.values,
        y=batting.index
    )

    for index, value in enumerate(batting.values):
        plt.text(value + 50, index, str(value), va="center")

    plt.title("Best Batting Teams")
    plt.xlabel("Runs")
    plt.ylabel("Team")

    plt.grid(axis="x", linestyle="--", alpha=0.3)

    plt.tight_layout()

    plt.savefig("output/charts/best_batting_team.png", dpi=300)

    plt.show(block=False)
    plt.pause(2)
    plt.close()


def best_bowling_team_analysis(ball):

    print("\n" + "=" * 60)
    print("BEST BOWLING TEAM")
    print("=" * 60)

    bowling = (
        ball.groupby("bowling_team")["is_wicket"]
        .sum()
        .sort_values(ascending=False)
    )

    print(bowling)

    plt.figure(figsize=(12, 7))

    sns.barplot(
        x=bowling.values,
        y=bowling.index
    )

    for index, value in enumerate(bowling.values):
        plt.text(value + 5, index, str(value), va="center")

    plt.title("Best Bowling Teams")
    plt.xlabel("Wickets")
    plt.ylabel("Team")

    plt.grid(axis="x", linestyle="--", alpha=0.3)

    plt.tight_layout()

    plt.savefig("output/charts/best_bowling_team.png", dpi=300)

    plt.show(block=False)
    plt.pause(2)
    plt.close()

def best_bowling_team_analysis(ball):

    print("\n" + "=" * 60)
    print("BEST BOWLING TEAM")
    print("=" * 60)

    bowling = (
        ball.groupby("bowling_team")["is_wicket"]
        .sum()
        .sort_values(ascending=False)
    )

    print(bowling)

    plt.figure(figsize=(12, 7))

    sns.barplot(
        x=bowling.values,
        y=bowling.index
    )

    for index, value in enumerate(bowling.values):
        plt.text(value + 5, index, str(value), va="center")

    plt.title("Best Bowling Teams")
    plt.xlabel("Wickets")
    plt.ylabel("Team")

    plt.grid(axis="x", linestyle="--", alpha=0.3)

    plt.tight_layout()

    plt.savefig("output/charts/best_bowling_team.png", dpi=300)

    plt.show(block=False)
    plt.pause(2)
    plt.close()
   