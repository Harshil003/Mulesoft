import sqlite3
con =sqlite3.connect("movies.db")


# con.execute('create table Movies(id int primary key,name text not null,actor text not null,actress text not null,director text not null,release_year int)')

name=input("Enter the Movie Name:")
actor=input("Enter the Actor Name:")
actress=input("Enter the Actress Name:")
director=input("Enter the Director Name:")
year=input("Enter the Release_year:")


con.execute("""insert into Movies (name,actor,actress,director,release_year) values(?,?,?,?,?)""",(name,actor,actress,director,year))

con.commit()
print("Data enter successfully...")

data = con.execute("select * from Movies ")
for row in data:
    print("name {}".format(row[0]))
    print("actor {}".format(row[1]))
    print("actress {}".format(row[2]))
    print("director {}".format(row[3]))
    print("year {}".format(row[4]))



