import duckdb

# Connect to your dbt-created DuckDB file
con = duckdb.connect(r"C:\Users\megha\Documents\ResearchWork\DBTProjects\DWUseCase\dw_project\dw_project.duckdb")

# List all tables/models
print(con.execute("SHOW TABLES").fetchdf())

# View contents of one
df = con.execute("SELECT * FROM reporting LIMIT 10").fetchdf()
print(df)
