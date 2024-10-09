import mysql.connector.connection
from settings.connections import varConnection
from settings.settings import varMainLanguage
from languages import pt_br


varSearch = int(input('Digite seu código EAN13: '))

for varHost, varUser, varPassword, varDatabase, varTable, varTableStructure, varFilterColumn in varConnection:
    varAcess = mysql.connector.connect(
        host = varHost,
        user = varUser,
        password = varPassword,
        database = varDatabase
    )
    varSelection = varAcess.cursor()
    varSelection.execute('SELECT {} FROM {}.{} WHERE {} = {}'.format(varTableStructure, varDatabase, varTable, varFilterColumn, varSearch))
    for slt_ID, slt_PRODUCT, slt_PRICE, slt_EAN in varSelection:
        print('\nID: {}\nPRODUTO: {}\nEAN: {}\nPREÇO: {}\n'.format(slt_ID, slt_PRODUCT, slt_PRICE, slt_EAN))
    varAcess.close()

    