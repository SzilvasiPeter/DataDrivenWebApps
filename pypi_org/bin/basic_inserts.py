import os
import pypi_org.data.db_session as db_session
from pypi_org.data.package import Package
from pypi_org.data.releases import Release


def main():
    init_db()
    while(True):
        insert_a_package()


def insert_a_package():

    p = Package()
    p.id = input('Package id / name: ').strip().lower()
    p.summary = input('Package summary: ').strip()
    p.author_name = input('Author: ').strip()
    p.license = input('License: ').strip()

    print("Release 1")
    r1 = Release()
    r1.major_ver = int(input("Major version: "))
    r1.minor_ver = int(input("Minor version: "))
    r1.build_ver = int(input("Build version: "))
    r1.size = int(input("Size in bytes: "))
    p.releases.append(r1)

    print("Release 2")
    r2 = Release()
    r2.major_ver = int(input("Major version: "))
    r2.minor_ver = int(input("Minor version: "))
    r2.build_ver = int(input("Build version: "))
    r2.size = int(input("Size in bytes: "))
    p.releases.append(r2)

    import sqlalchemy.orm
    session: sqlalchemy.orm.Session = db_session.factory()

    session.add(p)

    session.commit()

def init_db():
    top_folder = os.path.dirname(__file__)
    rel_file = os.path.join('..', 'db', 'pypi.sqlite')
    db_file = os.path.abspath(os.path.join(top_folder, rel_file))
    db_session.global_init(db_file)


if __name__ == '__main__':
    main()