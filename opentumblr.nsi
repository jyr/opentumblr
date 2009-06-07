;--------------------------------
;Include Modern UI

  !include "MUI2.nsh"

;Algoritmo de compresi�n
SetCompressor lzma


;--------------------------------
;Confirmaci�n para abortar la instalaci�n
;Esta macro debe colocarse en esta posici�n del script sino no funcionara
  !define mui_abortwarning

;Definimos variable VERSION
!define VERSION "0.0.3"


;--------------------------------
;Pages

  ;Mostramos la p�gina de bienvenida
  !insertmacro MUI_PAGE_WELCOME
  ;P�gina donde mostramos el contrato de licencia 
  ;!insertmacro MUI_PAGE_LICENSE "licencia.txt"
  ;p�gina donde se muestran las distintas secciones definidas
  ;!insertmacro MUI_PAGE_COMPONENTS
  ;p�gina donde se selecciona el directorio donde instalar nuestra aplicacion
  !insertmacro MUI_PAGE_DIRECTORY
  ;p�gina de instalaci�n de ficheros
  !insertmacro MUI_PAGE_INSTFILES
  ;p�gina final
  !insertmacro MUI_PAGE_FINISH
  
;p�ginas referentes al desinstalador
  !insertmacro MUI_UNPAGE_WELCOME
  !insertmacro MUI_UNPAGE_CONFIRM
  !insertmacro MUI_UNPAGE_INSTFILES
  !insertmacro MUI_UNPAGE_FINISH
  
;--------------------------------
;Languages
 
  !insertmacro MUI_LANGUAGE "Spanish"

; Para generar instaladores en diferentes idiomas podemos escribir lo siguiente:
;  !insertmacro MUI_LANGUAGE ${LANGUAGE}
; De esta forma pasando la variable LANGUAGE al compilador podremos generar
;paquetes en distintos idiomas sin cambiar el script

;;;;;;;;;;;;;;;;;;;;;;;;;
; Configuration General ;
;;;;;;;;;;;;;;;;;;;;;;;;;
;Nuestro instalador se llamara si la version fuera la 1.0: Ejemplo-1.0-win32.exe
OutFile OpenTumblr-${VERSION}-win32.exe

;Aqui comprobamos que en la versi�n Inglesa se muestra correctamente el mensaje:
;Welcome to the $Name Setup Wizard
;Al tener reservado un espacio fijo para este mensaje, y al ser
;la frase en espa�ol mas larga:
; Bienvenido al Asistente de Instalaci�n de Aplicaci�n $Name
; no se ve el contenido de la variable $Name si el tama�o es muy grande
Name "OpenTumblr"
Caption "OpenTumblr ${VERSION} para Win32 Setup"
;Icon icono.ico

;Comprobacion de integridad del fichero activada
CRCCheck on
;Estilos visuales del XP activados
XPStyle on

/*
	Declaracion de variables a usar
	
*/
# tambi�n comprobamos los distintos
; tipos de comentarios que nos permite este lenguaje de script

Var PATH
Var PATH_ACCESO_DIRECTO
;Indicamos cual sera el directorio por defecto donde instalaremos nuestra
;aplicaci�n, el usuario puede cambiar este valor en tiempo de ejecuci�n.
InstallDir "$PROGRAMFILES\OpenTumblr"

; check if the program has already been installed, if so, take this dir
; as install dir
InstallDirRegKey HKLM SOFTWARE\OPENTUMBLR "Install_Dir"
;Mensaje que mostraremos para indicarle al usuario que seleccione un directorio
DirText "Elija un directorio donde instalar la aplicaci�n:"

;Indicamos que cuando la instalaci�n se complete no se cierre el instalador autom�ticamente
AutoCloseWindow false
;Mostramos todos los detalles del la instalaci�n al usuario.
ShowInstDetails show
;En caso de encontrarse los ficheros se sobreescriben
SetOverwrite on
;Optimizamos nuestro paquete en tiempo de compilaci�n, es �ltamente recomendable habilitar siempre esta opci�n
SetDatablockOptimize on
;Habilitamos la compresi�n de nuestro instalador
SetCompress auto
;Personalizamos el mensaje de desinstalaci�n
UninstallText "Este es el desinstalador del OpenTumblr."


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Install settings                                                    ;
; En esta secci�n a�adimos los ficheros que forman nuestra aplicaci�n ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

Section "Programa"
	;StrCpy $PATH "OPENTUMBLR"
	StrCpy $PATH_ACCESO_DIRECTO "OpenTumblr-${VERSION}"

	SetOutPath $INSTDIR\$PATH

;Incluimos todos los ficheros que componen nuestra aplicaci�n
	File  /r dist

;Hacemos que la instalaci�n se realice para todos los usuarios del sistema
        SetShellVarContext all
;Creamos los directorios, acesos directos y claves del registro que queramos...
	CreateDirectory "$SMPROGRAMS\$PATH_ACCESO_DIRECTO"
	CreateShortCut "$SMPROGRAMS\$PATH_ACCESO_DIRECTO\OpenTumblr-${VERSION}.lnk" \
                       "$INSTDIR\dist\opentumblr-client.exe"
	CreateShortCut "$SMPROGRAMS\$PATH_ACCESO_DIRECTO\Licencia.lnk" \
                       "$INSTDIR\licencia.html"

;Creamos tambi�n el aceso directo al instalador
	CreateShortCut "$SMPROGRAMS\$PATH_ACCESO_DIRECTO\Desinstalar.lnk" \
                       "$INSTDIR\uninstall.exe"

        WriteRegStr HKLM \
            SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\$PATH \
            "DisplayName" "OpenTumblr- ${VERSION} cliente multiplataforma para tumblr"
        WriteRegStr HKLM \
            SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\$PATH \
            "UninstallString" '"$INSTDIR\uninstall.exe"'
	WriteUninstaller "uninstall.exe"

	WriteRegStr HKLM SOFTWARE\$PATH "InstallDir" $INSTDIR
	WriteRegStr HKLM SOFTWARE\$PATH "Version" "${VERSION}"

	Exec "explorer $SMPROGRAMS\$PATH_ACCESO_DIRECTO\"
SectionEnd

;;;;;;;;;;;;;;;;;;;;;;
; Uninstall settings ;
;;;;;;;;;;;;;;;;;;;;;;

Section "Uninstall"
	;StrCpy $PATH "OPENTUMBLR"
	StrCpy $PATH_ACCESO_DIRECTO "OpenTumblr-${VERSION}"
        SetShellVarContext all
	RMDir /r $SMPROGRAMS\$PATH_ACCESO_DIRECTO
	RMDir /r $INSTDIR\$PATH
	RMDir /r $INSTDIR
	DeleteRegKey HKLM SOFTWARE\$PATH
        DeleteRegKey HKLM \
            Software\Microsoft\Windows\CurrentVersion\Uninstall\$PATH
SectionEnd

