import psycopg2

hostname = 'localhost'
username = 'postgres'
db_name = 'erp'
port_id = 5432
pwd = 'hacker123'

with psycopg2.connect(
    host=hostname,
    user=username,
    database=db_name,
    port=port_id,
    password=pwd
) as conn:
    print("connection successful!")
    with conn.cursor() as cur:
        # Show current data
        cur.execute('SELECT * FROM h;')


        name = 'shai'
        
        # ✅ Insert with ON CONFLICT (DO NOTHING)
        cur.execute(
            'INSERT INTO h(name) VALUES(%s) ON CONFLICT (name) DO NOTHING;',
            (name,)
        )
        conn.commit()

        # Show updated data
        cur.execute('SELECT * FROM h;')
        print(f"after insert: {[row for row in cur]}")