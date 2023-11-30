import sqlite3

conexion = sqlite3.connect('DBFirplak') # Conexión con la bd
cursorBD = conexion.cursor() # desplazamiento de bd, realizar acciones que se recrean, como seleccionar, actualizar...

# Tabla Pedido
def tableExit(nameTable):
    cursorBD.execute(''' SELECT COUNT(name) FROM SQLITE_MASTER WHERE TYPE = 'table' AND name = '{nameTable}' '''.format(nameTable))
    if cursorBD.fetchone()[0] == 1:
        return True
    else:
        cursorBD.execute(''' CREATE TABLE Pedido (ID INTEGER PRIMARY KEY AUTOINCREMENT, NumeroPedido VARCHAR, FechaCreacion DATETIME, CanalComercializacion VARCHAR, ClienteFinal VARCHAR) ''')
        return False
# Tabla LineaPedido
def tableExit(nameTable):
    cursorBD.execute(''' SELECT COUNT(name) FROM SQLITE_MASTER WHERE TYPE = 'table' AND name = '{nameTable}' '''.format(nameTable))
    if cursorBD.fetchone()[0] == 1:
        return True
    else:
        cursorBD.execute(''' CREATE TABLE LineaPedido (ID INTEGER PRIMARY KEY AUTOINCREMENT, PedidoID INTEGER FOREING KEY, SKUProducto VARCHAR, Cantidad INTEGER, FechaEntrega DATATIME, TipoProducto VARCHAR, Estado VARCHAR, PrecioUnitario FLOAT, MontoTotal FLOAT) ''')
        return False

# Tabla Bodega
def tableExit(nameTable):
    cursorBD.execute(''' SELECT COUNT(name) FROM SQLITE_MASTER WHERE TYPE = 'table' AND name = '{nameTable}' '''.format(nameTable))
    if cursorBD.fetchone()[0] == 1:
        return True
    else:
        cursorBD.execute(''' CREATE TABLE Bodega (ID INTEGER PRIMARY KEY AUTOINCREMENT, Nombre VARCHAR, Tipo VARCHAR) ''')
        return False
    
# Tabla AsignacionBodega
def tableExit(nameTable):
    cursorBD.execute(''' SELECT COUNT(name) FROM SQLITE_MASTER WHERE TYPE = 'table' AND name = '{nameTable}' '''.format(nameTable))
    if cursorBD.fetchone()[0] == 1:
        return True
    else:
        cursorBD.execute(''' CREATE TABLE AsignacionBodega (ID INTEGER PRIMARY KEY AUTOINCREMENT, LineaPedidoID INTEGER FOREING KEY, BodegaID INTEGER FOREING KEY, FechaAsignacion DATATIME, CantidadAsignada FLOAT) ''')
        return False

# Tabla DocumentoEntrega
def tableExit(nameTable):
    cursorBD.execute(''' SELECT COUNT(name) FROM SQLITE_MASTER WHERE TYPE = 'table' AND name = '{nameTable}' '''.format(nameTable))
    if cursorBD.fetchone()[0] == 1:
        return True
    else:
        cursorBD.execute(''' CREATE TABLE DocumentoEntrega (ID INTEGER PRIMARY KEY AUTOINCREMENT, NumeroDocumento FLOAT, FechaDespacho DATATIME, Estado BOOLEAN, FechaEntrega DATATIME) ''')
        return False
    
# Tabla GuiaTransporte
def tableExit(nameTable):
    cursorBD.execute(''' SELECT COUNT(name) FROM SQLITE_MASTER WHERE TYPE = 'table' AND name = '{nameTable}' '''.format(nameTable))
    if cursorBD.fetchone()[0] == 1:
        return True
    else:
        cursorBD.execute(''' CREATE TABLE GuiaTransporte (ID INTEGER PRIMARY KEY AUTOINCREMENT, NumeroGuia VARCHAR, FechaDespacho DATATIME, Cliente VARCHAR, Destino VARCHAR) ''')
        return False

# Tabla PruebaEntrega
def tableExit(nameTable):
    cursorBD.execute(''' SELECT COUNT(name) FROM SQLITE_MASTER WHERE TYPE = 'table' AND name = '{nameTable}' '''.format(nameTable))
    if cursorBD.fetchone()[0] == 1:
        return True
    else:
        cursorBD.execute(''' CREATE TABLE PruebaEntrega (ID INTEGER PRIMARY KEY AUTOINCREMENT, GuiaTransporteID INTEGER FOREING KEY, DocumentoEntregaID INTEGER FOREING KEY, FechaPrueba DATATIME, Observaciones VARCHAR, FirmaCliente VARCHAR ) ''')
        return False


# Tabla Factura
def tableExit(nameTable):
    cursorBD.execute(''' SELECT COUNT(name) FROM SQLITE_MASTER WHERE TYPE = 'table' AND name = '{nameTable}' '''.format(nameTable))
    if cursorBD.fetchone()[0] == 1:
        return True
    else:
        cursorBD.execute(''' CREATE TABLE Factura (ID INTEGER PRIMARY KEY AUTOINCREMENT, NumeroFactura VARCHAR, FechaRadicacion DATATIME, MontoTotal FLOAT) ''')
        return False

# Tabla DetalleFactura
def tableExit(nameTable):
    cursorBD.execute(''' SELECT COUNT(name) FROM SQLITE_MASTER WHERE TYPE = 'table' AND name = '{nameTable}' '''.format(nameTable))
    if cursorBD.fetchone()[0] == 1:
        return True
    else:
        cursorBD.execute(''' CREATE TABLE DetalleFactura (ID INTEGER PRIMARY KEY AUTOINCREMENT, FacturaID INTEGER FOREING KEY, DocuemtnoEntregaID INTEGER FOREING KEY, MontoDetalle INTEGER) ''')
        return False

tableExit('Pedido')
tableExit('LineaPedido')
tableExit('Bodega')
tableExit('AsignacionBodega')
tableExit('DocumentoEntrega')
tableExit('GuiaTransporte')
tableExit('PruebaEntrega')
tableExit('Factura')
tableExit('DetalleFactura')


#INSERTAR DATOS.

def InsertPedido(ID, NumeroPedido, FechaCreacion, CanalComercializacion, ClienteFinal):
    cursorBD.execute(''' INSERT INTO Pedido (ID, NumeroPedido, FechaCreacion, CanalComercializacion, ClienteFinal) VALUES(?, ?, ?, ?, ?) ''', (ID, NumeroPedido, FechaCreacion, CanalComercializacion, ClienteFinal))
    conexion.commit()
    
    
InsertPedido(12345, '1234A', 12/30/2000, 'AEA', 'PEOSASD')