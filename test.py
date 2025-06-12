import os

def count_json_files(folder):
    count = 0
    for root, dirs, files in os.walk(folder):
        count += len([f for f in files if f.endswith('.json')])
    return count

api_confirmed = 'API_confirmed'
sql_confirmed = 'SQL_confirmed'

api_count = count_json_files(api_confirmed)
sql_count = count_json_files(sql_confirmed)

print(f"API_confirmed: {api_count} JSON files")
print(f"SQL_confirmed: {sql_count} JSON files")