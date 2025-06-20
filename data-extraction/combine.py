import os
import pandas as pd

# ✏️ عدّل هذا المسار لو مكان مجلد الشغل مختلف عندك
input_root = "racing-data"  # مجلد فيه مجلدات الشهور
output_file = "final_combined_racing_data.csv"  # اسم ملف الدمج النهائي

# قائمة لتجميع كل الداتا
all_data = []

# المرور على كل شهر داخل racing-data
for month_folder in sorted(os.listdir(input_root)):
    month_path = os.path.join(input_root, month_folder)
    if not os.path.isdir(month_path):
        continue

    # المرور على كل يوم داخل الشهر
    for file in sorted(os.listdir(month_path)):
        if file.endswith(".csv") and not file.endswith("_error.csv"):
            file_path = os.path.join(month_path, file)
            try:
                df = pd.read_csv(file_path)
                all_data.append(df)
                print(f"✅ Loaded: {file_path}")
            except Exception as e:
                print(f"❌ Error loading {file_path}: {e}")

# دمج كل البيانات
if all_data:
    combined_df = pd.concat(all_data, ignore_index=True)
    combined_df.to_csv(output_file, index=False)
    print(f"\n📁 Saved combined CSV to: {output_file}")
    print(f"📊 Total rows: {len(combined_df)}")
else:
    print("⚠️ No data found to combine.")
