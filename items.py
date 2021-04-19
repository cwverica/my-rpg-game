class item(object):

    def __init__(self, hl_pts, atkpts, qnty, itm_type='d'):
        self.type = itm_type
        self.hl_pts = hl_pts
        self.qnty = qnty
        self.atkpts = atkpts


class weapon(item):

    def __init__(self):
        super().__init__(hl_pts=0, atkpts=3, qnty=-1, itm_type='w')




class disposable(item):
    
    def __init__(self, target):
        super().__init__(hl_pts=5, atkpts=0, qnty=1, itm_type='d')


    def heal_item(self, hl_pts, target):
        # take player, return type, and points regained

        pass
    
    def attack_item(self, atkpts, target):
        # target enemy, return type, and damage inflicted
        pass



import sqlite3

db = sqlite3.connect("items.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS items (name TEXT PRIMARY KEY NOT NULL, "
           "healpts INTEGER, atkpts INTEGER, qnty INTEGER, itm_type TEXT)")
# db.execute("CREATE TABLE IF NOT EXISTS itm_desc (name TEXT PRIMARY KEY NOT NULL, desc TEXT")


def get_qnty(name):
    cur_cursor = db.execute("SELECT qnty FROM items WHERE (name = ?)", (name,))
    cur_qnty = cur_cursor.fetchone()
    cur_qnty = cur_qnty[0]
    cur_cursor.close()
    return cur_qnty


def set_qnty(name, qnty):
    cur_cursor = db.execute("SELECT qnty FROM items WHERE (name = ?)", (name,))
    cur_cursor.execute("UPDATE items SET qnty = ? WHERE name = ?", (qnty, name))
    cur_cursor.close()

def get_atkpts(name):
    cur_cursor = db.execute("SELECT atkpts FROM items WHERE (name = ?)", (name,))
    atkpts = cur_cursor.fetchone()
    atkpts = atkpts[0]
    cur_cursor.close()
    return atkpts

def get_healpts(name):
    cur_cursor = db.execute("SELECT healpts FROM items WHERE (name = ?)", (name,))
    healpts = cur_cursor.fetchone()
    healpts = healpts[0]
    cur_cursor.close()
    return healpts


def get_itm_type(name):
    cur_cursor = db.execute("SELECT itm_type FROM items WHERE (name = ?)", (name,))
    itm_type = cur_cursor.fetchone()
    itm_type = itm_type[0]
    cur_cursor.close()
    return itm_type


def first_get(name, healpts=0, atkpts=0, qnty=1, itm_type='d'):
    db.execute("INSERT INTO items VALUES (?, ?, ?, ?, ?)", (name, healpts, atkpts, qnty, itm_type))


def last_use(itm_nm):
    db.execute("DELETE FROM items WHERE name = ?", (itm_nm,))
    print("You have used the last of your {}.".format(itm_nm))

def display_items():
    cursor = db.execute("SELECT * FROM items")
    row = cursor.fetchall()
    print(row)
    cursor.close()
    db.commit()

