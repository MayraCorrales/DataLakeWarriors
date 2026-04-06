from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
INPUT_FILE = BASE_DIR / "data" / "raw" / "eurostat" / "eurostat_raw.csv"
RAW_DIR = BASE_DIR / "data" / "raw" / "eurostat"
RAW_DIR.mkdir(parents=True, exist_ok=True)


def main() -> None:
    print(f"Reading Eurostat file from: {INPUT_FILE}")

    df = pd.read_csv(INPUT_FILE)

    print("\nRaw data preview:")
    print(df.head())
    print(f"\nRows: {len(df)}")
    print(f"Columns: {list(df.columns)}")

    output_file = RAW_DIR / "eurostat_raw_copy.csv"
    df.to_csv(output_file, index=False)

    print(f"\nRaw Eurostat data saved to: {output_file}")


if __name__ == "__main__":
    main()