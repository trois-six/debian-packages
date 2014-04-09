AR = '/usr/bin/ar'
ARFLAGS = 'rcs'
BINDIR = '/usr/bin'
CC = '/usr/bin/x86_64-w64-mingw32-gcc'
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('4', '9', '0')
CC_WIN32 = '/usr/bin/i686-w64-mingw32-gcc'
CC_WIN64 = '/usr/bin/x86_64-w64-mingw32-gcc'
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_cshlib = ['-fPIC']
COMPILER_CC = 'gcc'
CPPPATH_ST = '-I%s'
DEFINES = ['HAVE_DCERPC=1', 'HAVE_TALLOC=1']
DEFINES_DCERPC = ['HAVE_IMMEDIATE_STRUCTURES=1', '_GNU_SOURCE=1']
DEFINES_ST = '-D%s'
DEST_BINFMT = 'elf'
DEST_CPU = 'x86_64'
DEST_OS = 'linux'
ENABLE_SHARED = True
INCLUDES_DCERPC = ['/usr/include/samba-4.0']
LIBDIR = '/usr/lib'
LIBPATH_:LIBCLI-LDAP.SO.0 = ['/usr/lib/x86_64-linux-gnu/samba']
LIBPATH_:LIBDCERPC-SAMBA.SO.0 = ['/usr/lib/x86_64-linux-gnu/samba']
LIBPATH_:LIBERRORS.SO.0 = ['/usr/lib/x86_64-linux-gnu/samba']
LIBPATH_DCERPC = ['/usr/lib/x86_64-linux-gnu/samba']
LIBPATH_NDR-STANDARD = ['/usr/lib/x86_64-linux-gnu/samba']
LIBPATH_POPT = ['/usr/lib/x86_64-linux-gnu/samba']
LIBPATH_SAMBA-CREDENTIALS = ['/usr/lib/x86_64-linux-gnu/samba']
LIBPATH_SAMBA-HOSTCONFIG = ['/usr/lib/x86_64-linux-gnu/samba']
LIBPATH_SMBCLIENT-RAW = ['/usr/lib/x86_64-linux-gnu/samba']
LIBPATH_ST = '-L%s'
LIBPATH_TALLOC = ['/usr/lib/x86_64-linux-gnu/samba']
LIBS = ':libcli-ldap.so.0 dcerpc :libdcerpc-samba.so.0 :liberrors.so.0 popt talloc ndr-standard samba-hostconfig samba-credentials smbclient-raw'
LIB_:LIBCLI-LDAP.SO.0 = [':libcli-ldap.so.0']
LIB_:LIBDCERPC-SAMBA.SO.0 = [':libdcerpc-samba.so.0']
LIB_:LIBERRORS.SO.0 = [':liberrors.so.0']
LIB_DCERPC = ['dcerpc', 'dcerpc-binding', 'ndr', 'samba-util', 'tevent', 'talloc']
LIB_NDR-STANDARD = ['ndr-standard']
LIB_POPT = ['popt']
LIB_SAMBA-CREDENTIALS = ['samba-credentials']
LIB_SAMBA-HOSTCONFIG = ['samba-hostconfig']
LIB_SMBCLIENT-RAW = ['smbclient-raw']
LIB_ST = '-l%s'
LIB_TALLOC = ['talloc']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINK_CC = '/usr/bin/x86_64-w64-mingw32-gcc'
PKGCONFIG = '/usr/bin/pkg-config'
PREFIX = '/usr'
RPATH_ST = '-Wl,-rpath,%s'
SAMBA_INCS = '/usr/include/samba-4.0'
SAMBA_LIBS = '/usr/lib/x86_64-linux-gnu/samba'
SHLIB_MARKER = '-Wl,-Bdynamic'
SONAME_ST = '-Wl,-h,%s'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = '-Wl,-Bstatic'
STLIB_ST = '-l%s'
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.so'
cstlib_PATTERN = 'lib%s.a'
define_key = ['HAVE_DCERPC', 'HAVE_TALLOC']
macbundle_PATTERN = '%s.bundle'
