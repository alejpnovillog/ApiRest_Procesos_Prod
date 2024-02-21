##### TABLAS DEL MODULO APIREST DE RECEPCION ARCHIVOS SUCERP

###### SCHEMA **GXPPROD**

 1. TABLA **TIPOESTADO**               (tabla de referencia)

```
    Field('estadoid', type='id', comment='Id'),
    Field('estado', unique=True,      type='string', length=1,    required=True, comment='Estado'),
    Field('descestado', unique=True, type='string', length=50, required=True, comment='Desc Estado')

```

 2. TABLA **TIPOCUOTA**                (tabla de referencia)

```
    Field('tipocuotaid', type='id', comment='Id'),
    Field('tipocuota', unique=True, type='integer', required=True, comment='Tipo Cuota'),
    Field('desctipocuota', unique=True,  type='string', length=50, required=True, comment='Desc Tipo Cuota')

```

 3. TABLA **TIPOREGISTRO**             (tabla de referencia)

```
    Field('tiporegistroid', type='id', comment='Id'),
    Field('tiporegistro', unique=True, type='string', length=2, required=True, comment='Tipo Registro'),
    Field('desctiporegistro', unique=True, type='string', length=50, required=True, comment='Desc Tipo Registro')

```

 4. TABLA **TIPOSUBREGISTRO**          (tabla de referencia)

```
    Field('tiposubregistroid', type='id', comment='Id'),
    Field('tiposubregistro', unique=True, type='string', length=1, required=True, comment='Tipo Sub Registro'),
    Field('desctiposubregistro', unique=True, type='string', length=50, required=True, comment='Descr Tipo Sub Registro')

```

 5. TABLA **TIPOCUERPO**               (tabla de referencia)

```
    Field('tipocuerpoid', type='id', comment='Id'),
    Field('tipocuerpo', unique=True,  type='string', length=2,    required=True, comment='Tipo Cuerpo'),
    Field('desctipocuerpo', unique=True, type='string', length=50, required=True, comment='Desc Cuerpo')

```

 6. TABLA **TIPOTITULAR**                (tabla de referencia)

```
    Field('tipotitularid', type='id', comment='Id'),
    Field('tipotitular', unique=True, type='string', length=1,    required=True, comment='Tipo Tirular'),
    Field('desctipotitular', unique=True, type='string', length=50, required=True, comment='Desc Tipo Titular')

```

 7. TABLA **TIPOORIGEN**                 (tabla de referencia)

```
    Field('origenid', type='id', comment='Id'),
    Field('tipoorigen', unique=True, type='string', length=1, required=True, comment='Origen'),
    Field('descorigen', unique=True, type='string', length=50, required=True, comment='Desc Origen')

```

 8. TABLA **TIPOMOVIMIENTO**             (tabla de referencia)

```
    Field('codigotipomovimientoid', type='id', comment='Id'),
    Field('codigotipomovimiento', unique=True,  type='integer', required=True, comment='Codigo Tipo Movimiento'),
    Field('desctipomovimiento', unique=True, type='string', length=50, required=True, comment='Desc Tipo Movimiento')

```

 9. TABLA **TIPOPAGO**                   (tabla de referencia)

```
    Field('codigoformapagoid', type='id', comment='Id'),
    Field('codigoformapago', unique=True, type='integer', required=True, comment='Codigo Forma Pago'),
    Field('descrtipopago', unique=True, type='string', length=50, required=True, comment='Desc Tipo Pago')

```

10. TABLA **TIPOMONEDA**                (tabla de referencia)

```
    Field('codigomonedaid', type='id', comment='Id'),
    Field('codigomoneda', unique=True, type='integer', required=True, comment='Codigo Moneda'),
    Field('desctipomoneda', unique=True, type='string', length=50, required=True, comment='Desc Tipo Moneda')

```

11. TABLA **TIPODOCUMENTO**             (tabla de referencia)

```
    Field('tipodocumentoid', type='id', comment='Id'),
    Field('tipodocumento', unique=True, type='integer', required=True, comment='Tipo Documento'),
    Field('desctipodocumento', unique=True, type='string', length=50, required=True, comment='Desc Tipo Documento')

```

12. TABLA **PROVINCIAS**                (tabla de referencia)

```
    Field('provinciaid', type='id', comment='Id'),
    Field('provincia', unique=True, type='integer', required=True, comment='Provincia'),
    Field('descprovincia', unique=True, type='string', length=50, required=True, comment='Desc Provincia')

```

13. TABLA **ENCABEZADO**                (Formato E0 recibido)

```
    # 
    # Id de la tabla 
    Field('encabezadoid', type='id', comment='Id'),
    # 
    # Constante “E0”
    Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
    # 
    # Es la versión del protocolo. Por Ejemplo 01.40
    Field('versionprotocolo', type='string', length=5,    required=True, comment='Version Protocolo'),
    # 
    # Es el número de revisión. Por Ejemplo v01.40 r01.00
    Field('revisionprotocolo', type='string', length=5,    required=True, comment='Revision Protocolo'),
    # 
    # Código del organismo Municipal o Provincial que realiza la transferencia
    Field('codigoorganismo', type='integer', required=True, comment='Codigo Organismo'),
    # 
    # Número de envío (correlativo)
    Field('numeroenvio', type='bigint', required=True, comment='Nro Envio'),
    # CAMPO OPCIONAL
    # Fecha y hora de la producción del archivo de interacción. Formato aaaa-mm-dd hh:mm:ss
    Field('fechahora', type='datetime', required=True, comment='Fecha Hora'),
    #
    # Indica que el registro pertenece al archivo recibido de Sucerp
    Field('archivorecibidoid', type='reference RECEPCIONARCHIVOS', ondelete='CASCADE', comment='Id Fk RECEPCIONARCHIVOS'),
    #
    # Fecha time stamp de incorporación del registro
    Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp'),
    # 
    # Indica que fue procesado a la Db de la Matanza
    Field('procesadoDbMatanza', type='integer', required=True, comment='ProcesadoDbMatanza'),

```

14. TABLA **ALTAIMPOSITIVA**            (Formato C1-C recibido)

```
    # 
    # Id de la tabla 
    Field('altataxid', type='id', comment='Id'),
    #
    # Id de la tabla TIPO_REGISTRO "C1"
    Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
    #
    # Id de la tabla TIPO_SUBREGISTRO "C"
    Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
    #
    # Código del organismo Municipal o Provincial al cual corresponde la información
    Field('codigoorganismo', type='integer', required=True, comment='Codigo Organismo'),
    # CAMPO OPCIONAL
    # Número de trámite interno de la aplicación
    Field('numerotramite', type='bigint',  required=True, comment='Nro Tramite '),
    #
    # Código de tipo de trámite registral realizado
    Field('codigotipotramite', type='integer', required=True, comment='Codigo Tipo Tramite '),
    #
    # Descripción del tipo de trámite registral realizado
    Field('descrtipotramite', type='string', length=60, required=True, comment='Descr Tipo Tramite '),
    #
    # Código del tip    o de acción realizada por el contribuyente
    Field('codigotipoaccion', type='integer', required=True, comment='Codigo Tipo Accion'),
    #
    # Descripción del tipo de acción realizada por el contribuyente
    Field('descrtipoaccion', type='string', length=60,   required=True, comment='Descr Tipo Accion'),
    #
    # Identificador de tipo de formulario exigible para el trámite
    Field('tipoformulario', type='integer', required=True, comment='Tipo Formulario'),
    #
    # Número de formulario en el que se realizo el trámite
    Field('numeroformulario', type='integer', required=True, comment='Nro Formulario'),
    #
    # Patente del Vehículo (Reempadronado)
    Field('dominionuevo', type='string', length=8, required=True, comment='Dominio Nuevo'),
    #
    # Patente del Vehículo (Dominio Anterior)
    Field('dominioviejo', type='string', length=8, required=True, comment='Dominio Viejo'),
    #
    # Código del vehículo según la DNRPA. MTM (Marca – Tipo – Modelo) y FMM (Fabrica – Marca – Modelo).
    Field('codigomtmfmm', type='string', length=8, required=True, comment='Codigo Sucerp'),
    #
    # Tipo de origen del vehículo (N – Nacional, I - Importado)
    Field('origenid', type='reference TIPOORIGEN', ondelete='CASCADE', comment='Id FK Tipo Origen Vehiculo'),
    # CAMPO OPCIONAL
    # Categoría del vehículo
    Field('categoría', type='string', length=3, required=True, comment='Categoria'),
    #
    # Descripción de la marca del Vehículo
    Field('marca', type='string', length=60, required=True, comment='Marca'),
    #
    # Descripción del tipo de Vehículo
    Field('tipovehiculo', type='string', length=60, required=True, comment='Tipo Vehiculo'),
    #
    # Descripción del modelo del vehículo
    Field('modelo', type='string', length=100, required=True, comment='Modelo'),
    #
    # Año/Modelo del vehículo
    Field('yyyymodelo', type='integer', required=True, comment='Año Modelo'),
    # CAMPO OPCIONAL
    # Peso del vehículo
    Field('peso', type='integer', required=True, comment='Peso'),
    # CAMPO OPCIONAL
    # Carga del Vehículo
    Field('carga', type='integer', required=True, comment='Carga'),
    # CAMPO OPCIONAL
    # Cilindrada (sólo motovehículos)
    Field('cilindrada', type='integer', required=True, comment='Cilindrada'),
    #
    # Valuación del vehículo
    Field('valuacion', type='integer', required=True, comment='Valuacion'),
    #
    # Código de tipo de uso del vehículo
    Field('codigotipouso', type='string', length=2, required=True, comment='Codigo Tipo Uso'),
    #
    # Descripción del tipo de uso del vehículo
    Field('descrtipouso', type='string', length=100, required=True, comment='Descr Tipo Uso'),
    #
    # Fecha de vigencia. Formato aaaa-mm-dd
    Field('fechavigencia', type='date', required=True, comment='Fecha Vigencia'),
    #
    # Tipo de documento del titular principal. Según tabla anexa V
    Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id FK Tipo Documento'),
    #
    # Número de documento del titular principal
    Field('numerodocumento', type='bigint', required=True, comment='Nro Documento'),
    #
    # Número de CUIT o CUIL del titular principal
    Field('cuitcuil', type='bigint', required=True, comment='Cuit/Cuil'),
    #
    # Nombre y Apellido o Razón Social del titular principal
    Field('apenomrazonsocial', type='string', length=150,  required=True, comment='ApeNom Razon Social'),
    #
    # Calle donde recibirá el impuesto
    Field('calle', type='string', length=40,   required=True, comment='Calle'),
    #
    # Número donde recibirá el impuesto
    Field('numero', type='string', length=10,   requiSred=True, comment='Nro Puerta'),
    # CAMPO OPCIONAL
    # Piso donde recibirá el impuesto
    Field('piso', type='string', length=10,   required=True, comment='Piso'),
    # CAMPO OPCIONAL
    # Departamento donde recibirá el impuesto
    Field('departamento', type='string', length=10,   required=True, comment='Depto'),
    # CAMPO OPCIONAL
    # Barrio donde recibirá el impuesto
    Field('barrio', type='string', length=40,   required=True, comment='Barrio'),
    #
    # Localidad donde recibirá el impuesto
    Field('localidad', type='string', length=40,   required=True, comment='Localidad'),
    #
    # Código Postal donde recibirá el impuesto
    Field('codigopostal', type='string', length=8,    required=True, comment='Codigo Postal'),
    #
    # Código de provincia donde recibirá el impuesto
    Field('provinciaid', type='reference PROVINCIAS', ondelete='CASCADE', comment='Id FK Provincia'),
    #
    # Cantidad de titulares del vehículo
    Field('cantidadtitulares', type='integer', required=True, comment='Cantidad Titulares'),
    #
    # Código de Registro Seccional que realizó la transacción
    Field('codigoregistroseccional', type='integer', required=True, comment='Codigo Registro Seccional'),
    #
    # Nombre del Registro Seccional
    Field('razonsocial',  type='string', length=40,   required=True, comment='Razon Social'),
    #
    # Código del Registro Seccional de origen del trámite (sólo disponible en cambios de radicación y recuperos)
    Field('registroseccionalorigen', type='integer', required=True, comment='Registro Seccion Origen'),
    # CAMPO OPCIONAL
    # Razón social del Registro Seccional origen del trámite (sólo disponible en cambios de radicación).
    Field('razonsocialregistroseccionalorigen', type='string', length=40, required=True, comment='Raz Soc Reg Seccional Origeb'),
    # CAMPO OPCIONAL
    # Razón social de la Municipalidad origen del trámite.
    Field('municipalidadorigen', type='string', length=150,  required=True, comment='Municipalidad Origen'),
    #
    # Fecha de la operación. Formato aaaa-mm-dd hh:ii:ss
    Field('fechaoperacion', type='datetime', required=True, comment='fecha Operacion'),
    # CAMPO OPCIONAL
    # Contiene los datos de cada parámetro adicional que el organismo requiera al realizar el trámite. 
    # Dispone de un máximo de 10 valores adicionales. Ver anexo V
    Field('parametrosadicionales',   type='string', length=650,  required=True, comment='Parm Adicionales'),
    # CAMPO OPCIONAL
    # Reservado para uso futuro
    Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
    # CAMPO OPCIONAL
    # Observaciones
    Field('observaciones',  type='string', length=256,  required=True, comment='Observaciones'),
    #
    # Indica que el registro pertenece al archivo recibido de Sucerp
    Field('archivorecibidoid', type='reference RECEPCIONARCHIVOS', ondelete='CASCADE', comment='Id Fk RECEPCIONARCHIVOS'),
    #
    # Fecha time stamp de incorporación del registro
    Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp'),
    # 
    # Indica que fue procesado a la Db de la Matanza
    Field('procesadoDbMatanza', type='integer', required=True, comment='ProcesadoDbMatanza'),
    #
    # Indica que el registro pertenece al Informacion Vehiculo
    Field('infvehiculoid', type='reference INFORMACIONVEHICULO', ondelete='CASCADE', comment='Id Fk INFORMACIONVEHICULO'),

```

