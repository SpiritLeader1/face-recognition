import pandas as pd

# File paths
used_file = "testtask_face_used_old.xlsx"
not_used_file = "testtask_face_not_used_old.xlsx"
output_file = "testtask_combined_faces_old.xlsx"

# Load the Excel files
used_df = pd.read_excel(used_file)
not_used_df = pd.read_excel(not_used_file)

# Add an "Intact Number" column to the not used DataFrame
not_used_df["Intact Image Answer"] = [(i % 3) + 1 for i in range(len(not_used_df))]

# Combine the two DataFrames
combined_df = pd.concat([used_df, not_used_df], ignore_index=True)

# Save the combined DataFrame to a new Excel file
combined_df.to_excel(output_file, index=False)

