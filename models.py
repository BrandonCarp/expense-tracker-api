# 0. DATABASE_URL missing → crash at startup with a clear message. No app without the DB.

# 1. Categories are per-user (categories.user_id).
# 2. amount = Decimal, 2 places, 12 digits total.
# 3. expenses.date = DATE only (business date). Every table also gets created_at TIMESTAMPTZ (system time).
# 4. Required: amount, category, date. Optional: description. Rows are editable (U in CRUD)
# 5. v1 = hard delete only. Deleting a user cascades to their expenses and categories (DB-enforced). is_active flag = v2.
# 6. Category is not optional, base category would be Uncategorized. Expenses reassigned to uncategorized
# 7. Category names unique per (user_id, name) — not globally.