15. TABLA **ALTAIMPOSITIVATITULAR**     (Formato C1-T recibido)

```
    #
    # Id de identificación del registro
    Field('altataxtitularid', type='id', comment='Id'),
    #
    # Constante “C1 ”
    Field('tipocuerpoid', type='reference TIPOCUERPO', ondelete='CASCADE', comment='Id Fk Tipo Cuerpo'),
    #
    # Constante “T ”
    Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id Fk Tipo Sub Registro'),
    #
    # Tipo de documento del titular. Según tabla anexa V
    Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id Fk Tipo Documento'),
    #
    # Número de documento correspondiente al titular
    Field('numerodocumento', type='bigint', required=True, comment='Nro Documento'),
    #
    # Número de CUIT / CUIL correspondiente al titular
    Field('cuitcuil', type='bigint', required=True, comment='Cuit/Cuil'),
    #
    # Nombre y Apellido o Razón Social del titular del vehículo
    Field('apellidonombre', type='string', length=150, required=True, comment='Apellido y Nombre'),
    #
    # Porcentaje de posesión del vehiculo
    Field('porcentajetitularidad', type='integer', required=True, comment='Porcentaje Titular'),
    #
    # Calle del domicilio del titular
    Field('calle', type='string', length=40, required=True, comment='Calle'),
    #
    # Número de puerta del domicilio del titular
    Field('numero', type='string', length=10, required=True, comment='Nro Puerta'),
    # CAMPO OPCIONAL
    # Piso del departamento del domicilio del titular
    Field('piso', type='string', length=10, required=True, comment='Piso'),
    # CAMPO OPCIONAL
    # Departamento del domicilio del titular
    Field('departamento', type='string', length=10, required=True, comment='Depto'),
    # CAMPO OPCIONAL
    # Barrio del domicilio del titular
    Field('barrio', type='string', length=40, required=True, comment='Barrio'),
    #
    # Localidad del domicilio del titular
    Field('localidad', type='string', length=40, required=True, comment='Localidad'),
    #
    # Código Postal del titular
    Field('codigopostal', type='string', length=8, required=True, comment='Cod Postal'),
    #
    # Provincia del Titular. Según tabla Anexo VI
    Field('provinciaid', type='reference PROVINCIAS', ondelete='CASCADE', comment='Id Fk Provincia'),
    # CAMPO OPCIONAL
    # Reservado para uso futuro
    Field('reservado', type='string', length=256, required=True, comment='Reservado Sucerp'),
    #
    # Indica que el registro pertenece al archivo recibido de Sucerp
    Field('archivorecibidoid', type='reference RECEPCIONARCHIVOS', ondelete='CASCADE', comment='Id Fk RECEPCIONARCHIVOS'),
    #
    # Fecha de incorporación del registro
    Field('ktimestamp', type='datetime', required=True, comment='Timestamp'),
    # 
    # Indica que fue procesado a la Db de la Matanza
    Field('procesadoDbMatanza', type='integer', required=True, comment='ProcesadoDbMatanza'),
    #
    # Referencia a la Alta Impositiva
    Field('altataxid', type='reference ALTAIMPOSITIVA', ondelete='CASCADE', comment='Id FK ALTAIMPOSITIVA'),
    #
    # Referencia a la INFORMACIONVEHICULOTITULAR
    Field('infvehiculotitularid', type='reference INFORMACIONVEHICULOTITULAR', ondelete='CASCADE', comment='Id FK INFORMACIONVEHICULOTITULAR'),

```

16. TABLA **PROCESOIMPORTACIONEXPORTACION** (tabla de referencia)

```
    Field('procesoid', type='id', comment='Id'),
    Field('procesocodigotabla', type='integer', required=True, comment='Proceso Codigo Tabla'),
    Field('procesonombretabla', type='string', length=150, required=True, comment='Proceso Nombre Tabla'),
    Field('procesotransferencia', type='string', length=1, required=True, comment='Transferencia (S, Nulo)'),
    Field('procesofechatransferencia', type='datetime',  comment='Fecha Transferencia'),
    Field('procesobasedatos', type='string', length=1, required=True, comment='Base Datos (S, Nulo)'),
    Field('procesofechabasedatos', type='datetime',  comment='Fecha Base Datos'),
    Field('procesoaccion', type='string', length=1, required=True, comment='Accion ( E, I, Nulo)'),

```

17. TABLA **RECEPLOG**

```
    #
    # Id de identificación del registro
    Field('receplogid', type='id', comment='Id'),
    #
    # Nombre del archivo recibido
    Field('archivorecibido', type='string', length=1520, required=True, comment='Archivo recibido de Sucerp'),
    #
    # Nombre del formato procesado
    Field('fromatoprocesado', type='string', length=4, required=True, comment='Formato procesado'),
    #
    # Numero de orden dentro del formato con error
    Field('numerocampoformato', type='integer', required=True, comment='Numero de campo en el formato'),
    #
    # Fecha de incorporación del registro
    Field('ktimestamp', type='datetime', required=True, comment='Timestamp')

```

18. TABLA **BAJAIMPOSITIVA**

```
    #
    # Id identificador del registro
    Field('bajataxid', type='id', comment='Id'),
    #
    # Constante “C2 ”
    Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id Fk Tipo Registro'),
    #
    # Constante “C”
    Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id Fk Tipo Sub Registro'),
    #
    # Código del organismo Municipal o Provincial al cual corresponde la información
    Field('codigoorganismo', type='integer', required=True, comment='Cod Organismo'),
    # CAMPO OPCIONAL
    # Número de trámite interno de la aplicación
    Field('numerotramite', type='bigint', required=True, comment='Nro Tramite'),
    #
    # Código de trámite registral realizado
    Field('codigotipotramite', type='integer', required=True, comment='Cod Tipo Tramite'),
    #
    # Descripción del tipo de trámite registral realizado
    Field('descrtipotramite', type='string', length=60, required=True, comment='Descripcion Tramite'),
    #
    # Código del tipo de acción realizada por el contribuyente
    Field('codigotipoaccion', type='integer', required=True, comment='Cod Tipo Accion'),
    #
    # Descripción del tipo de acción realizada por el contribuyente
    Field('descrtipoaccion', type='string', length=60, required=True, comment='Descripcion Tipo Accion'),
    #
    # Identificador de tipo de formulario exigible para el trámit
    Field('tipoformulario', type='integer', required=True, comment='Tipo Formulario'),
    #
    # Número de formulario en el que se realizo el trámite
    Field('numeroformulario', type='integer', required=True, comment='Nro Formulario'),
    #
    # Patente del Vehículo (Reempadronado)
    Field('dominionuevo', type='string', length=8, required=True, comment='Dominio Nuevo'),
    #
    # Patente del Vehículo (Dominio Anterior)
    Field('dominioviejo', type='string', length=8, required=True, comment='Dominio Viejo'),
    #
    # Código del vehículo según la DNRPA. MTM (Marca – Tipo – Modelo) y FMM (Fabrica – Marca – Modelo).
    Field('codigomtmfmm', type='string', length=8, required=True, comment='Codigo Sucerp'),
    #
    # Tipo de origen del vehículo (N – Nacional, I - Importado)
    Field('origenid', type='reference TIPOORIGEN', ondelete='CASCADE', comment='Id Fk Tipo Origen'),
    # CAMPO OPCIONAL
    # Categoría del vehículo
    Field('categoría', type='string', length=3, required=True, comment='Categoria'),
    #
    # Descripción de la marca del Vehículo
    Field('marca', type='string', length=60, required=True, comment='Marca'),
    #
    # Descripción del tipo de Vehículo
    Field('tipovehiculo', type='string', length=60,   required=True, comment='Tipo Vehiculo'),
    #
    # Descripción del modelo del vehículo
    Field('modelo',  type='string', length=100,  required=True, comment='Modelo'),
    #
    # Año/Modelo del Vehículo
    Field('yyyymodelo', type='integer', required=True, comment='Año Modelo'),
    # CAMPO OPCIONAL
    # Peso del Vehículo
    Field('peso', type='integer', required=True, comment='Peso Vehiculo'),
    # CAMPO OPCIONAL
    # Carga del Vehículo
    Field('carga', type='integer', required=True, comment='Carga'),
    # CAMPO OPCIONAL
    # Cilindrada (sólo motovehículos)
    Field('cilindrada', type='integer', required=True, comment='Cilindrada'),
    #
    # Valuación del vehículo
    Field('valuacion', type='integer', required=True, comment='Valuacion'),
    #
    # Código de tipo de uso del vehículo
    Field('codigotipouso', type='string', length=2,    required=True, comment='Cod Tipo Uso'),
    #
    # Descripción del tipo de uso del vehículo
    Field('descrtipouso', type='string', length=100,  required=True, comment='Descripcion Tipo Uso'),
    #
    # Fecha de vigencia. Formato aaaa-mm-dd.
    Field('fechavigencia', type='date', required=True, comment='Fecha Vigencia'),
    #
    # Cantidad de titulares del vehículo
    Field('cantidadtitulares', type='integer', required=True, comment='Cantidad Titulares'),
    #
    # Código de Registro Seccional
    Field('codigoregistronacional', type='integer', required=True, comment='Codigo Registro  Nacional'),
    #
    # Nombre del registro Seccional
    Field('razonsocial', type='string', length=40,   required=True, comment='Razon Social'),
    # CAMPO OPCIONAL
    # Código del Registro Seccional de destino del trámite
    Field('registroseccionaldestino', type='integer', required=True, comment='Registro Seccional Destino'),
    #
    # Razón social del Registro Seccional destino del trámite (sólo disponible en cambios de radicación)
    Field('razonsocialregistroseccionalorigen', type='string', length=40, required=True, comment='Raz. Soc. Reg. Seccional  Orig.'),
    # CAMPO OPCIONAL
    # Razón social de la Municipalidad destino del trámite.
    Field('municipalidaddestino', type='string', length=150,  required=True, comment='Muni. Destino'),
    #
    # Fecha de la operación. Formato aaaa-mm-dd hh:mm:ss
    Field('fechaoperacion', type='datetime', required=True, comment='Fecha Operacion'),
    # CAMPO OPCIONAL
    # Contiene los datos de cada parámetro adicional que el organismo requiera al realizar el trámite. 
    # Dispone de un máximo de 10 valores adicionales. Ver anexo VII.
    Field('parametrosadicionales',   type='string', length=650,  required=True, comment='Param. Adicionales'),
    # CAMPO OPCIONAL
    # Reservado para uso futuro
    Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
    # CAMPO OPCIONAL
    # Observaciones
    Field('observaciones', type='string', length=256,  required=True, comment='Observaciones'),
    #
    # Indica que el registro pertenece al archivo recibido de Sucerp
    Field('archivorecibidoid', type='reference RECEPCIONARCHIVOS', ondelete='CASCADE', comment='Id Fk RECEPCIONARCHIVOS'),
    #
    # Fecha del ingreso del registro 
    Field('ktimestamp', type='datetime', required=True, comment='Key TimeStamp'),
    # 
    # Indica que fue procesado a la Db de la Matanza
    Field('procesadoDbMatanza', type='integer', required=True, comment='ProcesadoDbMatanza'),
    #
    # Indica que el registro pertenece al Informacion Vehiculo
    Field('infvehiculoid', type='reference INFORMACIONVEHICULO', ondelete='CASCADE', comment='Id Fk INFORMACIONVEHICULO'),

```

