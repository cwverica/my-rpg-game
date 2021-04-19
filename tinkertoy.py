import sqlite3

db = sqlite3.connect("items.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS items (name TEXT PRIMARY KEY NOT NULL, "
           "healpts INTEGER, atkpts INTEGER, qnty INTEGER, itm_type TEXT)")
# db.execute("CREATE TABLE IF NOT EXISTS itm_desc (name TEXT PRIMARY KEY NOT NULL, desc TEXT")


# def set_qnty(name):
#     cur_cursor = db.execute("SELECT qnty FROM items WHERE (name = ?)", (name,))
#     cur_qnty = cur_cursor.fetchone()
#     cur_qnty = cur_qnty[0]
#     if cur_qnty >= 0:
#         cur_qnty += 1
#         cur_cursor.execute("UPDATE items SET qnty = ? WHERE name = ?", (cur_qnty, name))
#         cur_cursor.close()
#
#
# def first_get(name, healpts=0, atkpts=0, qnty=1, itm_type='d'):
#         db.execute("INSERT INTO items VALUES (?, ?, ?, ?, ?)", (name, healpts, atkpts, qnty, itm_type))
#
#
#
# def display_items():
#     cursor = db.execute("SELECT * FROM items")
#     row = cursor.fetchall()
#     print(row)
#     cursor.close()
#     db.commit()
#
#
#
# # get_item('broadsword', atkpts=3, qnty=-1, itm_type='w')
# # get_item('axe', atkpts=4, qnty=-1, itm_type='w')
# # get_item('health vial', healpts=5, qnty=1, itm_type='d')
# # get_item('health vial', healpts=5, qnty=1, itm_type='d')
# # get_item('health vial', healpts=5, qnty=1, itm_type='d')
# # get_item('health vial', healpts=5, qnty=1, itm_type='d')
# display_items()
#
# itemz = db.execute("SELECT * FROM items")
# print(itemz.fetchall())
db.close()


