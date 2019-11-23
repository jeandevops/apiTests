from ldap3 import Server, Connection
server = Server("ldap://localhost:389")
con = Connection(server, "cn=admin,dc=dexter,dc=com", "4linux")

print(con.bind())