19. TABLA **BAJAIMPOSITIVATITULAR**

```
    #
    # Id identificador del registro
    Field('bajataxtitularid', type='id', comment='Id'),
    #
    # Constante “C2 ”
    Field('tipocuerpoid', type='reference TIPOCUERPO', ondelete='CASCADE', comment='Id Fk Tipo Cuerpo'),
    #
    # Constante “T ”
    Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id Fk Tipo Sub Registro'),
    #
    # Tipo de documento del titular. Según tabla anexa V
    Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id Fk Tipo Documento'),
    #
    # Número de documento correspondiente al titular
    Field('numerodocumento', type='bigint', required=True, comment='Nro Documento'),
    #
    # Número de CUIT / CUIL correspondiente al titular
    Field('cuitcuil', type='bigint', required=True, comment='Cuit/Cuil'),
    #
    # Nombre y Apellido o Razón Social del titular del vehículo
    Field('apellidonombre', type='string', length=150,  required=True, comment='Apellido y Nombre'),
    #
    # Porcentaje de posesión del vehiculo
    Field('porcentajetitularidad', type='integer', required=True, comment='Procentaje Titular'),
    #
    # Calle del domicilio del titular
    Field('calle', type='string', length=40, required=True, comment='Calle'),
    #
    # Número de puerta del domicilio del titular
    Field('numero', type='string', length=10, required=True, comment='Nro Puerta'),
    #
    # Piso del departamento del domicilio del titular
    Field('piso', type='string', length=10, required=True, comment='Piso'),
    #
    # Departamento del domicilio del titular
    Field('departamento', type='string', length=10, required=True, comment='Depto'),
    # CAMPO OPCIONAL
    # Barrio del domicilio del titular
    Field('barrio', type='string', length=40, required=True, comment='Barrio'),
    #
    # Localidad del domicilio del titular
    Field('localidad', type='string', length=40, required=True, comment='Localidad'),
    #
    # Código Postal del titular
    Field('codigopostal', type='string', length=8,    required=True, comment='Cod Postal'),
    #
    # Provincia del Titular. Según tabla Anexo VI
    Field('provinciaid', type='reference PROVINCIAS', ondelete='CASCADE', comment='Id Fk Provincias'),
    # CAMPO OPCIONAL
    # Reservado para uso futuro
    Field('reservado', type='string', length=256, required=True, comment='Reservado Sucerp'),
    #
    # Indica que el registro pertenece al archivo recibido de Sucerp
    Field('archivorecibidoid', type='reference RECEPCIONARCHIVOS', ondelete='CASCADE', comment='Id Fk RECEPCIONARCHIVOS'),
    #
    # Fecha del ingreso del registro 
    Field('ktimestamp', type='datetime', required=True, comment='Timestamp'),
    # 
    # Indica que fue procesado a la Db de la Matanza
    Field('procesadoDbMatanza', type='integer', required=True, comment='ProcesadoDbMatanza'),
    #
    # Referencia a la INFORMACIONVEHICULOTITULAR
    Field('infvehiculotitularid', type='reference INFORMACIONVEHICULOTITULAR', ondelete='CASCADE', comment='Id FK INFORMACIONVEHICULOTITULAR'),

```

20. TABLA **IMPUESTOSELLOS**

```
    #
    # Id identificador del registro
    Field('taxsellosid', type='id', comment='Id'),
    #
    # Constante “C3 ”
    Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
    #
    # Constante “C”
    Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
    #
    # Código del organismo Municipal o Provincial al cual corresponde la información
    Field('codigoorganismo', type='integer', required=True, comment='Codigo Organismo'),
    #
    # Número de trámite interno de la aplicación
    Field('numerotramite', type='bigint', required=True, comment='Nro Tramite'),
    #
    # Código del tipo de acción realizada por el contribuyente
    Field('codigotipoaccion', type='integer', required=True, comment='Cod Tipo Accion'),
    #
    # Descripción del tipo de acción realizada por el contribuyente
    Field('descrtipoaccion', type='string', length=60, required=True, comment='Descr. Tipo Accion'),
    #
    # Identificador de tipo de formulario exigible para el trámite
    Field('tipoformulario', type='integer', required=True, comment='Tipo Formulario'),
    #
    # Número de formulario en el que se realizo el trámite
    Field('numeroformulario', type='integer', required=True, comment='Nro Formulario'),
    # CAMPO OPCIONAL
    # Patente del Vehículo (Reempadronado), es opcional, 
    # puede llegar o el dominio o el nº de recibo, nunca los dos a la vez
    Field('dominionuevo', type='string', length=8, required=True, comment='Dominio Nuevo'),
    # CAMPO OPCIONAL
    # Patente del Vehículo (Dominio Anterior)
    Field('dominioviejo', type='string', length=8, required=True, comment='Dominio Viejo' ),
    # CAMPO OPCIONAL
    # Nº de recibo que otorga el registro seccional, es opcional, 
    # puede llegar o el dominio o el nº de recibo, nunca los dos a la vez
    Field('recibo', type='string', length=15, required=True, comment='Recibo'),
    # CAMPO OPCIONAL
    # Código del vehículo según la DNRPA. MTM (Marca – Tipo – Modelo) 
    # y FMM (Fabrica – Marca – Modelo).
    Field('codigomtmfmm', type='string', length=8, required=True, comment='Codigo Sucerp'),
    # CAMPO OPCIONAL
    # Tipo de origen del vehículo (N – Nacional, I - Importado)
    Field('origenid', type='reference TIPOORIGEN', ondelete='CASCADE', comment='Id FK Origen'),
    # CAMPO OPCIONAL
    # Categoría del vehículo
    Field('categoría', type='string', length=3, required=True, comment='Categoria'),
    # CAMPO OPCIONAL
    # Descripción de la marca del Vehículo
    Field('marca', type='string', length=60, required=True, comment='Marca'),
    # CAMPO OPCIONAL
    # Descripción del tipo de Vehículo
    Field('tipovehiculo', type='string', length=60, required=True, comment='Tipo Vehiculo'),
    # CAMPO OPCIONAL
    # Descripción del modelo del vehículo 
    Field('modelo', type='string', length=100, required=True, comment='Modelo'),
    # CAMPO OPCIONAL
    # Año/Modelo del Vehículo
    Field('yyyymodelo', type='integer', required=True, comment='Año Modelo'),
    # CAMPO OPCIONAL
    # Código de tipo de uso del vehículo
    Field('codigotipouso', type='string', length=2, required=True, comment='Codigo Tipo Uso'),
    # CAMPO OPCIONAL
    # Descripción del tipo de uso del vehículo
    Field('descrtipouso', type='string', length=100, required=True, comment='Descr Tipo Uso'),
    # CAMPO OPCIONAL
    # Valuación del Vehículo
    Field('valuacion', type='integer', required=True, comment='Valuacion'),
    #
    # Cantidad de partes
    Field('cantidadpartes', type='integer', required=True, comment='Cantidad Partes'),
    #
    # Total de los montos de impuesto adicionales al contrato
    Field('montoimpuestoadicional', type='decimal(12, 2)', required=True, comment='Monto Impuesto Adicional'),
    #
    # Total de los montos de punitorios cobrados
    Field('montopunitorios', type='decimal(12, 2)', required=True, comment='Monto Punitorios'),
    #
    # Total de los montos percibido
    Field('montototalcobrado', type='decimal(12, 2)', required=True, comment='Monto Total Cobrado'),
    #
    # Total del monto abonado fuera del RRSS, exhibido ante la presentación de un comprobante. 
    # Puede ser el importe parcial o total del sello
    Field('montoabonado', type='decimal(12, 2)', required=True, comment='Monto Abonado'),
    # CAMPO OPCIONAL
    # Según tabla Anexo III
    Field('codigoformapagoid', type='reference TIPOPAGO', ondelete='CASCADE', comment='Id FK Cod Forma Pago'),
    # CAMPO OPCIONAL
    # Según tabla Anexo IV
    Field('codigomonedaid', type='reference TIPOMONEDA', ondelete='CASCADE', comment='Id FK Cod Moneda'),
    # CAMPO OPCIONAL
    # Código de entidad bancaria
    Field('codigoentidadbancaria', type='integer', required=True, comment='Codigo Entidad Bancaria'),
    # CAMPO OPCIONAL
    # Razón Social de la entidad bancaria
    Field('descrentidadbancaria', type='string', length=60, required=True, comment='Descr Entidad Bancaria'),
    # CAMPO OPCIONAL
    # Número de cheque
    Field('numerocheque', type='string', length=20, required=True, comment='Nro Cheque'),
    # 
    # S: Esta exento, N: no esta exento
    Field('exencion', type='string', length=1, required=True, comment='Execcion'),
    # CAMPO OPCIONAL
    # Código de la exención
    Field('codigoexencion', type='string', length=10, required=True, comment='Codigo Execcion'),
    # CAMPO OPCIONAL
    # Descripción de la exención
    Field('descripcionexencion', type='string', length=100, required=True, comment='Descr Execcion'),
    # CAMPO OPCIONAL
    # Fecha de depósito. Formato aaaa-mm-dd hh:mm:ss
    Field('fechadeposito', type='datetime', required=True, comment='fecha Deposito'),
    #
    #  Código de Registro Seccional
    Field('codigoregistroseccional', type='integer', required=True, comment='Codigo Registro Seccional'),
    #
    # Número de CUIT del encargado del Registro Seccional
    Field('cuitregistroseccional', type='bigint', required=True, comment='Cuit Registro Seccional'),
    #
    # Nombre del Registro Seccional
    Field('razonsocial', type='string', length=40, required=True, comment='Razon Social'),
    #
    # Fecha de la operación. Formato aaaa-mm-dd hh:mm:ss
    Field('fechaoperacion', type='datetime', required=True, comment='fecha Operacion'),
    # CAMPO OPCIONAL
    # Contiene los datos de cada parámetro adicional que el organismo requiera al realizar el trámite. 
    # Dispone de un máximo de 10 valores adicionales. Ver anexo VII.
    Field('parametrosadicionales', type='string', length=650, required=True, comment='Parm Adicionales'),
    # CAMPO OPCIONAL
    # Reservado para uso futuro
    Field('reservado', type='string', length=256, required=True, comment='Reservado'),
    # CAMPO OPCIONAL
    # Observaciones
    Field('observaciones', type='string', length=256, required=True, comment='Observaciones'),
    # CAMPO OPCIONAL
    # Observaciones anulación
    Field('observacionesanulacion', type='string', length=256, required=True, comment='Observaciones Anulacion'),
    #
    # Indica que el registro pertenece al archivo recibido de Sucerp
    Field('archivorecibidoid', type='reference RECEPCIONARCHIVOS', ondelete='CASCADE', comment='Id Fk RECEPCIONARCHIVOS'),
    #
    # Fecha del ingreso del registro 
    Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp'),
    # 
    # Indica que fue procesado a la Db de la Matanza
    Field('procesadoDbMatanza', type='integer', required=True, comment='ProcesadoDbMatanza'),
    #
    # Indica que el registro pertenece al Informacion Vehiculo
    Field('infvehiculoid', type='reference INFORMACIONVEHICULO', ondelete='CASCADE', comment='Id Fk INFORMACIONVEHICULO'),
    #
    # Relación de TRAMITESGENERALES
    Field('tramitesgeneralesid', type='reference TRAMITESGENERALES', ondelete='CASCADE', comment='Id FK Tramite Grales Tramites'),

```

