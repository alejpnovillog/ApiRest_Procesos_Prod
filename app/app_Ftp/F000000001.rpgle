**FREE

    CTL-OPT ALWNULL(*USRCTL ) ACTGRP(*NEW) EXTBININT(*YES) ;
    // /opt/ibm/iAccessClientSolutions/acsbundle.jar
    // ANOVILLO1.PROVINCIAS
    // ANOVILLO1.TIPOCUERPO
    // ANOVILLO1.TIPOCUOTA
    // ANOVILLO1.TIPODOCUMENTO FOR SYSTEM NAME TIPOD00001
    // ANOVILLO1.TIPOESTADO
    // ANOVILLO1.TIPOMONEDA
    // ANOVILLO1.TIPOMOVIMIENTO FOR SYSTEM NAME TIPOM00001
    // ANOVILLO1.TIPOORIGEN
    // ANOVILLO1.TIPOPAGO
    // ANOVILLO1.TIPOREGISTRO
    // ANOVILLO1.TIPOSUBREGISTRO FOR SYSTEM NAME TIPOS00002
    // ANOVILLO1.TIPOTITULAR FOR SYSTEM NAME TIPOT00001

    // ANOVILLO1.ALTAIMPOSITIVA FOR SYSTEM NAME ALTAI00002
    // ANOVILLO1.ALTAIMPOSITIVATITULAR FOR SYSTEM NAME ALTAI00001

    // ANOVILLO1.ANULACIONTRAMITESSELLOS FOR SYSTEM NAME ANULA00001
    // ANOVILLO1.ANULACIONTRAMITESSELLOSDETALLE FOR SYSTEM NAME ANULA00002

    // ANOVILLO1.BAJAIMPOSITIVA FOR SYSTEM NAME BAJAI00002 WRKPFCST FILE(BAJAI00002)
    // ANOVILLO1.BAJAIMPOSITIVATITULAR FOR SYSTEM NAME BAJAI00001 WRKPFCST FILE(BAJAI00001)

    // ANOVILLO1.CAMBIOTITULARIDADTITULAR FOR SYSTEM NAME CAMBI00002 WRKPFCST FILE(CAMBI00002)
    // ANOVILLO1.CAMBIOTITULARIDAD FOR SYSTEM NAME CAMBI00003 WRKPFCST FILE(CAMBI00003)

    // ANOVILLO1.ENCABEZADO WRKPFCST FILE(ENCABEZADO)

    // ANOVILLO1.IMPUESTOSELLOS FOR SYSTEM NAME IMPUE00001
    // ANOVILLO1.IMPUESTOSELLOSPARTES FOR SYSTEM NAME IMPUE00002
    // ANOVILLO1.IMPUESTOSELLOSPARTESTIPOTRAMITE FOR SYSTEM NAME IMPUE00003

    // ANOVILLO1.IMPUESTOAUTOMOTOR FOR SYSTEM NAME IMPUE00004

    // ANOVILLO1.INFORMACIONVEHICULO FOR SYSTEM NAME INFOR00001
    // ANOVILLO1.INFORMACIONVEHICULOTITULAR FOR SYSTEM NAME INFOR00002

    // ANOVILLO1.INFORMACIORADICACION FOR SYSTEM NAME INFOR00003

    // ANOVILLO1.PIE

    // ANOVILLO1.RECEPLOG

    // ANOVILLO1.PROCESOIMPORTACIONEXPORTACION FOR SYSTEM NAME PROCE00005
    
    // ANOVILLO1.TRAMITESGENERALESTITULARES FOR SYSTEM NAME TRAMI00001
    // ANOVILLO1.TRAMITESGENERALES FOR SYSTEM NAME TRAMI00002


    //   Tabla de  Documentos de Cta.Cte.
    Dcl-f F000000001 usage(*INPUT) ;

    dcl-c int3 3; 
    dcl-c int5 5; 
    dcl-c int10 10; 
    dcl-c int20 20; 

    dcl-c zoned15 15;
    dcl-c zoned12 12;
    dcl-c zoned10 10;
    dcl-c zoned5  5;
    dcl-c decimal2 2;

    dcl-c cero 0;
    dcl-c negativo -1;
    dcl-c noexiste 100;

    dcl-c tipointeger const('int');
    dcl-c tipozoned const('zoned');
    dcl-c tipodate  const('date');
    dcl-c tipochr const('chr');

    dcl-c lenarray 50;

    dcl-c varchr1 1 ;
    dcl-c varchr2 2 ;
    dcl-c varchr3 3 ;
    dcl-c varchr4 4 ;
    dcl-c varchr5 5 ;
    dcl-c varchr8 8 ;
    dcl-c varchr10 10 ;
    dcl-c varchr15 15 ;
    dcl-c varchr19 19 ;
    dcl-c varchr20 20 ;
    dcl-c varchr32 32 ;
    dcl-c varchr40 40 ;
    dcl-c varchr50 50 ;
    dcl-c varchr60 60 ;
    dcl-c varchr100 100;    
    dcl-c varchr150 150;
    dcl-c varchr256 256;
    dcl-c varchr650 650;

    dcl-c chr1 1;
    dcl-c chr5 5;
    dcl-c chr120 120;
    dcl-c chr256 256;
    dcl-c chr650 650;
    dcl-c chr1024 1024;
    dcl-c chr2390 2390;

    dcl-c num1 1;
    dcl-c num2 2;
    dcl-c num4 4;
    dcl-c num5 5;
    dcl-c num6 6;
    dcl-c num15 15;
    dcl-c num52 52;

    dcl-c PGMGETSQLCODE const('GETSQLCODE');
    dcl-c PGMQCMDEXC const('QSYS/QCMDEXC');


    dcl-s InputString char(chr650) ;
    dcl-s Delimiter char(chr1) inz('|');
    dcl-s Values varchar(varchr650) nullind dim(lenarray);
    dcl-s Token char(chr650);
    dcl-s Count packed(num5) inz(cero);
    dcl-s ValuesInd bindec(num4:cero) dim(lenarray);

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // definimos un area de trabajo
    dcl-ds JSONData qualified;
        Registro char(chr2390);

    end-ds;

    // Obtencion de la descripcion del SQLCODE
    Dcl-PR GETSQLCODE  ExtPgm(PGMGETSQLCODE);
        *N             Char(chr5);
        *N             Char(chr1024);
    End-PR;

    // Definicion de Procedimientos
    Dcl-PR CmdExc  ExtPgm(PGMQCMDEXC);
        PaCmd          Char(chr256);
        PaLen          Packed(num15:num5);
    End-PR;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // definimos la funcion para tratar los campos tipo integer
    dcl-pr VariosType ;
      parm1 varchar(varchr650) options(*nullind);
    end-pr;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // definimos la funcion para tratar los campos tipo integer
    dcl-pr AsignaDatos ;
      parm1 pointer value;
      parm2 varchar(varchr5) value;
      parm3 int(int3) value;
      parm5 int(int10) value;
    end-pr;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // definimos la recepcion de un parametro
    dcl-pi *n  ;
      archvorecibido char(chr120);
    end-pi;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tipo indicador
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    dcl-s FindInd  bindec(num4:cero);


    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tipo integer (3)
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    // Cantidad Partes
    dcl-s cantidadpartes           int(int3)  nullind ;
    // Cantidad de registros detalle anulacion
    dcl-s cantidaddetalles         int(int3)  nullind ;
    // Cantidad Titulares
    dcl-s cantidadtitulares        int(int3)  nullind ;
    // Codigo de tipo de Tramite
    dcl-s codigotipotramite        int(int3)  nullind ;
    // Tipo Movimiento
    dcl-s codigotipomovimiento     int(int3)  nullind ;
    // Tipo Registro
    dcl-s codtiporegistro          int(int3)  nullind ;
    // Cod Forma Pago OPCIONAL
    dcl-s codigoformapago          int(int3)  nullind ;
    // Cod Moneda OPCIONAL
    dcl-s codigomoneda             int(int3)  nullind ;
    // Codigo Entidad Bancaria OPCIONAL
    dcl-s codigoentidadbancaria    int(int3)  nullind ;
    // Codigo Tipo Accion
    dcl-s codigotipoaccion         int(int3)  nullind ;
    // Numero de Cuota
    dcl-s numerocuota              int(int3)  nullind ;
    // Porcentaje Titular
    dcl-s porcentajetitularidad    int(int3)  nullind ;
    // Provincia
    dcl-s provincia                int(int3)  nullind ;
    // Tipo Interviniente
    dcl-s tipointerviniente        int(int3)  nullind ;
    // Tipo Cuota
    dcl-s tipocuota                int(int3)  nullind ;
    // Tipo Documento
    dcl-s tipodocumento            int(int3)  nullind ;
    // Tipo Formulario
    dcl-s tipoformulario           int(int3)  nullind ;
    // Numero del campo del formato
    dcl-s numerocampo              int(int3);

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tipo integer (int10)
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    // Cantidad de registros
    dcl-s cantidadregistros        int(int10) nullind ;
    // Carga OPCIONAL
    dcl-s carga                    int(int10) nullind ;
    // Cilindrada OPCIONAL
    dcl-s cilindrada               int(int10) nullind ;
    // Codigo Registro  Nacional
    dcl-s codigoregistronacional   int(int10) nullind ;
    // Codigo Organismo
    dcl-s codigoorganismo          int(int10) nullind ;
    // Codigo Registro Seccional
    dcl-s codigoregistroseccional  int(int10) nullind ;
    // Nro Formulario
    dcl-s numeroformulario         int(int10) nullind ;
    // Número del comprobante entregado por el
    dcl-s numerorecibo             int(int10) nullind ;
    // Peso OPCIONAL
    dcl-s peso                     int(int10) nullind ;
    // Registro Seccion Origen
    dcl-s registroseccionalorigen  int(int10) nullind ;
    // Registro Seccional Destino
    dcl-s registroseccionaldestino int(int10) nullind ;
    // Valuacion
    dcl-s valuacion                int(int10) nullind ;
    // Año fiscal
    dcl-s yyyy                     int(int10) nullind ;
    // Año Modelo
    dcl-s yyyymodelo               int(int10) nullind ;
    // tiporegistroid
    dcl-s tiporegistroid           int(int10) nullind ;
    // tiposubregistroid
    dcl-s tiposubregistroid        int(int10) nullind ;
    // origenid
    dcl-s origenid                 int(int10) nullind ;
    // tipodocumentoid
    dcl-s tipodocumentoid          int(int10) nullind ;
    // provinciaid
    dcl-s provinciaid              int(int10) nullind ;
    // tipocuerpoid
    dcl-s tipocuerpoid             int(int10) nullind ;
    // tipocuotaid
    dcl-s tipocuotaid              int(int10) nullind ;
    // codigomonedaid
    dcl-s codigomonedaid           int(int10) nullind ;
    // codigotipomovimientoid
    dcl-s codigotipomovimientoid   int(int10) nullind ;
    // tipotitularid
    dcl-s tipotitularid            int(int10) nullind ;
    // codigoformapagoid
    dcl-s codigoformapagoid        int(int10) nullind ;
    // Id ALTAIMPOSITIVATITULAR
    dcl-s altataxtitularid         int(int10) nullind ;
    // Id ALTAIMPOSITIVA
    dcl-s altataxid                int(int10) nullind ;
    // Id BAJAIMPOSITIVATITULAR
    dcl-s bajataxtitularid         int(int10) nullind ;
    // Id BAJAIMPOSITIVA
    dcl-s bajataxid                int(int10) nullind ;
    // Id INFORMACIONVEHICULO
    dcl-s infvehiculoid            int(int10) nullind ;
    // Id INFORMACIONVEHICULOTITULAR
    dcl-s infvehiculotitularid     int(int10) nullind ;
    // Id CAMBIOTITULARIDAD
    dcl-s cambiotitularidadid      int(int10) nullind;
    // Id CAMBIOTITULARIDADTITULAR
    dcl-s cambiotitularidadtitid   int(int10) nullind;
    // INFORMACIORADICACION
    dcl-s infradicacionid          int(int10) nullind;
    // ANULACIONTRAMITESSELLOS
    dcl-s anultramitesellosid      int(int10) nullind;
    // ANULACIONTRAMITESSELLOSDETALLE
    dcl-s anultramitesellosdetid   int(int10) nullind;
    // TRAMITESGENERALES
    dcl-s tramitesgeneralesid      int(int10) nullind;
    // TRAMITESGENERALESTITULARES
    dcl-s tramitesgeneralestitid   int(int10) nullind;
    // PIE
    dcl-s pieid                    int(int10) nullind;
    // IMPUESTOSELLOS
    dcl-s taxsellosid              int(int10) nullind;
    // IMPUESTOSELLOSPARTES
    dcl-s taxsellospartesid        int(int10) nullind;
    // IMPUESTOSELLOSPARTESTIPOTRAMITE
    dcl-s taxsellospartestipotramiteid int(int10) nullind ;

    dcl-s taxautomotorid           int(int10) nullind;
    dcl-s encabezadoid             int(int10) nullind;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tipo integer (int20)
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    // Numero de Tramite OPCIONAL
    dcl-s numerotramite            int(int20) nullind ;
    // Nro Envio
    dcl-s numeroenvio              int(int20) nullind ;
    // Nro Documento
    dcl-s numerodocumento          int(int20) nullind ;
    // Cuit/Cuil
    dcl-s cuitcuil                 int(int20) nullind ;
    // Cuit Registro Seccional
    dcl-s cuitregistroseccional    int(int20) nullind ;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tipo character (1)
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    // Estado Dominial
    dcl-s estadodominial                     varchar(varchr1) nullind ;
    // Execcion
    dcl-s exencion                           varchar(varchr1) nullind ;
    // Estado de la radicación del vehículo (A = Activa,
    dcl-s estado                             varchar(varchr1) nullind ;
    // Flag Vencimiento
    dcl-s flagvencimiento                    varchar(varchr1) nullind ;
    // Guarda Habitual
    dcl-s guardahabitual                     varchar(varchr1) nullind ;
    // Determina de donde proviene la información del
    dcl-s origeninformacion                  varchar(varchr1) nullind ;
    // Tipo Origen Vehiculo
    dcl-s origen                             varchar(varchr1) nullind ;
    // Determina el tipo de anulación, puede ser un
    dcl-s tipoanulacion                      varchar(varchr1) nullind ;
    // Determina el tipo de titular transferido.
    dcl-s tipotitular                        varchar(varchr1) nullind ;
    // Tipo de la radicación (D - Definitiva, P -
    dcl-s tipo                               varchar(varchr1) nullind ;
    // Tipo se Sub Registro
    dcl-s tiposubregistro                    varchar(varchr1) nullind ;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tipo character (2)
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    // Codigo Tipo Uso
    dcl-s codigotipouso                      varchar(varchr2) nullind ;
    // Tipo de Registro
    dcl-s tiporegistro                       varchar(varchr2) nullind ;
    // Tipo de Cuerpo
    dcl-s tipocuerpo                         varchar(varchr2) nullind ;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tipo character (3)
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    // Categoria OPCIONAL
    dcl-s categoria                          varchar(varchr3) nullind ;
    // Categoria controlsucerp
    dcl-s controlsucerp                      varchar(varchr3) nullind ;
    // formato procesado para el log
    dcl-s formato                            varchar(varchr4) ;


     // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tipo character (5)
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    // Version Protocolo
    dcl-s versionprtocolo                    varchar(varchr5) nullind ;
    // Revision Protocolo
    dcl-s revisionprotocolo                  varchar(varchr5) nullind ;

     // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tipo character (8)
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    // Codigo Sucerp
    dcl-s codigomtmfmm                       varchar(varchr8) nullind ;
    // Codigo Postal
    dcl-s codigopostal                       varchar(varchr8) nullind ;
    // Dominio Nuevo
    dcl-s dominionuevo                       varchar(varchr8) nullind ;
    // Dominio Viejo
    dcl-s dominioviejo                       varchar(varchr8) nullind ;
    // Petente del vehiculo
    dcl-s dominio                            varchar(varchr8) nullind ;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tipo character (int10)
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    // Codigo Execcion OPCIONAL
    dcl-s codigoexencion                     varchar(varchr10) nullind ;
    // Depto OPCIONAL
    dcl-s departamento                       varchar(varchr10) nullind ;
    // Nro Puerta
    dcl-s numero                             varchar(varchr10) nullind ;
    // Piso OPCIONAL
    dcl-s piso                               varchar(varchr10) nullind ;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tipo character (19)
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    // Fecha Transferencia OPCIONAL
    dcl-s fechatransferencia                 varchar(varchr19) nullind ;
    // Fecha Proceso
    dcl-s fechaproceso                       varchar(varchr19) nullind ;
    // Fecha Contrato
    dcl-s fechacontrato                      varchar(varchr19) nullind ;
    // fecha Deposito OPCIONAL
    dcl-s fechadeposito                      varchar(varchr19) nullind ;
    // Fecha Hora
    dcl-s fechahora                          varchar(varchr19) nullind ;
    // Fecha Operacion
    dcl-s fechaoperacion                     varchar(varchr19) nullind ;
    // Fecha Cobro OPCIONAL
    dcl-s fechacobro                         varchar(varchr19) nullind ;
    // Fecha Tramite OPCIONAL
    dcl-s fechatramite                       varchar(varchr19) nullind ;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tipo character (15)
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    // recibo que da Registro Seccional OPCIONAL
    dcl-s recibo                             varchar(varchr15) nullind ;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tipo character (int20)
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    // Nro Cheque OPCIONAL
    dcl-s numerocheque                       varchar(varchr20) nullind ;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tipo character (32)
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    // Hash de verificación de redundancia cíclica, la
    dcl-s checksum                           varchar(varchr32) nullind ;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tipo character (40)
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    // Localidad
    dcl-s localidad                          varchar(varchr40) nullind ;
    // Descr Registro Seccional OPCIONAL
    dcl-s descrregistroseccional             varchar(varchr40) nullind ;
    // Calle
    dcl-s calle                              varchar(varchr40) nullind ;
    // Barrio OPCIONAL
    dcl-s barrio                             varchar(varchr40) nullind ;
    // Raz Soc Reg Seccional Origen OPCIONAL
    dcl-s razonsocialregistroseccional       varchar(varchr40) nullind ;
    // Raz. Soc. Reg. Seccional  Destino OPTIONAL
    dcl-s razonsocialregistroseccionaldest   varchar(varchr40) nullind ;
    // Raz Soc Reg Seccional Origen OPCIONAL
    dcl-s razonsocialregistroseccionalorigen varchar(varchr40) nullind ;
    // Razon Social
    dcl-s razonsocial                        varchar(varchr40) nullind ;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tipo character (60)
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    // Descr Tipo Tramite OPCIONAL
    dcl-s descrtipotramite                   varchar(varchr60) nullind ;
    // Descr Entidad Bancaria OPCIONAL
    dcl-s descrentidadbancaria               varchar(varchr60) nullind ;
    // Descr Tipo Interviniente
    dcl-s descrtipointerviniente             varchar(varchr60) nullind ;
    // Descripcion de tipo de Tramite
    dcl-s dscrtipotramite                    varchar(varchr60) nullind ;
    // Descr Tipo Accion
    dcl-s descrtipoaccion                    varchar(varchr60) nullind ;
    // Marca
    dcl-s marca                              varchar(varchr60) nullind ;
    // Tipo Vehiculo
    dcl-s tipovehiculo                       varchar(varchr60) nullind ;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tipo character (100)
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    // Descr Execcion OPCIONAL
    dcl-s descripcionexencion                varchar(varchr100) nullind ;
    // Descr Tipo Uso
    dcl-s descrtipouso                       varchar(varchr100) nullind ;
    // Modelo
    dcl-s modelo                             varchar(varchr100) nullind ;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tipo character (150)
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    // Apellido y Nombre OPCIONAL
    dcl-s apellidonombre                     varchar(varchr150) nullind ;
    // ApeNom Razon Social
    dcl-s apenomrazonsocial                  varchar(varchr150) nullind ;
    // Muni. Destino OPCIONAL
    dcl-s municipalidaddestino               varchar(varchr150) nullind ;
    // Municipalidad Origen OPCIONAL
    dcl-s municipalidadorigen                varchar(varchr150) nullind ;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tipo character (256)
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    // Observaciones OPCIONAL
    dcl-s observaciones                      varchar(varchr256) nullind ;
    // Observaciones Anulacion OPCIONAL
    dcl-s observacionesanulacion             varchar(varchr256) nullind ;
    // Reservado OPCIONAL
    dcl-s reservado                          varchar(varchr256) nullind ;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tipo character (650)
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    // Parm Adicionales OPCIONAL
    dcl-s parametrosadicionales              varchar(varchr650) nullind ;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Definiciones date

    // Fecha alta en la juridisccion
    dcl-s fechaalta                          date nullind ;
    // Fecha baja en la jurisdiccion
    dcl-s fechabaja                          date nullind ;
    // Fecha Bonificacion
    dcl-s fechabonificacion                  date nullind ;
    // Fecha Vencimiento
    dcl-s fechavencimiento                   date nullind ;
    // Fecha vigencia contrato
    dcl-s fechavigenciacontrato              date nullind ;
    // Fecha Inscripcion Inicial
    dcl-s fechainscripcioninicial            date nullind ;
    // Fecha Ultima Transferencia
    dcl-s fechaultimatransferencia           date nullind ;
    // Fecha Ultimo Movimiento
    dcl-s fechaultimomovimiento              date nullind ;
    // Fecha Vigencia
    dcl-s fechavigencia                      date nullind ;
    // Fecha Cambiio Estado Dominial
    dcl-s fechacambioestadodominial          date nullind ;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Definiciones zoned

    // Alicuota
    dcl-s alicuota                           zoned(zoned5:decimal2) nullind ;
    // Base Imponible
    dcl-s baseimponible                      zoned(zoned12:decimal2) nullind ;
    // Importe Adicional
    dcl-s importeadicional                   zoned(zoned12:decimal2) nullind ;
    // Importe Bonificado
    dcl-s importebonificado                  zoned(zoned10:decimal2) nullind ;
    // Importe Comun
    dcl-s importecomun                       zoned(zoned10:decimal2) nullind ;
    // Importe Total OPCIONAL
    dcl-s importetotal                       zoned(zoned10:decimal2) nullind ;
    // Importe Impuesto OPCIONAL
    dcl-s importeimpuesto                    zoned(zoned10:decimal2) nullind ;
    // Importe Punitorio OPCIONAL
    dcl-s importepunitorio                   zoned(zoned10:decimal2) nullind ;
    // Monto Impuesto Adicional
    dcl-s montoimpuestoadicional             zoned(zoned12:decimal2) nullind ;
    // Monto Impuesto
    dcl-s montoimpuesto                      zoned(zoned12:decimal2) nullind ;
    // Monto Punitorios
    dcl-s montopunitorios                    zoned(zoned12:decimal2) nullind ;
    // Monto Total Cobrado
    dcl-s montototalcobrado                  zoned(zoned12:decimal2) nullind ;
    // Monto Abonado
    dcl-s montoabonado                       zoned(zoned12:decimal2) nullind ;
    // Monto Contrato
    dcl-s montocontrato                      zoned(zoned12:decimal2) nullind ;
    // Monto Abonado Fuera Registro
    dcl-s montofueraregistro                 zoned(zoned12:decimal2) nullind ;
    // Monto Adicional
    dcl-s montoadicional                     zoned(zoned12:decimal2) nullind ;
    // Porcentaje Contrato
    dcl-s porcentajecontrato                 zoned(zoned5:decimal2) nullind ;
    // Porcentaje Impuesto
    dcl-s porcentajeimpuesto                 zoned(zoned5:decimal2) nullind ;
    // Key TimeStamp
    dcl-s ktimestamp timestamp ;


    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Definimos la estructura para Indicadores
    dcl-ds Ind qualified;

      Ind001  like(FindInd) ;
      Ind002  like(FindInd) ;
      Ind003  like(FindInd) ;
      Ind004  like(FindInd) ;
      Ind005  like(FindInd) ;
      Ind006  like(FindInd) ;
      Ind007  like(FindInd) ;
      Ind008  like(FindInd) ;
      Ind009  like(FindInd) ;
      Ind010  like(FindInd) ;
      Ind011  like(FindInd) ;
      Ind012  like(FindInd) ;
      Ind013  like(FindInd) ;
      Ind014  like(FindInd) ;
      Ind015  like(FindInd) ;
      Ind016  like(FindInd) ;
      Ind017  like(FindInd) ;
      Ind018  like(FindInd) ;
      Ind019  like(FindInd) ;
      Ind020  like(FindInd) ;
      Ind021  like(FindInd) ;
      Ind022  like(FindInd) ;
      Ind023  like(FindInd) ;
      Ind024  like(FindInd) ;
      Ind025  like(FindInd) ;
      Ind026  like(FindInd) ;
      Ind027  like(FindInd) ;
      Ind028  like(FindInd) ;
      Ind029  like(FindInd) ;
      Ind030  like(FindInd) ;
      Ind031  like(FindInd) ;
      Ind032  like(FindInd) ;
      Ind033  like(FindInd) ;
      Ind034  like(FindInd) ;
      Ind035  like(FindInd) ;
      Ind036  like(FindInd) ;
      Ind037  like(FindInd) ;
      Ind038  like(FindInd) ;
      Ind039  like(FindInd) ;
      Ind040  like(FindInd) ;
      Ind041  like(FindInd) ;
      Ind042  like(FindInd) ;
      Ind043  like(FindInd) ;
      Ind044  like(FindInd) ;
      Ind045  like(FindInd) ;
      Ind046  like(FindInd) ;
      Ind047  like(FindInd) ;
      Ind048  like(FindInd) ;
      Ind049  like(FindInd) ;
      Ind050  like(FindInd) ;
      IndMaster like(FindInd) pos(num1)   dim(lenarray);

    end-ds;



    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Definimos la estructura para E0 ENCABEZADO
    dcl-ds fE0 qualified;

      tiporegistro           like(tiporegistro) nullind ;
      versionprtocolo        like(versionprtocolo) nullind ;
      revisionprotocolo      like(revisionprotocolo) nullind ;
      codigoorganismo        like(codigoorganismo) nullind ;
      numeroenvio            like(numeroenvio) nullind ;
      fechahora              like(fechahora) nullind ;
      ktimestamp             like(ktimestamp) nullind ;

    end-ds;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Definimos la estructura para C1-C ALTAIMPOSITIVA
    dcl-ds fC1C qualified;

      tiporegistro             like(tiporegistro) nullind ;
      tiposubregistro          like(tiposubregistro) nullind ;
      codigoorganismo          like(codigoorganismo) nullind ;
      numerotramite            like(numerotramite) nullind ;
      codigotipotramite        like(codigotipotramite) nullind ;
      dscrtipotramite          like(dscrtipotramite) nullind ;
      codigotipoaccion         like(codigotipoaccion) nullind ;
      descrtipoaccion          like(descrtipoaccion) nullind ;
      tipoformulario           like(tipoformulario) nullind ;
      numeroformulario         like(numeroformulario) nullind ;
      dominionuevo             like(dominionuevo) nullind ;
      dominioviejo             like(dominioviejo) nullind ;
      codigomtmfmm             like(codigomtmfmm) nullind ;
      origen                   like(origen) nullind ;
      categoria                like(categoria) nullind ;
      marca                    like(marca) nullind ;
      tipovehiculo             like(tipovehiculo) nullind ;
      modelo                   like(modelo) nullind ;
      yyyymodelo               like(yyyymodelo) nullind ;
      peso                     like(peso) nullind ;
      carga                    like(carga) nullind ;
      cilindrada               like(cilindrada) nullind ;
      valuacion                like(valuacion) nullind ;
      codigotipouso            like(codigotipouso) nullind ;
      descrtipouso             like(descrtipouso) nullind ;
      fechavigencia            like(fechavigencia) nullind ;
      tipodocumento            like(tipodocumento) nullind ;
      numerodocumento          like(numerodocumento) nullind ;
      cuitcuil                 like(cuitcuil) nullind ;
      apenomrazonsocial        like(apenomrazonsocial) nullind;
      calle                    like(calle) nullind ;
      numero                   like(numero) nullind ;
      piso                     like(piso) nullind ;
      departamento             like(departamento) nullind ;
      barrio                   like(barrio) nullind ;
      localidad                like(localidad) nullind ;
      codigopostal             like(codigopostal) nullind ;
      provincia                like(provincia) nullind ;
      cantidadtitulares        like(cantidadtitulares) nullind;
      codigoregistroseccional  like(codigoregistroseccional) nullind;
      razonsocial              like(razonsocial) nullind ;
      registroseccionalorigen  like(registroseccionalorigen) nullind ;
      razonsocialregistroseccionalo...
                    rigen like(razonsocialregistroseccionalorigen) nullind ;

      municipalidadorigen      like(municipalidadorigen) nullind ;
      fechaoperacion           like(fechaoperacion) nullind ;
      parametrosadicionales    like(parametrosadicionales) nullind;
      reservado                like(reservado) nullind ;
      observaciones            like(observaciones) nullind ;
      ktimestamp               like(ktimestamp) nullind ;

    end-ds;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Definimos la estructura para C1-T ALTAIMPOSITIVATITULAR
    dcl-ds fC1T qualified;

      tipocuerpo             like(tipocuerpo) nullind ;
      tiposubregistro        like(tiposubregistro) nullind ;
      tipodocumento          like(tipodocumento) nullind ;
      numerodocumento        like(numerodocumento) nullind ;
      cuitcuil               like(cuitcuil) nullind ;
      apenomrazonsocial      like(apenomrazonsocial) nullind ;
      porcentajetitularidad  like(porcentajetitularidad) nullind ;
      calle                  like(calle) nullind ;
      numero                 like(numero) nullind ;
      piso                   like(piso) nullind ;
      departamento           like(departamento) nullind ;
      barrio                 like(barrio) nullind ;
      localidad              like(localidad) nullind;
      codigopostal           like(codigopostal) nullind;
      provincia              like(provincia) nullind;
      reservado              like(reservado) nullind;
      ktimestamp             like(ktimestamp) nullind;

    end-ds ;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Definimos la estructura para C2-C BAJAIMPOSITIVA
    dcl-ds fC2C qualified;

      tiporegistro           like(tiporegistro) nullind ;
      tiposubregistro        like(tiposubregistro) nullind ;
      codigoorganismo        like(codigoorganismo) nullind ;
      numerotramite          like(numerotramite) nullind ;
      codigotipotramite      like(codigotipotramite) nullind ;
      dscrtipotramite        like(dscrtipotramite) nullind ;
      codigotipoaccion       like(codigotipoaccion) nullind ;
      descrtipoaccion        like(descrtipoaccion) nullind ;
      tipoformulario         like(tipoformulario) nullind ;
      numeroformulario       like(numeroformulario) nullind ;
      dominionuevo           like(dominionuevo) nullind ;
      dominioviejo           like(dominioviejo) nullind ;
      codigomtmfmm           like(codigomtmfmm) nullind ;
      origen                 like(origen) nullind ;
      categoria              like(categoria) nullind ;
      marca                  like(marca) nullind ;
      tipovehiculo           like(tipovehiculo) nullind ;
      modelo                 like(modelo) nullind ;
      yyyymodelo             like(yyyymodelo) nullind ;
      peso                   like(peso) nullind ;
      carga                  like(carga) nullind ;
      cilindrada             like(cilindrada) nullind ;
      valuacion              like(valuacion) nullind ;
      codigotipouso          like(codigotipouso) nullind ;
      descrtipouso           like(descrtipouso) nullind ;
      fechavigencia          like(fechavigencia) nullind ;
      cantidadtitulares      like(cantidadtitulares) nullind ;
      codigoregistronacional like(codigoregistronacional) nullind ;
      razonsocial            like(razonsocial) nullind ;
      registroseccionaldestino like(registroseccionaldestino) nullind ;
      razonsocialregistroseccio...
                naldest like(razonsocialregistroseccionaldest) nullind ;
      municipalidaddestino   like(municipalidaddestino) nullind ;
      fechaoperacion         like(fechaoperacion) nullind ;
      parametrosadicionales  like(parametrosadicionales) nullind ;
      reservado              like(reservado) nullind ;
      observaciones          like(observaciones) nullind ;
      ktimestamp             like(ktimestamp) nullind ;

    end-ds;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Definimos la estructura para C2-T BAJAIMPOSITIVATITULAR
    dcl-ds fC2T qualified;

      tipocuerpo             like(tipocuerpo) nullind ;
      tiposubregistro        like(tiposubregistro) nullind ;
      tipodocumento          like(tipodocumento) nullind ;
      numerodocumento        like(numerodocumento) nullind ;
      cuitcuil               like(cuitcuil) nullind ;
      apenomrazonsocial      like(apenomrazonsocial) nullind ;
      porcentajetitularidad  like(porcentajetitularidad) nullind ;
      calle                  like(calle) nullind ;
      numero                 like(numero) nullind ;
      piso                   like(piso) nullind ;
      departamento           like(departamento) nullind ;
      barrio                 like(barrio) nullind ;
      localidad              like(localidad) nullind ;
      codigopostal           like(codigopostal) nullind ;
      provincia              like(provincia) nullind ;
      reservado              like(reservado) nullind ;
      ktimestamp             like(ktimestamp) nullind ;

    end-ds;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Definimos la estructura para C3-C IMPUESTOSELLOS
    dcl-ds fC3C qualified;

      tiporegistro           like(tiporegistro) nullind ;
      tiposubregistro        like(tiposubregistro) nullind ;
      codigoorganismo        like(codigoorganismo) nullind ;
      numerotramite          like(numerotramite) nullind ;
      codigotipoaccion       like(codigotipoaccion) nullind ;
      descrtipoaccion        like(descrtipoaccion) nullind ;
      tipoformulario         like(tipoformulario) nullind ;
      numeroformulario       like(numeroformulario) nullind ;
      dominionuevo           like(dominionuevo) nullind ;
      dominioviejo           like(dominioviejo) nullind ;
      recibo                 like(recibo) nullind ;
      codigomtmfmm           like(codigomtmfmm) nullind ;
      origen                 like(origen) nullind ;
      categoria              like(categoria) nullind ;
      marca                  like(marca) nullind ;
      tipovehiculo           like(tipovehiculo) nullind ;
      modelo                 like(modelo)  nullind ;
      yyyymodelo             like(yyyymodelo) nullind ;
      codigotipouso          like(codigotipouso) nullind ;
      descrtipouso           like(descrtipouso) nullind ;
      valuacion              like(valuacion) nullind ;
      cantidadpartes         like(cantidadpartes) nullind ;
      montoimpuestoadicional like(montoimpuestoadicional) nullind ;
      montopunitorios        like(montopunitorios) nullind ;
      montototalcobrado      like(montototalcobrado) nullind ;
      montoabonado           like(montoabonado) nullind ;
      codigoformapago        like(codigoformapago) nullind ;
      codigomoneda           like(codigomoneda) nullind ;
      codigoentidadbancaria  like(codigoentidadbancaria) nullind ;
      descrentidadbancaria   like(descrentidadbancaria) nullind ;
      numerocheque           like(numerocheque) nullind ;
      exencion               like(exencion) nullind ;
      codigoexencion         like(codigoexencion) nullind ;
      descripcionexencion    like(descripcionexencion) nullind ;
      fechadeposito          like(fechadeposito) nullind ;
      codigoregistroseccional like(codigoregistroseccional) nullind ;
      cuitregistroseccional  like(cuitregistroseccional) nullind ;
      razonsocial            like(razonsocial) nullind ;
      fechaoperacion         like(fechaoperacion) nullind ;
      parametrosadicionales  like(parametrosadicionales) nullind ;
      reservado              like(reservado) nullind ;
      observaciones          like(observaciones) nullind ;
      observacionesanulacion like(observacionesanulacion) nullind ;
      ktimestamp             like(ktimestamp) nullind ;

    end-ds;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Definimos la estructura para C3-P IMPUESTOSELLOSPARTES
    dcl-ds fC3P qualified;

      tipocuerpo             like(tipocuerpo) nullind ;
      tiposubregistro        like(tiposubregistro) nullind ;
      tipointerviniente      like(tipointerviniente) nullind ;
      descrtipointerviniente like(descrtipointerviniente) nullind ;
      tipodocumento          like(tipodocumento) nullind ;
      numerodocumento        like(numerodocumento) nullind ;
      cuitcuil               like(cuitcuil) nullind ;
      apellidonombre         like(apellidonombre) nullind ;
      porcentajetitularidad  like(porcentajetitularidad) nullind ;
      calle                  like(calle) nullind ;
      numero                 like(numero) nullind ;
      piso                   like(piso) nullind ;
      departamento           like(departamento) nullind ;
      barrio                 like(barrio) nullind ;
      localidad              like(localidad) nullind ;
      codigopostal           like(codigopostal) nullind ;
      provincia              like(provincia) nullind ;
      exencion               like(exencion) nullind ;
      codigoexencion         like(codigoexencion) nullind ;
      descripcionexencion    like(descripcionexencion) nullind ;
      codigotipotramite      like(codigotipotramite) nullind ;
      descrtipotramite       like(descrtipotramite) nullind ;
      reservado              like(reservado) nullind ;
      ktimestamp             like(ktimestamp) nullind ;

    end-ds;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Definimos la estructura para C3-T  IMPUESTOSELLOSPARTESTIPOTRAMITE
    // DESCRIPCION DEL CAMPO RESERVADO DE LA ESTRUCTURA
    // 1-2 Exención objetiva Char(1) Determina si tiene exención objetiva (S o N)
    // 3-18 Código de exención Char(15) Código de exención
    // 19-20 Celebración instrumento Char(1) Determina el lugar de celebración del
    //                                      instrumento (D = Dentro de la provincia, F =
    //                                      Fuera de la provincia).
    // 20-21 Dispone de factura Char(1) Establece si dispone de factura o no (S o N).
    // 22-23 Inscripto en IIBB Char(1) Establece si el vendedor se encuentra inscripto
    //                                en Ingresos Brutos de la jurisdicción (S o N).
    // 24-36 Importe de multa zoned(zoned12:decimal2) Determina que monto del punitorio es la multa
    //                                   por el pago fuera del vencimiento.

    dcl-ds fC3T qualified;

      tipocuerpo             like(tipocuerpo) nullind ;
      tiposubregistro        like(tiposubregistro) nullind ;
      codigotipotramite      like(codigotipotramite) nullind ;
      descrtipotramite       like(descrtipotramite) nullind ;
      montocontrato          like(montocontrato) nullind ;
      baseimponible          like(baseimponible) nullind ;
      montoimpuesto          like(montoimpuesto) nullind ;
      montopunitorios        like(montopunitorios) nullind ;
      montofueraregistro     like(montofueraregistro) nullind ;
      montoadicional         like(montoadicional) nullind ;
      alicuota               like(alicuota) nullind ;
      porcentajecontrato     like(porcentajecontrato) nullind ;
      porcentajeimpuesto     like(porcentajeimpuesto) nullind ;
      fechacontrato          like(fechacontrato) nullind ;
      reservado              like(reservado) nullind ;
      ktimestamp             like(ktimestamp) nullind ;

    end-ds;


    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Definimos la estructura para C4 IMPUESTOAUTOMOTOR
    dcl-ds fC4 qualified;

      tiporegistro           like(tiporegistro) nullind ;
      codigoorganismo        like(codigoorganismo) nullind ;
      numerotramite          like(numerotramite) nullind ;
      codigotipomovimiento   like(codigotipomovimiento) nullind ;
      codtiporegistro        like(codtiporegistro) nullind ;
      dominionuevo           like(dominionuevo) nullind ;
      dominioviejo           like(dominioviejo) nullind ;
      yyyy                   like(yyyy) nullind ;
      numerocuota            like(numerocuota) nullind ;
      fechabonificacion      like(fechabonificacion) nullind ;
      fechavencimiento       like(fechavencimiento) nullind ;
      flagvencimiento        like(flagvencimiento) nullind ;
      importebonificado      like(importebonificado) nullind ;
      importecomun           like(importecomun) nullind ;
      fechaproceso           like(fechaproceso) nullind ;
      importetotal           like(importetotal) nullind ;
      importeimpuesto        like(importeimpuesto) nullind ;
      importepunitorio       like(importepunitorio) nullind ;
      codigoformapago        like(codigoformapago) nullind ;
      codigomoneda           like(codigomoneda) nullind ;
      codigoentidadbancaria  like(codigoentidadbancaria) nullind ;
      descrentidadbancaria   like(descrentidadbancaria) nullind ;
      numerocheque           like(numerocheque) nullind ;
      fechacobro             like(fechacobro) nullind ;
      fechatransferencia     like(fechatransferencia) nullind ;
      codigoregistroseccional like(codigoregistroseccional) nullind ;
      descrregistroseccional like(descrregistroseccional) nullind ;
      reservado              like(reservado) nullind ;
      observaciones          like(observaciones) nullind ;
      ktimestamp             like(ktimestamp) nullind ;

    end-ds;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Definimos la estructura para C5-C INFORMACIONVEHICULO
    dcl-ds fC5C qualified;

      tiporegistro           like(tiporegistro) nullind ;
      tiposubregistro        like(tiposubregistro) nullind ;
      codigoorganismo        like(codigoorganismo) nullind ;
      dominionuevo           like(dominionuevo) nullind ;
      dominioviejo           like(dominioviejo) nullind ;
      codigomtmfmm           like(codigomtmfmm) nullind ;
      origen                 like(origen) nullind ;
      categoria              like(categoria) nullind ;
      marca                  like(marca) nullind ;
      tipovehiculo           like(tipovehiculo) nullind ;
      modelo                 like(modelo) nullind ;
      yyyymodelo             like(yyyymodelo) nullind ;
      peso                   like(peso) nullind ;
      carga                  like(carga) nullind ;
      cilindrada             like(cilindrada) nullind ;
      valuacion              like(valuacion) nullind ;
      codigotipouso          like(codigotipouso) nullind ;
      descrtipouso           like(descrtipouso) nullind ;
      fechainscripcioninicial like(fechainscripcioninicial) nullind ;
      fechaultimatransferencia like(fechaultimatransferencia) nullind ;
      fechaultimomovimiento   like(fechaultimomovimiento) nullind ;
      estadodominial          like(estadodominial) nullind ;
      fechacambioestadodominial like(fechacambioestadodominial) nullind ;
      guardahabitual         like(guardahabitual) nullind ;
      calle                  like(calle) nullind ;
      numero                 like(numero) nullind ;
      piso                   like(piso) nullind ;
      departamento           like(departamento) nullind ;
      barrio                 like(barrio) nullind ;
      localidad              like(localidad) nullind ;
      codigopostal           like(codigopostal) nullind ;
      provincia              like(provincia) nullind ;
      cantidadtitulares      like(cantidadtitulares) nullind ;
      codigoregistroseccional like(codigoregistroseccional) nullind ;
      razonsocial            like(razonsocial) nullind ;
      fechaoperacion         like(fechaoperacion) nullind ;
      reservado              like(reservado) nullind ;
      controlsucerp          like(controlsucerp) nullind ;
      ktimestamp             like(ktimestamp) nullind ;

    end-ds;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Definimos la estructura para C5-T INFORMACIONVEHICULOTITULAR
    dcl-ds fC5T qualified;

      tipocuerpo             like(tipocuerpo) nullind ;
      tiposubregistro        like(tiposubregistro) nullind ;
      tipodocumento          like(tipodocumento) nullind ;
      numerodocumento        like(numerodocumento) nullind ;
      cuitcuil               like(cuitcuil) nullind ;
      apellidonombre         like(apellidonombre) nullind ;
      porcentajetitularidad  like(porcentajetitularidad) nullind ;
      calle                  like(calle) nullind ;
      numero                 like(numero) nullind ;
      piso                   like(piso) nullind ;
      departamento           like(departamento) nullind ;
      barrio                 like(barrio) nullind ;
      localidad              like(localidad) nullind ;
      codigopostal           like(codigopostal) nullind ;
      provincia              like(provincia) nullind ;
      reservado              like(reservado) nullind ;
      ktimestamp             like(ktimestamp) nullind ;

    end-ds;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Definimos la estructura para C6-C CAMBIOTITULARIDAD
    dcl-ds fC6C qualified;

      tiporegistro           like(tiporegistro) nullind ;
      tiposubregistro        like(tiposubregistro) nullind ;
      codigoorganismo        like(codigoorganismo) nullind ;
      numerotramite          like(numerotramite) nullind ;
      codigotipotramite      like(codigotipotramite) nullind ;
      dscrtipotramite        like(dscrtipotramite) nullind ;
      codigotipoaccion       like(codigotipoaccion) nullind ;
      descrtipoaccion        like(descrtipoaccion) nullind ;
      tipoformulario         like(tipoformulario) nullind ;
      numeroformulario       like(numeroformulario) nullind ;
      dominionuevo           like(dominionuevo) nullind ;
      dominioviejo           like(dominioviejo) nullind ;
      codigomtmfmm           like(codigomtmfmm) nullind ;
      origen                 like(origen) nullind ;
      categoria              like(categoria) nullind ;
      marca                  like(marca) nullind ;
      tipovehiculo           like(tipovehiculo) nullind ;
      modelo                 like(modelo) nullind ;
      yyyymodelo             like(yyyymodelo) nullind ;
      peso                   like(peso) nullind ;
      carga                  like(carga) nullind ;
      cilindrada             like(cilindrada) nullind ;
      valuacion              like(valuacion) nullind ;
      codigotipouso          like(codigotipouso) nullind ;
      descrtipouso           like(descrtipouso) nullind ;
      fechavigencia          like(fechavigencia) nullind ;
      tipodocumento          like(tipodocumento) nullind ;
      numerodocumento        like(numerodocumento) nullind ;
      cuitcuil               like(cuitcuil) nullind ;
      apellidonombre         like(apellidonombre) nullind ;
      calle                  like(calle) nullind ;
      numero                 like(numero) nullind ;
      piso                   like(piso) nullind ;
      departamento           like(departamento) nullind ;
      barrio                 like(barrio) nullind ;
      localidad              like(localidad) nullind ;
      codigopostal           like(codigopostal) nullind ;
      provincia              like(provincia) nullind ;
      cantidadtitulares      like(cantidadtitulares) nullind ;
      codigoregistroseccional like(codigoregistroseccional) nullind ;
      razonsocial            like(razonsocial) nullind ;
      fechaoperacion         like(fechaoperacion) nullind ;
      parametrosadicionales  like(parametrosadicionales) nullind ;
      reservado              like(reservado) nullind ;
      observaciones          like(observaciones) nullind ;
      ktimestamp             like(ktimestamp) nullind ;

    end-ds;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Definimos la estructura para C6-T CAMBIOTITULARIDADTITULAR
    dcl-ds fC6T qualified;

      tipocuerpo             like(tipocuerpo) nullind ;
      tiposubregistro        like(tiposubregistro) nullind ;
      tipotitular            like(tipotitular) nullind ;
      tipodocumento          like(tipodocumento) nullind ;
      numerodocumento        like(numerodocumento) nullind ;
      cuitcuil               like(cuitcuil) nullind ;
      apellidonombre         like(apellidonombre) nullind;
      porcentajetitularidad  like(porcentajetitularidad) nullind ;
      calle                  like(calle) nullind ;
      numero                 like(numero) nullind ;
      piso                   like(piso) nullind ;
      departamento           like(departamento) nullind ;
      barrio                 like(barrio) nullind ;
      localidad              like(localidad) nullind ;
      codigopostal           like(codigopostal) nullind ;
      provincia              like(provincia) nullind ;
      reservado              like(reservado) nullind;
      ktimestamp             like(ktimestamp) nullind ;

    end-ds;


    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Definimos la estructura para C7  INFORMACIONRADICACIONES
    dcl-ds fC7 qualified;

       tiporegistro                 like(tiporegistro) nullind ;
       codigoorganismo              like(codigoorganismo) nullind ;
       dominio                      like(dominio) nullind ;
       estado                       like(estado) nullind ;
       tipo                         like(tipo) nullind ;
       fechaalta                    like(fechaalta) nullind ;
       fechabaja                    like(fechabaja) nullind ;
       origeninformacion            like(origeninformacion) nullind ;
       codigoregistroseccional      like(codigoregistroseccional) nullind ;
       razonsocialregistroseccional like(razonsocialregistroseccional) nullind;
       reservado                    like(reservado) nullind ;
       observaciones                like(observaciones) nullind ;
       ktimestamp                   like(ktimestamp) nullind ;

    end-ds;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Definimos la estructura para C8C  Anulacion de tramites y sellos
    dcl-ds fC8C qualified;

      tiporegistro             like(tiporegistro) nullind ;
      tiposubregistro          like(tiposubregistro) nullind ;
      codigoorganismo          like(codigoorganismo) nullind ;
      tipoanulacion            like(tipoanulacion) nullind ;
      numerotramite            like(numerotramite) nullind ;
      codigotipotramite        like(codigotipotramite) nullind ;
      dscrtipotramite          like(dscrtipotramite) nullind ;
      codigotipoaccion         like(codigotipoaccion) nullind ;
      descrtipoaccion          like(descrtipoaccion) nullind ;
      tipoformulario           like(tipoformulario) nullind ;
      numeroformulario         like(numeroformulario) nullind ;
      dominionuevo             like(dominionuevo) nullind ;
      dominioviejo             like(dominioviejo) nullind ;
      numerorecibo             like(numerorecibo) nullind ;
      codigomtmfmm             like(codigomtmfmm) nullind ;
      origen                   like(origen) nullind ;
      categoria                like(categoria) nullind ;
      marca                    like(marca) nullind ;
      tipovehiculo             like(tipovehiculo) nullind ;
      modelo                   like(modelo) nullind ;
      yyyymodelo               like(yyyymodelo) nullind ;
      fechavigenciacontrato    like(fechavigenciacontrato) nullind ;
      importetotal             like(importetotal) nullind ;
      importeimpuesto          like(importeimpuesto) nullind ;
      importepunitorio         like(importepunitorio) nullind ;
      importeadicional         like(importeadicional) nullind ;
      codigoformapago          like(codigoformapago) nullind ;
      codigomoneda             like(codigomoneda) nullind ;
      codigoentidadbancaria    like(codigoentidadbancaria) nullind ;
      descrentidadbancaria     like(descrentidadbancaria) nullind ;
      numerocheque             like(numerocheque) nullind ;
      fechatramite             like(fechatramite) nullind ;
      fechacobro               like(fechacobro) nullind ;
      fechadeposito            like(fechadeposito) nullind ;
      fechabaja                like(fechabaja) nullind ;
      cantidaddetalles         like(cantidaddetalles) nullind ;
      codigoregistroseccional  like(codigoregistroseccional) nullind ;
      descrregistroseccional   like(descrregistroseccional) nullind ;
      reservado                like(reservado) nullind ;
      observaciones            like(observaciones) nullind ;
      ktimestamp               like(ktimestamp) nullind ;

    end-ds;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Definimos la estructura para C8D  Anulacion de tramites y sellos Detalle
    dcl-ds fC8D qualified;

      tiporegistro           like(tiporegistro) nullind ;
      tiposubregistro        like(tiposubregistro) nullind ;
      yyyy                   like(yyyy) nullind ;
      numerocuota            like(numerocuota) nullind ;
      tipocuota              like(tipocuota) nullind ;
      importetotal           like(importetotal) nullind ;
      importeimpuesto        like(importeimpuesto) nullind ;
      importepunitorio       like(importepunitorio) nullind ;
      importeadicional       like(importeadicional) nullind ;
      reservado              like(reservado) nullind ;
      observaciones          like(observaciones) nullind ;
      ktimestamp             like(ktimestamp) nullind ;

    end-ds;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Definimos la estructura para C9-C  Tramites Generales
    dcl-ds fC9C qualified;

      tiporegistro           like(tiporegistro) nullind ;
      tiposubregistro        like(tiposubregistro) nullind ;
      codigoorganismo        like(codigoorganismo) nullind ;
      numerotramite          like(numerotramite) nullind ;
      codigotipotramite      like(codigotipotramite) nullind ;
      dscrtipotramite        like(dscrtipotramite) nullind ;
      codigotipoaccion       like(codigotipoaccion) nullind ;
      descrtipoaccion        like(descrtipoaccion) nullind ;
      tipoformulario         like(tipoformulario) nullind ;
      numeroformulario       like(numeroformulario) nullind ;
      dominionuevo           like(dominionuevo) nullind ;
      dominioviejo           like(dominioviejo) nullind ;
      codigomtmfmm           like(codigomtmfmm) nullind ;
      origen                 like(origen) nullind ;
      categoria              like(categoria) nullind ;
      marca                  like(marca) nullind ;
      tipovehiculo           like(tipovehiculo) nullind ;
      modelo                 like(modelo) nullind ;
      yyyymodelo             like(yyyymodelo) nullind ;
      peso                   like(peso) nullind ;
      carga                  like(carga) nullind ;
      cilindrada             like(cilindrada) nullind ;
      valuacion              like(valuacion) nullind ;
      codigotipouso          like(codigotipouso) nullind ;
      descrtipouso           like(descrtipouso) nullind ;
      fechavigencia          like(fechavigencia) nullind ;
      tipodocumento          like(tipodocumento) nullind ;
      numerodocumento        like(numerodocumento) nullind ;
      cuitcuil               like(cuitcuil) nullind ;
      apenomrazonsocial      like(apenomrazonsocial) nullind ;
      calle                  like(calle) nullind ;
      numero                 like(numero) nullind ;
      piso                   like(piso) nullind ;
      departamento           like(departamento) nullind ;
      barrio                 like(barrio) nullind ;
      ktimestamp             like(ktimestamp) nullind ;

    end-ds;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Definimos la estructura para C9-T  Tramites Generales - Ttitulares
    dcl-ds fC9T qualified;

      tipocuerpo             like(tipocuerpo) nullind ;
      tiposubregistro        like(tiposubregistro) nullind ;
      tipotitular            like(tipotitular) nullind ;
      tipodocumento          like(tipodocumento) nullind ;
      numerodocumento        like(numerodocumento) nullind ;
      cuitcuil               like(cuitcuil) nullind ;
      apellidonombre         like(apellidonombre) nullind ;
      porcentajetitularidad  like(porcentajetitularidad) nullind ;
      calle                  like(calle) nullind ;
      numero                 like(numero) nullind ;
      piso                   like(piso) nullind ;
      departamento           like(departamento) nullind ;
      barrio                 like(barrio) nullind ;
      localidad              like(localidad) nullind ;
      codigopostal           like(codigopostal) nullind ;
      provincia              like(provincia) nullind ;
      reservado              like(reservado) nullind ;
      ktimestamp             like(ktimestamp) nullind ;

    end-ds;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Definimos la estructura para P0  Pie
    dcl-ds fP0 qualified;

      tiporegistro           like(tiporegistro) nullind ;
      cantidadregistros      like(cantidadregistros) nullind ;
      checksum               like(checksum) nullind ;
      ktimestamp             like(ktimestamp) nullind ;

    end-ds;

    MONITOR;

      // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
      // Inicializacion de variables
      exsr inicializacion;

      // Leer el archivo F000000001
      READ F000000001;

      DOW NOT %EOF(F000000001);

          // asignamos el valor leido del archivo
          JSONData = FLD0000001;

          // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
          // determina el valor del tipo de registro E0
          IF %SUBST(JSONData:num1:num2) = 'E0';

             InputString =  JSONData;
             exsr fmtE0;

          ENDIF;


          // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
          // determina el valor del tipo de registro C1
          IF %SUBST(JSONData:num1:num2) = 'C1' ;

             InputString =  JSONData;

            // para el caso del subregistro con valor C
            IF %SUBST(JSONData:num4:num1) = 'C' ;
               exsr fmtC1C;

            ENDIF;

            // para el caso del subregistro con valor T
            IF %SUBST(JSONData:num4:num1) = 'T' ;
               exsr fmtC1T;

            ENDIF;

          ENDIF;

          // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
          // determina el valor del tipo de registro C2
          IF %SUBST(JSONData:num1:num2) = 'C2' ;

             InputString =  JSONData;

            // para el caso del subregistro con valor C
            IF %SUBST(JSONData:num4:num1) = 'C' ;
               exsr fmtC2C;

            ENDIF;

            // para el caso del subregistro con valor T
            IF %SUBST(JSONData:num4:num1) = 'T' ;
               exsr fmtC2T;

            ENDIF;

          ENDIF;

          // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
          // determina el valor del tipo de registro C3
          IF %SUBST(JSONData:num1:num2) = 'C3' ;

             InputString =  JSONData;

            // para el caso del subregistro con valor C
            IF %SUBST(JSONData:num4:num1) = 'C' ;
               exsr fmtC3C;

            ENDIF;

            // para el caso del subregistro con valor P
            IF %SUBST(JSONData:num4:num1) = 'P' ;
               exsr fmtC3P;

            ENDIF;

            // para el caso del subregistro con valor T
            IF %SUBST(JSONData:num4:num1) = 'T' ;
               exsr fmtC3T;

            ENDIF;


          ENDIF;

          // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
          // determina el valor del tipo de registro C4
          IF %SUBST(JSONData:num1:num2) = 'C4' ;

            InputString =  JSONData;

            exsr fmtC4;

          ENDIF;

          // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
          // determina el valor del tipo de registro C5
          IF %SUBST(JSONData:num1:num2) = 'C5' ;

             InputString =  JSONData;

            // para el caso del subregistro con valor C
            IF %SUBST(JSONData:num4:num1) = 'C' ;
               exsr fmtC5C;

            ENDIF;

            // para el caso del subregistro con valor T
            IF %SUBST(JSONData:num4:num1) = 'T' ;
               exsr fmtC5T;

            ENDIF;

          ENDIF;

          // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
          // determina el valor del tipo de registro C6
          IF %SUBST(JSONData:num1:num2) = 'C6' ;

             InputString =  JSONData;

            // para el caso del subregistro con valor C
            IF %SUBST(JSONData:num4:num1) = 'C' ;
               exsr fmtC6C;

            ENDIF;

            // para el caso del subregistro con valor T
            IF %SUBST(JSONData:num4:num1) = 'T' ;
               exsr fmtC6T;

            ENDIF;

          ENDIF;

          // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
          // determina el valor del tipo de registro C7
          IF %SUBST(JSONData:num1:num2) = 'C7' ;

             InputString =  JSONData;

               exsr fmtC7;

          ENDIF;

          // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
          // determina el valor del tipo de registro C8
          IF %SUBST(JSONData:num1:num2) = 'C8' ;

             InputString =  JSONData;

            // para el caso del subregistro con valor C
            IF %SUBST(JSONData:num4:num1) = 'C' ;
               exsr fmtC8C;

            ENDIF;

            // para el caso del subregistro con valor T
            IF %SUBST(JSONData:num4:num1) = 'D' ;
               exsr fmtC8D;

            ENDIF;

          ENDIF;

          // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
          // determina el valor del tipo de registro C9
          IF %SUBST(JSONData:num1:num2) = 'C9' ;

             InputString =  JSONData;

            // para el caso del subregistro con valor C
            IF %SUBST(JSONData:num4:num1) = 'C' ;
               exsr fmtC9C;

            ENDIF;

            // para el caso del subregistro con valor T
            IF %SUBST(JSONData:num4:num1) = 'T' ;
               exsr fmtC9T;

            ENDIF;

          ENDIF;

          // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
          // determina el valor del tipo de registro P0
          IF %SUBST(JSONData:num1:num2) = 'P0';

             InputString =  JSONData;
             exsr fmtP0;

          ENDIF;

          // Leer el siguiente registro
           READ F000000001;

      ENDDO;

      *INLR = *ON;

    ON-ERROR *ALL;
      *INLR = *ON;

    ENDMON;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // generamos una lista del InputSring
    begsr genracionLista;

      MONITOR;

        clear Count;
        clear Token;
        clear Values;

        // Ciclo para dividir la cadena
        dow %scan(Delimiter: InputString) > cero;

          Count += num1;
          Token = %subst(InputString: num1: %scan(Delimiter: InputString) - num1);
          Values(Count) = %trimr(Token);
          InputString = %subst(InputString: %scan(Delimiter: InputString) + num1);
          VariosType(Values(Count)) ;

        enddo;

        // Agregar el último valor después del último delimitador
        Count += num1;
        Values(Count) = %trimr(InputString);
        VariosType(Values(Count)) ;

      ON-ERROR *ALL;
        *INLR = *ON;

      ENDMON;


    endsr;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // realizamos la inicializacion de variables
    begsr inicializacion;

      MONITOR;

        clear fC1C ;
        clear fC1T ;
        clear fC2C;
        clear fC2T ;
        clear fC3C ;
        clear fC3P ;
        clear fC3T ;
        clear fC4  ;
        clear fC5C ;
        clear fC5T ;
        clear fC6C ;
        clear fC6T ;
        clear fC7  ;
        clear fC8C ;
        clear fC8D ;
        clear fC9C ;
        clear fC9T ;
        clear fP0  ;

        clear JSONData.Registro ;
        clear cantidadpartes  ;
        clear cantidaddetalles ;

        clear cantidadtitulares  ;
        clear codigotipotramite    ;
        clear codigotipomovimiento ;
        clear codtiporegistro ;
        clear codigoformapago ;
        clear codigomoneda ;
        clear codigoentidadbancaria ;
        clear codigotipoaccion ;
        clear numerocuota ;
        clear porcentajetitularidad ;
        clear provincia ;
        clear tipointerviniente ;
        clear tipocuota ;
        clear tipodocumento ;
        clear tipoformulario ;

        clear cantidadregistros ;
        clear carga ;
        clear cilindrada ;
        clear codigoregistronacional ;
        clear codigoorganismo ;
        clear codigoregistroseccional ;
        clear numeroformulario ;
        clear numerorecibo ;
        clear peso ;
        clear registroseccionalorigen ;
        clear registroseccionaldestino ;
        clear valuacion ;
        clear yyyy ;
        clear yyyymodelo ;

        clear numerotramite ;
        clear numeroenvio ;
        clear numerodocumento ;
        clear cuitcuil ;
        clear cuitregistroseccional ;

        clear estadodominial ;
        clear exencion ;
        clear estado ;
        clear flagvencimiento ;
        clear guardahabitual ;
        clear origeninformacion ;
        clear origen ;
        clear tipoanulacion ;
        clear tipotitular ;
        clear tipo ;
        clear tiposubregistro ;

        clear codigotipouso ;
        clear tiporegistro  ;


        clear categoria ;

        clear versionprtocolo   ;
        clear revisionprotocolo ;


        clear codigomtmfmm  ;
        clear codigopostal  ;
        clear dominionuevo  ;
        clear dominioviejo  ;
        clear dominio       ;

        clear codigoexencion ;
        clear departamento   ;
        clear numero         ;
        clear piso           ;

        clear fechatransferencia ;
        clear fechaproceso       ;
        clear fechacontrato      ;
        clear fechadeposito      ;
        clear fechahora          ;
        clear fechaoperacion     ;
        clear fechacobro         ;

        clear recibo             ;
        clear numerocheque       ;
        clear checksum           ;

        clear localidad          ;
        clear descrregistroseccional ;
        clear calle    ;
        clear barrio   ;
        clear razonsocialregistroseccional       ;
        clear razonsocialregistroseccionaldest   ;
        clear razonsocialregistroseccionalorigen ;
        clear razonsocial                        ;

        clear descrtipotramite       ;
        clear descrentidadbancaria   ;
        clear descrtipointerviniente ;
        clear dscrtipotramite        ;
        clear descrtipoaccion        ;
        clear marca                  ;
        clear tipovehiculo           ;

        clear descripcionexencion  ;
        clear descrtipouso         ;
        clear modelo               ;

        clear apellidonombre       ;
        clear apenomrazonsocial    ;
        clear municipalidaddestino ;
        clear municipalidadorigen  ;

        clear observaciones          ;
        clear observacionesanulacion ;
        clear reservado              ;

        clear parametrosadicionales  ;

        clear fechaalta                ;
        clear fechabaja                ;
        clear fechabonificacion        ;
        clear fechavencimiento         ;
        clear fechavigenciacontrato    ;
        clear fechainscripcioninicial  ;
        clear fechaultimatransferencia ;
        clear fechaultimomovimiento    ;
        clear fechavigencia            ;
        clear fechacambioestadodominial ;

        clear alicuota             ;
        clear baseimponible        ;
        clear importeadicional     ;
        clear importebonificado    ;
        clear importecomun         ;
        clear importetotal         ;
        clear importeimpuesto      ;
        clear importepunitorio     ;
        clear montoimpuestoadicional ;
        clear montoimpuesto          ;
        clear montopunitorios        ;
        clear montototalcobrado      ;
        clear montoabonado           ;
        clear montocontrato          ;
        clear montofueraregistro     ;
        clear montoadicional         ;
        clear porcentajecontrato     ;
        clear porcentajeimpuesto     ;
        clear ktimestamp ;
    
        clear Count;
        clear Token;
        clear Values;

      ON-ERROR *ALL;
        *INLR = *ON;

      ENDMON;


    endsr;


    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tratamiento del Formato E0 ENCABEZADO
    begsr fmtE0;

      MONITOR;
        exsr genracionLista;

        // Llenamos la estructura fE0
        clear fE0;
        clear Ind;

        // Asignamos los campos de tipo character
        AsignaDatos(%addr(fE0.tiporegistro):tipochr:1:cero);
        AsignaDatos(%addr(fE0.versionprtocolo):tipochr:2:cero);
        AsignaDatos(%addr(fE0.revisionprotocolo):tipochr:3:cero);
        AsignaDatos(%addr(fE0.codigoorganismo):tipointeger:4:int10);
        AsignaDatos(%addr(fE0.numeroenvio):tipointeger:5:int20);
        AsignaDatos(%addr(fE0.fechahora):tipochr:6:cero);
        fE0.ktimestamp = %timestamp(*SYS:num1);

        // **********************************************************
        // Validamos el tipo de Registro
        FindTipoRegistro(%addr(fE0.tiporegistro));

        // Si la funcion fue exitosa
        if sqlcode = cero;
          InsertENCABEZADO() ;

          // Si la funcion fue exitosa
          if sqlcode <> cero;

            // InsertLog

          ENDIF;

        ENDIF;

      ON-ERROR *ALL;
        RETURN;


      ENDMON;  

    endsr;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tratamiento del formato C1C ALTAIMPOSITIVA
    begsr fmtC1C;

      MONITOR;

        exsr genracionLista;

        // Llenamos la estructura fE0
        clear fC1C;
        clear Ind;

        // Asignamos los campos de tipo character a ID
        AsignaDatos(%addr(fC1C.tiporegistro):tipochr:1:cero);
        AsignaDatos(%addr(fC1C.tiposubregistro):tipochr:2:cero);
        AsignaDatos(%addr(fC1C.codigoorganismo):tipointeger:3:int10);
        AsignaDatos(%addr(fC1C.numerotramite):tipointeger:4:int20);
        AsignaDatos(%addr(fC1C.codigotipotramite):tipointeger:5:int3);
        AsignaDatos(%addr(fC1C.dscrtipotramite):tipochr:6:cero);
        AsignaDatos(%addr(fC1C.codigotipoaccion):tipointeger:7:int3);
        AsignaDatos(%addr(fC1C.descrtipoaccion):tipochr:8:cero);
        AsignaDatos(%addr(fC1C.tipoformulario):tipointeger:9:int3);
        AsignaDatos(%addr(fC1C.numeroformulario):tipointeger:10:int10);
        AsignaDatos(%addr(fC1C.dominionuevo):tipochr:11:cero);
        AsignaDatos(%addr(fC1C.dominioviejo):tipochr:12:cero);
        AsignaDatos(%addr(fC1C.codigomtmfmm):tipochr:13:cero);
        AsignaDatos(%addr(fC1C.origen):tipochr:14:cero);
        AsignaDatos(%addr(fC1C.categoria):tipochr:15:cero);
        AsignaDatos(%addr(fC1C.marca):tipochr:16:cero);
        AsignaDatos(%addr(fC1C.tipovehiculo):tipochr:17:cero);
        AsignaDatos(%addr(fC1C.modelo):tipochr:18:cero);
        AsignaDatos(%addr(fC1C.yyyymodelo):tipointeger:19:int10);
        AsignaDatos(%addr(fC1C.peso):tipointeger:20:int10);
        AsignaDatos(%addr(fC1C.carga):tipointeger:21:int10);
        AsignaDatos(%addr(fC1C.cilindrada):tipointeger:22:int10);
        AsignaDatos(%addr(fC1C.valuacion):tipointeger:23:int10);
        AsignaDatos(%addr(fC1C.codigotipouso):tipochr:24:cero);
        AsignaDatos(%addr(fC1C.descrtipouso):tipochr:25:cero);
        AsignaDatos(%addr(fC1C.fechavigencia):tipodate:26:cero);
        AsignaDatos(%addr(fC1C.tipodocumento):tipointeger:27:int3);
        AsignaDatos(%addr(fC1C.numerodocumento):tipointeger:28:int20);
        AsignaDatos(%addr(fC1C.cuitcuil):tipointeger:29:int20);
        AsignaDatos(%addr(fC1C.apenomrazonsocial):tipochr:30:cero);
        AsignaDatos(%addr(fC1C.calle):tipochr:31:cero);
        AsignaDatos(%addr(fC1C.numero):tipochr:32:cero);
        AsignaDatos(%addr(fC1C.piso):tipochr:33:cero);
        AsignaDatos(%addr(fC1C.departamento):tipochr:34:cero);
        AsignaDatos(%addr(fC1C.barrio):tipochr:35:cero);
        AsignaDatos(%addr(fC1C.localidad):tipochr:36:cero);
        AsignaDatos(%addr(fC1C.codigopostal):tipochr:37:cero);
        AsignaDatos(%addr(fC1C.provincia):tipointeger:38:int3);
        AsignaDatos(%addr(fC1C.cantidadtitulares):tipointeger:39:int3);
        AsignaDatos(%addr(fC1C.codigoregistroseccional):tipointeger:40:int10);
        AsignaDatos(%addr(fC1C.razonsocial):tipochr:41:cero);
        AsignaDatos(%addr(fC1C.registroseccionalorigen):tipointeger:42:int10);
        AsignaDatos(%addr(fC1C.razonsocialregistroseccionalorigen):
                                                          tipochr:43:cero);
        AsignaDatos(%addr(fC1C.municipalidadorigen):tipochr:44:cero);
        AsignaDatos(%addr(fC1C.fechaoperacion):tipochr:45:cero);
        AsignaDatos(%addr(fC1C.parametrosadicionales):tipochr:46:cero);
        AsignaDatos(%addr(fC1C.reservado):tipochr:47:cero);
        AsignaDatos(%addr(fC1C.observaciones):tipochr:48:cero);

        fC1C.ktimestamp = %timestamp(*SYS:num1);

        // **********************************************************
        // Validamos el tipo de Registro
        FindTipoRegistro(%addr(fC1C.tiporegistro));

        // Si la funcion fue exitosa
        if sqlcode = cero;
          // Validamos el tipo de Sub Registro
          FindTipoSubRegistro(%addr(fC1C.tiposubregistro));

          // Si la funcion fue exitosa
          if sqlcode = cero;
            // Validamos el Origen del Vehiculo
            FindOrigen(%addr(fC1C.origen));

            // Si la funcion fue exitosa
            if sqlcode = cero;
              // Validamos el Tipo de Documento
              FindTipoDocumento(%addr(fC1C.tipodocumento));

              // Si la funcion fue exitosa
              if sqlcode = cero;
                // Validamos la provincia
                FindProvincia(%addr(fC1C.provincia));

                // Si la funcion fue exitosa
                if sqlcode = cero;
                  InsertALTAIMPOSITIVA();

                  // Si la funcion fue exitosa
                  if sqlcode <> cero;

                  // InsertLog

                  ENDIF;

                ENDIF;

              ENDIF;

            ENDIF;

          ENDIF;

        ENDIF;

      ON-ERROR *ALL;
        RETURN;


      ENDMON;  


    endsr;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tratamiento del fC1T ALTAIMPOSITIVATITULAR
    begsr fmtC1T;

      MONITOR;

        exsr genracionLista;

        // Llenamos la estructura fE0
        clear fC1T;
        clear Ind;

        // Asignamos los campos de tipo character
        AsignaDatos(%addr(fC1T.tipocuerpo):tipochr:1:cero);
        AsignaDatos(%addr(fC1T.tiposubregistro):tipochr:2:cero);
        AsignaDatos(%addr(fC1T.tipodocumento):tipointeger:3:int3);
        AsignaDatos(%addr(fC1T.numerodocumento):tipointeger:4:int20);
        AsignaDatos(%addr(fC1T.cuitcuil):tipointeger:5:int20);
        AsignaDatos(%addr(fC1T.apenomrazonsocial):tipochr:6:cero);
        AsignaDatos(%addr(fC1T.porcentajetitularidad):tipointeger:7:int3);
        AsignaDatos(%addr(fC1T.calle):tipochr:8:cero);
        AsignaDatos(%addr(fC1T.numero):tipochr:9:cero);
        AsignaDatos(%addr(fC1T.piso):tipochr:10:cero);
        AsignaDatos(%addr(fC1T.departamento):tipochr:11:cero);
        AsignaDatos(%addr(fC1T.barrio):tipochr:12:cero);
        AsignaDatos(%addr(fC1T.localidad):tipochr:13:cero);
        AsignaDatos(%addr(fC1T.codigopostal):tipochr:14:cero);
        AsignaDatos(%addr(fC1T.provincia):tipointeger:15:int3);
        AsignaDatos(%addr(fC1T.reservado):tipochr:16:cero);

        fC1T.ktimestamp = %timestamp(*SYS:num1);

        // **********************************************************
        // Validamos el tipo de Cuerpo
        FindTipoCuerpo(%addr(fC1T.tipocuerpo));

        // Si la funcion fue exitosa
        if sqlcode = cero;
          // Validamos el tipo Sub Registro
          FindTipoSubRegistro(%addr(fC1T.tiposubregistro));

          // Si la funcion fue exitosa
          if sqlcode = cero;
            // Validamos el tipo de Documento
            FindTipoDocumento(%addr(fC1T.tipodocumento));

            // Si la funcion fue exitosa
            if sqlcode = cero;
              // Validamos la provincia
              FindProvincia(%addr(fC1T.provincia));

              // Si la funcion fue exitosa
              if sqlcode = cero;
                InsertALTAIMPOSITIVATITULAR() ;

                // Si la funcion fue exitosa
                if sqlcode <> cero;

                // InsertLog

                ENDIF;

              ENDIF;

            ENDIF;

          ENDIF;

        ENDIF;

      ON-ERROR *ALL;
        RETURN;

      ENDMON;  

    endsr;


    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tratamiento del fC2C BAJAIMPOSITIVA
    begsr fmtC2C;

      MONITOR;

        exsr genracionLista;

        // Llenamos la estructura fC2C
        clear fC2C;
        clear Ind;

        // Asignamos los campos de tipo character
        AsignaDatos(%addr(fC2C.tiporegistro):tipochr:1:cero);
        AsignaDatos(%addr(fC2C.tiposubregistro):tipochr:2:cero);
        AsignaDatos(%addr(fC2C.codigoorganismo):tipointeger:3:int10);
        AsignaDatos(%addr(fC2C.numerotramite):tipointeger:4:int20);
        AsignaDatos(%addr(fC2C.codigotipotramite):tipointeger:5:int3);
        AsignaDatos(%addr(fC2C.dscrtipotramite):tipochr:6:cero);
        AsignaDatos(%addr(fC2C.codigotipoaccion):tipointeger:7:int3);
        AsignaDatos(%addr(fC2C.descrtipoaccion):tipochr:8:cero);
        AsignaDatos(%addr(fC2C.tipoformulario):tipointeger:9:int3);
        AsignaDatos(%addr(fC2C.numeroformulario):tipointeger:10:int10);
        AsignaDatos(%addr(fC2C.dominionuevo):tipochr:11:cero);
        AsignaDatos(%addr(fC2C.dominioviejo):tipochr:12:cero);
        AsignaDatos(%addr(fC2C.codigomtmfmm):tipochr:13:cero);
        AsignaDatos(%addr(fC2C.origen):tipochr:14:cero);
        AsignaDatos(%addr(fC2C.categoria):tipochr:15:cero);
        AsignaDatos(%addr(fC2C.marca):tipochr:16:cero);
        AsignaDatos(%addr(fC2C.tipovehiculo):tipochr:17:cero);
        AsignaDatos(%addr(fC2C.modelo):tipochr:18:cero);
        AsignaDatos(%addr(fC2C.yyyymodelo):tipointeger:19:int10);
        AsignaDatos(%addr(fC2C.peso):tipointeger:20:int10);
        AsignaDatos(%addr(fC2C.carga):tipointeger:21:int10);
        AsignaDatos(%addr(fC2C.cilindrada):tipointeger:22:int10);
        AsignaDatos(%addr(fC2C.valuacion):tipointeger:23:int10);
        AsignaDatos(%addr(fC2C.codigotipouso):tipochr:24:cero);
        AsignaDatos(%addr(fC2C.descrtipouso):tipochr:25:cero);
        AsignaDatos(%addr(fC2C.fechavigencia):tipodate:26:cero);
        AsignaDatos(%addr(fC2C.cantidadtitulares):tipointeger:27:int3);
        AsignaDatos(%addr(fC2C.codigoregistronacional):tipointeger:28:int10);
        AsignaDatos(%addr(fC2C.razonsocial):tipochr:29:cero);
        AsignaDatos(%addr(fC2C.registroseccionaldestino):tipointeger:30:int10);
        AsignaDatos(%addr(fC2C.razonsocialregistroseccionaldest):tipochr:31:cero);
        AsignaDatos(%addr(fC2C.municipalidaddestino):tipochr:32:cero);
        AsignaDatos(%addr(fC2C.fechaoperacion):tipochr:33:cero);
        AsignaDatos(%addr(fC2C.parametrosadicionales):tipochr:34:cero);
        AsignaDatos(%addr(fC2C.reservado):tipochr:35:cero);
        AsignaDatos(%addr(fC2C.observaciones):tipochr:36:cero);

        fC2C.ktimestamp  = %timestamp(*SYS:num1);

        // **********************************************************
        // Validamos el tipo de Registro
        FindTipoRegistro(%addr(fC2C.tiporegistro));

        // Si la funcion fue exitosa
        if sqlcode = cero;
          // Validamos el tipo de Sub Registro
          FindTipoSubRegistro(%addr(fC2C.tiposubregistro));
          // Si la funcion fue exitosa
          if sqlcode = cero;
            // Validamos el Origen del Vehiculo
            FindOrigen(%addr(fC2C.origen));
            // Si la funcion fue exitosa
            if sqlcode = cero;
              InsertBAJAIMPOSITIVA();

              // Si la funcion fue exitosa
              if sqlcode <> cero;

                // InsertLog

              ENDIF;

            ENDIF;

          ENDIF;

        ENDIF;

      ON-ERROR *ALL;
        RETURN;

      ENDMON;  


    endsr;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tratamiento del fC2T BAJAIMPOSITIVATITULAR
    begsr fmtC2T;

      MONITOR;

        exsr genracionLista;

        // Llenamos la estructura fE0 BAJAIMPOSITIVATITULAR
        clear fC2T;
        clear Ind;

        // Asignamos los campos de tipo character
        AsignaDatos(%addr(fC2T.tipocuerpo):tipochr:1:cero);
        AsignaDatos(%addr(fC2T.tiposubregistro):tipochr:2:cero);
        AsignaDatos(%addr(fC2T.tipodocumento):tipointeger:3:int3);
        AsignaDatos(%addr(fC2T.numerodocumento):tipointeger:4:int20);
        AsignaDatos(%addr(fC2T.cuitcuil):tipointeger:5:int20);
        AsignaDatos(%addr(fC2T.apenomrazonsocial):tipochr:6:cero);
        AsignaDatos(%addr(fC2T.porcentajetitularidad):tipointeger:7:int3);
        AsignaDatos(%addr(fC2T.calle):tipochr:8:cero);
        AsignaDatos(%addr(fC2T.numero):tipochr:9:cero);
        AsignaDatos(%addr(fC2T.piso):tipochr:10:cero);
        AsignaDatos(%addr(fC2T.departamento):tipochr:11:cero);
        AsignaDatos(%addr(fC2T.barrio):tipochr:12:cero);
        AsignaDatos(%addr(fC2T.localidad):tipochr:13:cero);
        AsignaDatos(%addr(fC2T.codigopostal):tipochr:14:cero);
        AsignaDatos(%addr(fC2T.provincia):tipointeger:15:int3);
        AsignaDatos(%addr(fC2T.reservado):tipochr:16:cero);

        fC2T.ktimestamp = %timestamp(*SYS:num1);

        // **********************************************************
        // Validamos el tipo de Registro
        FindTipoCuerpo(%addr(fC2T.tipocuerpo));

        // Si la funcion fue exitosa
        if sqlcode = cero;
          // Validamos el tipo de Sub Registro
          FindTipoSubRegistro(%addr(fC2T.tiposubregistro));

          // Si la funcion fue exitosa
          if sqlcode = cero;
            // Validamos el Tipo de Documento
            FindTipoDocumento(%addr(fC2T.tipodocumento));

            // Si la funcion fue exitosa
            if sqlcode = cero;
              // Validamos la provincia
              FindProvincia(%addr(fC2T.provincia));

              // Si la funcion fue exitosa
              if sqlcode = cero;
                InsertBAJAIMPOSITIVATITULAR();

                // Si la funcion fue exitosa
                if sqlcode <> cero;

                  // InsertLog

                ENDIF;

              ENDIF;

            ENDIF;

          ENDIF;

        ENDIF;

      ON-ERROR *ALL;
        RETURN;

      ENDMON;  

    endsr;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tratamiento del fC3C IMPUESTOSELLOS
    begsr fmtC3C;

      MONITOR;

        exsr genracionLista;

        // Llenamos la estructura fC3C IMPUESTOSELLOS
        clear fC3C;
        clear Ind;

        // Asignamos los campos de tipo character
        AsignaDatos(%addr(fC3C.tiporegistro):tipochr:1:cero);
        AsignaDatos(%addr(fC3C.tiposubregistro):tipochr:2:cero);
        AsignaDatos(%addr(fC3C.codigoorganismo):tipointeger:3:int10);
        AsignaDatos(%addr(fC3C.numerotramite):tipointeger:4:int20);
        AsignaDatos(%addr(fC3C.codigotipoaccion):tipointeger:5:int3);
        AsignaDatos(%addr(fC3C.descrtipoaccion):tipochr:6:cero);
        AsignaDatos(%addr(fC3C.tipoformulario):tipointeger:7:int3);
        AsignaDatos(%addr(fC3C.numeroformulario):tipointeger:8:int10);
        AsignaDatos(%addr(fC3C.dominionuevo):tipochr:9:cero);
        AsignaDatos(%addr(fC3C.dominioviejo):tipochr:10:cero);
        AsignaDatos(%addr(fC3C.recibo):tipochr:11:cero);
        AsignaDatos(%addr(fC3C.codigomtmfmm):tipochr:12:cero);
        AsignaDatos(%addr(fC3C.origen):tipochr:13:cero);
        AsignaDatos(%addr(fC3C.categoria):tipochr:14:cero);
        AsignaDatos(%addr(fC3C.marca):tipochr:15:cero);
        AsignaDatos(%addr(fC3C.tipovehiculo):tipochr:16:cero);
        AsignaDatos(%addr(fC3C.modelo):tipochr:17:cero);
        AsignaDatos(%addr(fC3C.yyyymodelo):tipointeger:18:int10);
        AsignaDatos(%addr(fC3C.codigotipouso):tipochr:19:cero);
        AsignaDatos(%addr(fC3C.descrtipouso):tipochr:20:cero);
        AsignaDatos(%addr(fC3C.valuacion):tipointeger:21:int10);
        AsignaDatos(%addr(fC3C.cantidadpartes):tipointeger:22:int3);
        AsignaDatos(%addr(fC3C.montoimpuestoadicional):tipozoned:23:zoned12);
        AsignaDatos(%addr(fC3C.montopunitorios):tipozoned:24:zoned12);
        AsignaDatos(%addr(fC3C.montototalcobrado):tipozoned:25:zoned12);
        AsignaDatos(%addr(fC3C.montoabonado):tipozoned:26:zoned12);
        AsignaDatos(%addr(fC3C.codigoformapago):tipointeger:27:int3);
        AsignaDatos(%addr(fC3C.codigomoneda):tipointeger:28:int3);
        AsignaDatos(%addr(fC3C.codigoentidadbancaria):tipointeger:29:int3);
        AsignaDatos(%addr(fC3C.descrentidadbancaria):tipochr:30:cero);
        AsignaDatos(%addr(fC3C.numerocheque):tipochr:31:cero);
        AsignaDatos(%addr(fC3C.exencion):tipochr:32:cero);
        AsignaDatos(%addr(fC3C.codigoexencion):tipochr:33:cero);
        AsignaDatos(%addr(fC3C.descripcionexencion):tipochr:34:cero);
        AsignaDatos(%addr(fC3C.fechadeposito):tipochr:35:cero);
        AsignaDatos(%addr(fC3C.codigoregistroseccional):tipointeger:36:int10);
        AsignaDatos(%addr(fC3C.cuitregistroseccional):tipointeger:37:int20);
        AsignaDatos(%addr(fC3C.razonsocial):tipochr:38:cero);
        AsignaDatos(%addr(fC3C.fechaoperacion):tipochr:39:cero);
        AsignaDatos(%addr(fC3C.parametrosadicionales):tipochr:40:cero);
        AsignaDatos(%addr(fC3C.reservado):tipochr:41:cero);
        AsignaDatos(%addr(fC3C.observaciones):tipochr:42:cero);
        AsignaDatos(%addr(fC3C.observacionesanulacion):tipochr:43:cero);

        fC3C.ktimestamp  = %timestamp(*SYS:num1);

        FindTipoRegistro(%addr(fC3C.tiporegistro));

        // Si la funcion fue exitosa
        if sqlcode = cero;
          FindTipoSubRegistro(%addr(fC3C.tiposubregistro));

          // Si la funcion fue exitosa
          if sqlcode = cero;
            FindOrigen(%addr(fC3C.origen));

            // Si la funcion fue exitosa
            if sqlcode = cero;
              FindCodigoFormaPago(%addr(fC3C.codigoformapago));

              // Si la funcion fue exitosa
              if sqlcode = cero;
                FindCodigoMoneda(%addr(fC3C.codigomoneda));

                // Si la funcion fue exitosa
                if sqlcode = cero;
                    InsertIMPUESTOSELLOS();

                    // Si la funcion fue exitosa
                    if sqlcode <> cero;

                      // InsertLog

                    ENDIF;

                ENDIF;

              ENDIF;

            ENDIF;

          ENDIF;

        ENDIF;

      ON-ERROR *ALL;
        RETURN;

      ENDMON;  


    endsr;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tratamiento del fC3P IMPUESTOSELLOSPARTES
    begsr fmtC3P;

      MONITOR;

        exsr genracionLista;

        // Llenamos la estructura fC3P IMPUESTOSELLOSPARTES
        clear fC3P;
        clear Ind;

        // Asignamos los campos de tipo character
        AsignaDatos(%addr(fC3P.tipocuerpo):tipochr:1:cero);
        AsignaDatos(%addr(fC3P.tiposubregistro):tipochr:2:cero);
        AsignaDatos(%addr(fC3P.tipointerviniente):tipointeger:3:int3);
        AsignaDatos(%addr(fC3P.descrtipointerviniente):tipochr:4:cero);
        AsignaDatos(%addr(fC3P.tipodocumento):tipointeger:5:int3);
        AsignaDatos(%addr(fC3P.numerodocumento):tipointeger:6:int20);
        AsignaDatos(%addr(fC3P.cuitcuil):tipointeger:7:int20);
        AsignaDatos(%addr(fC3P.apellidonombre):tipochr:8:cero);
        AsignaDatos(%addr(fC3P.porcentajetitularidad):tipointeger:9:int3);
        AsignaDatos(%addr(fC3P.calle):tipochr:10:cero);
        AsignaDatos(%addr(fC3P.numero):tipochr:11:cero);
        AsignaDatos(%addr(fC3P.piso):tipochr:12:cero);
        AsignaDatos(%addr(fC3P.departamento):tipochr:13:cero);
        AsignaDatos(%addr(fC3P.barrio):tipochr:14:cero);
        AsignaDatos(%addr(fC3P.localidad):tipochr:15:cero);
        AsignaDatos(%addr(fC3P.codigopostal):tipochr:16:cero);
        AsignaDatos(%addr(fC3P.provincia):tipointeger:17:int3);
        AsignaDatos(%addr(fC3P.exencion):tipochr:18:cero);
        AsignaDatos(%addr(fC3P.codigoexencion):tipochr:19:cero);
        AsignaDatos(%addr(fC3P.descripcionexencion):tipochr:20:cero);
        AsignaDatos(%addr(fC3P.codigotipotramite):tipointeger:21:int3);
        AsignaDatos(%addr(fC3P.descrtipotramite):tipochr:22:cero);
        AsignaDatos(%addr(fC3P.reservado):tipochr:23:cero);

        fC3P.ktimestamp = %timestamp(*SYS:num1);

        FindTipoCuerpo(%addr(fC3P.tipocuerpo));

        // Si la funcion fue exitosa
        if sqlcode = cero;
          FindTipoSubRegistro(%addr(fC3P.tiposubregistro));

          // Si la funcion fue exitosa
          if sqlcode = cero;
            FindTipoDocumento(%addr(fC3P.tipodocumento));

            // Si la funcion fue exitosa
            if sqlcode = cero;
              FindProvincia(%addr(fC3P.provincia));

              // Si la funcion fue exitosa
              if sqlcode = cero;
                InsertIMPUESTOSELLOSPARTES();

                // Si la funcion fue exitosa
                if sqlcode <> cero;

                  // InsertLog

                ENDIF;

              ENDIF;

            ENDIF;

          ENDIF;

        ENDIF;

      ON-ERROR *ALL;
        RETURN;

      ENDMON;  


    endsr;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tratamiento del fC3T IMPUESTOSELLOSPARTESTIPOTRAMITE
    begsr fmtC3T;

      MONITOR;

        exsr genracionLista;

        // Llenamos la estructura fC3T IMPUESTOSELLOSPARTESTIPOTRAMITE
        clear fC3T;
        clear Ind;

        // Asignamos los campos de tipo character
        AsignaDatos(%addr(fC3T.tipocuerpo):tipochr:1:cero);
        AsignaDatos(%addr(fC3T.tiposubregistro):tipochr:2:cero);
        AsignaDatos(%addr(fC3T.codigotipotramite):tipointeger:3:int3);
        AsignaDatos(%addr(fC3T.descrtipotramite):tipochr:4:cero);
        AsignaDatos(%addr(fC3T.montocontrato):tipozoned:5:zoned12);
        AsignaDatos(%addr(fC3T.baseimponible):tipozoned:6:zoned12);
        AsignaDatos(%addr(fC3T.montoimpuesto):tipozoned:7:zoned12);
        AsignaDatos(%addr(fC3T.montopunitorios):tipozoned:8:zoned12);
        AsignaDatos(%addr(fC3T.montofueraregistro):tipozoned:9:zoned12);
        AsignaDatos(%addr(fC3T.montoadicional):tipozoned:10:zoned12);
        AsignaDatos(%addr(fC3T.alicuota):tipozoned:11:zoned5);
        AsignaDatos(%addr(fC3T.porcentajecontrato):tipozoned:12:zoned5);
        AsignaDatos(%addr(fC3T.porcentajeimpuesto):tipozoned:13:zoned5);
        AsignaDatos(%addr(fC3T.fechacontrato):tipochr:14:cero);
        AsignaDatos(%addr(fC3T.reservado):tipochr:15:cero);
        fC3T.ktimestamp  = %timestamp(*SYS:num1);

        FindTipoCuerpo(%addr(fC3T.tipocuerpo));

        // Si la funcion fue exitosa
        if sqlcode = cero;
          FindTipoSubRegistro(%addr(fC3T.tiposubregistro));

            // Si la funcion fue exitosa
            if sqlcode = cero;
              InsertIMPUESTOSELLOSPARTESTIPOTRAMITE();

              // Si la funcion fue exitosa
              if sqlcode <> cero;

                // InsertLog

              ENDIF;

            ENDIF;

        ENDIF;

      ON-ERROR *ALL;
        RETURN;

      ENDMON;  

    endsr;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tratamiento del fC4 IMPUESTOAUTOMOTOR
    begsr fmtC4;

      MONITOR;

        exsr genracionLista;

        // Llenamos la estructura fC4 IMPUESTOAUTOMOTOR
        clear fC4;
        clear Ind;

        // Asignamos los campos de tipo character
        AsignaDatos(%addr(fC4.tiporegistro):tipochr:1:cero);
        AsignaDatos(%addr(fC4.codigoorganismo):tipointeger:2:int10);
        AsignaDatos(%addr(fC4.numerotramite):tipointeger:3:int20);
        AsignaDatos(%addr(fC4.codigotipomovimiento):tipointeger:4:int3);
        AsignaDatos(%addr(fC4.codtiporegistro):tipointeger:5:int3);  // = Tipo Cuota
        AsignaDatos(%addr(fC4.dominionuevo):tipochr:6:cero);
        AsignaDatos(%addr(fC4.dominioviejo):tipochr:7:cero);
        AsignaDatos(%addr(fC4.yyyy):tipointeger:8:int10);
        AsignaDatos(%addr(fC4.numerocuota):tipointeger:9:int3);
        AsignaDatos(%addr(fC4.fechabonificacion):tipodate:10:cero);
        AsignaDatos(%addr(fC4.fechavencimiento):tipodate:11:cero);
        AsignaDatos(%addr(fC4.flagvencimiento):tipochr:12:cero);
        AsignaDatos(%addr(fC4.importebonificado):tipozoned:13:int10);
        AsignaDatos(%addr(fC4.importecomun):tipozoned:14:int10);
        AsignaDatos(%addr(fC4.fechaproceso):tipochr:15:cero);
        AsignaDatos(%addr(fC4.importetotal):tipozoned:16:int10);
        AsignaDatos(%addr(fC4.importeimpuesto):tipozoned:17:int10);
        AsignaDatos(%addr(fC4.importepunitorio):tipozoned:18:int10);
        AsignaDatos(%addr(fC4.codigoformapago):tipointeger:19:int3);
        AsignaDatos(%addr(fC4.codigomoneda):tipointeger:20:int3);
        AsignaDatos(%addr(fC4.codigoentidadbancaria):tipointeger:21:int3);
        AsignaDatos(%addr(fC4.descrentidadbancaria):tipochr:22:cero);
        AsignaDatos(%addr(fC4.numerocheque):tipochr:23:cero);
        AsignaDatos(%addr(fC4.fechacobro):tipochr:24:cero);
        AsignaDatos(%addr(fC4.fechatransferencia):tipochr:25:cero);
        AsignaDatos(%addr(fC4.codigoregistroseccional):tipointeger:26:int10);
        AsignaDatos(%addr(fC4.descrregistroseccional):tipochr:27:cero);
        AsignaDatos(%addr(fC4.reservado):tipochr:28:cero);
        AsignaDatos(%addr(fC4.observaciones):tipochr:29:cero);
        fC4.ktimestamp  = %timestamp(*SYS:num1);

        FindTipoRegistro(%addr(fC4.tiporegistro));

        // Si la funcion fue exitosa
        if sqlcode = cero;
          FindCodigoTipoMovimiento(%addr(fC4.codigotipomovimiento));

            // Si la funcion fue exitosa
            if sqlcode = cero;
              FindCodigoFormaPago(%addr(fC4.codigoformapago));

              // Si la funcion fue exitosa
              if sqlcode = cero;
                FindCodigoMoneda(%addr(fC4.codigomoneda));

                // Si la funcion fue exitosa
                if sqlcode = cero;
                  InsertIMPUESTOAUTOMOTOR();

                  // Si la funcion fue exitosa
                  if sqlcode <> cero;

                    // InsertLog

                  ENDIF;

                ENDIF;

              ENDIF;

            ENDIF;

        ENDIF;

      ON-ERROR *ALL;
        RETURN;

      ENDMON;  


    endsr;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tratamiento del fC5C INFORMACIONVEHICULO
    begsr fmtC5C;

      MONITOR;

        exsr genracionLista;

        // Llenamos la estructura fC5 INFORMACIONVEHICULO
        clear fC5C;
        clear Ind;

        // Asignamos los campos de tipo character
        AsignaDatos(%addr(fC5C.tiporegistro):tipochr:1:cero);
        AsignaDatos(%addr(fC5C.tiposubregistro):tipochr:2:cero);
        AsignaDatos(%addr(fC5C.codigoorganismo):tipointeger:3:int10);
        AsignaDatos(%addr(fC5C.dominionuevo):tipochr:4:cero);
        AsignaDatos(%addr(fC5C.dominioviejo):tipochr:5:cero);
        AsignaDatos(%addr(fC5C.codigomtmfmm):tipochr:6:cero);
        AsignaDatos(%addr(fC5C.origen):tipochr:7:cero);
        AsignaDatos(%addr(fC5C.categoria):tipochr:8:cero);
        AsignaDatos(%addr(fC5C.marca):tipochr:9:cero);
        AsignaDatos(%addr(fC5C.tipovehiculo):tipochr:10:cero);
        AsignaDatos(%addr(fC5C.modelo):tipochr:11:cero);
        AsignaDatos(%addr(fC5C.yyyymodelo):tipointeger:12:int10);
        AsignaDatos(%addr(fC5C.peso):tipointeger:13:int10);
        AsignaDatos(%addr(fC5C.carga):tipointeger:14:int10);
        AsignaDatos(%addr(fC5C.cilindrada):tipointeger:15:int10);
        AsignaDatos(%addr(fC5C.valuacion):tipointeger:16:int10);
        AsignaDatos(%addr(fC5C.codigotipouso):tipochr:17:cero);
        AsignaDatos(%addr(fC5C.descrtipouso):tipochr:18:cero);
        AsignaDatos(%addr(fC5C.fechainscripcioninicial):tipodate:19:cero);
        AsignaDatos(%addr(fC5C.fechaultimatransferencia):tipodate:20:cero);
        AsignaDatos(%addr(fC5C.fechaultimomovimiento):tipodate:21:cero);
        AsignaDatos(%addr(fC5C.estadodominial):tipochr:22:cero);
        AsignaDatos(%addr(fC5C.fechacambioestadodominial):tipodate:23:cero);
        AsignaDatos(%addr(fC5C.guardahabitual):tipochr:24:cero);
        AsignaDatos(%addr(fC5C.calle):tipochr:25:cero);
        AsignaDatos(%addr(fC5C.numero):tipochr:26:cero);
        AsignaDatos(%addr(fC5C.piso):tipochr:27:cero);
        AsignaDatos(%addr(fC5C.departamento):tipochr:28:cero);
        AsignaDatos(%addr(fC5C.barrio):tipochr:29:cero);
        AsignaDatos(%addr(fC5C.localidad):tipochr:30:cero);
        AsignaDatos(%addr(fC5C.codigopostal):tipochr:31:cero);
        AsignaDatos(%addr(fC5C.provincia):tipointeger:32:int3);
        AsignaDatos(%addr(fC5C.cantidadtitulares):tipointeger:33:int3);
        AsignaDatos(%addr(fC5C.codigoregistroseccional):tipointeger:34:int10);
        AsignaDatos(%addr(fC5C.razonsocial):tipochr:35:cero);
        AsignaDatos(%addr(fC5C.fechaoperacion):tipochr:36:cero);
        AsignaDatos(%addr(fC5C.reservado):tipochr:37:cero);
        AsignaDatos(%addr(fC5C.controlsucerp):tipochr:38:cero);
        fC5C.ktimestamp  = %timestamp(*SYS:num1);

        FindTipoRegistro(%addr(fC5C.tiporegistro));

        // Si la funcion fue exitosa
        if sqlcode = cero;
          FindTipoSubRegistro(%addr(fC5C.tiposubregistro));

            // Si la funcion fue exitosa
            if sqlcode = cero;
              FindOrigen(%addr(fC5C.origen));

                // Si la funcion fue exitosa
                if sqlcode = cero;
                  FindProvincia(%addr(fC5C.provincia));

                    // Si la funcion fue exitosa
                    if sqlcode = cero;
                      InsertINFORMACIONVEHICULO();

                      // Si la funcion fue exitosa
                      if sqlcode <> cero;

                        // InsertLog

                      ENDIF;

                    ENDIF;

                ENDIF;

            ENDIF;

        ENDIF;

      ON-ERROR *ALL;
        RETURN;

      ENDMON;  

    endsr;


    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tratamiento del fC5T INFORMACIONVEHICULOTITULAR
    begsr fmtC5T;

      MONITOR;

        exsr genracionLista;

        // Llenamos la estructura fC5T INFORMACIONVEHICULOTITULAR
        clear fC5T;
        clear Ind;

        // Asignamos los campos de tipo character
        AsignaDatos(%addr(fC5T.tipocuerpo):tipochr:1:cero);
        AsignaDatos(%addr(fC5T.tiposubregistro):tipochr:2:cero);
        AsignaDatos(%addr(fC5T.tipodocumento):tipointeger:3:int3);
        AsignaDatos(%addr(fC5T.numerodocumento):tipointeger:4:int20);
        AsignaDatos(%addr(fC5T.cuitcuil):tipointeger:5:int20);
        AsignaDatos(%addr(fC5T.apellidonombre):tipochr:6:cero);
        AsignaDatos(%addr(fC5T.porcentajetitularidad):tipointeger:7:int3);
        AsignaDatos(%addr(fC5T.calle):tipochr:8:cero);
        AsignaDatos(%addr(fC5T.numero):tipochr:9:cero);
        AsignaDatos(%addr(fC5T.piso):tipochr:10:cero);
        AsignaDatos(%addr(fC5T.departamento):tipochr:11:cero);
        AsignaDatos(%addr(fC5T.barrio):tipochr:12:cero);
        AsignaDatos(%addr(fC5T.localidad):tipochr:13:cero);
        AsignaDatos(%addr(fC5T.codigopostal):tipochr:14:cero);
        AsignaDatos(%addr(fC5T.provincia):tipointeger:15:int3);
        AsignaDatos(%addr(fC5T.reservado):tipochr:16:cero);
        fC5T.ktimestamp   = %timestamp(*SYS:num1);

        FindTipoCuerpo(%addr(fC5T.tipocuerpo));

        // Si la funcion fue exitosa
        if sqlcode = cero;
          FindTipoSubRegistro(%addr(fC5T.tiposubregistro));

            // Si la funcion fue exitosa
            if sqlcode = cero;
              FindTipoDocumento(%addr(fC5T.tipodocumento));

                // Si la funcion fue exitosa
                if sqlcode = cero;
                  FindProvincia(%addr(fC5T.provincia));

                    // Si la funcion fue exitosa
                    if sqlcode = cero;
                      InsertINFORMACIONVEHICULOTITULAR();

                      // Si la funcion fue exitosa
                      if sqlcode <> cero;

                        // InsertLog

                      ENDIF;

                    ENDIF;

                ENDIF;

            ENDIF;

        ENDIF;

      ON-ERROR *ALL;
        RETURN;

      ENDMON;  


    endsr;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tratamiento del fC6C CAMBIOTITULARIDAD
    begsr fmtC6C;

      MONITOR;

        exsr genracionLista;

        // Llenamos la estructura fC6C son 45 CAMBIOTITULARIDAD
        clear fC6C;
        clear Ind;

        // Asignamos los campos de tipo character
        AsignaDatos(%addr(fC6C.tiporegistro):tipochr:1:cero);
        AsignaDatos(%addr(fC6C.tiposubregistro):tipochr:2:cero);
        AsignaDatos(%addr(fC6C.codigoorganismo):tipointeger:3:int10);
        AsignaDatos(%addr(fC6C.numerotramite):tipointeger:4:int20);
        AsignaDatos(%addr(fC6C.codigotipotramite):tipointeger:5:int3);
        AsignaDatos(%addr(fC6C.dscrtipotramite):tipochr:6:cero);
        AsignaDatos(%addr(fC6C.codigotipoaccion):tipointeger:7:int3);
        AsignaDatos(%addr(fC6C.descrtipoaccion):tipochr:8:cero);
        AsignaDatos(%addr(fC6C.tipoformulario):tipointeger:9:int3);
        AsignaDatos(%addr(fC6C.numeroformulario):tipointeger:10:int10);
        AsignaDatos(%addr(fC6C.dominionuevo):tipochr:11:cero);
        AsignaDatos(%addr(fC6C.dominioviejo):tipochr:12:cero);
        AsignaDatos(%addr(fC6C.codigomtmfmm):tipochr:13:cero);
        AsignaDatos(%addr(fC6C.origen):tipochr:14:cero);
        AsignaDatos(%addr(fC6C.categoria):tipochr:15:cero);
        AsignaDatos(%addr(fC6C.marca):tipochr:16:cero);
        AsignaDatos(%addr(fC6C.tipovehiculo):tipochr:17:cero);
        AsignaDatos(%addr(fC6C.modelo):tipochr:18:cero);
        AsignaDatos(%addr(fC6C.yyyymodelo):tipointeger:19:int10);
        AsignaDatos(%addr(fC6C.peso):tipointeger:20:int10);
        AsignaDatos(%addr(fC6C.carga):tipointeger:21:int10);
        AsignaDatos(%addr(fC6C.cilindrada):tipointeger:22:int10);
        AsignaDatos(%addr(fC6C.valuacion):tipointeger:23:int10);
        AsignaDatos(%addr(fC6C.codigotipouso):tipochr:24:cero);
        AsignaDatos(%addr(fC6C.descrtipouso):tipochr:25:cero);
        AsignaDatos(%addr(fC6C.fechavigencia):tipodate:26:cero);
        AsignaDatos(%addr(fC6C.tipodocumento):tipointeger:27:int3);
        AsignaDatos(%addr(fC6C.numerodocumento):tipointeger:28:int20);
        AsignaDatos(%addr(fC6C.cuitcuil):tipointeger:29:int20);
        AsignaDatos(%addr(fC6C.apellidonombre):tipochr:30:cero);
        AsignaDatos(%addr(fC6C.calle):tipochr:31:cero);
        AsignaDatos(%addr(fC6C.numero):tipochr:32:cero);
        AsignaDatos(%addr(fC6C.piso):tipochr:33:cero);
        AsignaDatos(%addr(fC6C.departamento):tipochr:34:cero);
        AsignaDatos(%addr(fC6C.barrio):tipochr:35:cero);
        AsignaDatos(%addr(fC6C.localidad):tipochr:36:cero);
        AsignaDatos(%addr(fC6C.codigopostal):tipochr:37:cero);
        AsignaDatos(%addr(fC6C.provincia):tipointeger:38:int3);
        AsignaDatos(%addr(fC6C.cantidadtitulares):tipointeger:39:int3);
        AsignaDatos(%addr(fC6C.codigoregistroseccional):tipointeger:40:int10);
        AsignaDatos(%addr(fC6C.razonsocial):tipochr:41:cero);
        AsignaDatos(%addr(fC6C.fechaoperacion):tipochr:42:cero);
        AsignaDatos(%addr(fC6C.parametrosadicionales):tipochr:43:cero);
        AsignaDatos(%addr(fC6C.reservado):tipochr:44:cero);
        AsignaDatos(%addr(fC6C.observaciones):tipochr:45:cero);
        fC6C.ktimestamp   = %timestamp(*SYS:num1);

        FindTipoRegistro(%addr(fC6C.tiporegistro));

        // Si la funcion fue exitosa
        if sqlcode = cero;
          FindTipoSubRegistro(%addr(fC6C.tiposubregistro));

          // Si la funcion fue exitosa
          if sqlcode = cero;
            FindOrigen(%addr(fC6C.origen));

            // Si la funcion fue exitosa
            if sqlcode = cero;
              FindTipoDocumento(%addr(fC6C.tipodocumento));

              // Si la funcion fue exitosa
              if sqlcode = cero;
                FindProvincia(%addr(fC6C.provincia));

                // Si la funcion fue exitosa
                if sqlcode = cero;
                  InsertCAMBIOTITULARIDAD();

                  // Si la funcion fue exitosa
                  if sqlcode <> cero;

                    // InsertLog

                  ENDIF;

                ENDIF;

              ENDIF;

            ENDIF;

          ENDIF;

        ENDIF;

      ON-ERROR *ALL;
        RETURN;

      ENDMON;  


    endsr;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tratamiento del fC6T CAMBIOTITULARIDADTITULAR
    begsr fmtC6T;

      MONITOR;

        exsr genracionLista;

        // Llenamos la estructura fC6T CAMBIOTITULARIDADTITULAR
        clear fC6T;
        clear Ind;

        // Asignamos los campos de tipo character
        AsignaDatos(%addr(fC6T.tipocuerpo):tipochr:1:cero);
        AsignaDatos(%addr(fC6T.tiposubregistro):tipochr:2:cero);
        AsignaDatos(%addr(fC6T.tipotitular):tipochr:3:cero);
        AsignaDatos(%addr(fC6T.tipodocumento):tipointeger:4:int3);
        AsignaDatos(%addr(fC6T.numerodocumento):tipointeger:5:int20);
        AsignaDatos(%addr(fC6T.cuitcuil):tipointeger:6:int20);
        AsignaDatos(%addr(fC6T.apellidonombre):tipochr:7:cero);
        AsignaDatos(%addr(fC6T.porcentajetitularidad):tipointeger:8:int3);
        AsignaDatos(%addr(fC6T.calle):tipochr:9:cero);
        AsignaDatos(%addr(fC6T.numero):tipochr:10:cero);
        AsignaDatos(%addr(fC6T.piso):tipochr:11:cero);
        AsignaDatos(%addr(fC6T.departamento):tipochr:12:cero);
        AsignaDatos(%addr(fC6T.barrio):tipochr:13:cero);
        AsignaDatos(%addr(fC6T.localidad):tipochr:14:cero);
        AsignaDatos(%addr(fC6T.codigopostal):tipochr:15:cero);
        AsignaDatos(%addr(fC6T.provincia):tipointeger:16:int3);
        AsignaDatos(%addr(fC6T.reservado):tipochr:17:cero);
        fC6T.ktimestamp   = %timestamp(*SYS:num1);

        FindTipoCuerpo(%addr(fC6T.tipocuerpo));

        // Si la funcion fue exitosa
        if sqlcode = cero;
          FindTipoSubRegistro(%addr(fC6T.tiposubregistro));

          // Si la funcion fue exitosa
          if sqlcode = cero;
            FindTipoTitular(%addr(fC6T.tipotitular));

            // Si la funcion fue exitosa
            if sqlcode = cero;
              FindTipoDocumento(%addr(fC6T.tipodocumento));

              // Si la funcion fue exitosa
              if sqlcode = cero;
                FindProvincia(%addr(fC6T.provincia));

                // Si la funcion fue exitosa
                if sqlcode = cero;
                  InsertCAMBIOTITULARIDADTITULAR();

                  // Si la funcion fue exitosa
                  if sqlcode <> cero;

                    // InsertLog

                  ENDIF;

                ENDIF;

              ENDIF;

            ENDIF;

          ENDIF;

        ENDIF;

      ON-ERROR *ALL;
        RETURN;

      ENDMON;  

    endsr;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tratamiento del fC7 INFORMACIONRADICACIONES
    begsr fmtC7;

      MONITOR;

        exsr genracionLista;

        // Llenamos la estructura fC7 INFORMACIONRADICACIONES
        clear fC7;
        clear Ind;

        // Asignamos los campos de tipo character
        AsignaDatos(%addr(fC7.tiporegistro):tipochr:1:cero);
        AsignaDatos(%addr(fC7.codigoorganismo):tipointeger:2:int10);
        AsignaDatos(%addr(fC7.dominio):tipochr:3:cero);
        AsignaDatos(%addr(fC7.estado):tipochr:4:cero);
        AsignaDatos(%addr(fC7.tipo):tipochr:5:cero);
        AsignaDatos(%addr(fC7.fechaalta):tipodate:6:cero);
        AsignaDatos(%addr(fC7.fechabaja):tipodate:7:cero);
        AsignaDatos(%addr(fC7.origeninformacion):tipochr:8:cero);
        AsignaDatos(%addr(fC7.codigoregistroseccional):tipointeger:9:int10);
        AsignaDatos(%addr(fC7.razonsocialregistroseccional):tipochr:10:cero);
        AsignaDatos(%addr(fC7.reservado):tipochr:11:cero);
        AsignaDatos(%addr(fC7.observaciones):tipochr:12:cero);
        fC7.ktimestamp   = %timestamp(*SYS:num1);

        FindTipoRegistro(%addr(fC7.tiporegistro));

        // Si la funcion fue exitosa
        if sqlcode = cero;
          InsertINFORMACIORADICACION();

          // Si la funcion fue exitosa
          if sqlcode <> cero;

            // InsertLog

          ENDIF;

      ENDIF;

      ON-ERROR *ALL;
        RETURN;

      ENDMON;  

    endsr;


    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tratamiento del fC8C ANULACIONTRAMITESELLOS
    begsr fmtC8C;

      MONITOR;

        exsr genracionLista;

        // Llenamos la estructura fC6C
        clear fC8C;
        clear Ind;

        // Asignamos los campos de tipo character
        AsignaDatos(%addr(fC8C.tiporegistro):tipochr:1:cero);
        AsignaDatos(%addr(fC8C.tiposubregistro):tipochr:2:cero);
        AsignaDatos(%addr(fC8C.codigoorganismo):tipointeger:3:int10);
        AsignaDatos(%addr(fC8C.tipoanulacion):tipochr:4:cero);
        AsignaDatos(%addr(fC8C.numerotramite):tipointeger:5:int20);
        AsignaDatos(%addr(fC8C.codigotipotramite):tipointeger:6:int3);
        AsignaDatos(%addr(fC8C.dscrtipotramite):tipochr:7:cero);
        AsignaDatos(%addr(fC8C.codigotipoaccion):tipointeger:8:int3);
        AsignaDatos(%addr(fC8C.descrtipoaccion):tipochr:9:cero);
        AsignaDatos(%addr(fC8C.tipoformulario):tipointeger:10:int3);
        AsignaDatos(%addr(fC8C.numeroformulario):tipointeger:11:int10);
        AsignaDatos(%addr(fC8C.dominionuevo):tipochr:12:cero);
        AsignaDatos(%addr(fC8C.dominioviejo):tipochr:13:cero);
        AsignaDatos(%addr(fC8C.numerorecibo):tipochr:14:cero);
        AsignaDatos(%addr(fC8C.codigomtmfmm):tipochr:15:cero);
        AsignaDatos(%addr(fC8C.origen):tipochr:16:cero);
        AsignaDatos(%addr(fC8C.categoria):tipochr:17:cero);
        AsignaDatos(%addr(fC8C.marca):tipochr:18:cero);
        AsignaDatos(%addr(fC8C.tipovehiculo):tipochr:19:cero);
        AsignaDatos(%addr(fC8C.modelo):tipochr:20:cero);
        AsignaDatos(%addr(fC8C.yyyymodelo):tipointeger:21:int10);
        AsignaDatos(%addr(fC8C.fechavigenciacontrato):tipodate:22:cero);
        AsignaDatos(%addr(fC8C.importetotal):tipozoned:23:int10);
        AsignaDatos(%addr(fC8C.importeimpuesto):tipozoned:24:int10);
        AsignaDatos(%addr(fC8C.importepunitorio):tipozoned:25:int10);
        AsignaDatos(%addr(fC8C.importeadicional):tipozoned:26:zoned12);
        AsignaDatos(%addr(fC8C.codigoformapago):tipointeger:27:int3);
        AsignaDatos(%addr(fC8C.codigomoneda):tipointeger:28:int3);
        AsignaDatos(%addr(fC8C.codigoentidadbancaria):tipointeger:29:int3);
        AsignaDatos(%addr(fC8C.descrentidadbancaria):tipochr:30:cero);
        AsignaDatos(%addr(fC8C.numerocheque):tipochr:31:cero);
        AsignaDatos(%addr(fC8C.fechatramite):tipochr:32:cero);
        AsignaDatos(%addr(fC8C.fechacobro):tipochr:33:cero);
        AsignaDatos(%addr(fC8C.fechadeposito):tipochr:34:cero);
        AsignaDatos(%addr(fC8C.fechabaja):tipodate:35:cero);
        AsignaDatos(%addr(fC8C.cantidaddetalles):tipointeger:36:int3);
        AsignaDatos(%addr(fC8C.codigoregistroseccional):tipointeger:37:int10);
        AsignaDatos(%addr(fC8C.descrregistroseccional):tipochr:38:cero);
        AsignaDatos(%addr(fC8C.reservado):tipochr:39:cero);
        AsignaDatos(%addr(fC8C.observaciones):tipochr:40:cero);
        fC8C.ktimestamp  = %timestamp(*SYS:num1);

        FindTipoRegistro(%addr(fC8C.tiporegistro));

        // Si la funcion fue exitosa
        if sqlcode = cero;
          FindTipoSubRegistro(%addr(fC8C.tiposubregistro));

          // Si la funcion fue exitosa
          if sqlcode = cero;
            FindOrigen(%addr(fC8C.origen));

            // Si la funcion fue exitosa
            if sqlcode = cero;
              FindCodigoFormaPago(%addr(fC8C.codigoformapago));

              // Si la funcion fue exitosa
              if sqlcode = cero;
                FindCodigoMoneda(%addr(fC8C.codigomoneda));

                // Si la funcion fue exitosa
                if sqlcode = cero;
                  InsertANULACIONTRAMITESSELLOS();

                  // Si la funcion fue exitosa
                  if sqlcode <> cero;

                    // InsertLog

                  ENDIF;

                ENDIF;

              ENDIF;

            ENDIF;    

          ENDIF;

        ENDIF;  

      ON-ERROR *ALL;
        RETURN;

      ENDMON;  

    endsr;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tratamiento del fC8D ANULACIONTRAMITESELLOSDETALLES
    begsr fmtC8D;

      MONITOR;

        exsr genracionLista;

        // Llenamos la estructura fC8D
        clear fC8D;
        clear Ind;

        // Asignamos los campos de tipo character
        AsignaDatos(%addr(fC8D.tiporegistro):tipochr:1:cero);
        AsignaDatos(%addr(fC8D.tiposubregistro):tipochr:2:cero);
        AsignaDatos(%addr(fC8D.yyyy):tipointeger:3:int10);
        AsignaDatos(%addr(fC8D.numerocuota):tipointeger:4:int3);
        AsignaDatos(%addr(fC8D.tipocuota):tipointeger:5:int3);
        AsignaDatos(%addr(fC8D.importetotal):tipozoned:6:int10);
        AsignaDatos(%addr(fC8D.importeimpuesto):tipozoned:7:int10);
        AsignaDatos(%addr(fC8D.importepunitorio):tipozoned:8:int10);
        AsignaDatos(%addr(fC8D.importeadicional):tipozoned:9:zoned12);
        AsignaDatos(%addr(fC8D.reservado):tipochr:10:cero);
        AsignaDatos(%addr(fC8D.observaciones):tipochr:11:cero);
        fC8D.ktimestamp   = %timestamp(*SYS:num1);

        FindTipoRegistro(%addr(fC8D.tiporegistro));

        // Si la funcion fue exitosa
        if sqlcode = cero;
          FindTipoSubRegistro(%addr(fC8D.tiposubregistro));

          // Si la funcion fue exitosa
          if sqlcode = cero;
              // Si la funcion fue exitosa
              if sqlcode = cero;
                FindTipoCuota(%addr(fC8D.tipocuota));

                // Si la funcion fue exitosa
                if sqlcode = cero;
                  InsertANULACIONTRAMITESSELLOSDETALLE();

                  // Si la funcion fue exitosa
                  if sqlcode <> cero;

                    // InsertLog

                  ENDIF;

                ENDIF;

              ENDIF;

          ENDIF;

        ENDIF;

      ON-ERROR *ALL;
        RETURN;

      ENDMON;  

    endsr;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tratamiento del fC9C TRAMITESGENERALES
    begsr fmtC9C;

      MONITOR;

        exsr genracionLista;

        // Llenamos la estructura fC9C
        clear fC9C;
        clear Ind;

        // Asignamos los campos de tipo character
        AsignaDatos(%addr(fC9C.tiporegistro):tipochr:1:cero);
        AsignaDatos(%addr(fC9C.tiposubregistro):tipochr:2:cero);
        AsignaDatos(%addr(fC9C.codigoorganismo):tipointeger:3:int10);
        AsignaDatos(%addr(fC9C.numerotramite):tipointeger:4:int20);
        AsignaDatos(%addr(fC9C.codigotipotramite):tipointeger:5:int3);
        AsignaDatos(%addr(fC9C.dscrtipotramite):tipochr:6:cero);
        AsignaDatos(%addr(fC9C.codigotipoaccion):tipointeger:7:int3);
        AsignaDatos(%addr(fC9C.descrtipoaccion):tipochr:8:cero);
        AsignaDatos(%addr(fC9C.tipoformulario):tipointeger:9:int3);
        AsignaDatos(%addr(fC9C.numeroformulario):tipointeger:10:int10);
        AsignaDatos(%addr(fC9C.dominionuevo):tipochr:10:cero);
        AsignaDatos(%addr(fC9C.dominioviejo):tipochr:12:cero);
        AsignaDatos(%addr(fC9C.codigomtmfmm):tipochr:13:cero);
        AsignaDatos(%addr(fC9C.origen):tipochr:14:cero);
        AsignaDatos(%addr(fC9C.categoria):tipochr:15:cero);
        AsignaDatos(%addr(fC9C.marca):tipochr:16:cero);
        AsignaDatos(%addr(fC9C.tipovehiculo):tipochr:17:cero);
        AsignaDatos(%addr(fC9C.modelo):tipochr:18:cero);
        AsignaDatos(%addr(fC9C.yyyymodelo):tipointeger:19:int10);
        AsignaDatos(%addr(fC9C.peso):tipointeger:20:int10);
        AsignaDatos(%addr(fC9C.carga):tipointeger:21:int10);
        AsignaDatos(%addr(fC9C.cilindrada):tipointeger:22:int10);
        AsignaDatos(%addr(fC9C.valuacion):tipointeger:23:int10);
        AsignaDatos(%addr(fC9C.codigotipouso):tipochr:24:cero);
        AsignaDatos(%addr(fC9C.descrtipouso):tipochr:25:cero);
        AsignaDatos(%addr(fC9C.fechavigencia):tipodate:26:cero);
        AsignaDatos(%addr(fC9C.tipodocumento):tipointeger:27:int3);
        AsignaDatos(%addr(fC9C.numerodocumento):tipointeger:28:int20);
        AsignaDatos(%addr(fC9C.cuitcuil):tipointeger:29:int20);
        AsignaDatos(%addr(fC9C.apenomrazonsocial):tipochr:30:cero);
        AsignaDatos(%addr(fC9C.calle):tipochr:31:cero);
        AsignaDatos(%addr(fC9C.numero):tipochr:32:cero);
        AsignaDatos(%addr(fC9C.piso):tipochr:33:cero);
        AsignaDatos(%addr(fC9C.departamento):tipochr:34:cero);
        AsignaDatos(%addr(fC9C.barrio):tipochr:35:cero);
        fC9C.ktimestamp   = %timestamp(*SYS:num1);

        // **********************************************************
        // Validamos el tipo de Registro
        FindTipoRegistro(%addr(fC9C.tiporegistro));

        // Si la funcion fue exitosa
        if sqlcode = cero;

          // Validamos el tipo de Sub Registro
          FindTipoSubRegistro(%addr(fC9C.tiposubregistro));

          // Si la funcion fue exitosa
          if sqlcode = cero;

            // Validamos el Origen del Vehiculo
            FindOrigen(%addr(fC9C.origen));

            // Si la funcion fue exitosa
            if sqlcode = cero;

              // Validamos el Tipo de Documento
              FindTipoDocumento(%addr(fC9C.tipodocumento));

              // Si la funcion fue exitosa
              if sqlcode = cero;

                InsertTRAMITESGENERALES();

                // Si la funcion fue exitosa
                if sqlcode <> cero;

                  // InsertLog

                ENDIF;

              ENDIF;

            ENDIF;

          ENDIF;

        ENDIF;

      ON-ERROR *ALL;
        RETURN;

      ENDMON;  

    endsr;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tratamiento del fC9T TRAMITESGENERALESTITULARES
    begsr fmtC9T;

      MONITOR;

        exsr genracionLista;

        // Llenamos la estructura fC9T
        clear fC9T;
        clear Ind;

        // Asignamos los campos de tipo character
        AsignaDatos(%addr(fC9T.tipocuerpo):tipochr:1:cero);
        AsignaDatos(%addr(fC9T.tiposubregistro):tipochr:2:cero);
        AsignaDatos(%addr(fC9T.tipotitular):tipochr:3:cero);
        AsignaDatos(%addr(fC9T.tipodocumento):tipointeger:4:int3);
        AsignaDatos(%addr(fC9T.numerodocumento):tipointeger:5:int20);
        AsignaDatos(%addr(fC9T.cuitcuil):tipointeger:6:int20);
        AsignaDatos(%addr(fC9T.apellidonombre):tipochr:7:cero);
        AsignaDatos(%addr(fC9T.porcentajetitularidad):tipointeger:8:int3);
        AsignaDatos(%addr(fC9T.calle):tipochr:9:cero);
        AsignaDatos(%addr(fC9T.numero):tipochr:10:cero);
        AsignaDatos(%addr(fC9T.piso):tipochr:11:cero);
        AsignaDatos(%addr(fC9T.departamento):tipochr:12:cero);
        AsignaDatos(%addr(fC9T.barrio):tipochr:13:cero);
        AsignaDatos(%addr(fC9T.localidad):tipochr:14:cero);
        AsignaDatos(%addr(fC9T.codigopostal):tipochr:15:cero);
        AsignaDatos(%addr(fC9T.provincia):tipointeger:16:int3);
        AsignaDatos(%addr(fC9T.reservado):tipochr:17:cero);

        fC9T.ktimestamp   = %timestamp(*SYS:num1);


        FindTipoCuerpo(%addr(fC9T.tipocuerpo));
        // Si la funcion fue exitosa
        if sqlcode = cero;

          FindTipoSubRegistro(%addr(fC9T.tiposubregistro));
            // Si la funcion fue exitosa
          if sqlcode = cero;

            FindTipoTitular(%addr(fC9T.tipotitular));
            // Si la funcion fue exitosa
            if sqlcode = cero;

              FindTipoDocumento(%addr(fC9T.tipodocumento));
              // Si la funcion fue exitosa
              if sqlcode = cero;

                FindProvincia(%addr(fC9T.provincia));

                  // Si la funcion fue exitosa
                  if sqlcode = cero;
                    InsertTRAMITESGENERALESTITULARES();

                    // Si la funcion fue exitosa
                    if sqlcode <> cero;

                      // InsertLog

                    ENDIF;

                  ENDIF;

              ENDIF;

            ENDIF;

          ENDIF;

        ENDIF;

      ON-ERROR *ALL;
        RETURN;

      ENDMON;  

    endsr;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Tratamiento del Formato P0 PIE
    begsr fmtP0;
    
      MONITOR;


        exsr genracionLista;

        // Llenamos la estructura fP0
        clear fP0;
        clear Ind;

        // Asignamos los campos de tipo character
        AsignaDatos(%addr(fP0.tiporegistro):tipochr:1:cero);
        AsignaDatos(%addr(fP0.cantidadregistros):tipointeger:2:int10);
        AsignaDatos(%addr(fP0.checksum):tipochr:3:cero);

        fP0.ktimestamp  = %timestamp(*SYS:num1);

        FindTipoRegistro(%addr(fP0.tiporegistro));
        // Si la funcion fue exitosa
        if sqlcode = cero;

          InsertPIE();
          // Si la funcion fue exitosa
          if sqlcode <> cero;

            // InsertLog

          ENDIF;

        ENDIF;

      ON-ERROR *ALL;
        RETURN;

      ENDMON;  

    endsr;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Conversion a campos Varios
    dcl-proc VariosType;

        dcl-pi *n;
            parm1 varchar(varchr650) options(*nullind);
        end-pi;

        // Validamos la longitud del parametro si tiene informacion
        if %len(%trim(parm1)) > cero  ;
            parm1 = %trim(parm1) ;
            %nullind(parm1) = *off ;

        // Si no tiene informacion
        else;
            %nullind(parm1) = *on ;

        ENDIF;

    end-proc;


    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Conversion a campos Varios
    //
    //      parm1 Es la direccion de memoria de la variable
    //      parm2 Es el tipo de dato que vamos asignar
    //      parm3 Es el Indice para la variable Values
    //      parm5 Es la dimension de campos integer
    dcl-proc AsignaDatos;

        dcl-pi *n;
            parm1 pointer value;
            parm2 varchar(varchr5) value;
            parm3 int(int3) value;
            parm5 int(int10) value;

        end-pi;

        dcl-s valorint3   int(int3)       nullind based(parm1);
        dcl-s valorint10  int(int10)      nullind based(parm1);
        dcl-s valorint20  int(int20)      nullind based(parm1);
        dcl-s valordate   date         nullind based(parm1);
        dcl-s valorstr    varchar(varchr650) nullind based(parm1);
        dcl-s valorzon122 zoned(zoned12:decimal2)  nullind based(parm1);
        dcl-s valorzon102 zoned(zoned10:decimal2)  nullind based(parm1);
        dcl-s valorzon52  zoned(zoned5:decimal2)   nullind based(parm1);

        clear valorint3   ;
        clear valorint10  ;
        clear valorint20  ;
        clear valordate   ;
        clear valorstr    ;
        clear valorzon122 ;
        clear valorzon102 ;
        clear valorzon52  ;

        MONITOR;
          // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
          // Tratamiento para tipos integer
          if parm2 = tipointeger;

            // Si el valor no es nulo
            if not %nullind(Values(parm3)) ;

              // verificamos que el campo tenga informacion
              // si no tiene forzamos un cero 
              if %len(Values(parm3)) = cero;

                %nullind(Values(parm3)) = *on ;

                // asignamos el valor para determinar que no es nulo  
                ValuesInd(parm3) = negativo;
                Ind.IndMaster(parm3) = negativo;

                // Integer(3)
                if parm5 = int3;
                  %nullind(valorint3) = %nullind(Values(parm3));
                  clear valorint3  ;
                ENDIF;

                // Integer(int10)
                if parm5 = int10;
                  %nullind(valorint10) = %nullind(Values(parm3));
                  clear valorint10 ;
                ENDIF;

                // Integer(int20)
                if parm5 = int20;
                  %nullind(valorint20) = %nullind(Values(parm3));
                  clear valorint20 ;
                ENDIF;

              else;  

                // asignamos el valor para determinar que es nulo  
                ValuesInd(parm3) = cero;
                Ind.IndMaster(parm3) = cero;

                // Integer(3)
                if parm5 = int3;
                  valorint3  = %int(Values(parm3));
                ENDIF;

                // Integer(int10)
                if parm5 = int10;
                  valorint10  = %int(Values(parm3));
                ENDIF;

                // Integer(int20)
                if parm5 = int20;
                  valorint20  = %int(Values(parm3));
                ENDIF;

              ENDIF;  

            // si el valor es nulo
            else;

              // asignamos el valor para determinar que no es nulo  
              ValuesInd(parm3) = negativo;
              Ind.IndMaster(parm3) = negativo;

              // Integer(3)
              if parm5 = int3;
                %nullind(valorint3) = %nullind(Values(parm3));
                clear valorint3  ;
              ENDIF;

              // Integer(int10)
              if parm5 = int10;
                %nullind(valorint10) = %nullind(Values(parm3));
                clear valorint10 ;
              ENDIF;

              // Integer(int20)
              if parm5 = int20;
                %nullind(valorint20) = %nullind(Values(parm3));
                clear valorint20 ;
              ENDIF;

            endif;

          endif;

          // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
          // Tratamiento para tipos zoned
          if parm2 = tipozoned;

            // Si el valor no es nulo
            if not %nullind(Values(parm3));

              // verificamos que el campo tenga informacion
              // si no tiene forzamos un cero 
              if %len(Values(parm3)) = cero;

                %nullind(Values(parm3)) = *on ;

                // asignamos el valor para determinar que no es nulo  
                ValuesInd(parm3) = negativo;
                Ind.IndMaster(parm3) = negativo;

                // para el caso de una longitud 12
                if parm5 = zoned12;
                  %nullind(valorzon122) = %nullind(Values(parm3));
                  clear valorzon122  ;
                ENDIF;

                // para el caso de una longitud 10
                if parm5 = zoned10;
                  %nullind(valorzon102) = %nullind(Values(parm3));
                  clear valorzon102  ;
                ENDIF;

                // para el caso de una longitud 5
                if parm5 = zoned5;
                  %nullind(valorzon52) = %nullind(Values(parm3));
                  clear valorzon52  ;
                ENDIF;

              else;  


                // asignamos el valor para determinar que es nulo  
                ValuesInd(parm3) = cero;
                Ind.IndMaster(parm3) = cero;

                // para el caso de una longitud 12
                if parm5 = zoned12;
                  valorzon122  = %DEC(%trim(Values(parm3)):zoned12:decimal2) ;
                ENDIF;

                // para el caso de una longitud 10
                if parm5 = zoned10;
                  valorzon102  = %DEC(%trim(Values(parm3)):zoned10:decimal2) ;
                ENDIF;

                // para el caso de una longitud 5
                if parm5 = zoned5;
                  valorzon52  = %DEC(%trim(Values(parm3)):zoned5:decimal2) ;
                ENDIF;

              ENDIF;

            // si el valor es nulo
            else;

              // asignamos el valor para determinar que no es nulo  
              ValuesInd(parm3) = negativo;
              Ind.IndMaster(parm3) = negativo;

              // para el caso de una longitud 12
              if parm5 = zoned12;
                %nullind(valorzon122) = %nullind(Values(parm3));
                clear valorzon122  ;
              ENDIF;

              // para el caso de una longitud 10
              if parm5 = zoned10;
                %nullind(valorzon102) = %nullind(Values(parm3));
                clear valorzon102  ;
              ENDIF;

              // para el caso de una longitud 5
              if parm5 = zoned5;
                %nullind(valorzon52) = %nullind(Values(parm3));
                clear valorzon52  ;
              ENDIF;

            endif;

          endif;

          // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
          // Tratamiento para tipos date
          if parm2 = tipodate;

            // Si el valor no es nulo
            if not %nullind(Values(parm3));

              // verificamos que el campo tenga informacion
              // si no tiene forzamos un cero 
              if %len(Values(parm3)) = cero;

                %nullind(Values(parm3)) = *on ;

                // asignamos el valor para determinar que no es nulo  
                ValuesInd(parm3) = negativo;
                Ind.IndMaster(parm3) = negativo;

                %nullind(valordate) = %nullind(Values(parm3));

              else;

                // asignamos el valor para determinar que es nulo  
                ValuesInd(parm3) = cero;
                Ind.IndMaster(parm3) = cero;

                valordate  = %date(%trim(Values(parm3))) ;

              ENDIF;

            // si el valor es nulo
            else;

              // asignamos el valor para determinar que no es nulo  
              ValuesInd(parm3) = negativo;
              Ind.IndMaster(parm3) = negativo;

              %nullind(valordate) = %nullind(Values(parm3));

            endif;

          endif;

          // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
          // Tratamiento para tipos character
          if parm2 = tipochr;

            // Si el valor no es nulo
            if not %nullind(Values(parm3));

              // asignamos el valor para determinar que es nulo  
              ValuesInd(parm3) = cero;
              Ind.IndMaster(parm3) = cero;

              valorstr  = %trim(Values(parm3)) ;

            // si el valor es nulo
            else;

              // asignamos el valor para determinar que no es nulo  
              ValuesInd(parm3) = negativo;
              Ind.IndMaster(parm3) = negativo;

              %nullind(valordate) = %nullind(Values(parm3));
              valorstr  = %trim(Values(parm3)) ;

            endif;

          endif;

        ON-ERROR;
          // insert receplog por error
          formato = %SUBST(JSONData:num1:num4);
          numerocampo = parm3;
          ktimestamp = %timestamp(*SYS:num1);
          InsertRECEPLOG();
          *INLR = *ON;
          RETURN;


        ENDMON;  

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Validacion de Tipo de Registro
    //
    //      parmtiporegistro Es la direccion de memoria de la variable
    dcl-proc FindTipoRegistro;

        dcl-pi *n;
            parmtiporegistro pointer value;

        end-pi;

        // Tipo de Registro
        dcl-s tiporegistroBase like(tiporegistro) nullind 
                                based(parmtiporegistro);

        // Descripcion del tipo de Registro
        dcl-s desctiporegistro varchar(varchr50) nullind;

        // ********************************************************************
        // funcionalidad del procedimiento
        // ********************************************************************
        clear tiporegistroid ;

        // ****************************************************
        // Validamos si existe tipo de Registro
        EXEC SQL
             SELECT "tiporegistroid" INTO :tiporegistroid
               FROM TIPOREGISTRO
               WHERE "tiporegistro" = :tiporegistroBase ;

        // ********************************
        // Si no existe el Tipo de Registro
        if sqlcode =  noexiste;

            desctiporegistro = 'Descripcion del ' + tiporegistroBase ;

           // ************************************
           // Generamos el nuevo tipo de registro

           EXEC SQL
             INSERT INTO TIPOREGISTRO (
              "tiporegistro", "desctiporegistro" )

               VALUES ( :tiporegistroBase, :desctiporegistro );

           // *************************************
           // Validamos si la operacion fue exitosa
           if sqlcode  = cero;

              // **********************************
              // Realizamos el Commit
              EXEC SQL COMMIT;

              // **********************************
              // Recuperamos el ultimo id  generado
              EXEC SQL values  identity_val_local() into :tiporegistroid ;

           ENDIF;

        ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Validacion de Tipo de Sub Registro
    //
    //      parmtiporegistro Es la direccion de memoria de la variable
    dcl-proc FindTipoSubRegistro;

        dcl-pi *n;
            parmtiposubregistro pointer value;

        end-pi;

        // Tipo de Registro
        dcl-s tiposubregistroBase like(tiposubregistro) nullind 
                                  based(parmtiposubregistro);

        // Descripcion del tipo de Sub Registro
        dcl-s desctiposubregistro varchar(varchr50) nullind;

        // ********************************************************************
        // funcionalidad del procedimiento
        // ********************************************************************
        clear tiposubregistroid ;

        // ****************************************************
        // Validamos si existe tipo de Sub Registro
        EXEC SQL
             SELECT "tiposubregistroid" INTO :tiposubregistroid
               FROM TIPOSUBREGISTRO
               WHERE "tiposubregistro" = :tiposubregistroBase ;

        // ************************************
        // Si no existe el Tipo de Sub Registro
        if sqlcode =  noexiste;

            desctiposubregistro = 'Descripcion del ' + tiposubregistroBase ;


           // ***************************************
           // Generamos el nuevo tipo de sub registro

           EXEC SQL
             INSERT INTO TIPOSUBREGISTRO (
              "tiposubregistro", "desctiposubregistro" )

               VALUES ( :tiposubregistroBase, :desctiposubregistro );

           // *************************************
           // Validamos si la operacion fue exitosa
           if sqlcode  = cero;

              // **********************************
              // Realizamos el Commit
              EXEC SQL COMMIT;

              // **********************************
              // Recuperamos el ultimo id  generado
              EXEC SQL values  identity_val_local() into :tiposubregistroid ;

           ENDIF;

        ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Validacion de Origen del Vehiculo
    //
    //      parmorigen Es la direccion de memoria de la variable
    dcl-proc FindOrigen;

        dcl-pi *n;
            parmorigen pointer value;

        end-pi;

        // Origen del Vehiculo
        dcl-s origenBase like(origen) nullind based(parmorigen);

        // Descripcion del Origen del Vehiculo
        dcl-s descorigen varchar(varchr50) nullind;

        // ********************************************************************
        // funcionalidad del procedimiento
        // ********************************************************************
        clear origenid ;

        // ****************************************************
        // Validamos si existe Origen del Vehiculo
        EXEC SQL
             SELECT "origenid" INTO :origenid
               FROM TIPOORIGEN
               WHERE "tipoorigen" = :origenBase ;

        // ************************************
        // Si no existe el Tipo de Sub Registro
        if sqlcode =  noexiste;

            descorigen = 'Descripcion del ' + origenBase ;

           // ***************************************
           // Generamos el nuevo tipo de sub registro

           EXEC SQL
             INSERT INTO TIPOORIGEN (
              "tipoorigen", "descorigen" )

               VALUES ( :origenBase, :descorigen );

           // *************************************
           // Validamos si la operacion fue exitosa
           if sqlcode  = cero;

              // **********************************
              // Realizamos el Commit
              EXEC SQL COMMIT;

              // **********************************
              // Recuperamos el ultimo id  generado
              EXEC SQL values  identity_val_local() into :origenid ;

           ENDIF;

        ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Validacion la provincia
    //
    //      parmprovincia Es la direccion de memoria de la variable
    dcl-proc FindProvincia;

        dcl-pi *n;
            parmprovincia pointer value;

        end-pi;

        // Provincia de la provincia
        dcl-s provinciaBase   like(provincia) nullind based(parmprovincia);

        // Descripcion de la provincia
        dcl-s descprovincia varchar(varchr50) nullind;

        // ********************************************************************
        // funcionalidad del procedimiento
        // ********************************************************************
        clear provinciaid ;

        // ****************************************************
        // Validamos si existe Provincia
        EXEC SQL
             SELECT "provinciaid" INTO :provinciaid
               FROM PROVINCIAS
               WHERE "provincia" = :provinciaBase ;

        // *************************
        // Si no existe la provincia
        if sqlcode =  noexiste;

            descprovincia = 'Descripcion de ' + %char(provinciaBase) ;

           // ***************************************
           // Generamos la nueva provincia

           EXEC SQL
             INSERT INTO PROVINCIAS (
              "provincia", "descprovincia" )

               VALUES ( :provinciaBase, :descprovincia );

           // *************************************
           // Validamos si la operacion fue exitosa
           if sqlcode  = cero;

              // **********************************
              // Realizamos el Commit
              EXEC SQL COMMIT;

              // **********************************
              // Recuperamos el ultimo id  generado
              EXEC SQL values  identity_val_local() into :provinciaid ;

           ENDIF;

        ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Validacion del Tipo de Cuerpo
    //
    //      parmtipocuerpo Es la direccion de memoria de la variable
    dcl-proc FindTipoCuerpo;

        dcl-pi *n;
            parmtipocuerpo pointer value;

        end-pi;

        // Tipo de Cuerpo
        dcl-s tipocuerpoBase   like(tipocuerpo) nullind based(parmtipocuerpo);

        // Descripcion de Tipo de Cuerpo
        dcl-s desctipocuerpo varchar(varchr50) nullind;

        // ********************************************************************
        // funcionalidad del procedimiento
        // ********************************************************************
        clear tipocuerpoid ;

        // ****************************************************
        // Validamos si existe el Tipo de Cuerpo
        EXEC SQL
             SELECT "tipocuerpoid" INTO :tipocuerpoid
               FROM TIPOCUERPO
               WHERE "tipocuerpo" = :tipocuerpoBase ;

        // *************************
        // Si no existe el Tipo de Cuerpo
        if sqlcode =  noexiste;

            desctipocuerpo = 'Descripcion de ' + %char(tipocuerpoBase) ;


           // ***************************************
           // Generamos el nuevo Tipo de Cuerpo

           EXEC SQL
             INSERT INTO TIPOCUERPO (
              "tipocuerpo", "desctipocuerpo" )

               VALUES ( :tipocuerpoBase, :desctipocuerpo );

           // *************************************
           // Validamos si la operacion fue exitosa
           if sqlcode  = cero;

              // **********************************
              // Realizamos el Commit
              EXEC SQL COMMIT;

              // **********************************
              // Recuperamos el ultimo id  generado
              EXEC SQL values  identity_val_local() into :tipocuerpoid ;

           ENDIF;

        ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Validacion del Tipo de Documento
    //
    //      parmtipodocumento Es la direccion de memoria de la variable
    dcl-proc FindTipoDocumento;

        dcl-pi *n;
            parmtipodocumento pointer value;

        end-pi;

        // Tipo de Documento
        dcl-s tipodocumentoBase like(tipodocumento) nullind 
                                              based(parmtipodocumento);

        // Descripcion de Tipo de Documento
        dcl-s desctipodocumento varchar(varchr50) nullind;

        // ********************************************************************
        // funcionalidad del procedimiento
        // ********************************************************************
        clear tipodocumentoid ;

        // ****************************************************
        // Validamos si existe el Tipo de Documento
        EXEC SQL
             SELECT "tipodocumentoid" INTO :tipodocumentoid
               FROM "TIPODOCUMENTO"
               WHERE "tipodocumento" = :tipodocumentoBase ;

        // *************************
        // Si no existe el Tipo de Documento
        if sqlcode =  noexiste;

            desctipodocumento = 'Descripcion de ' + %char(tipodocumentoBase) ;


           // ***************************************
           // Generamos el nuevo Tipo de Documento

           EXEC SQL
             INSERT INTO "TIPODOCUMENTO" (
              "tipodocumento", "desctipodocumento" )

               VALUES (:tipodocumentoBase, :desctipodocumento );

           // *************************************
           // Validamos si la operacion fue exitosa
           if sqlcode  = cero;

              // **********************************
              // Realizamos el Commit
              EXEC SQL COMMIT;

              // **********************************
              // Recuperamos el ultimo id  generado
              EXEC SQL values  identity_val_local() into :tipodocumentoid ;

           ENDIF;

        ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Validacion del Tipo de Cuota
    //
    //      parmtipocuota Es la direccion de memoria de la variable
    dcl-proc FindTipoCuota;

        dcl-pi *n;
            parmtipocuota pointer value;

        end-pi;

        // Tipo de Cuota
        dcl-s tipocuotaBase  like(tipocuota) nullind based(parmtipocuota);

        // Descripcion de Tipo de Cuota
        dcl-s desctipocuota varchar(varchr50) nullind;

        // ********************************************************************
        // funcionalidad del procedimiento
        // ********************************************************************
        clear tipocuotaid ;

        // ****************************************************
        // Validamos si existe el Tipo de Cuota
        EXEC SQL
             SELECT "tipocuotaid" INTO :tipocuotaid
               FROM TIPOCUOTA
               WHERE "tipocuota" = :tipocuotaBase ;

        // *************************
        // Si no existe el Tipo de Cuota
        if sqlcode =  noexiste;

          desctipocuota = 'Descripcion de ' + %char(tipocuotaBase) ;


          // ***************************************
          // Generamos el nuevo Tipo de Cuota

          EXEC SQL
            INSERT INTO TIPOCUOTA (
              "tipocuota", "desctipocuota" )

              VALUES ( :tipocuotaBase, :desctipocuota );

          // *************************************
          // Validamos si la operacion fue exitosa
          if sqlcode  = cero;

            // **********************************
            // Realizamos el Commit
            EXEC SQL COMMIT;

            // **********************************
            // Recuperamos el ultimo id  generado
            EXEC SQL values  identity_val_local() into :tipocuotaid ;

          ENDIF;

        ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Validacion del Codigo de Moneda
    //
    //      parmtipocuota Es la direccion de memoria de la variable
    dcl-proc FindCodigoMoneda;

        dcl-pi *n;
            parmcodigomoneda pointer value;

        end-pi;

        // Codigo de Moneda
        dcl-s codigomonedaBase like(codigomoneda) nullind 
                                based(parmcodigomoneda);

        // Descripcion de Tipo de Moneda
        dcl-s desctipomoneda varchar(varchr50) nullind;

        // ********************************************************************
        // funcionalidad del procedimiento
        // ********************************************************************
        clear codigomonedaid ;

        // ****************************************************
        // Validamos si existe el Codigo de Moneda
        EXEC SQL
             SELECT "codigomonedaid" INTO :codigomonedaid
               FROM TIPOMONEDA
               WHERE "codigomoneda" = :codigomonedaBase ;

        // *************************
        // Si no existe el Tipo de Cuota
        if sqlcode =  noexiste;

          desctipomoneda = 'Descripcion de ' + %char(codigomonedaBase) ;


          // ***************************************
          // Generamos el nuevo Codigo de Moneda

          EXEC SQL
            INSERT INTO TIPOMONEDA (
              "codigomoneda", "desctipomoneda" )

              VALUES ( :codigomonedaBase, :desctipomoneda );

          // *************************************
          // Validamos si la operacion fue exitosa
          if sqlcode  = cero;

            // **********************************
            // Realizamos el Commit
            EXEC SQL COMMIT;

            // **********************************
            // Recuperamos el ultimo id  generado
            EXEC SQL values  identity_val_local() into :codigomonedaid ;

          ENDIF;

        ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Validacion del Codigo de Tipo de Movimiento
    //
    //      parmcodigotipomovimiento Es la direccion de memoria de la variable
    dcl-proc FindCodigoTipoMovimiento;

        dcl-pi *n;
            parmcodigotipomovimiento pointer value;

        end-pi;

        // Codigo de Tipo de Movimiento
        dcl-s codigotipomovimientoBase like(codigotipomovimiento) nullind 
                                    based(parmcodigotipomovimiento);

        // Descripcion de Codigo de Tipo de Movimiento
        dcl-s desctipomovimiento varchar(varchr50) nullind;

        // ********************************************************************
        // funcionalidad del procedimiento
        // ********************************************************************
        clear codigotipomovimientoid ;

        // ****************************************************
        // Validamos si existe el Codigo de Tipo de Movimiento
        EXEC SQL
             SELECT "codigotipomovimientoid" INTO :codigotipomovimientoid
               FROM "TIPOMOVIMIENTO"
               WHERE "codigotipomovimiento" = :codigotipomovimientoBase ;

        // ********************************************
        // Si no existe el Codigo de Tipo de Movimiento
        if sqlcode =  noexiste;

          desctipomovimiento = 'Descripcion de ' + 
                                %char(codigotipomovimientoBase) ;


          // ***********************************************
          // Generamos el nuevo Codigo de Tipo de Movimiento

          EXEC SQL
            INSERT INTO "TIPOMOVIMIENTO" (
              "codigotipomovimiento", "desctipomovimiento" )

              VALUES ( :codigotipomovimientoBase, :desctipomovimiento );

          // *************************************
          // Validamos si la operacion fue exitosa
          if sqlcode  = cero;

          // **********************************
          // Realizamos el Commit
          EXEC SQL COMMIT;

          // **********************************
          // Recuperamos el ultimo id  generado
          EXEC SQL values  identity_val_local() into :codigotipomovimientoid ;

          ENDIF;

        ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Validacion del Tipo de Titular
    //
    //      parmtipotitular Es la direccion de memoria de la variable
    dcl-proc FindTipoTitular;

        dcl-pi *n;
            parmtipotitular pointer value;

        end-pi;

        // Tipo de Titular
        dcl-s tipotitularBase like(tipotitular) nullind based(parmtipotitular);

        // Descripcion de Tipo de Titular
        dcl-s desctipotitular varchar(varchr50) nullind;

        // ********************************************************************
        // funcionalidad del procedimiento
        // ********************************************************************
        clear tipotitularid ;

        // ****************************************************
        // Validamos si existe el Tipo de Titular
        EXEC SQL
             SELECT "tipotitularid" INTO :tipotitularid
               FROM "TIPOTITULAR"
               WHERE "tipotitular" = :tipotitularBase ;

        // ********************************************
        // Si no existe el Tipo de Titular
        if sqlcode =  noexiste;

            desctipotitular = 'Descripcion de ' + tipotitularBase ;


           // **********************************
           // Generamos el nuevo Tipo de Titular

           EXEC SQL
             INSERT INTO "TIPOTITULAR" (
               "tipotitular", "desctipotitular" )

               VALUES ( :tipotitularBase, :desctipotitular );

           // *************************************
           // Validamos si la operacion fue exitosa
           if sqlcode  = cero;

              // **********************************
              // Realizamos el Commit
              EXEC SQL COMMIT;

              // **********************************
              // Recuperamos el ultimo id  generado
              EXEC SQL values identity_val_local() into :codigotipomovimientoid;

           ENDIF;

        ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Validacion del Codigo de Forma de Pago
    //
    //      parmcodigotipomovimiento Es la direccion de memoria de la variable
    dcl-proc FindCodigoFormaPago;

        dcl-pi *n;
            parmcodigoformapago pointer value;

        end-pi;

        // Codigo de Codigo de Forma de Pago
        dcl-s codigoformapagoBase like(codigoformapago) nullind 
                                                    based(parmcodigoformapago);

        // Descripcion de Codigo de Forma de Pago
        dcl-s descrtipopago varchar(varchr50) nullind;

        // ********************************************************************
        // funcionalidad del procedimiento
        // ********************************************************************
        clear codigoformapagoid ;

        // **********************************************
        // Validamos si existe el Codigo de Forma de Pago
        EXEC SQL
             SELECT "codigoformapagoid" INTO :codigoformapagoid
               FROM TIPOPAGO
               WHERE "codigoformapago" = :codigoformapagoBase ;

        // ********************************************
        // Si no existe el Codigo de Forma de Pago
        if sqlcode =  noexiste;

            descrtipopago = 'Descripcion de ' + %char(codigoformapagoBase) ;


           // ***********************************************
           // Generamos el nuevo Codigo de Forma de Pago

           EXEC SQL
             INSERT INTO TIPOPAGO (
               "codigoformapago", "descrtipopago" )

               VALUES (
                :codigoformapagoBase, :descrtipopago );

           // *************************************
           // Validamos si la operacion fue exitosa
           if sqlcode  = cero;

              // **********************************
              // Realizamos el Commit
              EXEC SQL COMMIT;

              // **********************************
              // Recuperamos el ultimo id  generado
              EXEC SQL values  identity_val_local() into :codigoformapagoid ;

           ENDIF;

        ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Validacion de ALTAIMPOSITIVA
    //
    //      parmdominionuevo Es la direccion de memoria de la variable
    //      parmdominioviejo Es la direccion de memoria de la variable
    //      parmcodigomtmfmm Es la direccion de memoria de la variable
    dcl-proc FindALTAIMPOSITIVA;

        dcl-pi *n;
            parmdominionuevo pointer value;
            parmdominioviejo pointer value;
            parmcodigomtmfmm pointer value;

        end-pi;

        // Codigo Sucerp
        dcl-s codigomtmfmmBase like(codigomtmfmm) nullind 
                                based(parmcodigomtmfmm);

        // Dominio Nuevo
        dcl-s dominionuevoBase like(dominionuevo) nullind 
                                based(parmdominionuevo);

        // Dominio Viejo
        dcl-s dominioviejoBase like(dominioviejo) nullind 
                                based(parmdominioviejo);

        // ********************************************************************
        // funcionalidad del procedimiento
        // ********************************************************************
        clear altataxtitularid ;

        // **********************************************
        // Validamos si existe el ALTAIMPOSITIVA
        EXEC SQL
             SELECT "altataxid" INTO :altataxtitularid
               FROM "ALTAIMPOSITIVA"
               WHERE  ( "dominionuevo" = :dominionuevoBase ) AND
                      ( "dominioviejo" = :dominioviejoBase ) AND
                      ( "codigomtmfmm" = :codigomtmfmmBase );

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Validacion de ALTAIMPOSITIVATITULAR
    //
    //      parmtipodocumento Es la direccion de memoria de la variable
    //      parmnumerodocumento Es la direccion de memoria de la variable
    //      parmcuitcuil Es la direccion de memoria de la variable
    dcl-proc FindALTAIMPOSITIVATITULAR;

        dcl-pi *n;
            parmtipodocumento pointer value;
            parmnumerodocumento pointer value;
            parmcuitcuil pointer value;

        end-pi;

        // Tipo Documento
        dcl-s tipodocumentoBase like(tipodocumento) nullind 
                                                    based(parmtipodocumento);
        // Nro Documento
        dcl-s numerodocumentoBase like(numerodocumento) nullind 
                                                    based(parmnumerodocumento);
        // Cuit/Cuil
        dcl-s cuitcuilBase like(cuitcuil) nullind 
                                                    based(parmcuitcuil);

        // ********************************************************************
        // funcionalidad del procedimiento
        // ********************************************************************
        clear altataxtitularid ;

        // Obtenemos el tipodocumentoid
        FindTipoDocumento(parmtipodocumento);

        // **********************************************
        // Validamos si existe el ALTAIMPOSITIVATITULAR
        EXEC SQL
             SELECT "altataxtitularid" INTO :altataxtitularid
              FROM "ALTAIMPOSITIVATITULAR"
              WHERE ("tipodocumentoid" = :tipodocumentoid AND
                     "numerodocumento" = :numerodocumentoBase) OR
                    ("cuitcuil"        = :cuitcuilBase) ;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Validacion de BAJAIMPOSITIVA
    //
    //      parmdominionuevo Es la direccion de memoria de la variable
    //      parmdominioviejo Es la direccion de memoria de la variable
    //      parmcodigomtmfmm Es la direccion de memoria de la variable
    dcl-proc FindBAJAIMPOSITIVA;

        dcl-pi *n;
            parmdominionuevo pointer value;
            parmdominioviejo pointer value;
            parmcodigomtmfmm pointer value;

        end-pi;

        // Codigo Sucerp
        dcl-s codigomtmfmmBase like(codigomtmfmm) nullind 
                                based(parmcodigomtmfmm);

        // Dominio Nuevo
        dcl-s dominionuevoBase like(dominionuevo) nullind 
                                based(parmdominionuevo);

        // Dominio Viejo
        dcl-s dominioviejoBase like(dominioviejo) nullind 
                                based(parmdominioviejo);

        // ********************************************************************
        // funcionalidad del procedimiento
        // ********************************************************************
        clear bajataxid ;

        // **********************************************
        // Validamos si existe el ALTAIMPOSITIVA
        EXEC SQL
             SELECT "bajataxid" INTO :bajataxid
               FROM "BAJAIMPOSITIVA"
               WHERE  ( "dominionuevo" = :dominionuevoBase ) AND
                      ( "dominioviejo" = :dominioviejoBase ) AND
                      ( "codigomtmfmm" = :codigomtmfmmBase );

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Validacion de BAJAIMPOSITIVATITULAR
    //
    //      parmtipodocumento Es la direccion de memoria de la variable
    //      parmnumerodocumento Es la direccion de memoria de la variable
    //      parmcuitcuil Es la direccion de memoria de la variable
    dcl-proc FindBAJAIMPOSITIVATITULAR;

        dcl-pi *n;
            parmtipodocumento pointer value;
            parmnumerodocumento pointer value;
            parmcuitcuil pointer value;

        end-pi;

        // Tipo Documento
        dcl-s tipodocumentoBase like(tipodocumento) nullind 
                                              based(parmtipodocumento);
        // Nro Documento
        dcl-s numerodocumentoBase like(numerodocumento) nullind 
                                              based(parmnumerodocumento);
        // Cuit/Cuil
        dcl-s cuitcuilBase like(cuitcuil) nullind based(parmcuitcuil);

        // ********************************************************************
        // funcionalidad del procedimiento
        // ********************************************************************
        clear bajataxtitularid ;

        // Obtenemos el tipodocumentoid
        FindTipoDocumento(parmtipodocumento);


        // **********************************************
        // Validamos si existe el ALTAIMPOSITIVATITULAR
        EXEC SQL
             SELECT "bajataxtitularid" INTO :bajataxtitularid
              FROM "BAJAIMPOSITIVATITULAR"
              WHERE ("tipodocumentoid" = :tipodocumentoid AND
                     "numerodocumento" = :numerodocumentoBase) OR
                    ("cuitcuil"        = :cuitcuilBase) ;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Nuevo ENCABEZADO
    //
    dcl-proc InsertENCABEZADO;

      // ********************************************************************
      // funcionalidad del procedimiento
      // ********************************************************************

      clear encabezadoid;

      // Realizamos un control por salida de Escape
      EXEC SQL  WHENEVER SQLERROR DO ERRORPROC();

      // Realizamos el encabezado
      EXEC SQL
        INSERT INTO ENCABEZADO (
          TIPOR00001, VERSI00001, REVIS00001,
          CODIG00001, NUMER00001, FECHA00001,
          KTIME00001)

          VALUES (
          :tiporegistroid:Ind.Ind001 ,
          :fE0.versionprtocolo:Ind.Ind002 ,
          :fE0.revisionprotocolo:Ind.Ind003 ,
          :fE0.codigoorganismo:Ind.Ind004 ,
          :fE0.numeroenvio:Ind.Ind005 ,
          :fE0.fechahora:Ind.Ind006 ,
          :fE0.ktimestamp ) ;


      // *************************************
      // Validamos si la operacion fue exitosa
      if sqlcode  = cero;

        // **********************************
        // Realizamos el Commit
        EXEC SQL COMMIT;

        // **********************************
        // Recuperamos el ultimo id  generado
        EXEC SQL values  identity_val_local() into :encabezadoid ;

      ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Nuevo RECEPLOG
    //
    dcl-proc InsertRECEPLOG;

      // ********************************************************************
      // funcionalidad del procedimiento
      // ********************************************************************

      // Realizamos un control por salida de Escape
      EXEC SQL  WHENEVER SQLERROR DO ERRORPROC();

      // Realizamos el encabezado
      EXEC SQL
        INSERT INTO RECEPLOG (

          ARCHIVOREC, FORMATO001, NUMERO0001,
          KTIME00001)

          VALUES (
          :archvorecibido ,
          :formato ,
          :numerocampo ,
          :ktimestamp ) ;


      // *************************************
      // Validamos si la operacion fue exitosa
      if sqlcode  = cero;

        // **********************************
        // Realizamos el Commit
        EXEC SQL COMMIT;

      ENDIF;

    end-proc;



    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Nueva ALTAIMPOSITIVA
    //
    //      parmcodigotipomovimiento Es la direccion de memoria de la variable
    dcl-proc InsertALTAIMPOSITIVA;

      // ********************************************************************
      // funcionalidad del procedimiento
      // ********************************************************************

      clear altataxid;

      // Realizamos un control por salida de Escape
      EXEC SQL  WHENEVER SQLERROR DO ERRORPROC();

      EXEC SQL
        INSERT INTO "ALTAIMPOSITIVA" (
          TIPOR00001,
          TIPOS00001, CODIG00001,
          NUMER00001, CODIG00002, DESCR00001,
          CODIG00003, DESCR00002, TIPOF00001,
          NUMER00002, DOMIN00001, DOMIN00002,
          CODIG00004, ORIGE00001, CATEG00001,
          MARCA00001, TIPOV00001, MODEL00001,
          YYYYM00001, PESO_00001, CARGA00001,
          CILIN00001, VALUA00001, CODIG00005,
          DESCR00003, FECHA00001, TIPOD00001,
          NUMER00003, CUITC00001, APENO00001,
          CALLE00001, NUMER00004, PISO_00001,
          DEPAR00001, BARRI00001, LOCAL00001,
          CODIG00006, PROVI00001, CANTI00001,
          CODIG00007, RAZON00001, REGIS00001,
          RAZON00002, MUNIC00001, FECHA00002,
          PARAM00001, RESER00001, OBSER00001,
          ALTAT00002, KTIME00001 )

          VALUES (
          :tiporegistroid:Ind.Ind001 ,
          :tiposubregistroid:Ind.Ind002 ,
          :fC1C.codigoorganismo:Ind.Ind003 ,
          :fC1C.numerotramite:Ind.Ind004 ,
          :fC1C.codigotipotramite:Ind.Ind005 ,
          :fC1C.dscrtipotramite:Ind.Ind006 ,
          :fC1C.codigotipoaccion:Ind.Ind007 ,
          :fC1C.descrtipoaccion:Ind.Ind008 ,
          :fC1C.tipoformulario:Ind.Ind009 ,
          :fC1C.numeroformulario:Ind.Ind010 ,
          :fC1C.dominionuevo:Ind.Ind011 ,
          :fC1C.dominioviejo:Ind.Ind012 ,
          :fC1C.codigomtmfmm:Ind.Ind013 ,
          :origenid:Ind.Ind014 ,
          :fC1C.categoria:Ind.Ind015 ,
          :fC1C.marca:Ind.Ind016 ,
          :fC1C.tipovehiculo:Ind.Ind017 ,
          :fC1C.modelo:Ind.Ind018 ,
          :fC1C.yyyymodelo:Ind.Ind019 ,
          :fC1C.peso:Ind.Ind020 ,
          :fC1C.carga:Ind.Ind021 ,
          :fC1C.cilindrada:Ind.Ind022 ,
          :fC1C.valuacion:Ind.Ind023 ,
          :fC1C.codigotipouso:Ind.Ind024 ,
          :fC1C.descrtipouso:Ind.Ind025 ,
          :fC1C.fechavigencia:Ind.Ind026 ,
          :tipodocumentoid:Ind.Ind027 ,
          :fC1C.numerodocumento:Ind.Ind028 ,
          :fC1C.cuitcuil:Ind.Ind029 ,
          :fC1C.apenomrazonsocial:Ind.Ind030 ,
          :fC1C.calle:Ind.Ind031 ,
          :fC1C.numero:Ind.Ind032 ,
          :fC1C.piso:Ind.Ind033 ,
          :fC1C.departamento:Ind.Ind034 ,
          :fC1C.barrio:Ind.Ind035 ,
          :fC1C.localidad:Ind.Ind036 ,
          :fC1C.codigopostal:Ind.Ind037 ,
          :provinciaid:Ind.Ind038 ,
          :fC1C.cantidadtitulares:Ind.Ind039 ,
          :fC1C.codigoregistroseccional:Ind.Ind040 ,
          :fC1C.razonsocial:Ind.Ind041 ,
          :fC1C.registroseccionalorigen:Ind.Ind042 ,
          :fC1C.razonsocialregistroseccionalorigen:Ind.Ind043 ,
          :fC1C.municipalidadorigen:Ind.Ind044 ,
          :fC1C.fechaoperacion:Ind.Ind045 ,
          :fC1C.parametrosadicionales:Ind.Ind046 ,
          :fC1C.reservado:Ind.Ind047 ,
          :fC1C.observaciones:Ind.Ind048 ,
          NULL, :fC1C.ktimestamp ) ;

      // *************************************
      // Validamos si la operacion fue exitosa
      if sqlcode  = cero;

        // **********************************
        // Realizamos el Commit
        EXEC SQL COMMIT;

        // **********************************
        // Recuperamos el ultimo id  generado
        EXEC SQL values  identity_val_local() into :altataxid ;

      ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Nueva ALTAIMPOSITIVATITULAR
    //
    dcl-proc InsertALTAIMPOSITIVATITULAR;

      // ********************************************************************
      // funcionalidad del procedimiento
      // ********************************************************************

      clear altataxtitularid;

      // Realizamos un control por salida de Escape
      EXEC SQL  WHENEVER SQLERROR DO ERRORPROC();

      // Realizamos el altimpositivatitular
      EXEC SQL
        INSERT INTO "ALTAIMPOSITIVATITULAR" (
          TIPOC00001, TIPOS00001, TIPOD00001,
          NUMER00001, CUITC00001, APELL00001,
          PORCE00001, CALLE00001, NUMER00002,
          PISO_00001, DEPAR00001, BARRI00001,
          LOCAL00001, CODIG00001, PROVI00001,
          RESER00001, KTIME00001 )

          VALUES (
          :tipocuerpoid:Ind.Ind001 ,
          :tiposubregistroid:Ind.Ind002 ,
          :tipodocumentoid:Ind.Ind003 ,
          :fC1T.numerodocumento:Ind.Ind004 ,
          :fC1T.cuitcuil:Ind.Ind005 ,
          :fC1T.apenomrazonsocial:Ind.Ind006 ,
          :fC1T.porcentajetitularidad:Ind.Ind007 ,
          :fC1T.calle:Ind.Ind008 ,
          :fC1T.numero:Ind.Ind009 ,
          :fC1T.piso:Ind.Ind010 ,
          :fC1T.departamento:Ind.Ind011 ,
          :fC1C.barrio:Ind.Ind012 ,
          :fC1T.localidad:Ind.Ind013 ,
          :fC1T.codigopostal:Ind.Ind014 ,
          :provinciaid:Ind.Ind015 ,
          :fC1T.reservado:Ind.Ind016 ,
          :fC1T.ktimestamp ) ;

      // *************************************
      // Validamos si la operacion fue exitosa
      if sqlcode  = cero;

        // **********************************
        // Realizamos el Commit
        EXEC SQL COMMIT;

        // **********************************
        // Recuperamos el ultimo id  generado
        EXEC SQL values  identity_val_local() into :altataxtitularid ;

      ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Nueva BAJAIMPOSITIVA
    //
    dcl-proc InsertBAJAIMPOSITIVA;

      // ********************************************************************
      // funcionalidad del procedimiento
      // ********************************************************************

      clear bajataxid;

      // Realizamos un control por salida de Escape
      EXEC SQL  WHENEVER SQLERROR DO ERRORPROC();

      // Realizamos el bajaimpositiva
      EXEC SQL
        INSERT INTO "BAJAIMPOSITIVA" (
        	TIPOR00001 , TIPOS00001 , CODIG00001 ,
        	NUMER00001 , CODIG00002 , DESCR00001 ,
        	CODIG00003 , DESCR00002 , TIPOF00001 ,
        	NUMER00002 , DOMIN00001 , DOMIN00002 ,
        	CODIG00004 , ORIGE00001 , CATEG00001 ,
        	MARCA00001 , TIPOV00001 , MODEL00001 ,
        	YYYYM00001 , PESO_00001 , CARGA00001 ,
        	CILIN00001 , VALUA00001 , CODIG00005 ,
        	DESCR00003 , FECHA00001 , CANTI00001 ,
        	CODIG00006 , RAZON00001 , REGIS00001 ,
        	RAZON00002 , MUNIC00001 , FECHA00002 ,
        	PARAM00001 , RESER00001 , OBSER00001 ,
        	BAJAT00002 , KTIME00001 )

          VALUES (
          :tiporegistroid:Ind.Ind001 ,
          :tiposubregistroid:Ind.Ind002 ,
          :fC2C.codigoorganismo:Ind.Ind003 ,
          :fC2C.numerotramite:Ind.Ind004 ,
          :fC2C.codigotipotramite:Ind.Ind005 ,
          :fC2C.dscrtipotramite:Ind.Ind006 ,
          :fC2C.codigotipoaccion:Ind.Ind007 ,
          :fC2C.descrtipoaccion:Ind.Ind008 ,
          :fC2C.tipoformulario:Ind.Ind009 ,
          :fC2C.numeroformulario:Ind.Ind010 ,
          :fC2C.dominionuevo:Ind.Ind011 ,
          :fC2C.dominioviejo:Ind.Ind012 ,
          :fC2C.codigomtmfmm:Ind.Ind013 ,
          :origenid:Ind.Ind014 ,
          :fC2C.categoria:Ind.Ind015 ,
          :fC2C.marca:Ind.Ind016 ,
          :fC2C.tipovehiculo:Ind.Ind017 ,
          :fC2C.modelo:Ind.Ind018 ,
          :fC2C.yyyymodelo:Ind.Ind019 ,
          :fC2C.peso:Ind.Ind020 ,
          :fC2C.carga:Ind.Ind021 ,
          :fC2C.cilindrada:Ind.Ind022 ,
          :fC2C.valuacion:Ind.Ind023 ,
          :fC2C.codigotipouso:Ind.Ind024 ,
          :fC2C.descrtipouso:Ind.Ind025 ,
          :fC2C.fechavigencia:Ind.Ind026 ,
          :fC2C.codigoregistronacional:Ind.Ind027 ,
          :fC2C.razonsocial:Ind.Ind028 ,
          :fC2C.registroseccionaldestino:Ind.Ind029 ,
          :fC2C.razonsocialregistroseccionaldest:Ind.Ind030 ,
          :fC2C.municipalidaddestino:Ind.Ind031 ,
          :fC2C.fechaoperacion:Ind.Ind032 ,
          :fC2C.parametrosadicionales:Ind.Ind033 ,
          :fC2C.reservado:Ind.Ind034 ,
          :fC2C.observaciones:Ind.Ind035 ,
          :fC2C.cantidadtitulares:Ind.Ind036 ,
          NULL, :fC1C.ktimestamp ) ;

      // *************************************
      // Validamos si la operacion fue exitosa
      if sqlcode  = cero;

        // **********************************
        // Realizamos el Commit
        EXEC SQL COMMIT;

        // **********************************
        // Recuperamos el ultimo id  generado
        EXEC SQL values  identity_val_local() into :bajataxid ;

      ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Nueva BAJAIMPOSITIVATITULAR
    //
    dcl-proc InsertBAJAIMPOSITIVATITULAR;

      // ********************************************************************
      // funcionalidad del procedimiento bajataxtitularid
      // ********************************************************************

      clear bajataxtitularid;

      // Realizamos un control por salida de Escape
      EXEC SQL  WHENEVER SQLERROR DO ERRORPROC();

      // Realizamos el bajaimpositivatitular
      EXEC SQL
        INSERT INTO "BAJAIMPOSITIVATITULAR" (
          TIPOC00001 , TIPOS00001 , TIPOD00001 ,
        	NUMER00001 , CUITC00001 , APELL00001 ,
        	PORCE00001 , CALLE00001 , NUMER00002 ,
        	PISO_00001 , DEPAR00001 , BARRI00001 ,
        	LOCAL00001 , CODIG00001 , PROVI00001 ,
          RESER00001, KTIME00001 )

          VALUES (
          :tipocuerpoid:Ind.Ind001 ,
          :tiposubregistroid:Ind.Ind002 ,
          :tipodocumentoid:Ind.Ind003 ,
          :fC2T.numerodocumento:Ind.Ind004 ,
          :fC2T.cuitcuil:Ind.Ind005 ,
          :fC2T.apenomrazonsocial:Ind.Ind006 ,
          :fC2T.porcentajetitularidad:Ind.Ind007 ,
          :fC2T.calle:Ind.Ind008 ,
          :fC2T.numero:Ind.Ind009 ,
          :fC2T.piso:Ind.Ind010 ,
          :fC2T.departamento:Ind.Ind011 ,
          :fC2T.barrio:Ind.Ind012 ,
          :fC2T.localidad:Ind.Ind013 ,
          :fC2T.codigopostal:Ind.Ind014 ,
          :provinciaid:Ind.Ind015 ,
          :fC2T.reservado:Ind.Ind016 ,
          :fC2T.ktimestamp ) ;

      // *************************************
      // Validamos si la operacion fue exitosa
      if sqlcode = cero;

        // **********************************
        // Realizamos el Commit
        EXEC SQL COMMIT;

        // **********************************
        // Recuperamos el ultimo id  generado
        EXEC SQL values  identity_val_local() into :bajataxtitularid ;

      ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Nueva IMPUESTOSELLOS
    //
    dcl-proc InsertIMPUESTOSELLOS;

      // ********************************************************************
      // funcionalidad del procedimiento taxsellosid
      // ********************************************************************

      clear taxsellosid;

      // Realizamos un control por salida de Escape
      EXEC SQL  WHENEVER SQLERROR DO ERRORPROC();

      // Realizamos el impuestosellos
      EXEC SQL
        INSERT INTO "IMPUESTOSELLOS" (
          TIPOR00001 , TIPOS00001 , CODIG00001 ,
          NUMER00001 , CODIG00002 ,	DESCR00001 ,
          TIPOF00001 , NUMER00002 , DOMIN00001 ,
          DOMIN00002 , RECIB00001 , CODIG00003 ,
          ORIGE00001 , CATEG00001 , MARCA00001 ,
          TIPOV00001 , MODEL00001 , YYYYM00001 ,
          CODIG00004 , DESCR00002 , VALUA00001 ,
          CANTI00001 , MONTO00001 , MONTO00002 ,
          MONTO00003 , MONTO00004 , CODIG00005 ,
          CODIG00006 , CODIG00007 , DESCR00003 ,
          NUMER00003 , EXENC00001 , CODIG00008 ,
          DESCR00004 , FECHA00001 , CODIG00009 ,
          CUITR00001 , RAZON00001 , FECHA00002 ,
          PARAM00001 , RESER00001 , OBSER00001 ,
          OBSER00002 , KTIME00001  )

          VALUES (
          :tiporegistroid:Ind.Ind001 ,
          :tiposubregistroid:Ind.Ind002 ,
          :fC3C.codigoorganismo:Ind.Ind003 ,
          :fC3C.numerotramite:Ind.Ind004 ,
          :fC3C.codigotipoaccion:Ind.Ind005 ,
          :fC3C.descrtipoaccion:Ind.Ind006 ,
          :fC3C.tipoformulario:Ind.Ind007 ,
          :fC3C.numeroformulario:Ind.Ind008 ,
          :fC3C.dominionuevo:Ind.Ind009 ,
          :fC3C.dominioviejo:Ind.Ind010 ,
          :fC3C.recibo:Ind.Ind011 ,
          :fC3C.codigomtmfmm:Ind.Ind012 ,
          :origenid:Ind.Ind013 ,
          :fC3C.categoria:Ind.Ind014 ,
          :fC3C.marca:Ind.Ind015 ,
          :fC3C.tipovehiculo:Ind.Ind016 ,
          :fC3C.modelo:Ind.Ind017 ,
          :fC3C.yyyymodelo:Ind.Ind018 ,
          :fC3C.codigotipouso:Ind.Ind019 ,
          :fC3C.descrtipouso:Ind.Ind020 ,
          :fC3C.valuacion:Ind.Ind021 ,
          :fC3C.cantidadpartes:Ind.Ind022 ,
          :fC3C.montoimpuestoadicional:Ind.Ind023 ,
          :fC3C.montopunitorios:Ind.Ind024 ,
          :fC3C.montototalcobrado:Ind.Ind025 ,
          :fC3C.montoabonado:Ind.Ind026 ,
          :fC3C.codigoformapago:Ind.Ind027 ,
          :codigomonedaid:Ind.Ind028 ,
          :fC3C.codigoentidadbancaria:Ind.Ind029 ,
          :fC3C.descrentidadbancaria:Ind.Ind030 ,
          :fC3C.numerocheque:Ind.Ind031 ,
          :fC3C.exencion:Ind.Ind032 ,
          :fC3C.codigoexencion:Ind.Ind033 ,
          :fC3C.descripcionexencion:Ind.Ind034 ,
          :fC3C.fechadeposito:Ind.Ind035 ,
          :fC3C.codigoregistroseccional:Ind.Ind036 ,
          :fC3C.cuitregistroseccional:Ind.Ind037 ,
          :fC3C.razonsocial:Ind.Ind038 ,
          :fC3C.fechaoperacion:Ind.Ind039 ,
          :fC3C.parametrosadicionales:Ind.Ind040 ,
          :fC3C.reservado:Ind.Ind041 ,
          :fC3C.observaciones:Ind.Ind042 ,
          :fC3C.observacionesanulacion:Ind.Ind043 ,
          :fC3C.ktimestamp);

      // *************************************
      // Validamos si la operacion fue exitosa
      if sqlcode = cero;

        // **********************************
        // Realizamos el Commit
        EXEC SQL COMMIT;

        // **********************************
        // Recuperamos el ultimo id  generado
        EXEC SQL values  identity_val_local() into :taxsellosid ;

      ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Nueva IMPUESTOSELLOSPARTES
    //
    dcl-proc InsertIMPUESTOSELLOSPARTES;

      // ********************************************************************
      // funcionalidad del procedimiento
      // ********************************************************************

      clear taxsellospartesid;

      // Realizamos un control por salida de Escape
      EXEC SQL  WHENEVER SQLERROR DO ERRORPROC();

      // Realizamos el impuestosellospartes
      EXEC SQL
        INSERT INTO "IMPUESTOSELLOSPARTES" (
        	TIPOC00001 , TIPOS00001 , TIPOI00001 ,
        	DESCR00001 , TIPOD00001 , NUMER00001 ,
        	CUITC00001 , APELL00001 , PORCE00001 ,
        	CALLE00001 , NUMER00002 , PISO_00001 ,
        	DEPAR00001 , BARRI00001 , LOCAL00001 ,
        	CODIG00001 , PROVI00001 , EXENC00001 ,
        	CODIG00002 , DESCR00002 , CODIG00003 ,
        	DESCR00003 , RESER00001 , KTIME00001 )

          VALUES (
          :tipocuerpoid:Ind.Ind001 ,
          :tiposubregistroid:Ind.Ind002 ,
          :fC3P.tipointerviniente:Ind.Ind003 ,
          :fC3P.descrtipointerviniente:Ind.Ind004 ,
          :tipodocumentoid:Ind.Ind005 ,
          :fC3P.numerodocumento:Ind.Ind006 ,
          :fC3P.cuitcuil:Ind.Ind007 ,
          :fC3P.apellidonombre:Ind.Ind008 ,
          :fC3P.porcentajetitularidad:Ind.Ind009 ,
          :fC3P.calle:Ind.Ind010 ,
          :fC3P.numero:Ind.Ind011 ,
          :fC3P.piso:Ind.Ind012 ,
          :fC3P.departamento:Ind.Ind013 ,
          :fC3P.barrio:Ind.Ind014 ,
          :fC3P.localidad:Ind.Ind015 ,
          :fC3P.codigopostal:Ind.Ind016 ,
          :provinciaid:Ind.Ind017 ,
          :fC3P.exencion:Ind.Ind018 ,
          :fC3P.codigoexencion:Ind.Ind019 ,
          :fC3P.descripcionexencion:Ind.Ind020 ,
          :fC3P.codigotipotramite:Ind.Ind021 ,
          :fC3P.descrtipotramite:Ind.Ind022 ,
          :fC3P.reservado:Ind.Ind023 ,
          :fC3P.ktimestamp );

      // *************************************
      // Validamos si la operacion fue exitosa
      if sqlcode = cero;

        // **********************************
        // Realizamos el Commit
        EXEC SQL COMMIT;

        // **********************************
        // Recuperamos el ultimo id  generado
        EXEC SQL values  identity_val_local() into :taxsellospartesid ;

      ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Nueva IMPUESTOSELLOSPARTESTIPOTRAMITE
    //
    dcl-proc InsertIMPUESTOSELLOSPARTESTIPOTRAMITE;

      // ********************************************************************
      // funcionalidad del procedimiento
      // ********************************************************************

      clear taxsellospartestipotramiteid;

      // Realizamos un control por salida de Escape
      EXEC SQL  WHENEVER SQLERROR DO ERRORPROC();

      // Realizamos el impuestosellospartestipotramirte
      EXEC SQL
        INSERT INTO "IMPUESTOSELLOSPARTESTIPOTRAMITE" (
        	TIPOC00001 , TIPOS00001 , CODIG00001 ,
        	DESCR00001 , MONTO00001 , BASEI00001 ,
        	MONTO00002 , MONTO00003 , MONTO00004 ,
        	MONTO00005 , ALICU00001 , PORCE00001 ,
        	PORCE00002 , FECHA00001 , RESER00001 ,
        	KTIME00001 )

          VALUES (
          :tipocuerpoid:Ind.Ind001 ,
          :tiposubregistroid:Ind.Ind002 ,
          :fC3T.codigotipotramite:Ind.Ind003 ,
          :fC3T.descrtipotramite:Ind.Ind004 ,
          :fC3T.montocontrato:Ind.Ind005  ,
          :fC3T.baseimponible:Ind.Ind006 ,
          :fC3T.montoimpuesto:Ind.Ind007  ,
          :fC3T.montopunitorios:Ind.Ind008 ,
          :fC3T.montofueraregistro:Ind.Ind009 ,
          :fC3T.montoadicional:Ind.Ind010 ,
          :fC3T.alicuota:Ind.Ind011 ,
          :fC3T.porcentajecontrato:Ind.Ind012 ,
          :fC3T.porcentajeimpuesto:Ind.Ind013 ,
          :fC3T.fechacontrato:Ind.Ind014  ,
          :fC3T.reservado:Ind.Ind015 ,
          :fC3T.ktimestamp);

      // *************************************
      // Validamos si la operacion fue exitosa
      if sqlcode = cero;

        // **********************************
        // Realizamos el Commit
        EXEC SQL COMMIT;

        // **********************************
        // Recuperamos el ultimo id  generado
        EXEC SQL values identity_val_local() into :taxsellospartestipotramiteid;

      ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Nueva IMPUESTOAUTOMOTOR
    //
    dcl-proc InsertIMPUESTOAUTOMOTOR;

      // ********************************************************************
      // funcionalidad del procedimiento
      // ********************************************************************

      clear taxautomotorid;

      // Realizamos un control por salida de Escape
      EXEC SQL  WHENEVER SQLERROR DO ERRORPROC();

      // Realizamos el impuestosautomotor
      EXEC SQL
        INSERT INTO "IMPUESTOAUTOMOTOR" (
        	TIPOC00001 , CODIG00001 , NUMER00001 ,
        	CODIG00002 , TIPOR00001 , DOMIN00001 ,
        	DOMIN00002 , YYYY_00001 , NUMER00002 ,
        	FECHA00001 , FECHA00002 , FLAGV00001 ,
        	IMPOR00001 , IMPOR00002 , FECHA00003 ,
        	IMPOR00003 , IMPOR00004 , IMPOR00005 ,
        	CODIG00003 , CODIG00004 , CODIG00005 ,
        	DESCR00001 , NUMER00003 , FECHA00004 ,
        	FECHA00005 , CODIG00006 , DESCR00002 ,
        	RESER00001 , OBSER00001 , KTIME00001 )
          VALUES (
          :tiporegistroid:Ind.Ind001 ,
          :fC4.codigoorganismo:Ind.Ind002 ,
          :fC4.numerotramite:Ind.Ind003 ,
          :codigotipomovimientoid:Ind.Ind004 ,
          :tipocuotaid:Ind.Ind005 ,
          :fC4.dominionuevo:Ind.Ind006 ,
          :fC4.dominioviejo:Ind.Ind007 ,
          :fC4.yyyy:Ind.Ind008 ,
          :fC4.numerocuota:Ind.Ind009 ,
          :fC4.fechabonificacion:Ind.Ind010 ,
          :fC4.fechavencimiento:Ind.Ind011 ,
          :fC4.flagvencimiento:Ind.Ind012 ,
          :fC4.importebonificado:Ind.Ind013 ,
          :fC4.importecomun:Ind.Ind014 ,
          :fC4.fechaproceso:Ind.Ind015 ,
          :fC4.importetotal:Ind.Ind016 ,
          :fC4.importeimpuesto:Ind.Ind017 ,
          :fC4.importepunitorio:Ind.Ind018 ,
          :codigoformapagoid:Ind.Ind019 ,
          :codigomonedaid:Ind.Ind020 ,
          :fC4.codigoentidadbancaria:Ind.Ind021 ,
          :fC4.descrentidadbancaria:Ind.Ind022 ,
          :fC4.numerocheque:Ind.Ind023 ,
          :fC4.fechacobro:Ind.Ind024 ,
          :fC4.fechatransferencia:Ind.Ind025 ,
          :fC4.codigoregistroseccional:Ind.Ind026 ,
          :fC4.descrregistroseccional:Ind.Ind027 ,
          :fC4.reservado:Ind.Ind028 ,
          :fC4.observaciones:Ind.Ind029 ,
          :fC4.ktimestamp);

      // *************************************
      // Validamos si la operacion fue exitosa
      if sqlcode = cero;

        // **********************************
        // Realizamos el Commit
        EXEC SQL COMMIT;

        // **********************************
        // Recuperamos el ultimo id  generado
        EXEC SQL values identity_val_local() into :taxautomotorid;

      ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Nueva INFORMACIONVEHICULO
    //
    dcl-proc InsertINFORMACIONVEHICULO;

      // ********************************************************************
      // funcionalidad del procedimiento
      // ********************************************************************

      clear infvehiculoid;

      // Realizamos un control por salida de Escape
      EXEC SQL  WHENEVER SQLERROR DO ERRORPROC();

      // Realizamos el informacionvehiculo
      EXEC SQL
        INSERT INTO "INFORMACIONVEHICULO" (
        	TIPOR00001 , TIPOS00001 , CODIG00001 ,
        	DOMIN00001 , DOMIN00002 , CODIG00002 ,
        	ORIGE00001 , CATEG00001 , MARCA00001 ,
        	TIPOV00001 , MODEL00001 , YYYYM00001 ,
        	PESO_00001 , CARGA00001 , CILIN00001 ,
        	VALUA00001 , CODIG00003 , DESCR00001 ,
        	FECHA00001 , FECHA00002 , FECHA00003 ,
        	ESTAD00001 , FECHA00004 , GUARD00001 ,
        	CALLE00001 , NUMER00001 , PISO_00001 ,
        	DEPAR00001 , BARRI00001 , LOCAL00001 ,
        	CODIG00004 , PROVI00001 , CANTI00001 ,
        	CODIG00005 , RAZON00001 , FECHA00005 ,
        	RESER00001 , CONTR00001 , KTIME00001 )
          VALUES (
          :tiporegistroid:Ind.Ind001 ,
          :tiposubregistroid:Ind.Ind002 ,
          :fC5C.codigoorganismo:Ind.Ind003 ,
          :fC5C.dominionuevo:Ind.Ind004 ,
          :fC5C.dominioviejo:Ind.Ind005 ,
          :fC5C.codigomtmfmm:Ind.Ind006 ,
          :origenid:Ind.Ind007 ,
          :fC5C.categoria:Ind.Ind008 ,
          :fC5C.marca:Ind.Ind009 ,
          :fC5C.tipovehiculo:Ind.Ind010 ,
          :fC5C.modelo:Ind.Ind011 ,
          :fC5C.yyyymodelo:Ind.Ind012 ,
          :fC5C.peso:Ind.Ind013 ,
          :fC5C.carga:Ind.Ind014 ,
          :fC5C.cilindrada:Ind.Ind015 ,
          :fC5C.valuacion:Ind.Ind016 ,
          :fC5C.codigotipouso:Ind.Ind017 ,
          :fC5C.descrtipouso:Ind.Ind018 ,
          :fC5C.fechainscripcioninicial:Ind.Ind019 ,
          :fC5C.fechaultimatransferencia:Ind.Ind020 ,
          :fC5C.fechaultimomovimiento:Ind.Ind021 ,
          :fC5C.estadodominial:Ind.Ind022 ,
          :fC5C.fechacambioestadodominial:Ind.Ind023 ,
          :fC5C.guardahabitual:Ind.Ind024 ,
          :fC5C.calle:Ind.Ind025 ,
          :fC5C.numero:Ind.Ind026 ,
          :fC5C.piso:Ind.Ind027 ,
          :fC5C.departamento:Ind.Ind028 ,
          :fC5C.barrio:Ind.Ind029 ,
          :fC5C.localidad:Ind.Ind030 ,
          :fC5C.codigopostal:Ind.Ind031 ,
          :provinciaid:Ind.Ind032 ,
          :fC5C.cantidadtitulares:Ind.Ind033 ,
          :fC5C.codigoregistroseccional:Ind.Ind034 ,
          :fC5C.razonsocial:Ind.Ind035 ,
          :fC5C.fechaoperacion:Ind.Ind036 ,
          :fC5C.reservado:Ind.Ind037 ,
          :fC5C.controlsucerp:Ind.Ind038 ,
          :fC5C.ktimestamp);

      // *************************************
      // Validamos si la operacion fue exitosa
      if sqlcode = cero;

        // **********************************
        // Realizamos el Commit
        EXEC SQL COMMIT;

        // **********************************
        // Recuperamos el ultimo id  generado
        EXEC SQL values identity_val_local() into :infvehiculoid;

      ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Nueva INFORMACIONVEHICULOTITULAR
    //
    dcl-proc InsertINFORMACIONVEHICULOTITULAR;

      // ********************************************************************
      // funcionalidad del procedimiento
      // ********************************************************************

      clear infvehiculotitularid;

      // Realizamos un control por salida de Escape
      EXEC SQL  WHENEVER SQLERROR DO ERRORPROC();

      // Realizamos el informacioradicacion
      EXEC SQL
        INSERT INTO "INFORMACIONVEHICULOTITULAR" (
        	TIPOC00001 , TIPOS00001 , TIPOD00001 ,
        	NUMER00001 , CUITC00001 , APELL00001 ,
        	PORCE00001 , CALLE00001 , NUMER00002 ,
        	PISO_00001 , DEPAR00001 , BARRI00001 ,
        	LOCAL00001 , CODIG00001 , PROVI00001 ,
        	RESER00001 , INFVE00002 , KTIME00001 )

          VALUES (
          :tipocuerpoid:Ind.Ind001 ,
          :tiposubregistroid:Ind.Ind002 ,
          :tipodocumentoid:Ind.Ind003 ,
          :fC5T.numerodocumento:Ind.Ind004 ,
          :fC5T.cuitcuil:Ind.Ind005 ,
          :fC5T.apellidonombre:Ind.Ind006 ,
          :fC5T.porcentajetitularidad:Ind.Ind007 ,
          :fC5T.calle:Ind.Ind008 ,
          :fC5T.numero:Ind.Ind009 ,
          :fC5T.piso:Ind.Ind010 ,
          :fC5T.departamento:Ind.Ind011 ,
          :fC5T.barrio:Ind.Ind012 ,
          :fC5T.localidad:Ind.Ind013 ,
          :fC5T.codigopostal:Ind.Ind014 ,
          :provinciaid:Ind.Ind015 ,
          :fC5T.reservado:Ind.Ind016 ,
          NULL,
          :fC5T.ktimestamp);

      // *************************************
      // Validamos si la operacion fue exitosa
      if sqlcode = cero;

        // **********************************
        // Realizamos el Commit
        EXEC SQL COMMIT;

        // **********************************
        // Recuperamos el ultimo id  generado
        EXEC SQL values  identity_val_local() into :infvehiculotitularid ;

      ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Nueva CAMBIOTITULARIDAD
    //
    dcl-proc InsertCAMBIOTITULARIDAD;

      // ********************************************************************
      // funcionalidad del procedimiento
      // ********************************************************************

      clear cambiotitularidadid;

      // Realizamos un control por salida de Escape
      EXEC SQL  WHENEVER SQLERROR DO ERRORPROC();

      // Realizamos el informacioradicacion
      EXEC SQL
        INSERT INTO "CAMBIOTITULARIDAD" (
        	TIPOR00001 , TIPOS00001 , CODIG00001 ,
        	NUMER00001 , CODIG00002 , DESCR00001 ,
        	CODIG00003 , DESCR00002 , TIPOF00001 ,
        	NUMER00002 , DOMIN00001 , DOMIN00002 ,
        	CODIG00004 , ORIGE00001 , CATEG00001 ,
        	MARCA00001 , TIPOV00001 , MODEL00001 ,
        	YYYYM00001 , PESO_00001 , CARGA00001 ,
        	CILIN00001 , VALUA00001 , CODIG00005 ,
        	DESCR00003 , FECHA00001 , TIPOD00001 ,
        	NUMER00003 , CUITC00001 , APENO00001 ,
        	CALLE00001 , NUMER00004 , PISO_00001 ,
        	DEPAR00001 , BARRI00001 , LOCAL00001 ,
        	CODIG00006 , PROVI00001 , CANTI00001 ,
        	CODIG00007 , RAZON00001 , FECHA00002 ,
        	PARAM00001 , RESER00001 , OBSER00001 ,
        	CAMBI00002 , KTIME00001 )

          VALUES (
          :tiporegistroid:Ind.Ind002 ,
          :tiposubregistroid:Ind.Ind003 ,
          :fC6C.codigoorganismo:Ind.Ind004 ,
          :fC6C.numerotramite:Ind.Ind005 ,
          :fC6C.codigotipotramite:Ind.Ind006 ,
          :fC6C.dscrtipotramite:Ind.Ind007 ,
          :fC6C.codigotipoaccion:Ind.Ind008 ,
          :fC6C.descrtipoaccion:Ind.Ind009 ,
          :fC6C.tipoformulario:Ind.Ind010 ,
          :fC6C.numeroformulario:Ind.Ind011 ,
          :fC6C.dominionuevo:Ind.Ind012 ,
          :fC6C.dominioviejo:Ind.Ind013 ,
          :fC6C.codigomtmfmm:Ind.Ind014 ,
          :origenid:Ind.Ind015 ,
          :fC6C.categoria:Ind.Ind016 ,
          :fC6C.marca:Ind.Ind017 ,
          :fC6C.tipovehiculo:Ind.Ind018 ,
          :fC6C.modelo:Ind.Ind019 ,
          :fC6C.yyyymodelo:Ind.Ind020 ,
          :fC6C.peso:Ind.Ind021 ,
          :fC6C.carga:Ind.Ind022 ,
          :fC6C.cilindrada:Ind.Ind023 ,
          :fC6C.valuacion:Ind.Ind024 ,
          :fC6C.codigotipouso:Ind.Ind025 ,
          :fC6C.descrtipouso:Ind.Ind026 ,
          :fC6C.fechavigencia:Ind.Ind027 ,
          :tipodocumentoid:Ind.Ind028 ,
          :fC6C.numerodocumento:Ind.Ind029 ,
          :fC6C.cuitcuil:Ind.Ind030 ,
          :fC6C.apellidonombre:Ind.Ind031 ,
          :fC6C.calle:Ind.Ind032 ,
          :fC6C.numero:Ind.Ind033 ,
          :fC6C.piso:Ind.Ind034 ,
          :fC6C.departamento:Ind.Ind035 ,
          :fC6C.barrio:Ind.Ind036 ,
          :fC6C.localidad:Ind.Ind037 ,
          :fC6C.codigopostal:Ind.Ind038 ,
          :provinciaid:Ind.Ind039 ,
          :fC6C.cantidadtitulares:Ind.Ind040 ,
          :fC6C.codigoregistroseccional:Ind.Ind041 ,
          :fC6C.razonsocial:Ind.Ind042 ,
          :fC6C.fechaoperacion:Ind.Ind043 ,
          :fC6C.parametrosadicionales:Ind.Ind044 ,
          :fC6C.reservado:Ind.Ind045 ,
          :fC6C.observaciones:Ind.Ind046 ,
          NULL, :fC6C.ktimestamp);

      // *************************************
      // Validamos si la operacion fue exitosa
      if sqlcode = cero;

        // **********************************
        // Realizamos el Commit
        EXEC SQL COMMIT;

        // **********************************
        // Recuperamos el ultimo id  generado
        EXEC SQL values identity_val_local() into :cambiotitularidadid;

      ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Nueva CAMBIOTITULARIDADTITULAR
    //
    dcl-proc InsertCAMBIOTITULARIDADTITULAR;

      // ********************************************************************
      // funcionalidad del procedimiento
      // ********************************************************************

      clear cambiotitularidadtitid;

      // Realizamos un control por salida de Escape
      EXEC SQL  WHENEVER SQLERROR DO ERRORPROC();

      // Realizamos el informacioradicacion
      EXEC SQL
        INSERT INTO "CAMBIOTITULARIDADTITULAR" (
        	TIPOC00001 , TIPOS00001 , TIPOT00001 ,
        	TIPOD00001 , NUMER00001 , CUITC00001 ,
        	APELL00001 , PORCE00001 , CALLE00001 ,
        	NUMER00002 , PISO_00001 , DEPAR00001 ,
        	BARRI00001 , LOCAL00001 , CODIG00001 ,
        	PROVI00001 , RESER00001 , KTIME00001 )

          VALUES (
          :tiporegistroid:Ind.Ind001 ,
          :tiposubregistroid:Ind.Ind002 ,
          :tipotitularid:Ind.Ind003 ,
          :tipodocumentoid:Ind.Ind004 ,
          :fC6T.numerodocumento:Ind.Ind005 ,
          :fC6T.cuitcuil:Ind.Ind006 ,
          :fC6T.apellidonombre:Ind.Ind007 ,
          :fC6T.porcentajetitularidad:Ind.Ind008 ,
          :fC6T.calle:Ind.Ind009 ,
          :fC6T.numero:Ind.Ind010 ,
          :fC6T.piso:Ind.Ind011 ,
          :fC6T.departamento:Ind.Ind012 ,
          :fC6T.barrio:Ind.Ind013 ,
          :fC6T.localidad:Ind.Ind014 ,
          :fC6T.codigopostal:Ind.Ind015 ,
          :provinciaid:Ind.Ind016 ,
          :fC6T.reservado:Ind.Ind017 ,
          :fC6T.ktimestamp);

      // *************************************
      // Validamos si la operacion fue exitosa
      if sqlcode = cero;

        // **********************************
        // Realizamos el Commit
        EXEC SQL COMMIT;

        // **********************************
        // Recuperamos el ultimo id  generado
        EXEC SQL values identity_val_local() into :cambiotitularidadtitid;

      ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Nueva INFORMACIORADICACION
    //
    dcl-proc InsertINFORMACIORADICACION;

      // ********************************************************************
      // funcionalidad del procedimiento
      // ********************************************************************

      clear infradicacionid;

      // Realizamos un control por salida de Escape
      EXEC SQL  WHENEVER SQLERROR DO ERRORPROC();

      // Realizamos el informacioradicacion
      EXEC SQL
        INSERT INTO "INFORMACIORADICACION" (
        	TIPOR00001 , CODIG00001 , DOMIN00001 ,
        	ESTAD00001 , TIPOR00002 , FECHA00001 ,
        	FECHA00002 , ORIGE00001 , CODIG00002 ,
        	RAZON00001 , RESER00001 , OBSER00001 ,
        	KTIME00001 )

          VALUES (
          :tiporegistroid:Ind.Ind001 ,
          :fC7.codigoorganismo:Ind.Ind002 ,
          :fC7.dominio:Ind.Ind003 ,
          :fC7.estado:Ind.Ind004 ,
          :fC7.tipo:Ind.Ind005 ,
          :fC7.fechaalta:Ind.Ind006 ,
          :fC7.fechabaja:Ind.Ind007 ,
          :fC7.origeninformacion:Ind.Ind008 ,
          :fC7.codigoregistroseccional:Ind.Ind009 ,
          :fC7.razonsocialregistroseccional:Ind.Ind010 ,
          :fC7.reservado:Ind.Ind011 ,
          :fC7.observaciones:Ind.Ind012 ,
          :fC7.ktimestamp);

      // *************************************
      // Validamos si la operacion fue exitosa
      if sqlcode = cero;

        // **********************************
        // Realizamos el Commit
        EXEC SQL COMMIT;

        // **********************************
        // Recuperamos el ultimo id  generado
        EXEC SQL values identity_val_local() into :infradicacionid;

      ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Nueva ANULACIONTRAMITESSELLOS
    //
    dcl-proc InsertANULACIONTRAMITESSELLOS;

      // ********************************************************************
      // funcionalidad del procedimiento
      // ********************************************************************

      clear anultramitesellosid;

      // Realizamos un control por salida de Escape
      EXEC SQL  WHENEVER SQLERROR DO ERRORPROC();

      // Realizamos el informacioradicacion
      EXEC SQL
        INSERT INTO "ANULACIONTRAMITESSELLOS" (
        	TIPOR00001 , TIPOS00001 , CODIG00001 ,
        	TIPOA00001 , NUMER00001 , CODIG00002 ,
        	DESCR00001 , CODIG00003 , DESCR00002 ,
        	TIPOF00001 , NUMER00002 , DOMIN00001 ,
        	DOMIN00002 , NUMER00003 , CODIG00004 ,
        	ORIGE00001 , CATEG00001 , MARCA00001 ,
        	TIPOV00001 , MODEL00001 , YYYYM00001 ,
        	FECHA00001 , MONTO00001 , MONTO00002 ,
        	MONTO00003 , MONTO00004 , CODIG00005 ,
        	CODIG00006 , CODIG00007 , DESCR00003 ,
        	NUMER00004 , FECHA00002 , FECHA00003 ,
        	FECHA00004 , FECHA00005 , CANTI00001 ,
        	CODIG00008 , DESCR00004 , RESER00001 ,
        	OBSER00001 , KTIME00001 )

          VALUES (
          :tiporegistroid:Ind.Ind001 ,
          :tiposubregistroid:Ind.Ind002 ,
          :fC8C.codigoorganismo:Ind.Ind003 ,
          :fC8C.tipoanulacion:Ind.Ind004 ,
          :fC8C.numerotramite:Ind.Ind005 ,
          :fC8C.codigotipotramite:Ind.Ind006 ,
          :fC8C.dscrtipotramite:Ind.Ind007 ,
          :fC8C.codigotipoaccion:Ind.Ind008 ,
          :fC8C.descrtipoaccion:Ind.Ind009 ,
          :fC8C.tipoformulario:Ind.Ind010 ,
          :fC8C.numeroformulario:Ind.Ind011 ,
          :fC8C.dominionuevo:Ind.Ind012 ,
          :fC8C.dominioviejo:Ind.Ind013 ,
          :fC8C.numerorecibo:Ind.Ind014 ,
          :fC8C.codigomtmfmm:Ind.Ind015 ,
          :origenid:Ind.Ind016 ,
          :fC8C.categoria:Ind.Ind017 ,
          :fC8C.marca:Ind.Ind018 ,
          :fC8C.tipovehiculo:Ind.Ind019 ,
          :fC8C.modelo:Ind.Ind020 ,
          :fC8C.yyyymodelo:Ind.Ind021 ,
          :fC8C.fechavigenciacontrato:Ind.Ind022 ,
          :fC8C.importetotal:Ind.Ind023 ,
          :fC8C.importeimpuesto:Ind.Ind024 ,
          :fC8C.importepunitorio:Ind.Ind025 ,
          :fC8C.importeadicional:Ind.Ind026 ,
          :codigoformapagoid:Ind.Ind027 ,
          :codigomonedaid:Ind.Ind028 ,
          :fC8C.codigoentidadbancaria:Ind.Ind029 ,
          :fC8C.descrentidadbancaria:Ind.Ind030 ,
          :fC8C.numerocheque:Ind.Ind031 ,
          :fC8C.fechatramite:Ind.Ind032 ,
          :fC8C.fechacobro:Ind.Ind033 ,
          :fC8C.fechadeposito:Ind.Ind034 ,
          :fC8C.fechabaja:Ind.Ind035 ,
          :fC8C.cantidaddetalles:Ind.Ind036 ,
          :fC8C.codigoregistroseccional:Ind.Ind037 ,
          :fC8C.descrregistroseccional:Ind.Ind038 ,
          :fC8C.reservado:Ind.Ind039 ,
          :fC8C.observaciones:Ind.Ind040 ,
          :fC8C.ktimestamp);

      // *************************************
      // Validamos si la operacion fue exitosa
      if sqlcode = cero;

        // **********************************
        // Realizamos el Commit
        EXEC SQL COMMIT;

        // **********************************
        // Recuperamos el ultimo id  generado
        EXEC SQL values  identity_val_local() into :anultramitesellosid ;

      ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Nueva ANULACIONTRAMITESSELLOSDETALLE
    //
    dcl-proc InsertANULACIONTRAMITESSELLOSDETALLE;

      // ********************************************************************
      // funcionalidad del procedimiento
      // ********************************************************************

      clear anultramitesellosdetid;

      // Realizamos un control por salida de Escape
      EXEC SQL  WHENEVER SQLERROR DO ERRORPROC();

      // Realizamos el informacioradicacion
      EXEC SQL
        INSERT INTO "ANULACIONTRAMITESSELLOSDETALLE" (
        	TIPOR00001 , TIPOS00001 , YYYY_00001 ,
        	NUMER00001 , TIPOC00001 , IMPOR00001 ,
        	IMPOR00002 , IMPOR00003 , IMPOR00004 ,
        	RESER00001 , OBSER00001 , ANULT00002 ,
        	KTIME00001 )

          VALUES (
          :tiporegistroid:Ind.Ind001 ,
          :tiposubregistroid:Ind.Ind002 ,
          :fC8D.yyyy:Ind.Ind003 ,
          :fC8D.numerocuota:Ind.Ind004 ,
          :tipocuotaid:Ind.Ind005 ,
          :fC8D.importetotal:Ind.Ind006 ,
          :fC8D.importeimpuesto:Ind.Ind007 ,
          :fC8D.importepunitorio:Ind.Ind008 ,
          :fC8D.importeadicional:Ind.Ind009 ,
          :fC8D.reservado:Ind.Ind010 ,
          :fC8D.observaciones:Ind.Ind011 ,
          NULL, :fC8D.ktimestamp);

      // *************************************
      // Validamos si la operacion fue exitosa
      if sqlcode = cero;

        // **********************************
        // Realizamos el Commit
        EXEC SQL COMMIT;

        // **********************************
        // Recuperamos el ultimo id  generado
        EXEC SQL values  identity_val_local() into :anultramitesellosdetid ;

      ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Nueva TRAMITESGENERALES
    //
    dcl-proc InsertTRAMITESGENERALES;

      // ********************************************************************
      // funcionalidad del procedimiento
      // ********************************************************************

      clear tramitesgeneralesid;

      // Realizamos un control por salida de Escape
      EXEC SQL  WHENEVER SQLERROR DO ERRORPROC();

      // Realizamos el informacioradicacion
      EXEC SQL
        INSERT INTO "TRAMITESGENERALES" (
        	TIPOR00001 , TIPOS00001 , CODIG00001 ,
        	NUMER00001 , CODIG00002 , DESCR00001 ,
        	CODIG00003 , DESCR00002 , TIPOF00001 ,
        	NUMER00002 , DOMIN00001 , DOMIN00002 ,
        	CODIG00004 , ORIGE00001 , CATEG00001 ,
        	MARCA00001 , TIPOV00001 , MODEL00001 ,
        	YYYYM00001 , PESO_00001 , CARGA00001 ,
          CILIN00001 , VALUA00001 , CODIG00005 ,
        	DESCR00003 , FECHA00001 , TIPOD00001 ,
        	NUMER00003 , CUITC00001 , APENO00001 ,
        	CALLE00001 , NUMER00004 , PISO_00001 ,
        	DEPAR00001 , BARRI00001 , TRAMI00002 ,
        	KTIME00001 )

          VALUES (
          :tiporegistroid:Ind.Ind001 ,
          :tiposubregistroid:Ind.Ind002 ,
          :fC9C.codigoorganismo:Ind.Ind003 ,
          :fC9C.numerotramite:Ind.Ind004 ,
          :fC9C.codigotipotramite:Ind.Ind005 ,
          :fC9C.dscrtipotramite:Ind.Ind006 ,
          :fC9C.codigotipoaccion:Ind.Ind007 ,
          :fC9C.descrtipoaccion:Ind.Ind008 ,
          :fC9C.tipoformulario:Ind.Ind009 ,
          :fC9C.numeroformulario:Ind.Ind010 ,
          :fC9C.dominionuevo:Ind.Ind011 ,
          :fC9C.dominioviejo:Ind.Ind012 ,
          :fC9C.codigomtmfmm:Ind.Ind013 ,
          :origenid:Ind.Ind014 ,
          :fC9C.categoria:Ind.Ind015 ,
          :fC9C.marca:Ind.Ind016 ,
          :fC9C.tipovehiculo:Ind.Ind017 ,
          :fC9C.modelo:Ind.Ind018 ,
          :fC9C.yyyymodelo:Ind.Ind019 ,
          :fC9C.peso:Ind.Ind020 ,
          :fC9C.carga:Ind.Ind021 ,
          :fC9C.cilindrada:Ind.Ind022 ,
          :fC9C.valuacion:Ind.Ind023 ,
          :fC9C.codigotipouso:Ind.Ind024 ,
          :fC9C.descrtipouso:Ind.Ind025 ,
          :fC9C.fechavigencia:Ind.Ind026 ,
          :tipodocumentoid:Ind.Ind027 ,
          :fC9C.numerodocumento:Ind.Ind028 ,
          :fC9C.cuitcuil:Ind.Ind029 ,
          :fC9C.apenomrazonsocial:Ind.Ind030 ,
          :fC9C.calle:Ind.Ind031 ,
          :fC9C.numero:Ind.Ind032 ,
          :fC9C.piso:Ind.Ind033 ,
          :fC9C.departamento:Ind.Ind034 ,
          :fC9C.barrio:Ind.Ind035 ,
          NULL, :fC9C.ktimestamp );

      // *************************************
      // Validamos si la operacion fue exitosa
      if sqlcode = cero;

        // **********************************
        // Realizamos el Commit
        EXEC SQL COMMIT;

        // **********************************
        // Recuperamos el ultimo id  generado
        EXEC SQL values  identity_val_local() into :tramitesgeneralesid ;


      ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Nueva TRAMITESGENERALESTITULARES
    //
    dcl-proc InsertTRAMITESGENERALESTITULARES;

      // ********************************************************************
      // funcionalidad del procedimiento
      // ********************************************************************

      clear tramitesgeneralestitid;

      // Realizamos un control por salida de Escape
      EXEC SQL  WHENEVER SQLERROR DO ERRORPROC();

      // Realizamos el informacioradicacion
      EXEC SQL
        INSERT INTO "TRAMITESGENERALESTITULARES" (
        	TIPOR00001 , TIPOS00001 , TIPOT00001 ,
        	TIPOD00001 , NUMER00001 , CUITC00001 ,
        	APELL00001 , PORCE00001 , CALLE00001 ,
        	NUMER00002 , PISO_00001 , DEPAR00001 ,
        	BARRI00001 , LOCAL00001 , CODIG00001 ,
        	PROVI00001 , RESER00001 , KTIME00001 )

          VALUES (
          :tiporegistroid:Ind.Ind001 ,
          :tiposubregistroid:Ind.Ind002 ,
          :tipotitularid:Ind.Ind003 ,
          :tipodocumentoid:Ind.Ind004 ,
          :fC9T.numerodocumento:Ind.Ind005 ,
          :fC9T.cuitcuil:Ind.Ind006 ,
          :fC9T.apellidonombre:Ind.Ind007 ,
          :fC9T.porcentajetitularidad:Ind.Ind008 ,
          :fC9T.calle:Ind.Ind009 ,
          :fC9T.numero:Ind.Ind010 ,
          :fC9T.piso:Ind.Ind011 ,
          :fC9T.departamento:Ind.Ind012 ,
          :fC9T.barrio:Ind.Ind013 ,
          :fC9T.localidad:Ind.Ind014 ,
          :fC9T.codigopostal:Ind.Ind015 ,
          :provinciaid:Ind.Ind016 ,
          :fC9T.reservado:Ind.Ind017 ,
          :fC9T.ktimestamp );

      // *************************************
      // Validamos si la operacion fue exitosa
      if sqlcode = cero;

        // **********************************
        // Realizamos el Commit
        EXEC SQL COMMIT;

        // **********************************
        // Recuperamos el ultimo id  generado
        EXEC SQL values  identity_val_local() into :tramitesgeneralestitid ;

      ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Nueva PIE
    //
    dcl-proc InsertPIE;

      // ********************************************************************
      // funcionalidad del procedimiento
      // ********************************************************************

      clear pieid;

      // Realizamos un control por salida de Escape
      EXEC SQL  WHENEVER SQLERROR DO ERRORPROC();

      // Realizamos el informacioradicacion
      EXEC SQL
        INSERT INTO PIE (
        	 TIPOR00001 , CANTI00001 , CHECK00001 ,
        	 KTIME00001 )

          VALUES (
          :tiporegistroid:Ind.Ind001 ,
          :fP0.cantidadregistros:Ind.Ind002 ,
          :fP0.checksum:Ind.Ind003 ,
          :fP0.ktimestamp);

      // *************************************
      // Validamos si la operacion fue exitosa
      if sqlcode = cero;

        // **********************************
        // Realizamos el Commit
        EXEC SQL COMMIT;

        // **********************************
        // Recuperamos el ultimo id  generado
        EXEC SQL values  identity_val_local() into :pieid ;

      ENDIF;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // UpdateTitularINFORMACIONVEHICULOTITULAR
    //
    dcl-proc UpdateTitularINFORMACIONVEHICULOTITULAR;
        dcl-pi *n;
            parmtipodocumento pointer value;
            parmnumerodocumento pointer value;
            parmcuitcuil pointer value;

        end-pi;

        // Tipo Documento
        dcl-s tipodocumentoBase like(tipodocumento) nullind 
                                                based(parmtipodocumento);
        // Nro Documento
        dcl-s numerodocumentoBase like(numerodocumento) nullind 
                                                based(parmnumerodocumento);
        // Cuit/Cuil
        dcl-s cuitcuilBase like(cuitcuil) nullind based(parmcuitcuil);


      // ********************************************************************
      // funcionalidad del procedimiento
      // ********************************************************************

      // Obtenemos el tipodocumentoid
      FindTipoDocumento(parmtipodocumento);

      // *************************************
      // Actualizamos INFORMACIONVEHICULO
       EXEC SQL DECLARE C2 DYNAMIC SCROLL CURSOR FOR
           SELECT A."infvehiculoid", B."tipodocumentoid",
                  B."numerodocumento", B."cuitcuil"
           FROM  "INFORMACIONVEHICULO" A,
                 "INFORMACIONVEHICULOTITULAR" B,
                 "ALTAIMPOSITIVA" C,
                 "ALTAIMPOSITIVATITULAR" D
           WHERE ((A."dominionuevo" = C."dominionuevo") OR
                  (A."dominioviejo" = C."dominioviejo") OR
                  (A."codigomtmfmm" = C."codigomtmfmm") ) AND
                 ( C."altataxtitularid" = D."altataxtitularid" ) AND
                 ((B."tipodocumentoid" = :tipodocumentoid) AND
                  (B."numerodocumento" = :numerodocumentoBase)) OR
                  (B."cuitcuil" = :cuitcuilBase) ;

      // abrimos el cursor
      EXEC SQL OPEN C2;

      // Navegamos por el cursor
      DOW SQLCODE = cero;

        // Recuperamos el id de ALTAIMPOSITIVA altataxtitularid
        EXEC SQL FETCH FROM C2 INTO :infvehiculoid, :tipodocumentoid,
                                    :numerodocumento, :cuitcuil ;

        // Si es Fin de Archivo
        IF SQLCODE = noexiste;
            LEAVE;
        ENDIF;

        // Actualizamos BAJAIMPOSITIVA para relacionar con BAJAIMPOSITIVATITULAR
        //  Y ALTAIMPOSITIVA
        EXEC SQL UPDATE "INFORMACIONVEHICULOTITULAR" 
                    SET INFVE00002 = :infvehiculoid
                    WHERE (("tipodocumentoid" = :tipodocumentoid) AND
                           ("numerodocumento" = :numerodocumento)) OR
                          ("cuitcuil" = :cuitcuil) ;
      ENDDO;

      // cerramos el cursor
      EXEC SQL CLOSE C2;


    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Nueva UpdateTitularBAJAIMPOSITIVATITULAR
    //
    dcl-proc UpdateTitularBAJAIMPOSITIVATITULAR;
        dcl-pi *n;
            parmtipodocumento pointer value;
            parmnumerodocumento pointer value;
            parmcuitcuil pointer value;

        end-pi;

        // Tipo Documento
        dcl-s tipodocumentoBase like(tipodocumento) nullind 
                                              based(parmtipodocumento);
        // Nro Documento
        dcl-s numerodocumentoBase like(numerodocumento) nullind 
                                              based(parmnumerodocumento);
        // Cuit/Cuil
        dcl-s cuitcuilBase like(cuitcuil) nullind based(parmcuitcuil);

      // ********************************************************************
      // funcionalidad del procedimiento
      // ********************************************************************
      // Realizamos el bajaimpositivatitular

      // Obtenemos el tipodocumentoid
      FindTipoDocumento(parmtipodocumento);


      // *************************************
      // Actualizamos BAJAIMPOSITIVA
      EXEC SQL DECLARE C1 DYNAMIC SCROLL CURSOR FOR
           SELECT A."altataxtitularid", A."dominionuevo", 
                  A."dominioviejo", A."codigomtmfmm"
           FROM "ALTAIMPOSITIVA" A, "BAJAIMPOSITIVA" B
           WHERE ((A."tipodocumentoid" = :tipodocumentoid) AND
                  (A."numerodocumento" = :numerodocumentoBase)) OR
                  (A."cuitcuil"        = :cuitcuilBase) AND
                 ((A."dominionuevo" = B."dominionuevo") OR
                  (A."dominioviejo" = B."dominioviejo") OR
                  (A."codigomtmfmm" = B."codigomtmfmm") );


      // abrimos el cursor
      EXEC SQL OPEN C1;

      // Navegamos por el cursor
      DOW SQLCODE = cero;

        // Recuperamos el id de ALTAIMPOSITIVA altataxtitularid
        EXEC SQL FETCH FROM C1 INTO :altataxtitularid, :dominionuevo,
                                    :dominioviejo, :codigomtmfmm ;

        // Si es Fin de Archivo
        IF SQLCODE = noexiste;
           LEAVE;
        ENDIF;

        // Actualizamos BAJAIMPOSITIVA para relacionar con BAJAIMPOSITIVATITULAR
        //  Y ALTAIMPOSITIVA
        EXEC SQL UPDATE "BAJAIMPOSITIVA" SET BAJAT00002 = :altataxtitularid
                    WHERE (("dominionuevo" = :dominionuevo) OR
                           ("dominioviejo" = :dominioviejo) OR
                           ("codigomtmfmm" = :codigomtmfmm) );
      ENDDO;

      // cerramos el cursor
      EXEC SQL CLOSE C1;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Nueva UpdateInsertALTAIMPOSITIVATITULAR
    //
    dcl-proc UpdateInsertALTAIMPOSITIVATITULAR;

        dcl-pi *n;
            parmtipodocumento pointer value;
            parmnumerodocumento pointer value;
            parmcuitcuil pointer value;

        end-pi;

        // Tipo Documento
        dcl-s tipodocumentoBase like(tipodocumento) nullind 
                                              based(parmtipodocumento);
        // Nro Documento
        dcl-s numerodocumentoBase like(numerodocumento) nullind 
                                              based(parmnumerodocumento);
        // Cuit/Cuil
        dcl-s cuitcuilBase like(cuitcuil) nullind based(parmcuitcuil);


      // ********************************************************************
      // funcionalidad del procedimiento
      // ********************************************************************
      // Obtenemos el tipodocumentoid
      FindTipoDocumento(parmtipodocumento);

      // *************************************
      // Actualizamos ALTAIMPOSITIVA
      EXEC SQL DECLARE C0 DYNAMIC SCROLL CURSOR FOR
          SELECT "altataxid"
          FROM "ALTAIMPOSITIVA"
          WHERE ("tipodocumentoid" = :tipodocumentoid AND
                 "numerodocumento" = :numerodocumentoBase) OR
                 ("cuitcuil"       = :cuitcuilBase) ;

      // abrimos el cursor
      EXEC SQL OPEN C0;

      // Navegamos por el cursor
      DOW SQLCODE = cero;

        // Recuperamos el id de ALTAIMPOSITIVA
        EXEC SQL FETCH FROM C0 INTO :altataxid ;

        // Si es Fin de Archivo
        IF SQLCODE = noexiste;
           LEAVE;
        ENDIF;

        // Actualizamos ALTAIMPOSITIVA para relacionar con ALTAIMPOSITIVATITULAR
        EXEC SQL UPDATE "ALTAIMPOSITIVA" 
                    SET "altataxtitularid" = :altataxtitularid
                    WHERE "altataxid" = :altataxid ;

      ENDDO;

      // cerramos el cursor
      EXEC SQL CLOSE C0;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Validacion de IMPUESTOSELLOS
    //
    //      parmdominionuevo Es la direccion de memoria de la variable
    //      parmdominioviejo Es la direccion de memoria de la variable
    //      parmcodigomtmfmm Es la direccion de memoria de la variable
    dcl-proc FindIMPUESTOSELLOS;

        dcl-pi *n;
            parmdominionuevo pointer value;
            parmdominioviejo pointer value;
            parmcodigomtmfmm pointer value;

        end-pi;

        // Codigo Sucerp
        dcl-s codigomtmfmmBase like(codigomtmfmm) nullind 
                                based(parmcodigomtmfmm);

        // Dominio Nuevo
        dcl-s dominionuevoBase like(dominionuevo) nullind 
                                based(parmdominionuevo);

        // Dominio Viejo
        dcl-s dominioviejoBase like(dominioviejo) nullind 
                                based(parmdominioviejo);

        // ********************************************************************
        // funcionalidad del procedimiento
        // ********************************************************************
        clear taxsellosid ;

        // **********************************************
        // Validamos si existe el IMPUESTOSELLOS
        EXEC SQL
             SELECT "taxsellosid" INTO :taxsellosid
               FROM "IMPUESTOSELLOS"
               WHERE  ( "dominionuevo" = :dominionuevoBase ) AND
                      ( "dominioviejo" = :dominioviejoBase ) AND
                      ( "codigomtmfmm" = :codigomtmfmmBase );

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Validacion de IMPUESTOSELLOSPARTES
    //
    //      parmdominionuevo Es la direccion de memoria de la variable
    //      parmdominioviejo Es la direccion de memoria de la variable
    //      parmcodigomtmfmm Es la direccion de memoria de la variable
    dcl-proc FindIMPUESTOSELLOSPARTES;

        dcl-pi *n;
            parmtipodocumento pointer value;
            parmnumerodocumento pointer value;
            parmcuitcuil pointer value;

        end-pi;

        // Tipo Documento
        dcl-s tipodocumentoBase like(tipodocumento) nullind 
                                              based(parmtipodocumento);
        // Nro Documento
        dcl-s numerodocumentoBase like(numerodocumento) nullind 
                                              based(parmnumerodocumento);
        // Cuit/Cuil
        dcl-s cuitcuilBase like(cuitcuil) nullind based(parmcuitcuil);

        // ********************************************************************
        // funcionalidad del procedimiento
        // ********************************************************************
        clear taxsellospartesid ;

        // Obtenemos el tipodocumentoid
        FindTipoDocumento(parmtipodocumento);

        // **********************************************
        // Validamos si existe el IMPUESTOSELLOS
        EXEC SQL
            SELECT "taxsellospartesid" INTO :taxsellospartesid
              FROM "IMPUESTOSELLOSPARTES"
              WHERE ("tipodocumentoid" = :tipodocumentoid AND
                     "numerodocumento" = :numerodocumentoBase) OR
                    ("cuitcuil"        = :cuitcuilBase) ;

    end-proc;

    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    // Validacion de IMPUESTOSELLOSPARTES
    //        EXEC SQL  WHENEVER SQLERROR DO ERRORPROC();
    //      parmdominionuevo Es la direccion de memoria de la variable
    //      parmdominioviejo Es la direccion de memoria de la variable
    //      parmcodigomtmfmm Es la direccion de memoria de la variable
    dcl-proc ERRORPROC;

      // *************************************
      // Validamos si la operacion fue exitosa
      if sqlcode = cero;

          // **********************************
          // Realizamos el Commit
          EXEC SQL COMMIT;

      ENDIF;

    end-proc;

 