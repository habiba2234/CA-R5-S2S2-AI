from preprocessing import Read_data_file, Drop_unnecessary_features, Check_data_type
from Config.Config import COLS_TO_DROP


file_path = "Titanic.csv"

df = Read_data_file(file_path)

if df is not None:
    print("Original Dataset:")
    print(df.head())

    print("\nData Quality Report:")
    print(Check_data_type(df))

    df = Drop_unnecessary_features(df, COLS_TO_DROP)

    print("\nDataset After Removing Unnecessary Features:")
    print(df.head())

    print("\nData Quality Report After Removing Features:")
    print(Check_data_type(df))