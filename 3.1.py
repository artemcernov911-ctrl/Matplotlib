input_file = "prices.csv"
output_file = "prices_cleaned.csv"

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

filtered_lines = [line for line in lines if line.strip() != '""']

with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(filtered_lines)

print(f"Готово. Очищенный файл сохранён как {output_file}")