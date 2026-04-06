from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
RAW_FILE = BASE_DIR / "data" / "raw" / "eurostat" / "eurostat_raw.csv"
PROCESSED_DIR = BASE_DIR / "data" / "processed" / "eurostat"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def clean_column_name(col: str) -> str:
    return (
        col.strip()
        .lower()
        .replace(" ", "_")
        .replace("-", "_")
        .replace("/", "_")
        .replace("(", "")
        .replace(")", "")
    )


def main() -> None:
    print(f"Reading raw file from: {RAW_FILE}")
    df = pd.read_csv(RAW_FILE)

    df.columns = [clean_column_name(col) for col in df.columns]
    df = df.dropna(how="all")
    df["source"] = "eurostat"

    output_csv = PROCESSED_DIR / "eurostat_clean.csv"

    df.to_csv(output_csv, index=False)

    print("Processed data preview:")
    print(df.head())
    print(f"Rows: {len(df)}")
    print(f"Columns: {list(df.columns)}")
    print(f"Processed Eurostat data saved to: {output_csv}")


if __name__ == "__main__":
    main()