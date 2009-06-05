;--------------------------------
;Include Modern UI

  !include "MUI2.nsh"

;Algoritmo de compresión
SetCompressor lzma


;--------------------------------
;Confirmación para abortar la instalación
;Esta macro debe colocarse en esta posición del script sino no funcionara
  !define mui_abortwarning

;Definimos variable VERSION
!define VERSION "0.0.3"


;--------------------------------
;Pages

  ;Mostramos la página de bienvenida
  !insertmacro MUI_PAGE_WELCOME
  ;Página donde mostramos el contrato de licencia 
  ;!insertmacro MUI_PAGE_LICENSE "licencia.txt"
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

; Para generar instaladores en diferentes idiomas podemos escribir lo siguiente:
;  !insertmacro MUI_LANGUAGE ${LANGUAGE}
; De esta forma pasando la variable LANGUAGE al compilador podremos generar
;paquetes en distintos idiomas sin cambiar el script

;;;;;;;;;;;;;;;;;;;;;;;;;
; Configuration General ;
;;;;;;;;;;;;;;;;;;;;;;;;;
;Nuestro instalador se llamara si la version fuera la 1.0: Ejemplo-1.0-win32.exe
OutFile OpenTumblr-${VERSION}-win32.exe

;Aqui comprobamos que en la versión Inglesa se muestra correctamente el mensaje:
;Welcome to the $Name Setup Wizard
;Al tener reservado un espacio fijo para este mensaje, y al ser
;la frase en español mas larga:
; Bienvenido al Asistente de Instalación de Aplicación $Name
; no se ve el contenido de la variable $Name si el tamaño es muy grande
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
# también comprobamos los distintos
; tipos de comentarios que nos permite este lenguaje de script

Var PATH
Var PATH_ACCESO_DIRECTO
;Indicamos cual sera el directorio por defecto donde instalaremos nuestra
;aplicación, el usuario puede cambiar este valor en tiempo de ejecución.
InstallDir "$PROGRAMFILES\OpenTumblr"

; check if the program has already been installed, if so, take this dir
; as install dir
InstallDirRegKey HKLM SOFTWARE\OPENTUMBLR "Install_Dir"
;Mensaje que mostraremos para indicarle al usuario que seleccione un directorio
DirText "Elija un directorio donde instalar la aplicación:"

;Indicamos que cuando la instalación se complete no se cierre el instalador automáticamente
AutoCloseWindow false
;Mostramos todos los detalles del la instalación al usuario.
ShowInstDetails show
;En caso de encontrarse los ficheros se sobreescriben
SetOverwrite on
;Optimizamos nuestro paquete en tiempo de compilación, es áltamente recomendable habilitar siempre esta opción
SetDatablockOptimize on
;Habilitamos la compresión de nuestro instalador
SetCompress auto
;Personalizamos el mensaje de desinstalación
UninstallText "Este es el desinstalador del OpenTumblr."


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Install settings                                                    ;
; En esta sección añadimos los ficheros que forman nuestra aplicación ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

Section "Programa"
	;StrCpy $PATH "OPENTUMBLR"
	StrCpy $PATH_ACCESO_DIRECTO "OpenTumblr-${VERSION}"

	SetOutPath $INSTDIR\$PATH

;Incluimos todos los ficheros que componen nuestra aplicación
	File  /r dist

;Hacemos que la instalación se realice para todos los usuarios del sistema
        SetShellVarContext all
;Creamos los directorios, acesos directos y claves del registro que queramos...
	CreateDirectory "$SMPROGRAMS\$PATH_ACCESO_DIRECTO"
	CreateShortCut "$SMPROGRAMS\$PATH_ACCESO_DIRECTO\OpenTumblr-${VERSION}.lnk" \
                       "$INSTDIR\dist\opentumblr-client.exe"
	CreateShortCut "$SMPROGRAMS\$PATH_ACCESO_DIRECTO\Licencia.lnk" \
                       "$INSTDIR\licencia.html"

;Creamos también el aceso directo al instalador
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

