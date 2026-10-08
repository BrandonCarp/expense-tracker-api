

#1. Ensure to load the .env file so its contents land in the process environment
#2. Read DATABASE_URL out of the environment - and fail loudly with a clear message if its absent, rather than letting 'None' travel onward
#3. Build a SQLAlchemy engine from that URL
#4. Build a session factory bound to that engine