import pandas as pd

def load_data(path):
  return pd.read_csv(path)

def clean_data(df):
  df = df.dropna()
  return df

def transform_data(df):
  df["total"] = df["value1:] + df["value2"]
  return df
def save_data(df, path):
  df.to_csv(path, index=False)

if __name__ == "__main__":
  df = load_data("input.csv")
  df = clean_data(df)
  df = transform_data(df)
  save_data(df, "output.csv")
  print("Pipeline complete.")