21. TABLA **IMPUESTOSELLOSPARTES**

```
    #
    # Id identificador del registro
    Field('taxsellospartesid', type='id', comment='Id'),
    #
    # Constante “C3 ”
    Field('tipocuerpoid', type='reference TIPOCUERPO', ondelete='CASCADE', comment='Id FK Tipo Cuerpo'),
    #
    # Constante “P ” 
    Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
    #
    # Tipo de interviniente en la operación.
    Field('tipointerviniente', type='integer', required=True, comment='Tipo Interviniente'),
    #
    # Descripción del tipo de parte del impuesto
    Field('descrtipointerviniente', type='string', length=60,   required=True, comment='Descr Tipo Interviniente'),
    # CAMPO OPCIONAL
    # Tipo de documento del titular. Según tabla anexa V
    Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id FK Tipo Documento'),
    # CAMPO OPCIONAL
    # Número de documento correspondiente al titular
    Field('numerodocumento', type='bigint', required=True, comment='Nro Documento'),
    #
    # Número de CUIT / CUIL correspondiente al titular
    Field('cuitcuil', type='bigint', required=True, comment='Cuit/Cuil'),
    # CAMPO OPCIONAL
    # Nombre y Apellido o Razón Social del titular del vehículo
    Field('apellidonombre', type='string', length=150,  required=True, comment='Apellido y Nombre'),
    #
    # Porcentaje de posesión del vehiculo
    Field('porcentajetitularidad', type='integer', required=True, comment='Porcentaje Titular'),
    # CAMPO OPCIONAL
    # Calle del domicilio del titular
    Field('calle', type='string', length=40,   required=True, comment='Calle'),
    # CAMPO OPCIONAL
    # Número de puerta del domicilio del titular
    Field('numero', type='string', length=10,   required=True, comment='Nro Puerta'),
    # CAMPO OPCIONAL
    # Piso del departamento del domicilio del titular
    Field('piso', type='string', length=10,   required=True, comment='Piso'),
    # CAMPO OPCIONAL
    # Departamento del domicilio del titular
    Field('departamento', type='string', length=10, required=True, comment='Depto'),
    # CAMPO OPCIONAL
    # Barrio del domicilio del titular
    Field('barrio', type='string', length=40,   required=True, comment='Barrio'),
    # CAMPO OPCIONAL
    # Localidad del domicilio del titular
    Field('localidad', type='string', length=40,   required=True, comment='Localidad'),
    # CAMPO OPCIONAL
    # Código Postal del titular
    Field('codigopostal', type='string', length=8,    required=True, comment='Codigo Postal'),
    # CAMPO OPCIONAL
    # Provincia del Titular. Según tabla Anexo VI
    Field('provinciaid', type='reference PROVINCIAS', ondelete='CASCADE', comment='Id FK Provincia'),
    #
    # S: Esta exento, N: no esta exento
    Field('exencion', type='string', length=1,    required=True, comment='Execcion'),
    # CAMPO OPCIONAL
    # Código de la exención
    Field('codigoexencion', type='string', length=10,   required=True, comment='Codigo Execcion'),
    # CAMPO OPCIONAL
    # Descripción de la exención
    Field('descripcionexencion', type='string', length=100,  required=True, comment='Descr Execcion'),
    # CAMPO OPCIONAL
    # Código de trámite registral realizado
    Field('codigotipotramite', type='integer', required=True, comment='Codigo Tipo Tramite'),
    # CAMPO OPCIONAL
    # Descripción del tipo de trámite registral realizado
    Field('descrtipotramite', type='string', length=60,   required=True, comment='Descr Tipo Tramite'),
    # CAMPO OPCIONAL
    # Reservado
    Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
    #
    # Indica que el registro pertenece al archivo recibido de Sucerp
    Field('archivorecibidoid', type='reference RECEPCIONARCHIVOS', ondelete='CASCADE', comment='Id Fk RECEPCIONARCHIVOS'),
    #
    # Fecha del ingreso del registro 
    Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp'),
    # 
    # Indica que fue procesado a la Db de la Matanza
    Field('procesadoDbMatanza', type='integer', required=True, comment='ProcesadoDbMatanza'),
    #
    # Referencia a la INFORMACIONVEHICULOTITULAR
    Field('infvehiculotitularid', type='reference INFORMACIONVEHICULOTITULAR', ondelete='CASCADE', comment='Id FK INFORMACIONVEHICULOTITULAR'),
    #
    # Relación de TRAMITESGENERALES
    Field('tramitesgeneralesid', type='reference TRAMITESGENERALES', ondelete='CASCADE', comment='Id FK Tramite Grales Tramites'),

```

22. TABLA  **IMPUESTOSELLOSPARTESTIPOTRAMITE**

```
    #
    # Id identificador del registro
    Field('taxsellospartestipotramiteid', type='id', comment='Id'),
    #
    # Constante “C3 ”
    Field('tipocuerpoid', type='reference TIPOCUERPO', ondelete='CASCADE', comment='Id FK Tipo Cuerpo'),
    #
    # Constante “T ”
    Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
    #
    # Código de trámite registral realizado
    Field('codigotipotramite', type='integer', required=True, comment='Codigo Tipo Tramite'),
    #
    # Descripción del tipo de trámite registral realizado
    Field('descrtipotramite', type='string', length=60,   required=True, comment='Descr Tipo Tramite'),
    #
    # Monto declarado del contrato para el instrumento
    Field('montocontrato', type='decimal(12, 2)', required=True, comment='Monto Contrato'),
    #
    # Base imponible del cálculo del impuesto
    Field('baseimponible', type='decimal(12, 2)', required=True, comment='Base Imponible'),
    #
    # Monto cobrado del impuesto
    Field('montoimpuesto', type='decimal(12, 2)', required=True, comment='Monto Impuesto'),
    #
    # Importe de punitorios cobrados del impuesto
    Field('montopunitorio', type='decimal(12, 2)', required=True, comment='monto Punitorio'),
    #
    # Importe abonado fuera del RRSS para el tipo de instrumentación
    Field('montofueraregistro', type='decimal(12, 2)', required=True, comment='Monto Abonado Fuera Registro'),
    #
    # Importe adicional del trámite
    Field('montoadicional', type='decimal(12, 2)', required=True, comment='Monto Adicional'),
    #
    # Alícuota aplicada al momento del cálculo del sello para este tipo de trámite
    Field('alicuota', type='decimal(5, 2)', required=True, comment='Alicuota'),
    #
    # Porcentaje del contrato del instrumento
    Field('porcentajecontrato', type='decimal(5, 2)', required=True, comment='Porcentaje Contrato'),
    #
    # Porcentaje del impuesto, será menor a 100 en caso de existir exenciones.
    Field('porcentajeimpuesto', type='decimal(5, 2)', required=True, comment='Porcentaje Impuesto'),
    #
    # Fecha de la instrumentación contrato sobre el cual se cobra el impuesto. Formato aaaa-mmdd hh:mm:ss
    Field('fechacontrato', type='datetime', required=True, comment='Fecha Contrato'),
    # CAMPO OPCIONAL
    # Reservado (**)
    Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
    #
    # Indica que el registro pertenece al archivo recibido de Sucerp
    Field('archivorecibidoid', type='reference RECEPCIONARCHIVOS', ondelete='CASCADE', comment='Id Fk RECEPCIONARCHIVOS'),
    #
    # Fecha del ingreso del registro 
    Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp'),
    # 
    # Indica que fue procesado a la Db de la Matanza
    Field('procesadoDbMatanza', type='integer', required=True, comment='ProcesadoDbMatanza'),
    #
    # Relación de IMPUESTOSELLOSPARTES
    Field('taxsellospartesid', type='reference IMPUESTOSELLOSPARTES', ondelete='CASCADE', comment='Id FK IMPUESTOSELLOSPARTES'),
    #
    # Relación de TRAMITESGENERALES
    Field('tramitesgeneralesid', type='reference TRAMITESGENERALES', ondelete='CASCADE', comment='Id FK Tramite Grales Tramites'),


```

23. TABLA **IMPUESTOAUTOMOTOR**

