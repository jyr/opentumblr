;--------------------------------
;Include Modern UI

  !include "MUI.nsh"

;Algoritmo de compresión
SetCompressor lzma


;--------------------------------
;Confirmación para abortar la instalación
  !define mui_abortwarning

;Definimos variable VERSION
!define VERSION "0.1.0"


;--------------------------------
;Pages

  ;Mostramos la página de bienvenida
  !insertmacro MUI_PAGE_WELCOME
  ;Página donde mostramos el contrato de licencia 
  !insertmacro MUI_PAGE_LICENSE "LICENSE"
  ;página donde se muestran las distintas secciones definidas
  ;!insertmacro MUI_PAGE_COMPONENTS
  ;página donde se selecciona el directorio donde instalar nuestra aplicacion
  !insertmacro MUI_PAGE_DIRECTORY
  ;página de instalación de ficheros
  !insertmacro MUI_PAGE_INSTFILES
  ;página final
  !insertmacro MUI_PAGE_FINISH
  
;páginas referentes al desinstalador
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
;la frase en español mas larga:
; Bienvenido al Asistente de Instalación de Aplicación $Name
; no se ve el contenido de la variable $Name si el tamaño es muy grande
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
DirText "Elija un directorio donde instalar la aplicación:"

;Evitar el cierre del instalador al terminar
AutoCloseWindow false

;Detalles del la instalación.
ShowInstDetails show

;Sobreescritura de los archivos.
SetOverwrite on

;Optimizacion del instable tiempo de compilación.
SetDatablockOptimize on

;Compresión delinstalador
SetCompress auto

;Mensaje de desinstalación
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

	;Instalación para todos los usuarios del sistema
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