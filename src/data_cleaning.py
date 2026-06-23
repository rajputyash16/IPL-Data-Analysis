import pandas as pd  # type: ignore

def load_data():
    matches= pd.read_csv("data/ipl_matches_clean.csv")
    ball_by_ball= pd.read_csv("data/ipl_ball_by_ball_clean.csv")

    return matches, ball_by_ball

def dataset_info(df, dataset_name):

    print("\n"+ "="*60)
    print(f"{dataset_name.upper()} DATASET")
    print("="*60)

    print(f"\nShape: {df.shape}")

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values :")
    print(df.isnull().sum())

    print("\nDuplicate Rows :", df.duplicated().sum())

    print("\nFirst 5 Rows :")
    print(df.head())

    print("\nSummary Statistics :")
    print(df.describe(include="all"))

def clean_data(df, dataset_name):

    print("\n" + "=" * 60)
    print(f"CLEANING {dataset_name.upper()} DATASET")
    print("=" * 60)

    duplicate_count = df.duplicated().sum()

    if duplicate_count > 0:
        df.drop_duplicates(inplace=True)
        print(f"Removed {duplicate_count} duplicate rows.")
    else:
        print("No duplicate rows found.")

    print("\nMissing Values:")
    print(df.isnull().sum())

    if dataset_name == "IPL Matches":

        team_name_mapping = {
            "Delhi Daredevils": "Delhi Capitals",
            "Kings XI Punjab": "Punjab Kings",
            "Royal Challengers Bangalore": "Royal Challengers Bengaluru",
            "Rising Pune Supergiants": "Rising Pune Supergiant"
        }

        for column in ["team1", "team2", "toss_winner", "winner"]:
            df[column] = df[column].replace(team_name_mapping)

        print("\nTeam names standardized successfully.")

    return df

def convert_data_types(matches, ball):
    matches["date"] = pd.to_datetime(matches["date"])
    ball["date"] = pd.to_datetime(ball["date"])
    return matches, ball

def validate_dataset(df, dataset_name):
  
    print("\n" + "=" * 60)
    print(f"VALIDATING {dataset_name.upper()} DATASET")
    print("=" * 60)

    print("\nNull Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nData Types:")
    print(df.dtypes)

    print("\nUnique Values:")
    print(df.nunique())