```
    #
    # Id identificador del registro
    Field('taxautomotorid', type='id', comment='Id'),
    #
    # Constante “C4 ”
    Field('tipocuerpoid', type='reference TIPOCUERPO', ondelete='CASCADE', comment='Id FK Tipo Cuerpo'),
    #
    # Código del organismo Municipal o Provincial al cual corresponde la información
    Field('codigoorganismo', type='integer', required=True, comment='Codigo Organismo'),
    # CAMPO OPCIONAL
    # Número de trámite interno de la aplicación
    Field('numerotramite', type='bigint', required=True, comment='Nro Tramite'),
    #
    # Según tabla Anexo I
    Field('codigotipomovimientoid', type='reference TIPOMOVIMIENTO', ondelete='CASCADE', comment='Id FK Cod Tipo Movimiento'),
    #
    # Según tabla Anexo II o los tipos que se convengan al momento de salir operativos.
    Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
    #
    # Patente del Vehículo
    Field('dominionuevo', type='string', length=8, required=True, comment='Dominio Nuevo'),
    #
    # Patente del Vehículo
    Field('dominioviejo', type='string', length=8, required=True, comment='Dominio Viejo'),
    #
    # Año Fiscal               
    Field('yyyy', type='integer', required=True, comment='Año'),
    #
    # Número de Cuota
    Field('numerocuota', type='integer', required=True, comment='Nro Cuota'),
    #
    # Fecha hasta la cual es válido el importe bonificado
    Field('fechabonificacion', type='date', required=True, comment='Fecha Bonificacion'),
    #
    # Fecha a partir de la cual se comienza a realizar el cálculo de punitorios
    Field('fechavencimiento', type='date', required=True, comment='Fecha Vencimiento'),
    #
    # Determina si la deuda vence o no se tiene en cuenta la fecha de vencimiento (S=Vence  N=No vence)
    Field('flagvencimiento', type='string', length=1, required=True, comment='Flag Vencimiento'),
    #
    # Importe bonificado               
    Field('importebonificado', type='decimal(10, 2)', required=True, comment='Importe Bonificado'),
    #
    # Importe de la deuda
    Field('importecomun', type='decimal(10, 2)', required=True, comment='Importe Comun'),
    #
    # Fecha de proceso de la deuda en el Municipio y/o Provincia. Formato aaaa-mm-dd hh:mm:ss               
    Field('fechaproceso', type='datetime', required=True, comment='Fecha Proceso'),
    # CAMPO OPCIONAL
    # Importe total percibido               
    Field('importetotal', type='decimal(10, 2)',      required=True, comment='Importe Total'),
    # CAMPO OPCIONAL
    # Importe percibido en concepto de impuesto               
    Field('importeimpuesto', type='decimal(10, 2)', required=True, comment='Importe Impuesto'),
    # CAMPO OPCIONAL
    # Importe percibido de punitorios               
    Field('importepunitorio', type='decimal(10, 2)', required=True, comment='Importe Punitorio'),
    # CAMPO OPCIONAL
    # Según tabla Anexo III               
    Field('codigoformapagoid', type='reference TIPOPAGO', ondelete='CASCADE', comment='Id FK Cod Forma Pago'),
    # CAMPO OPCIONAL
    # Según tabla Anexo IV               
    Field('codigomonedaid', type='reference TIPOMONEDA', ondelete='CASCADE', comment='Id FK Cod Moneda'),
    # CAMPO OPCIONAL
    # Código de entidad bancaria               
    Field('codigoentidadbancaria', type='integer', required=True, comment='Codigo Entidad Bancaria'),
    # CAMPO OPCIONAL
    # Razón Social de la entidad bancaria
    Field('descrentidadbancaria',     type='string', length=60,   required=True, comment='Descr Entidad Bancaria'),
    # CAMPO OPCIONAL
    # Número de cheque
    Field('numerocheque',             type='string', length=20,   required=True, comment='Nro Cheque'),
    # CAMPO OPCIONAL
    # Fecha de cobro. Formato aaaa-mm-dd hh:mm:ss
    Field('fechacobro', type='datetime', required=True, comment='Fecha Cobro'),
    # CAMPO OPCIONAL
    # Fecha de transferencia estimada. Formato aaaamm-dd hh:mm:s
    Field('fechatransferencia', type='datetime', required=True, comment='Fecha Transferencia'),
    # CAMPO OPCIONAL
    # Código del Registro Seccional
    Field('codigoregistroseccional', type='integer', required=True, comment='Codigo Registro Seccional'),
    # CAMPO OPCIONAL
    # Nombre del Registro Seccional
    Field('descrregistroseccional', type='string', length=40,   required=True, comment='Descr Registro Seccional'),
    # CAMPO OPCIONAL
    # Reservado para uso del organismo. Recuerde que no podrá contener ni caracteres pipe “|” ni el separador que utilice para el protocolo.
    Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
    # CAMPO OPCIONAL
    # Observaciones
    Field('observaciones',  type='string', length=256,  required=True, comment='Observaciones'),
    #
    # Indica que el registro pertenece al archivo recibido de Sucerp
    Field('archivorecibidoid', type='reference RECEPCIONARCHIVOS', ondelete='CASCADE', comment='Id Fk RECEPCIONARCHIVOS'),
    #
    # Fecha del ingreso del registro 
    Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp'),
    # 
    # Indica que fue procesado a la Db de la Matanza
    Field('procesadoDbMatanza', type='integer', required=True, comment='ProcesadoDbMatanza'),
    #
    # Indica que el registro pertenece al Informacion Vehiculo
    Field('infvehiculoid', type='reference INFORMACIONVEHICULO', ondelete='CASCADE', comment='Id Fk INFORMACIONVEHICULO'),

```

24. TABLA **INFORMACIONVEHICULO**

```
    #
    # Id identificador del registro
    Field('infvehiculoid', type='id', comment='Id'),
    #
    # Constante “C5 ”
    Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
    #
    # Constante “C”
    Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
    #
    # Código del organismo Municipal o Provincial al cual corresponde la información
    Field('codigoorganismo', type='integer', required=True, comment='Codigo Organismo'),
    #
    # Patente del Vehículo (Reempadronado)
    Field('dominionuevo', type='string', length=8,    required=True, comment='Dominio Nuevo'),
    #
    # Patente del Vehículo (Dominio Anterior)
    Field('dominioviejo', type='string', length=8,    required=True, comment='Dominio Viejo'),
    #
    # Código del vehículo según la DNRPA. MTM (Marca – Tipo – Modelo) y FMM (Fabrica – Marca – Modelo).
    Field('codigomtmfmm', type='string', length=8, required=True, comment='Codigo Sucerp'),
    #
    # Tipo de origen del vehículo (N – Nacional, I – Importado).
    Field('origenid', type='reference TIPOORIGEN', ondelete='CASCADE', comment='Id FK Origen'),
    # CAMPO OPCIONAL
    # Categoría del vehículo
    Field('categoría', type='string', length=3,    required=True, comment='Categoria'),
    #
    # Descripción de la marca del Vehículo
    Field('marca', type='string', length=60,   required=True, comment='Marca'),
    #
    # Descripción del tipo de Vehículo
    Field('tipovehiculo', type='string', length=60,   required=True, comment='Tipo Vehiculo'),
    #
    # Descripción del modelo del vehículo
    Field('modelo', type='string', length=100,  required=True, comment='Modelo'),
    #
    # Año/Modelo del Vehículo
    Field('yyyymodelo', type='integer', required=True, comment='Año Modelo'),
    # CAMPO OPCIONAL
    # Peso del Vehículo
    Field('peso', type='integer', required=True, comment='Peso'),
    # CAMPO OPCIONAL
    # Carga del Vehículo
    Field('carga', type='integer', required=True, comment='Carga'),
    # CAMPO OPCIONAL
    # Cilindrada (sólo motovehículos)
    Field('cilindrada', type='integer', required=True, comment='Cilindrada'),
    #
    # Valuación del Vehículo
    Field('valuacion', type='integer', required=True, comment='Valuacion'),
    #
    # Código de tipo de uso del vehículo
    Field('codigotipouso', type='string', length=2,    required=True, comment='Codigo Tipo Uso'),
    #
    # Descripción del tipo de uso del vehículo
    Field('descrtipouso', type='string', length=100,  required=True, comment='Descr Tipo Uso'),
    #
    # Fecha de la inscripción inicial del vehículo
    Field('fechainscripcioninicial', type='date', required=True, comment='Fecha Inscripcion Inicial'),
    # CAMPO OPCIONAL
    # Fecha de la última transferencia del vehículo
    Field('fechaultimatransferencia', type='date', required=True, comment='Fecha Ult Transferencia'),
    # CAMPO OPCIONAL
    # Fecha del último movimiento en SU jurisdicción
    Field('fechaultimomovimiento', type='date', required=True, comment='Fecha Ult Movimiento'),
    #
    # Estado dominial. Según tabla anexa VIII
    Field('estadodominial', type='string', length=1,    required=True, comment='Estado Dominial'),
    # CAMPO OPCIONAL
    # Fecha en que se produjo el último cambio dominial
    Field('fechacambioestadodominal', type='date', required=True, comment='Fecha Camb Estado Dominial'),
    #
    # Determina si dispone de una guarda habitual
    Field('guardahabitual', type='string', length=1,    required=True, comment='Guarda Habitual'),
    # CAMPO OPCIONAL
    # Calle del domicilio de guarda
    Field('calle', type='string', length=40, required=True, comment='Calle'),
    # CAMPO OPCIONAL
    # Número de puerta del domicilio de guarda
    Field('numero', type='string', length=10, required=True, comment='Nro Puerta'),
    # CAMPO OPCIONAL
    # Piso del departamento del domicilio de guarda
    Field('piso', type='string', length=10, required=True, comment='Piso'),
    # CAMPO OPCIONAL
    # Departamento del domicilio de guarda
    Field('departamento', type='string', length=10, required=True, comment='Depto'),
    # CAMPO OPCIONAL - EN LA DESCRIPCION ACTUAL EL CAMPO NO EXISTE 
    # Localidad del domicilio de guarda 
    Field('barrio', type='string', length=40, required=True, comment='Barrio'),
    # CAMPO OPCIONAL
    # Localidad del domicilio de guarda
    Field('localidad', type='string', length=40, required=True, comment='Localidad'),
    # CAMPO OPCIONAL
    # Código Postal de guarda
    Field('codigopostal', type='string', length=8, required=True, comment='Codigo Postal'),
    # CAMPO OPCIONAL
    # Provincia de guarda. Según tabla Anexo VI
    Field('provinciaid', type='reference PROVINCIAS', ondelete='CASCADE', comment='Id FK Provincia'),
    #
    # Cantidad de titulares del vehículo
    Field('cantidadtitulares', type='integer', required=True, comment='Cantidad Titulares'),
    #
    # Código de Registro Seccional
    Field('codigoregistroseccional', type='integer', required=True, comment='Codigo Registro Seccional'),
    #
    # Nombre del Registro Seccional
    Field('razonsocial',  type='string', length=40,   required=True, comment='Razon Social'),
    #
    # Fecha de la operación. Formato aaaa-mm-dd hh:mm:ss
    Field('fechaoperacion', type='datetime', required=True, comment='fecha Operacion'),
    # CAMPO OPCIONAL
    # Reservado para uso futuro
    Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
    # EN LA DESCRIPCION ACTUAL EL CAMPO NO EXISTE 
    # 
    Field('controlsucerp', type='string', length=3,    required=True, comment='Control Sucerp'),
    #
    # Indica que el registro pertenece al archivo recibido de Sucerp
    Field('archivorecibidoid', type='reference RECEPCIONARCHIVOS', ondelete='CASCADE', comment='Id Fk RECEPCIONARCHIVOS'),
    #
    # Fecha del ingreso del registro 
    Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp'),
    # 
    # Indica que fue procesado a la Db de la Matanza
    Field('procesadoDbMatanza', type='integer', required=True, comment='ProcesadoDbMatanza'),

```

25. TABLA **INFORMACIONVEHICULOTITULAR**

```
    #
    # Id identificador del registro
    Field('infvehiculotitularid', type='id', comment='Id'),
    #
    # Constante “C5 ” 
    Field('tipocuerpoid', type='reference TIPOCUERPO', ondelete='CASCADE', comment='Id FK Tipo Cuerpo'),
    #
    # Constante “T ”
    Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
    #
    # Tipo de documento del titular. Según tabla anexa V
    Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id FK Tipo Documento'),
    #
    # Número de documento correspondiente al titular
    Field('numerodocumento', type='bigint', required=True, comment='Nro Documento'),
    #
    # Número de CUIT / CUIL correspondiente al titular
    Field('cuitcuil', type='bigint', required=True, comment='Cuit/Cuil'),
    #
    # Nombre y Apellido o Razón Social del titular del vehículo
    Field('apellidonombre', type='string', length=150, required=True, comment='Apellido y Nombre'),
    #
    # Porcentaje de posesión del vehiculo
    Field('porcentajetitularidad', type='integer', required=True, comment='Porcentaje Titular'),
    #
    # Calle del domicilio del titular
    Field('calle', type='string', length=40, required=True, comment='Calle'),
    #
    # Número de puerta del domicilio del titular
    Field('numero', type='string', length=10, required=True, comment='Nro Puerta'),
    #
    # Piso del departamento del domicilio del titular
    Field('piso', type='string', length=10, required=True, comment='Piso'),
    #
    # Departamento del domicilio del titular
    Field('departamento', type='string', length=10, required=True, comment='Depto'),
    # CAMPO OPCIONAL
    # Barrio del domicilio del titular
    Field('barrio', type='string', length=40, required=True, comment='Barrio'),
    #
    # Localidad del domicilio del titular
    Field('localidad', type='string', length=40, required=True, comment='Localidad'),
    #
    # Código Postal del titular
    Field('codigopostal', type='string', length=8, required=True, comment='Codigo Postal'),
    #
    # Provincia del Titular. Según tabla Anexo VI
    Field('provinciaid', type='reference PROVINCIAS', ondelete='CASCADE', comment='Id FK Provincia'),
    # CAMPO OPCIONAL
    # Reservado para uso futuro
    Field('reservado', type='string', length=256, required=True, comment='Reservado'),
    #
    # Indica que el registro pertenece al archivo recibido de Sucerp
    Field('archivorecibidoid', type='reference RECEPCIONARCHIVOS', ondelete='CASCADE', comment='Id Fk RECEPCIONARCHIVOS'),
    #
    # Fecha del ingreso del registro 
    Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp'),
    # 
    # Indica que fue procesado a la Db de la Matanza
    Field('procesadoDbMatanza', type='integer', required=True, comment='ProcesadoDbMatanza'),

```

