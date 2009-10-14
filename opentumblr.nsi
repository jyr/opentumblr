;--------------------------------
;Include Modern UI

  !include "MUI.nsh"

;Algoritmo de compresi�n
SetCompressor lzma


;--------------------------------
;Confirmaci�n para abortar la instalaci�n
  !define mui_abortwarning

;Definimos variable VERSION
!define VERSION "0.1.0"


;--------------------------------
;Pages

  ;Mostramos la p�gina de bienvenida
  !insertmacro MUI_PAGE_WELCOME
  ;P�gina donde mostramos el contrato de licencia 
  !insertmacro MUI_PAGE_LICENSE "LICENSE"
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


;;;;;;;;;;;;;;;;;;;;;;;;;
; Configuration General ;
;;;;;;;;;;;;;;;;;;;;;;;;;

;Nombre del instalador
OutFile Opentumblr-${VERSION}-win32.exe

;Al tener reservado un espacio fijo para este mensaje, y al ser
;la frase en espa�ol mas larga:
; Bienvenido al Asistente de Instalaci�n de Aplicaci�n $Name
; no se ve el contenido de la variable $Name si el tama�o es muy grande
Name "Opentumblr"
Caption "Opentumblr ${VERSION} para Win32 Setup"
;Icon images\Opentumblr.ico

;Comprobacion de integridad del fichero activada
CRCCheck on
;Estilos visuales del XP activados
XPStyle on

/*
	Declaracion de variables a usar
	
*/

Var PATH
Var PATH_ACCESO_DIRECTO

;Directorio defualt de instalacion
InstallDir "$PROGRAMFILES\Opentumblr"

;Revisa si la applicacion ya esta instalada, tomando el dir para install dir
InstallDirRegKey HKLM SOFTWARE\Opentumblr "Install_Dir"

;Mensaje para seleccionar un directorio
DirText "Elija un directorio donde instalar la aplicaci�n:"

;Evitar el cierre del instalador al terminar
AutoCloseWindow false

;Detalles del la instalaci�n.
ShowInstDetails show

;Sobreescritura de los archivos.
SetOverwrite on

;Optimizacion del instable tiempo de compilaci�n.
SetDatablockOptimize on

;Compresi�n delinstalador
SetCompress auto

;Mensaje de desinstalaci�n
UninstallText "Este es el desinstalador de Opentumblr."


;;;;;;;;;;;;;;;;;;;;
; Install settings ;
;;;;;;;;;;;;;;;;;;;;

Section "Programa"
	StrCpy $PATH ""
	StrCpy $PATH_ACCESO_DIRECTO "Opentumblr-${VERSION}"

	SetOutPath $INSTDIR\$PATH

	;Archivos de la aplicacion a instalar
	File  /r dist
	File  LICENSE

	;Instalaci�n para todos los usuarios del sistema
        SetShellVarContext all
	;SetShellVarContext current

	;Creacion de directorios y acesos directos
	CreateDirectory "$SMPROGRAMS\$PATH_ACCESO_DIRECTO"
	CreateShortCut "$SMPROGRAMS\$PATH_ACCESO_DIRECTO\Opentumblr-${VERSION}.lnk"\
                       "$INSTDIR\dist\Opentumblr-client.exe"
	CreateShortCut "$SMPROGRAMS\$PATH_ACCESO_DIRECTO\LICENSE.lnk" \
                       "$INSTDIR\LICENSE"

	;Acceso directo al desinstalador
	CreateShortCut "$SMPROGRAMS\$PATH_ACCESO_DIRECTO\Desinstalar.lnk" \
                       "$INSTDIR\uninstall.exe"

	;Creacion del uninstall
	WriteUninstaller "uninstall.exe"

	Exec "explorer $SMPROGRAMS\$PATH_ACCESO_DIRECTO\"
SectionEnd

;;;;;;;;;;;;;;;;;;;;;;
; Uninstall settings ;
;;;;;;;;;;;;;;;;;;;;;;

Section "Uninstall"
	StrCpy $PATH ""
	StrCpy $PATH_ACCESO_DIRECTO "Opentumblr-${VERSION}"
        SetShellVarContext all
	RMDir /r $SMPROGRAMS\$PATH_ACCESO_DIRECTO
	RMDir /r $INSTDIR\$PATH
	RMDir /r $INSTDIR
SectionEnd