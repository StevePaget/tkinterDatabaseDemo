from tkinter import *
import tkinter.font as tkFont
import sqlite3 as sql

    
def makeDatabase(db):
    # this function will create the database tables from scratch and
    # add some dummy data. This should only be run once!
    c = db.cursor()
    c.execute("CREATE TABLE tblForms (formname text)")
    c.execute("CREATE TABLE tblPupils (firstname TEXT, surname TEXT, formname TEXT, year INT)")
    c.execute("INSERT INTO tblForms Values ('8JBC')") # simple command adding some data
    c.execute("INSERT INTO tblForms Values ('9SAP')")
    c.execute("INSERT INTO tblForms Values ('10EJL')")
    c.execute("INSERT INTO tblPupils Values (?,?,?,?)", ("Sally","Smith","9SAP", 9))
    c.execute("INSERT INTO tblPupils Values (?,?,?,?)", ("Bob","King","9SAP", 9))
    c.execute("INSERT INTO tblPupils Values (?,?,?,?)", ("Carol","Singer","8JBC", 8))
    db.commit()

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.titlefont = tkFont.Font(family="Arial", size=20, slant="italic")
        self.buttonfont = tkFont.Font(family="Arial", size=18)
        self.title = Label(self, anchor="w", justify="left", text="Welcome to my demo\nI hope you enjoy it.", bg="lightblue")
        self.title.grid(row=0, column=0, sticky="NSEW")
        self.columnconfigure(0,minsize=500)
        # connect to the database
        self.db = sql.connect("demofile.db")
        # run the procedure that generates new tables and records
        # this is just for the demo. You wouldn't make new tables every time
        #makeDatabase(self.db)

        # now print out what you find in there
        self.testDB()

        # this belongs at the end of the __init__ procedure.
        # It starts the main loop which runs the tkinter window
        self.mainloop()

    def testDB(self):
        # this just accesses the database and print out what it finds in the pupils table
        c = self.db.cursor()
        results = c.execute("SELECT * FROM tblPupils")
        for line in results.fetchall():
            print(line)

if __name__ == "__main__":
    app = App()