26. TABLA **CAMBIOTITULARIDAD**

```
    #
    # Id identificador del registro
    Field('cambiotitularidadid', type='id', comment='Id'),
    #
    # Constante “C6 ”
    Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
    #
    # Constante “C”
    Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
    #
    # Código del organismo Municipal o Provincial al cual corresponde la información
    Field('codigoorganismo', type='integer', required=True, comment='Codigo Organismo'),
    # CAMPO OPCIONAL
    # Número de trámite interno de la aplicación
    Field('numerotramite', type='bigint', required=True, comment='Nro Tramite'),
    #
    # Código de trámite registral realizado
    Field('codigotipotramite', type='integer', required=True, comment='Codigo Tipo Tramite'),
    #
    # Descripción del tipo de trámite registral realizado
    Field('descrtipotramite', type='string', length=60,   required=True, comment='Descr Tipo Tramite'),
    #
    # Código del tipo de acción realizada por el contribuyente
    Field('codigotipoaccion', type='integer', required=True, comment='Codigo Tipo Accion'),
    #
    # Descripción del tipo de acción realizada por el contribuyente
    Field('descrtipoaccion', type='string', length=60,   required=True, comment='Descr Tipo Accion'),
    #
    # Identificador de tipo de formulario exigible para el trámite
    Field('tipoformulario', type='integer', required=True, comment='Tipo Formulario'),
    #
    # Número de formulario en el que se realizo el trámite
    Field('numeroformulario', type='integer', required=True, comment='Nro Formulario'),
    #
    # Patente del Vehículo (Reempadronado)
    Field('dominionuevo', type='string', length=8,    required=True, comment='Dominio Nuevo'),
    #
    # Patente del Vehículo (Dominio Anterior)
    Field('dominioviejo', type='string', length=8,    required=True, comment='Dominio Viejo'),
    #
    # Código del vehículo según la DNRPA. MTM (Marca – Tipo – Modelo) y FMM (Fabrica – Marca – Modelo).
    Field('codigomtmfmm', type='string', length=8,    required=True, comment='Codigo Sucerp'),
    #
    # Tipo de origen del vehículo (N – Nacional, I – Importado).
    Field('origenid', type='reference TIPOORIGEN', ondelete='CASCADE', comment='Id FK Origen'),
    # CAMPO OPCIONAL
    # Categoría del vehículo
    Field('categoría', type='string', length=3, required=True, comment='Categoria'),
    #
    # Descripción de la marca del Vehículo
    Field('marca', type='string', length=60, required=True, comment='Marca'),
    #
    # Descripción del tipo de Vehículo
    Field('tipovehiculo', type='string', length=60, required=True, comment='Tipo Vehiculo'),
    #
    # Descripción del modelo del vehículo
    Field('modelo', type='string', length=100, required=True, comment='Modelo'),
    #
    # Año/Modelo del Vehículo
    Field('yyyymodelo', type='integer', required=True, comment='Año Modelo'),
    # CAMPO OPCIONAL
    # Peso del Vehículo
    Field('peso', type='integer', required=True, comment='Peso'),
    # CAMPO OPCIONAL
    # Carga del Vehículo
    Field('carga', type='integer', required=True, comment='Carga'),
    #
    # Cilindrada (sólo motovehículos)
    Field('cilindrada', type='integer', required=True, comment='Cilindrada'),
    #
    # Valuación del Vehículo
    Field('valuacion', type='integer', required=True, comment='Valuacion'),
    #
    # Código de tipo de uso del vehículo
    Field('codigotipouso', type='string', length=2, required=True, comment='Codigo Tipo Uso'),
    #
    # Descripción del tipo de uso del vehículo
    Field('descrtipouso', type='string', length=100, required=True, comment='Descr Tipo Uso'),
    #
    # Fecha de Transferencia. Formato aaaa-mm-dd
    Field('fechavigencia', type='date', required=True, comment='Fecha Vigencia'),
    #
    # Tipo de documento del titular principal. Según tabla anexa V
    Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id FK Tipo Documento'),
    #
    # Número de documento correspondiente al titular principal
    Field('numerodocumento', type='bigint', required=True, comment='Nro Documento'),
    #
    # Número de CUIT o CUIL del titular principal
    Field('cuitcuil', type='bigint', required=True, comment='Cuit/Cuil'),
    #
    # Nombre y Apellido o Razón Social del titular principal
    Field('apenomrazonsocial', type='string', length=150, required=True, comment='ApeNom Razon Social'),
    #
    # Calle donde recibirá el impuesto
    Field('calle', type='string', length=40, required=True, comment='Calle'),
    #
    # Número donde recibirá el impuesto
    Field('numero', type='string', length=10, required=True, comment='Nro Puerta'),
    # CAMPO OPCIONAL
    # Piso donde recibirá el impuesto
    Field('piso', type='string', length=10, required=True, comment='Piso'),
    # CAMPO OPCIONAL  
    # Departamento donde recibirá el impuesto
    Field('departamento', type='string', length=10, required=True, comment='Depto'),
    # CAMPO OPCIONAL
    # Barrio donde recibirá el impuesto
    Field('barrio', type='string', length=40, required=True, comment='Barrio'),
    #
    # Localidad donde recibirá el impuesto
    Field('localidad', type='string', length=40, required=True, comment='Localidad'),
    #
    # Código Postal donde recibirá el impuesto
    Field('codigopostal', type='string', length=8, required=True, comment='Codigo Postal'),
    #
    # Provincia donde recibirá el impuesto
    Field('provinciaid', type='reference PROVINCIAS', ondelete='CASCADE', comment='Id FK Provincia'),
    #
    # Cantidad de titulares del vehículo
    Field('cantidadtitulares', type='integer', required=True, comment='Cantidad Titulares'),
    #
    # Código de registro seccional que realizó la transacción
    Field('codigoregistroseccional', type='integer', required=True, comment='Codigo Registro Seccional'),
    #
    # Nombre del Registro Seccional
    Field('razonsocial', type='string', length=40, required=True, comment='Razon Social'),
    #
    # Fecha de la operación. Formato aaaa-mm-dd hh:mm:ss
    Field('fechaoperacion', type='datetime', required=True, comment='fecha Operacion'),
    # CAMPO OPCIONAL
    # Contiene los datos de cada parámetro adicional que el organismo requiera al realizar el trámite. 
    # Dispone de un máximo de 10 valores adicionales. Ver anexo VII.
    Field('parametrosadicionales', type='string', length=650, required=True, comment='Parm Adicionales'),
    # CAMPO OPCIONAL
    # Reservado para uso futuro
    Field('reservado', type='string', length=256, required=True, comment='Reservado'),
    # CAMPO OPCIONAL
    # Observaciones
    Field('observaciones', type='string', length=256, required=True, comment='Observaciones'),
    #
    # Indica que el registro pertenece al archivo recibido de Sucerp
    Field('archivorecibidoid', type='reference RECEPCIONARCHIVOS', ondelete='CASCADE', comment='Id Fk RECEPCIONARCHIVOS'),
    #
    # Fecha del ingreso del registro 
    Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp'),
    # 
    # Indica que fue procesado a la Db de la Matanza
    Field('procesadoDbMatanza', type='integer', required=True, comment='ProcesadoDbMatanza'),
    #
    # Indica que el registro pertenece al Informacion Vehiculo
    Field('infvehiculoid', type='reference INFORMACIONVEHICULO', ondelete='CASCADE', comment='Id Fk INFORMACIONVEHICULO'),

```

27. TABLA **CAMBIOTITULARIDADTITULAR**

```
    #
    # Id identificador del registro
    Field('cambiotitularidadtitid', type='id', comment='Id'),
    #
    # Constante “C6 ”
    Field('tipocuerpoid', type='reference TIPOCUERPO', ondelete='CASCADE', comment='Id FK Tipo Cuerpo'),
    #
    # Constante “T ”
    Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
    #
    # Determina el tipo de titular transferido. (N=Titular Nuevo – A=Titular Anterior)
    Field('tipotitularid', type='reference TIPOTITULAR', ondelete='CASCADE', comment='Id FK Tipo Titular'),
    #
    # Tipo de documento del titular. Según tabla anexa V
    Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id FK Tipo Documento'),
    #
    # Número de documento correspondiente al titular
    Field('numerodocumento', type='bigint', required=True, comment='Nro Documento'),
    #
    # Número de CUIT / CUIL correspondiente al titularId identificador del registro
    Field('cuitcuil', type='bigint', required=True, comment='Cuit/Cuil'),
    #
    # Nombre y Apellido o Razón Social del titular del vehículo
    Field('apellidonombre', type='string', length=150, required=True, comment='Apellido y Nombre'),
    #
    # Porcentaje de posesión del vehiculo
    Field('porcentajetitularidad', type='integer', required=True, comment='Porcentaje Titular'),
    #
    # Calle del domicilio del titular
    Field('calle', type='string', length=40, required=True, comment='Calle'),
    #
    # Número de puerta del domicilio del titular
    Field('numero', type='string', length=10, required=True, comment='Nro Puerta'),
    # CAMPO OPCIONAL
    # Piso del departamento del domicilio del titular
    Field('piso', type='string', length=10, required=True, comment='Piso'),
    # CAMPO OPCIONAL
    # Departamento del domicilio del titular
    Field('departamento', type='string', length=10, required=True, comment='Depto'),
    # CAMPO OPCIONAL
    # Barrio del domicilio del titular
    Field('barrio', type='string', length=40, required=True, comment='Barrio'),
    #
    # Localidad del domicilio del titular
    Field('localidad', type='string', length=40, required=True, comment='Localidad'),
    #
    # Código Postal del titular
    Field('codigopostal', type='string', length=8, required=True, comment='Codigo Postal'),
    #
    # Provincia del Titular. Según tabla Anexo VI
    Field('provinciaid', type='reference PROVINCIAS', ondelete='CASCADE', comment='Id FK Provincia'),
    # CAMPO OPCIONAL
    # Reservado para uso futuro
    Field('reservado', type='string', length=256, required=True, comment='Reservado'),
    #
    # Indica que el registro pertenece al archivo recibido de Sucerp
    Field('archivorecibidoid', type='reference RECEPCIONARCHIVOS', ondelete='CASCADE', comment='Id Fk RECEPCIONARCHIVOS'),
    #
    # Fecha del ingreso del registro 
    Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp'),
    # 
    # Indica que fue procesado a la Db de la Matanza
    Field('procesadoDbMatanza', type='integer', required=True, comment='ProcesadoDbMatanza'),
    #
    # Referencia a la INFORMACIONVEHICULOTITULAR
    Field('infvehiculotitularid', type='reference INFORMACIONVEHICULOTITULAR', ondelete='CASCADE', comment='Id FK INFORMACIONVEHICULOTITULAR'),

```

