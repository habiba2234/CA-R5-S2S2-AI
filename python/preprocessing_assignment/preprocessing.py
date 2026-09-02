import pandas as pd


def Read_data_file(file_path):
    try:
        df = pd.read_csv(file_path)
        return df

    except FileNotFoundError:
        print("Error: File not found.")

    except Exception as e:
        print(f"Error reading file: {e}")

def Drop_unnecessary_features(df, cols_to_drop):
    df = df.drop(columns=cols_to_drop)
    return df        

def Check_data_type(df):
    report = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.values,
        "Unique Values": df.nunique().values
    })

    return report.set_index("Column").T