28. TABLA **INFORMACIORADICACION**

```
    #
    # Id identificador del registro
    Field('infradicacionid', type='id', comment='Id'),
    #
    # Constante “C7 ”
    Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
    #
    # Código del organismo Municipal o Provincial al cual corresponde la información
    Field('codigoorganismo', type='integer', required=True, comment='Codigo Organismo'),
    #
    # Patente del Vehículo
    Field('dominio', type='string', length=8,    required=True, comment='Dominio'),
    #
    # Estado de la radicación del vehículo (A – Activa, B – Baja, C - Cancelada).
    Field('estadoid', type='reference TIPOESTADO',  ondelete='CASCADE', comment='Id FK Estado'),
    #
    # Tipo de la radicación (D – Definitiva, P – Pendiente, T – Temporal).
    Field('tiporadicacion', type='string', length=1,    required=True, comment='Tipo Radicacion'),
    #
    # Fecha de alta en la jurisdicción. Formato aaaamm-dd
    Field('fechaalta', type='date', required=True, comment='Fecha Alta'),
    #
    # Fecha de baja en la jurisdicción. Formato aaaamm-d
    Field('fechabajaradicacion', type='date', required=True, comment='Fecha Baja Radicacion'),
    #
    # Determina de donde proviene la información 
    # del estado de la radicación (M – Municipalidad, R – Registro Seccional).
    Field('origeninformacion', type='string', length=1,    required=True, comment='Origen Informacion'),
    #
    # Código del Registro Seccional donde se originó la modificación de la radicación.
    Field('codigoregistroseccional', type='integer', required=True, comment='Codigo Registro Seccional'),
    #
    # Razón Social del Registro Seccional donde se originó la modificación de la radicación.
    Field('razonsocialregistro', type='string', length=100,  required=True, comment='Razon Social Registro'),
    # CAMPO OPCIONAL
    # Reservado para uso futuro
    Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
    #
    # Observaciones ingresadas al momento 
    # de la modificación de la radiación por parte de un Registro Seccional
    Field('observaciones', type='string', length=256,  required=True, comment='Observaciones'),
    #
    # Indica que el registro pertenece al archivo recibido de Sucerp
    Field('archivorecibidoid', type='reference RECEPCIONARCHIVOS', ondelete='CASCADE', comment='Id Fk RECEPCIONARCHIVOS'),
    #
    # Fecha del ingreso del registro 
    Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp'),
    # 
    # Indica que fue procesado a la Db de la Matanza
    Field('procesadoDbMatanza', type='integer', required=True, comment='ProcesadoDbMatanza'),

```

29. TABLA **ANULACIONTRAMITESSELLOS**

```
    #
    # Id identificador del registro
    Field('anultramitesellosid', type='id',  comment='Id'),
    #
    # Constante “C8 ”
    Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
    #
    # Constante “C”
    Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
    #
    # Código del organismo Municipal o Provincial al cual corresponde la información
    Field('codigoorganismo', type='integer', required=True, comment='Codigo Organismo'),
    #
    # Determina el tipo de anulación, puede ser un trámite de patentes “P” o de sellos “S”
    Field('tipoanulacion',            type='string', length=1,    required=True, comment='Tipo Anulacion'),
    #
    # Número de trámite interno de la aplicación (sello o patente)
    Field('numerotramite', type='bigint',              required=True, comment='Nro Tramite'),
    #
    # Código de trámite registral realizado
    Field('codigotipotramite', type='integer', required=True, comment='Codigo Tipo Tramite'),
    #
    # Descripción del tipo de trámite registral realizado
    Field('descrtipotramite',         type='string', length=60,   required=True, comment='Descr Tipo Tramite'),
    #
    # Código del tipo de acción realizada por el contribuyente
    Field('codigotipoaccion', type='integer', required=True, comment='Codigo Tipo Accion'),
    #
    # Descripción del tipo de acción realizada por el contribuyente
    Field('descrtipoaccion', type='string', length=60,   required=True, comment='Descr Tipo Accion'),
    #
    # Identificador del tipo de formulario exigible para el trámite
    Field('tipoformulario', type='integer', required=True, comment='Tipo Formulario'),
    #
    # Número de formulario en el que se realizó el trámite
    Field('numeroformulario', type='integer', required=True, comment='Nro Formulario'),
    # CAMPO OPCIONAL
    # Patente del Vehículo (Reempadronado)
    Field('dominionuevo', type='string', length=8,    required=True, comment='Dominio Nuevo'),
    # CAMPO OPCIONAL
    # Patente del Vehículo (Dominio Anterior)
    Field('dominioviejo', type='string', length=8,    required=True, comment='Dominio Viejo'),
    # CAMPO OPCIONAL
    # Número del comprobante entregado por el Registro Seccional
    Field('numerorecibo',             type='string', length=15,   required=True, comment='Nro Recibo'),
    #
    # Código del vehículo según la DNRPA. MTM (Marca – Tipo – Modelo) y FMM (Fábrica – Marca – Modelo)
    Field('codigomtmfmm', type='string', length=8,    required=True, comment='Codigo Sucerp'),
    #
    # Tipo de origen del vehículo (N – Nacional, I – Importado)
    Field('origenid', type='reference TIPOORIGEN', ondelete='CASCADE', comment='Id FK Origen'),
    #
    # Categoría del vehículo
    Field('categoría', type='string', length=3,    required=True, comment='Categoria'),
    #
    # Descripción de la marca del Vehículo
    Field('marca', type='string', length=60,   required=True, comment='Marca'),
    #
    # Descripción del tipo de Vehículo
    Field('tipovehiculo', type='string', length=60,   required=True, comment='Tipo Vehiculo'),
    #
    # Descripción del modelo del vehículo
    Field('modelo', type='string', length=100,  required=True, comment='Modelo'),
    #
    # Año/Modelo del Vehículo
    Field('yyyymodelo', type='integer', required=True, comment='Año Modelo'),
    #
    # Formato de la fecha de contrato/vigencia aaaamm-dd.
    Field('fechavigencia', type='date', required=True, comment='Fecha Vigencia'),
    #
    # Importe total percibido
    Field('montototal',               type='decimal(12, 2)',      required=True, comment='Monto Total'),
    #
    # Importe total del impuesto
    Field('montoimpuesto', type='decimal(12, 2)', required=True, comment='Monto Impuesto'),
    #
    # Importe percibido por punitorios
    Field('montopunitorio', type='decimal(12, 2)', required=True, comment='monto Punitorio'),
    #
    # Importe adicional
    Field('montoadicional', type='decimal(12, 2)', required=True, comment='Monto Adicional'),
    #
    # Según tabla Anexo III
    Field('codigoformapagoid', type='reference TIPOPAGO', ondelete='CASCADE', comment='Id FK Cod Forma Pago'),
    #
    # Según tabla Anexo IV
    Field('codigomonedaid', type='reference TIPOMONEDA', ondelete='CASCADE', comment='Id FK Cod Moneda'),
    #
    # Código de entidad bancaria
    Field('codigoentidadbancaria', type='integer', required=True, comment='Codigo Entidad Bancaria'),
    #
    # Razón Social de la entidad bancaria
    Field('descrentidadbancaria',     type='string', length=60,   required=True, comment='Descr Entidad Bancaria'),
    #
    # Número de cheque
    Field('numerocheque',             type='string', length=20,   required=True, comment='Nro Cheque'),
    #
    # Formato de la fecha de emisión del trámite aaaa - mm - dd hh:mm:ss
    Field('fechatramite', type='datetime', required=True, comment='Fecha Tramite'),
    # CAMPO OPCIONAL
    # Formato de la fecha de cobro aaaa-mm- dd hh:mm:ss
    Field('fechacobro', type='datetime', required=True, comment='Fecha Cobro'),
    # CAMPO OPCIONAL
    # Formato de la fecha de depósito aaaa-mm- dd hh:mm:ss.
    Field('fechadeposito', type='datetime', required=True, comment='fecha Deposito'),
    #
    # Formato de la fecha de anulación del trámite aaaa-mm- dd hh:mm:ss
    Field('fechabaja', type='date', required=True, comment='Fecha Baja'),
    #
    # Cantidad de registros de detalles de la anulación
    Field('cantidaddetalle', type='integer', required=True, comment='Cantidad Detalle'),
    #
    # Código del Registro Seccional
    Field('codigoregistroseccional', type='integer', required=True, comment='Codigo Registro Seccional'),
    #
    # Nombre del Registro Seccional
    Field('descrregistroseccional', type='string', length=40,   required=True, comment='Descr Registro Seccional'),
    # CAMPO OPCIONAL
    # Reservado para el uso del organismo. 
    # Recuerde que no podrá contener ni caracteres pipe “|” 
    # ni el separador que utilice para el protocolo
    Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
    # CAMPO OPCIONAL
    # Observaciones
    Field('observaciones',            type='string', length=256,  required=True, comment='Observaciones'),
    #
    # Indica que el registro pertenece al archivo recibido de Sucerp
    Field('archivorecibidoid', type='reference RECEPCIONARCHIVOS', ondelete='CASCADE', comment='Id Fk RECEPCIONARCHIVOS'),
    #
    # Fecha del ingreso del registro 
    Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp'),
    # 
    # Indica que fue procesado a la Db de la Matanza
    Field('procesadoDbMatanza', type='integer', required=True, comment='ProcesadoDbMatanza'),
    #
    # Indica que el registro pertenece al Informacion Vehiculo
    Field('infvehiculoid', type='reference INFORMACIONVEHICULO', ondelete='CASCADE', comment='Id Fk INFORMACIONVEHICULO'),
    #
    # Relación de TRAMITESGENERALESTITULARES
    Field('tramitesgeneralesid', type='reference TRAMITESGENERALES', ondelete='CASCADE', comment='Id FK Tramite Grales Tramites'),

```

30. TABLA **ANULACIONTRAMITESSELLOSDETALLE**

```
    #
    # Id identificador del registro
    Field('anultramitesellosdetid', type='id', comment='Id'),
    #
    # Constante C8
    Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
    #
    # Constante “D”
    Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
    #
    # Año Fiscal
    Field('yyyy', type='integer', required=True, comment='Año'),
    #
    # Número de Cuota
    Field('numerocuota', type='integer', required=True, comment='Nro Cuota'),
    #
    # Según tabla Anexo II o los tipos que se convengan al momento de salir operativos
    Field('tipocuotaid', type='reference TIPOCUOTA', ondelete='CASCADE', comment='Id FK Tipo Cuota'),
    #
    # Importe total percibido
    Field('importetotal', type='decimal(10, 2)',      required=True, comment='Importe Total'),
    #
    # Importe total del impuesto
    Field('importeimpuesto', type='decimal(10, 2)', required=True, comment='Importe Impuesto'),
    #
    # Importe percibido por punitorios
    Field('importepunitorio', type='decimal(10, 2)', required=True, comment='Importe Punitorio'),
    #
    # Importe adicional
    Field('importeadicional',         type='decimal(10, 2)',      required=True, comment='Importe Adicional'),
    # CAMPO OPCIONAL
    # Reservado para el uso del organismo. 
    # Recuerde que no podrá contener ni caracteres pipe “|” 
    # ni el separador que utilice para el protocolo
    Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
    # CAMPO OPCIONAL
    # Observaciones
    Field('observaciones',            type='string', length=256,  required=True, comment='Observaciones'),
    #
    # Indica que el registro pertenece al archivo recibido de Sucerp
    Field('archivorecibidoid', type='reference RECEPCIONARCHIVOS', ondelete='CASCADE', comment='Id Fk RECEPCIONARCHIVOS'),
    #
    # Fecha del ingreso del registro 
    Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp'),
    # 
    # Indica que fue procesado a la Db de la Matanza
    Field('procesadoDbMatanza', type='integer', required=True, comment='ProcesadoDbMatanza'),

```

31. TABLA **TRAMITESGENERALES**

```
    #
    # Id identificador del registro
    Field('tramitesgeneralesid', type='id', comment='Id'),
    #
    # Constante “C9 ”
    Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
    #
    # Constante “C”
    Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
    #
    # Código del organismo Municipal o Provincial al cual corresponde la información
    Field('codigoorganismo', type='integer', required=True, comment='Codigo Organismo'),
    #
    # Número de trámite interno de la aplicación
    Field('numerotramite', type='bigint',              required=True, comment='Nro Tramite'),
    #
    # Código de trámite registral realizado
    Field('codigotipotramite', type='integer', required=True, comment='Codigo Tipo Tramite'),
    #
    # Descripción del tipo de trámite registral realizado
    Field('descrtipotramite',         type='string', length=60,   required=True, comment='Descr Tipo Tramite'),
    #
    # Código del tipo de acción realizada por el contribuyente
    Field('codigotipoaccion', type='integer', required=True, comment='Codigo Tipo Accion'),
    #
    # Descripción del tipo de acción realizada por el contribuyente
    Field('descrtipoaccion', type='string', length=60,   required=True, comment='Descr Tipo Accion'),
    #
    # Identificador de tipo de formulario exigible para el trámite
    Field('tipoformulario', type='integer', required=True, comment='Tipo Formulario'),
    #
    # Número de formulario en el que se realizó el trámite
    Field('numeroformulario', type='integer', required=True, comment='Nro Formulario'),
    #
    # Patente del Vehículo (Reempadronado)
    Field('dominionuevo', type='string', length=8,    required=True, comment='Dominio Nuevo'),
    #
    # Patente del Vehículo (Dominio Anterior)
    Field('dominioviejo', type='string', length=8,    required=True, comment='Dominio Viejo'),
    #
    # Código del vehículo según la DNRPA. 
    # MTM (Marca – Tipo – Modelo) y FMM (Fabrica – Marca – Modelo).
    Field('codigomtmfmm', type='string', length=8,    required=True, comment='Codigo Sucerp'),
    #
    # Tipo de origen del vehículo (N – Nacional, I – Importado).
    Field('origenid', type='reference TIPOORIGEN', ondelete='CASCADE', comment='Id FK Origen'),
    # CAMPO OPCIONAL
    # Categoría del vehículo
    Field('categoría', type='string', length=3,    required=True, comment='Categoria'),
    #
    # Descripción de la marca del Vehículo
    Field('marca', type='string', length=60,   required=True, comment='Marca'),
    #
    # Descripción del tipo de Vehículo
    Field('tipovehiculo', type='string', length=60,   required=True, comment='Tipo Vehiculo'),
    #
    # Descripción del modelo del vehículo
    Field('modelo', type='string', length=100,  required=True, comment='Modelo'),
    #
    # Año/Modelo del Vehículo
    Field('yyyymodelo', type='integer', required=True, comment='Año Modelo'),
    # CAMPO OPCIONAL
    # Peso del Vehículo
    Field('peso', type='integer', required=True, comment='Peso'),
    # CAMPO OPCIONAL
    # Carga del Vehículo
    Field('carga', type='integer', required=True, comment='Carga'),
    # CAMPO OPCIONAL
    # Cilindrada (sólo motovehículos)
    Field('cilindrada', type='integer', required=True, comment='Cilindrada'),
    #
    # Valuación del Vehículo
    Field('valuacion', type='integer', required=True, comment='Valuacion'),
    #
    # Código de tipo de uso del vehículo
    Field('codigotipouso', type='string', length=2,    required=True, comment='Codigo Tipo Uso'),
    #
    # Descripción del tipo de uso del vehículo
    Field('descrtipouso', type='string', length=100,  required=True, comment='Descr Tipo Uso'),
    #
    # Fecha de Transferencia. Formato aaaa-mm-dd
    Field('fechavigencia', type='date', required=True, comment='Fecha Vigencia'),
    #
    # Tipo de documento del titular principal. Según tabla anexa V
    Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id FK Tipo Documento'),
    #
    # Número de documento correspondiente al titular principal
    Field('numerodocumento', type='bigint', required=True, comment='Nro Documento'),
    #
    # Número de CUIT o CUIL del titular principal
    Field('cuitcuil', type='bigint', required=True, comment='Cuit/Cuil'),
    #
    # Nombre y Apellido o Razón Social del titular principal
    Field('apenomrazonsocial', type='string', length=150,  required=True, comment='ApeNom Razon Social'),
    #
    # Calle donde recibirá el impuesto
    Field('calle', type='string', length=40,   required=True, comment='Calle'),
    #
    # Número donde recibirá el impuesto
    Field('numero', type='string', length=10, required=True, comment='Nro Puerta'),
    # CAMPO OPCIONAL
    # Piso donde recibirá el impuesto
    Field('piso', type='string', length=10,   required=True, comment='Piso'),
    # CAMPO OPCIONAL
    # Departamento donde recibirá el impuesto
    Field('departamento', type='string', length=10,   required=True, comment='Depto'),
    # CAMPO OPCIONAL
    # Barrio donde recibirá el impuesto
    Field('barrio', type='string', length=40,   required=True, comment='Barrio'),
    #
    # Indica que el registro pertenece al archivo recibido de Sucerp
    Field('archivorecibidoid', type='reference RECEPCIONARCHIVOS', ondelete='CASCADE', comment='Id Fk RECEPCIONARCHIVOS'),
    #
    # Fecha del ingreso del registro 
    Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp'),
    # 
    # Indica que fue procesado a la Db de la Matanza
    Field('procesadoDbMatanza', type='integer', required=True, comment='ProcesadoDbMatanza'),
    #
    # Referencia a la INFORMACIONVEHICULOTITULAR
    Field('infvehiculotitularid', type='reference INFORMACIONVEHICULOTITULAR', ondelete='CASCADE', comment='Id FK INFORMACIONVEHICULOTITULAR'),
    #
    # Indica que el registro pertenece al Informacion Vehiculo
    Field('infvehiculoid', type='reference INFORMACIONVEHICULO', ondelete='CASCADE', comment='Id Fk INFORMACIONVEHICULO'),

```

32. TABLA **TRAMITESGENERALESTITULARES**

```
    #
    # Id identificador del registro
    Field('tramitesgeneralestitid', type='id', comment='Id'),
    #
    # Constante “C9 ”
    Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
    #
    # Constante “T ”
    Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
    #
    # Determina el tipo de titular transferido. (N=Titular Nuevo – A=Titular Anterior)
    Field('tipotitularid', type='reference TIPOTITULAR', ondelete='CASCADE', comment='Id FK Tipo Titular'),
    #
    # Tipo de documento del titular. Según tabla anexa V
    Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id FK Tipo Documento'),
    #
    # Número de documento correspondiente al titular
    Field('numerodocumento', type='bigint', required=True, comment='Nro Documento'),
    #
    # Número de CUIT / CUIL correspondiente al titular
    Field('cuitcuil', type='bigint', required=True, comment='Cuit/Cuil'),
    #
    # Nombre y Apellido o Razón Social del titular del vehículo
    Field('apellidonombre', type='string', length=150, required=True, comment='Apellido y Nombre'),
    #
    # Porcentaje de posesión del vehiculo
    Field('porcentajetitularidad', type='integer', required=True, comment='Procentaje Titular'),
    #
    # Calle del domicilio del titular
    Field('calle', type='string', length=40,   required=True, comment='Calle'),
    #
    # Número de puerta del domicilio del titular
    Field('numero', type='string', length=10,   required=True, comment='Nro Puerta'),
    # CAMPO OPCIONAL
    # Piso del departamento del domicilio del titular
    Field('piso', type='string', length=10,   required=True, comment='Piso'),
    # CAMPO OPCIONAL
    # Departamento del domicilio del titular
    Field('departamento', type='string', length=10,   required=True, comment='Depto'),
    # CAMPO OPCIONAL
    # Barrio del domicilio del titular
    Field('barrio', type='string', length=40,   required=True, comment='Barrio'),
    #
    # Localidad del domicilio del titular
    Field('localidad', type='string', length=40,   required=True, comment='Localidad'),
    #
    # Código Postal del titular
    Field('codigopostal', type='string', length=8,    required=True, comment='Codigo Postal'),
    #
    # Provincia del Titular. Según tabla Anexo VI
    Field('provinciaid', type='reference PROVINCIAS', ondelete='CASCADE', comment='Id FK Provincia'),
    # CAMPO OPCIONAL
    # Reservado para uso futuro
    Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
    #
    # Indica que el registro pertenece al archivo recibido de Sucerp
    Field('archivorecibidoid', type='reference RECEPCIONARCHIVOS', ondelete='CASCADE', comment='Id Fk RECEPCIONARCHIVOS'),
    #
    # Fecha del ingreso del registro 
    Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp'),
    # 
    # Indica que fue procesado a la Db de la Matanza
    Field('procesadoDbMatanza', type='integer', required=True, comment='ProcesadoDbMatanza'),
    #
    # Referencia a la INFORMACIONVEHICULOTITULAR
    Field('infvehiculotitularid', type='reference INFORMACIONVEHICULOTITULAR', ondelete='CASCADE', comment='Id FK INFORMACIONVEHICULOTITULAR'),
    #
    # Relación de TRAMITESGENERALES
    Field('tramitesgeneralesid', type='reference TRAMITESGENERALES', ondelete='CASCADE', comment='Id FK Tramite Grales Tramites'),

```

33. TABLA **PIE**

```
    #
    # Id identificador del registro
    Field('pieid', type='id', comment='Id'),
    #
    # Constante “P0 ”
    Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
    #
    # Cantidad de cuerpos enviados
    Field('cantidadregistros', type='integer', required=True, comment='Cantidad Regsitros'),
    #
    # Hash de verificación de redundancia cíclica, 
    # la misma se calcula utilizando el algoritmo MD5 
    # sobre el contenido del archivo sin incluir el 
    # encabezado ni pie del mismo.
    Field('checksum',                 type='string', length=32,   required=True, comment='Check Sum'),
    #
    # Indica que el registro pertenece al archivo recibido de Sucerp
    Field('archivorecibidoid', type='reference RECEPCIONARCHIVOS', ondelete='CASCADE', comment='Id Fk RECEPCIONARCHIVOS'),
    #
    # Fecha del ingreso del registro 
    Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp'),
    # 
    # Indica que fue procesado a la Db de la Matanza
    Field('procesadoDbMatanza', type='integer', required=True, comment='ProcesadoDbMatanza'),

```



###### OBSERVACIONES

 1. En el schema **GXPROD** note que no podemos actualizar las tablas creadas por el proceso de instalación ya que las crea con el usuario **GXUSR**

 2. Tenemos que tener habilitada la posibilidad de utilizar el **FTP** y el **SSH** que lo utilizamos para el proceso de transferencias y generación de las tabla

 3. Solo como aclaración e **FTP** y **SSH** es el servidor que se levanta en la iseries.

 4. Las tablas que describi anteriormente se pueden ver solo por el navigator pero no se puede actualizar por que no tenemos **autorización**

 5. Por último no pude generar el programa RGPILE que es parte del proceso el cual deberia estar en la **GXPROD** 