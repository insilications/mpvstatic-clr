AR = ['gcc-ar']
ARFLAGS = ['rcs']
BASHDIR = '/usr/share/bash-completion/completions'
BINDIR = '/usr/bin'
BIN_PERL = ['/usr/bin/perl']
CC = ['gcc']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('10', '2', '1')
CFLAGS = ['-g', '-O3', '-march=native', '-mtune=native', '-fgraphite-identity', '-Wall', '-Wl,--as-needed', '-Wl,--build-id=sha1', '-Wl,--enable-new-dtags', '-Wl,--hash-style=gnu', '-Wl,-O2', '-Wl,-z,now', '-Wl,-z,relro', '-falign-functions=32', '-flimit-function-alignment', '-fasynchronous-unwind-tables', '-fdevirtualize-at-ltrans', '-floop-nest-optimize', '-fno-math-errno', '-fno-semantic-interposition', '-fno-stack-protector', '-fno-trapping-math', '-ftree-loop-distribute-patterns', '-ftree-loop-vectorize', '-ftree-vectorize', '-funroll-loops', '-fuse-ld=bfd', '-fuse-linker-plugin', '-malign-data=cacheline', '-feliminate-unused-debug-types', '-fipa-pta', '-flto=16', '-fno-plt', '-mtls-dialect=gnu2', '-Wl,-sort-common', '-Wno-error', '-Wp,-D_REENTRANT', '-pipe', '-fPIC', '-D_ISOC99_SOURCE', '-D_GNU_SOURCE', '-D_FILE_OFFSET_BITS=64', '-Wall', '-std=c11', '-O3', '-g', '-Werror=implicit-function-declaration', '-Wno-error=deprecated-declarations', '-Wno-error=unused-function', '-Wempty-body', '-Wdisabled-optimization', '-Wstrict-prototypes', '-Wno-format-zero-length', '-Werror=format-security', '-Wno-redundant-decls', '-Wvla', '-Wno-format-truncation', '-Wimplicit-fallthrough', '-fno-math-errno', '-Wall', '-Wundef', '-Wmissing-prototypes', '-Wshadow', '-Wno-switch', '-Wparentheses', '-Wpointer-arith', '-Wno-pointer-sign', '-Wno-unused-result']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_cshlib = ['-fPIC']
CFLAGS_egl = ['-pthread']
CFLAGS_ffmpeg = ['-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread']
CFLAGS_libass = ['-pthread', '-pthread']
CFLAGS_libavdevice = ['-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread']
CFLAGS_libbluray = ['-pthread', '-pthread']
CFLAGS_libplacebo = ['-pthread', '-pthread', '-pthread', '-pthread']
CFLAGS_pthreads = ['-pthread']
COMPILER_CC = 'gcc'
CONFDIR = '/etc/mpv'
CONFLOADDIR = '/etc/mpv'
CPPPATH_ST = '-I%s'
CXXFLAGS_egl = ['-pthread']
CXXFLAGS_ffmpeg = ['-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread']
CXXFLAGS_libass = ['-pthread', '-pthread']
CXXFLAGS_libavdevice = ['-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread']
CXXFLAGS_libbluray = ['-pthread', '-pthread']
CXXFLAGS_libplacebo = ['-pthread', '-pthread', '-pthread', '-pthread']
DATADIR = '/usr/share'
DATAROOTDIR = '/usr/share'
DEFINES = []
DEFINES_ST = '-D%s'
DEFINES_pulse = ['_REENTRANT']
DEFINES_sdl2 = ['_REENTRANT']
DEFINE_COMMENTS = {'DEFAULT_DVD_DEVICE': '', 'DEFAULT_CDROM_DEVICE': '', 'HAVE_LGPL': '', 'HAVE_GPL': '', 'HAVE_CPLAYER': '', 'HAVE_LIBMPV_SHARED': '', 'HAVE_LIBMPV_STATIC': '', 'HAVE_STATIC_BUILD': '', 'HAVE_BUILD_DATE': '', 'HAVE_OPTIMIZE': '', 'HAVE_DEBUG_BUILD': '', 'HAVE_TESTS': '', 'HAVE_TA_LEAK_REPORT': '', 'HAVE_MANPAGE_BUILD': '', 'HAVE_HTML_BUILD': '', 'HAVE_PDF_BUILD': '', 'HAVE_LIBDL': '', 'HAVE_CPLUGINS': '', 'HAVE_ASM': '', 'HAVE_CLANG_DATABASE': '', 'HAVE_SWIFT_STATIC': '', 'HAVE_NOEXECSTACK': '', 'HAVE_LIBM': '', 'HAVE_MINGW': '', 'HAVE_POSIX': '', 'HAVE_ANDROID': '', 'HAVE_TVOS': '', 'HAVE_EGL_ANDROID': '', 'HAVE_POSIX_OR_MINGW': '', 'HAVE_SWIFT': '', 'HAVE_UWP': '', 'HAVE_WIN32_DESKTOP': '', 'HAVE_WIN32_INTERNAL_PTHREADS': '', 'HAVE_PTHREADS': '', 'HAVE_PTHREAD_DEBUG': '', 'HAVE_STDATOMIC': '', 'HAVE_LIBRT': '', 'HAVE_ICONV': '', 'HAVE_DOS_PATHS': '', 'HAVE_GLOB_POSIX': '', 'HAVE_GLOB_WIN32': '', 'HAVE_GLOB': '', 'HAVE_VT_H': '', 'HAVE_CONSIO_H': '', 'HAVE_GBM_H': '', 'HAVE_GLIBC_THREAD_NAME': '', 'HAVE_OSX_THREAD_NAME': '', 'HAVE_BSD_THREAD_NAME': '', 'HAVE_BSD_FSTATFS': '', 'HAVE_LINUX_FSTATFS': '', 'HAVE_LUAJIT': '', 'HAVE_LUA': '', 'HAVE_JAVASCRIPT': '', 'HAVE_LIBASS': '', 'HAVE_ZLIB': '', 'HAVE_LIBBLURAY': '', 'HAVE_DVDNAV': '', 'HAVE_CDDA': '', 'HAVE_UCHARDET': '', 'HAVE_RUBBERBAND': '', 'HAVE_ZIMG': '', 'HAVE_LCMS2': '', 'HAVE_VAPOURSYNTH': '', 'HAVE_LIBARCHIVE': '', 'HAVE_DVBIN': '', 'HAVE_SDL2': '', 'HAVE_SDL2_GAMEPAD': '', 'HAVE_FFMPEG': '', 'HAVE_LIBAVDEVICE': '', 'HAVE_FFMPEG_STRICT_ABI': '', 'HAVE_SDL2_AUDIO': '', 'HAVE_PULSE': '', 'HAVE_JACK': '', 'HAVE_OPENAL': '', 'HAVE_OPENSLES': '', 'HAVE_ALSA': '', 'HAVE_COREAUDIO': '', 'HAVE_AUDIOUNIT': '', 'HAVE_WASAPI': '', 'HAVE_SDL2_VIDEO': '', 'HAVE_COCOA': '', 'HAVE_DRM': '', 'HAVE_GBM': '', 'HAVE_WAYLAND_PROTOCOLS': '', 'HAVE_WAYLAND': '', 'HAVE_MEMFD_CREATE': '', 'HAVE_X11': '', 'HAVE_XV': '', 'HAVE_GL_COCOA': '', 'HAVE_GL_X11': '', 'HAVE_RPI': '', 'HAVE_EGL': '', 'HAVE_EGL_X11': '', 'HAVE_EGL_DRM': '', 'HAVE_GL_WAYLAND': '', 'HAVE_GL_WIN32': '', 'HAVE_GL_DXINTEROP': '', 'HAVE_EGL_ANGLE': '', 'HAVE_EGL_ANGLE_LIB': '', 'HAVE_EGL_ANGLE_WIN32': '', 'HAVE_VDPAU': '', 'HAVE_VDPAU_GL_X11': '', 'HAVE_VAAPI': '', 'HAVE_VAAPI_X11': '', 'HAVE_VAAPI_WAYLAND': '', 'HAVE_VAAPI_DRM': '', 'HAVE_VAAPI_X_EGL': '', 'HAVE_VAAPI_EGL': '', 'HAVE_CACA': '', 'HAVE_JPEG': '', 'HAVE_DIRECT3D': '', 'HAVE_SHADERC_SHARED': '', 'HAVE_SHADERC_STATIC': '', 'HAVE_SHADERC': '', 'HAVE_SPIRV_CROSS_SHARED': '', 'HAVE_SPIRV_CROSS_STATIC': '', 'HAVE_SPIRV_CROSS': '', 'HAVE_D3D11': '', 'HAVE_IOS_GL': '', 'HAVE_PLAIN_GL': '', 'HAVE_GL': '', 'HAVE_LIBPLACEBO': '', 'HAVE_VULKAN': '', 'HAVE_VAAPI_VULKAN': '', 'HAVE_EGL_HELPERS': '', 'HAVE_VIDEOTOOLBOX_HWACCEL': '', 'HAVE_VIDEOTOOLBOX_GL': '', 'HAVE_D3D_HWACCEL': '', 'HAVE_D3D9_HWACCEL': '', 'HAVE_GL_DXINTEROP_D3D9': '', 'HAVE_FFNVCODEC': '', 'HAVE_CUDA_HWACCEL': '', 'HAVE_CUDA_INTEROP': '', 'HAVE_RPI_MMAL': '', 'HAVE_WIN32_EXECUTABLE': '', 'HAVE_MACOS_TOUCHBAR': '', 'HAVE_MACOS_10_11_FEATURES': '', 'HAVE_MACOS_10_12_2_FEATURES': '', 'HAVE_MACOS_10_14_FEATURES': '', 'HAVE_MACOS_MEDIA_PLAYER': '', 'HAVE_MACOS_COCOA_CB': '', 'CONFIGURATION': '', 'MPV_CONFDIR': '', 'FULLCONFIG': ''}
DEST_BINFMT = 'elf'
DEST_CPU = 'x86_64'
DEST_OS = 'linux'
DOCDIR = '/usr/share/doc/mpv'
DVIDIR = '/usr/share/doc/mpv'
EXEC_PREFIX = '/usr'
HAVE_ALSA = 1
HAVE_CPLUGINS = 1
HAVE_DRM = 1
HAVE_EGL = 1
HAVE_FFMPEG = 1
HAVE_FFNVCODEC = 1
HAVE_GBM = 1
HAVE_GBM_H = 1
HAVE_GLIBC_THREAD_NAME = 1
HAVE_GLOB_POSIX = 1
HAVE_GL_WAYLAND = 1
HAVE_GL_X11 = 1
HAVE_ICONV = 1
HAVE_JPEG = 1
HAVE_LCMS2 = 1
HAVE_LIBARCHIVE = 1
HAVE_LIBASS = 1
HAVE_LIBAVDEVICE = 1
HAVE_LIBBLURAY = 1
HAVE_LIBDL = 1
HAVE_LIBM = 1
HAVE_LIBPLACEBO = 1
HAVE_LIBRT = 1
HAVE_LINUX_FSTATFS = 1
HAVE_LUAJIT = 1
HAVE_MEMFD_CREATE = 1
HAVE_NOEXECSTACK = 1
HAVE_POSIX = 1
HAVE_PTHREADS = 1
HAVE_PULSE = 1
HAVE_RUBBERBAND = 1
HAVE_SDL2 = 1
HAVE_SHADERC_STATIC = 1
HAVE_STDATOMIC = 1
HAVE_UCHARDET = 1
HAVE_VAAPI = 1
HAVE_VAAPI_DRM = 1
HAVE_VAAPI_WAYLAND = 1
HAVE_VAAPI_X11 = 1
HAVE_VAPOURSYNTH = 1
HAVE_VDPAU = 1
HAVE_VT_H = 1
HAVE_VULKAN = 1
HAVE_WAYLAND = 1
HAVE_WAYLAND_PROTOCOLS = 1
HAVE_X11 = 1
HAVE_ZIMG = 1
HAVE_ZLIB = 1
HTMLDIR = '/usr/share/doc/mpv'
INCLUDEDIR = '/usr/include'
INCLUDES_drm = ['/usr/include/libdrm']
INCLUDES_egl = ['/usr/include/libdrm']
INCLUDES_libass = ['/usr/include/fribidi', '/usr/include/freetype2', '/usr/include/libpng16', '/usr/include/harfbuzz', '/usr/include/glib-2.0', '/usr/lib64/glib-2.0/include']
INCLUDES_libbluray = ['/usr/include/libxml2', '/usr/include/freetype2', '/usr/include/libpng16', '/usr/include/harfbuzz', '/usr/include/glib-2.0', '/usr/lib64/glib-2.0/include']
INCLUDES_libplacebo = ['/usr/include/libdrm']
INCLUDES_luajit = ['/usr/include/luajit-2.1']
INCLUDES_sdl2 = ['/usr/include/SDL2']
INCLUDES_uchardet = ['/usr/include/uchardet']
INCLUDES_vapoursynth = ['/usr/include/vapoursynth', '/usr/include/python3.8', '/usr/include/vapoursynth']
INFODIR = '/usr/share/info'
LDFLAGS = ['-g', '-O3', '-march=native', '-mtune=native', '-fgraphite-identity', '-Wall', '-Wl,--as-needed', '-Wl,--build-id=sha1', '-Wl,--enable-new-dtags', '-Wl,--hash-style=gnu', '-Wl,-O2', '-Wl,-z,now', '-Wl,-z,relro', '-falign-functions=32', '-flimit-function-alignment', '-fasynchronous-unwind-tables', '-fdevirtualize-at-ltrans', '-floop-nest-optimize', '-fno-math-errno', '-fno-semantic-interposition', '-fno-stack-protector', '-fno-trapping-math', '-ftree-loop-distribute-patterns', '-ftree-loop-vectorize', '-ftree-vectorize', '-funroll-loops', '-fuse-ld=bfd', '-fuse-linker-plugin', '-malign-data=cacheline', '-feliminate-unused-debug-types', '-fipa-pta', '-flto=16', '-fno-plt', '-mtls-dialect=gnu2', '-Wl,-sort-common', '-Wno-error', '-Wp,-D_REENTRANT', '-pipe', '-fPIC', '-Wl,-Bdynamic', '-L/usr/lib64', '-pthread', '-lpthread', '-lrt', '-lc', '-ldl', '-lgcc', '-lgcc_s', '-lstdc++', '-lmvec', '-lm']
LIBDIR = '/usr/lib64'
LIBEXECDIR = '/usr/libexec'
LIBPATH_ST = '-L%s'
LIB_ST = '-l%s'
LIB_jpeg = ['jpeg']
LIB_libm = ['m']
LIB_librt = ['rt']
LIB_shaderc_static = ['shaderc_combined', 'stdc++']
LIB_zlib = ['z']
LINKFLAGS = ['-rdynamic']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cplugins = ['-rdynamic']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINKFLAGS_egl = ['-pthread']
LINKFLAGS_ffmpeg = ['-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread']
LINKFLAGS_libass = ['-pthread', '-pthread']
LINKFLAGS_libavdevice = ['-Wl,--no-undefined', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread', '-pthread']
LINKFLAGS_libbluray = ['-pthread', '-pthread']
LINKFLAGS_libplacebo = ['-pthread', '-pthread', '-pthread', '-pthread']
LINKFLAGS_luajit = ['-Wl,-E']
LINKFLAGS_noexecstack = ['-Wl,-z,noexecstack']
LINKFLAGS_sdl2 = ['-Wl,--no-undefined']
LINK_CC = ['gcc']
LOCALEDIR = '/usr/share/locale'
LOCALSTATEDIR = '/usr/var'
MANDIR = '/usr/share/man'
OLDINCLUDEDIR = '/usr/include'
PACKAGE = 'mpv'
PDFDIR = '/usr/share/doc/mpv'
PKG_CONFIG = ['/usr/bin/pkg-config']
PREFIX = '/usr'
PSDIR = '/usr/share/doc/mpv'
RPATH_ST = '-Wl,-rpath,%s'
RST2HTML = ['/usr/bin/rst2html.py']
RST2MAN = ['/usr/bin/rst2man']
SBINDIR = '/usr/sbin'
SHAREDSTATEDIR = '/usr/com'
SHLIB_MARKER = '-Wl,-Bdynamic'
SONAME_ST = '-Wl,-h,%s'
STLIBPATH_ST = '-L%s'
STLIBPATH_ffmpeg = ['/usr/nvidia/lib']
STLIBPATH_libavdevice = ['/usr/nvidia/lib']
STLIBPATH_pulse = ['/usr/lib64/pulseaudio']
STLIB_MARKER = '-Wl,-Bstatic'
STLIB_ST = '-l%s'
STLIB_alsa = ['asound', 'm', 'dl', 'pthread', 'rt']
STLIB_drm = ['drm', 'm']
STLIB_egl = ['EGL', 'pthread', 'm', 'dl', 'Xdamage', 'Xfixes', 'X11-xcb', 'xcb-glx', 'xcb-dri2', 'Xxf86vm', 'Xext', 'X11', 'pthread', 'xcb', 'Xau', 'Xdmcp', 'drm', 'm']
STLIB_ffmpeg = ['/usr/lib64/libavfilter.a', '/usr/cuda/lib64/libcublasLt_static.a', '/usr/cuda/lib64/libcublas_static.a', '/usr/cuda/lib64/libcudadevrt.a', '/usr/cuda/lib64/libcudart_static.a', '/usr/cuda/lib64/libcufft_static_nocallback.a', '/usr/cuda/lib64/libcufftw_static.a', '/usr/cuda/lib64/libculibos.a', '/usr/cuda/lib64/libcurand_static.a', '/usr/cuda/lib64/libcusolver_static.a', '/usr/cuda/lib64/libcusparse_static.a', '/usr/cuda/lib64/liblapack_static.a', '/usr/cuda/lib64/libmetis_static.a', '/usr/cuda/lib64/libnppc_static.a', '/usr/cuda/lib64/libnppial_static.a', '/usr/cuda/lib64/libnppicc_static.a', '/usr/cuda/lib64/libnppidei_static.a', '/usr/cuda/lib64/libnppif_static.a', '/usr/cuda/lib64/libnppig_static.a', '/usr/cuda/lib64/libnppim_static.a', '/usr/cuda/lib64/libnppist_static.a', '/usr/cuda/lib64/libnppisu_static.a', '/usr/cuda/lib64/libnppitc_static.a', '/usr/cuda/lib64/libnpps_static.a', '/usr/cuda/lib64/libnvjpeg_static.a', 'GL', 'EGL', 'GLX', 'nvcuvid', 'm', '/usr/lib64/libfribidi.a', '/usr/lib64/libass.a', 'm', '/usr/lib64/libfontconfig.a', '/usr/lib64/libexpat.a', '/usr/lib64/libfribidi.a', '/usr/lib64/libfreetype.a', '/usr/lib64/libbz2.a', '/usr/lib64/libpng16.a', 'm', '/usr/lib64/libz.a', 'm', '/usr/lib64/libz.a', '/usr/lib64/libharfbuzz.a', 'm', '/usr/lib64/libglib-2.0.a', '/usr/lib64/libpcre.a', '/usr/lib64/libgraphite2.a', '/usr/lib64/libbrotlidec.a', '/usr/lib64/libbrotlicommon.a', '/usr/cuda/lib64/libnppig_static.a', '/usr/cuda/lib64/libnppicc_static.a', '/usr/cuda/lib64/libnppc_static.a', '/usr/cuda/lib64/libnppidei_static.a', 'va', '/usr/lib64/libvidstab.a', 'm', 'gomp', 'pthread', '/usr/lib64/libzimg.a', 'stdc++', 'OpenCL', '/usr/lib64/libfontconfig.a', '/usr/lib64/libexpat.a', '/usr/lib64/libfreetype.a', '/usr/lib64/libbz2.a', '/usr/lib64/libpng16.a', 'm', '/usr/lib64/libz.a', 'm', '/usr/lib64/libz.a', '/usr/lib64/libharfbuzz.a', 'm', '/usr/lib64/libglib-2.0.a', '/usr/lib64/libpcre.a', '/usr/lib64/libgraphite2.a', '/usr/lib64/libbrotlidec.a', '/usr/lib64/libbrotlicommon.a', '/usr/lib64/libfreetype.a', '/usr/lib64/libbz2.a', '/usr/lib64/libpng16.a', 'm', '/usr/lib64/libz.a', 'm', '/usr/lib64/libz.a', '/usr/lib64/libharfbuzz.a', 'm', '/usr/lib64/libglib-2.0.a', '/usr/lib64/libpcre.a', '/usr/lib64/libgraphite2.a', '/usr/lib64/libbrotlidec.a', '/usr/lib64/libbrotlicommon.a', 'mfx', 'stdc++', 'dl', '/usr/lib64/libswscale.a', '/usr/cuda/lib64/libcublasLt_static.a', '/usr/cuda/lib64/libcublas_static.a', '/usr/cuda/lib64/libcudadevrt.a', '/usr/cuda/lib64/libcudart_static.a', '/usr/cuda/lib64/libcufft_static_nocallback.a', '/usr/cuda/lib64/libcufftw_static.a', '/usr/cuda/lib64/libculibos.a', '/usr/cuda/lib64/libcurand_static.a', '/usr/cuda/lib64/libcusolver_static.a', '/usr/cuda/lib64/libcusparse_static.a', '/usr/cuda/lib64/liblapack_static.a', '/usr/cuda/lib64/libmetis_static.a', '/usr/cuda/lib64/libnppc_static.a', '/usr/cuda/lib64/libnppial_static.a', '/usr/cuda/lib64/libnppicc_static.a', '/usr/cuda/lib64/libnppidei_static.a', '/usr/cuda/lib64/libnppif_static.a', '/usr/cuda/lib64/libnppig_static.a', '/usr/cuda/lib64/libnppim_static.a', '/usr/cuda/lib64/libnppist_static.a', '/usr/cuda/lib64/libnppisu_static.a', '/usr/cuda/lib64/libnppitc_static.a', '/usr/cuda/lib64/libnpps_static.a', '/usr/cuda/lib64/libnvjpeg_static.a', 'GL', 'EGL', 'GLX', 'nvcuvid', 'm', '/usr/lib64/libpostproc.a', '/usr/cuda/lib64/libcublasLt_static.a', '/usr/cuda/lib64/libcublas_static.a', '/usr/cuda/lib64/libcudadevrt.a', '/usr/cuda/lib64/libcudart_static.a', '/usr/cuda/lib64/libcufft_static_nocallback.a', '/usr/cuda/lib64/libcufftw_static.a', '/usr/cuda/lib64/libculibos.a', '/usr/cuda/lib64/libcurand_static.a', '/usr/cuda/lib64/libcusolver_static.a', '/usr/cuda/lib64/libcusparse_static.a', '/usr/cuda/lib64/liblapack_static.a', '/usr/cuda/lib64/libmetis_static.a', '/usr/cuda/lib64/libnppc_static.a', '/usr/cuda/lib64/libnppial_static.a', '/usr/cuda/lib64/libnppicc_static.a', '/usr/cuda/lib64/libnppidei_static.a', '/usr/cuda/lib64/libnppif_static.a', '/usr/cuda/lib64/libnppig_static.a', '/usr/cuda/lib64/libnppim_static.a', '/usr/cuda/lib64/libnppist_static.a', '/usr/cuda/lib64/libnppisu_static.a', '/usr/cuda/lib64/libnppitc_static.a', '/usr/cuda/lib64/libnpps_static.a', '/usr/cuda/lib64/libnvjpeg_static.a', 'GL', 'EGL', 'GLX', 'nvcuvid', 'm', '/usr/lib64/libavformat.a', '/usr/cuda/lib64/libcublasLt_static.a', '/usr/cuda/lib64/libcublas_static.a', '/usr/cuda/lib64/libcudadevrt.a', '/usr/cuda/lib64/libcudart_static.a', '/usr/cuda/lib64/libcufft_static_nocallback.a', '/usr/cuda/lib64/libcufftw_static.a', '/usr/cuda/lib64/libculibos.a', '/usr/cuda/lib64/libcurand_static.a', '/usr/cuda/lib64/libcusolver_static.a', '/usr/cuda/lib64/libcusparse_static.a', '/usr/cuda/lib64/liblapack_static.a', '/usr/cuda/lib64/libmetis_static.a', '/usr/cuda/lib64/libnppc_static.a', '/usr/cuda/lib64/libnppial_static.a', '/usr/cuda/lib64/libnppicc_static.a', '/usr/cuda/lib64/libnppidei_static.a', '/usr/cuda/lib64/libnppif_static.a', '/usr/cuda/lib64/libnppig_static.a', '/usr/cuda/lib64/libnppim_static.a', '/usr/cuda/lib64/libnppist_static.a', '/usr/cuda/lib64/libnppisu_static.a', '/usr/cuda/lib64/libnppitc_static.a', '/usr/cuda/lib64/libnpps_static.a', '/usr/cuda/lib64/libnvjpeg_static.a', 'GL', 'EGL', 'GLX', 'nvcuvid', 'm', '/usr/lib64/libxml2.a', '/usr/lib64/libz.a', '/usr/lib64/liblzma.a', 'm', '/usr/lib64/libbz2.a', '/usr/lib64/libvapoursynth-script.a', '/usr/lib64/libpython3.8.a', '/usr/lib64/libcrypt.a', 'pthread', 'dl', '/usr/lib64/libutil.a', 'm', '/usr/lib64/libvapoursynth.a', '/usr/lib64/libzimg.a', 'dl', '/usr/lib64/libzimg.a', 'stdc++', '/usr/lib64/libbluray.a', 'dl', 'pthread', '/usr/lib64/libxml2.a', '/usr/lib64/libz.a', '/usr/lib64/liblzma.a', 'm', '/usr/lib64/libfontconfig.a', '/usr/lib64/libexpat.a', '/usr/lib64/libfreetype.a', '/usr/lib64/libbz2.a', '/usr/lib64/libpng16.a', 'm', '/usr/lib64/libz.a', 'm', '/usr/lib64/libz.a', '/usr/lib64/libharfbuzz.a', 'm', '/usr/lib64/libglib-2.0.a', '/usr/lib64/libpcre.a', '/usr/lib64/libgraphite2.a', '/usr/lib64/libbrotlidec.a', '/usr/lib64/libbrotlicommon.a', '/usr/lib64/libz.a', '/usr/lib64/libssl.a', '/usr/lib64/libcrypto.a', '/usr/lib64/libz.a', 'dl', '/usr/lib64/librtmp.a', '/usr/lib64/libz.a', '/usr/lib64/libgmp.a', 'gnutls', '/usr/lib64/libgmp.a', '/usr/lib64/libunistring.a', '/usr/lib64/libatomic.a', '/usr/lib64/libtasn1.a', '/usr/lib64/libidn2.a', '/usr/lib64/libunistring.a', 'p11-kit', '/usr/lib64/libhogweed.a', '/usr/lib64/libgmp.a', '/usr/lib64/libnettle.a', '/usr/lib64/libsrt.a', 'stdc++', 'm', '/usr/lib64/libgcov.a', 'gcc_s', 'gcc', 'pthread', 'c', 'gcc_s', 'gcc', '/usr/lib64/libssl.a', '/usr/lib64/libcrypto.a', '/usr/lib64/libz.a', 'dl', '/usr/lib64/libavcodec.a', '/usr/cuda/lib64/libcublasLt_static.a', '/usr/cuda/lib64/libcublas_static.a', '/usr/cuda/lib64/libcudadevrt.a', '/usr/cuda/lib64/libcudart_static.a', '/usr/cuda/lib64/libcufft_static_nocallback.a', '/usr/cuda/lib64/libcufftw_static.a', '/usr/cuda/lib64/libculibos.a', '/usr/cuda/lib64/libcurand_static.a', '/usr/cuda/lib64/libcusolver_static.a', '/usr/cuda/lib64/libcusparse_static.a', '/usr/cuda/lib64/liblapack_static.a', '/usr/cuda/lib64/libmetis_static.a', '/usr/cuda/lib64/libnppc_static.a', '/usr/cuda/lib64/libnppial_static.a', '/usr/cuda/lib64/libnppicc_static.a', '/usr/cuda/lib64/libnppidei_static.a', '/usr/cuda/lib64/libnppif_static.a', '/usr/cuda/lib64/libnppig_static.a', '/usr/cuda/lib64/libnppim_static.a', '/usr/cuda/lib64/libnppist_static.a', '/usr/cuda/lib64/libnppisu_static.a', '/usr/cuda/lib64/libnppitc_static.a', '/usr/cuda/lib64/libnpps_static.a', '/usr/cuda/lib64/libnvjpeg_static.a', 'GL', 'EGL', 'GLX', 'nvcuvid', '/usr/lib64/libvpx.a', 'm', 'pthread', '/usr/lib64/libvpx.a', 'm', 'pthread', '/usr/lib64/libvpx.a', 'm', 'pthread', '/usr/lib64/libvpx.a', 'm', 'pthread', '/usr/lib64/libwebpmux.a', 'm', '/usr/lib64/libwebp.a', 'm', 'm', '/usr/lib64/liblzma.a', '/usr/lib64/libdav1d.a', 'dl', '/usr/lib64/libsnappy.a', 'stdc++', '/usr/lib64/libz.a', '/usr/lib64/libaom.a', 'm', 'pthread', '/usr/lib64/libfdk-aac.a', 'm', '/usr/lib64/libgsm.a', '/usr/lib64/libmp3lame.a', 'm', '/usr/lib64/libopenjp2.a', 'm', '/usr/lib64/libopus.a', 'm', '/usr/lib64/libspeex.a', 'm', '/usr/lib64/libtheoraenc.a', '/usr/lib64/libtheoradec.a', '/usr/lib64/libogg.a', '/usr/lib64/libvorbis.a', 'm', '/usr/lib64/libogg.a', '/usr/lib64/libvorbisenc.a', '/usr/lib64/libvorbis.a', 'm', '/usr/lib64/libogg.a', '/usr/lib64/libwebp.a', 'm', '/usr/lib64/libx264.a', 'pthread', 'm', 'dl', '/usr/lib64/libx265.a', 'stdc++', 'm', 'gcc_s', 'gcc', 'gcc_s', 'gcc', 'rt', 'dl', '/usr/lib64/libxvidcore.a', 'va', 'mfx', 'stdc++', 'dl', '/usr/lib64/libswresample.a', '/usr/cuda/lib64/libcublasLt_static.a', '/usr/cuda/lib64/libcublas_static.a', '/usr/cuda/lib64/libcudadevrt.a', '/usr/cuda/lib64/libcudart_static.a', '/usr/cuda/lib64/libcufft_static_nocallback.a', '/usr/cuda/lib64/libcufftw_static.a', '/usr/cuda/lib64/libculibos.a', '/usr/cuda/lib64/libcurand_static.a', '/usr/cuda/lib64/libcusolver_static.a', '/usr/cuda/lib64/libcusparse_static.a', '/usr/cuda/lib64/liblapack_static.a', '/usr/cuda/lib64/libmetis_static.a', '/usr/cuda/lib64/libnppc_static.a', '/usr/cuda/lib64/libnppial_static.a', '/usr/cuda/lib64/libnppicc_static.a', '/usr/cuda/lib64/libnppidei_static.a', '/usr/cuda/lib64/libnppif_static.a', '/usr/cuda/lib64/libnppig_static.a', '/usr/cuda/lib64/libnppim_static.a', '/usr/cuda/lib64/libnppist_static.a', '/usr/cuda/lib64/libnppisu_static.a', '/usr/cuda/lib64/libnppitc_static.a', '/usr/cuda/lib64/libnpps_static.a', '/usr/cuda/lib64/libnvjpeg_static.a', 'GL', 'EGL', 'GLX', 'nvcuvid', 'm', '/usr/lib64/libavutil.a', '/usr/cuda/lib64/libcublasLt_static.a', '/usr/cuda/lib64/libcublas_static.a', '/usr/cuda/lib64/libcudadevrt.a', '/usr/cuda/lib64/libcudart_static.a', '/usr/cuda/lib64/libcufft_static_nocallback.a', '/usr/cuda/lib64/libcufftw_static.a', '/usr/cuda/lib64/libculibos.a', '/usr/cuda/lib64/libcurand_static.a', '/usr/cuda/lib64/libcusolver_static.a', '/usr/cuda/lib64/libcusparse_static.a', '/usr/cuda/lib64/liblapack_static.a', '/usr/cuda/lib64/libmetis_static.a', '/usr/cuda/lib64/libnppc_static.a', '/usr/cuda/lib64/libnppial_static.a', '/usr/cuda/lib64/libnppicc_static.a', '/usr/cuda/lib64/libnppidei_static.a', '/usr/cuda/lib64/libnppif_static.a', '/usr/cuda/lib64/libnppig_static.a', '/usr/cuda/lib64/libnppim_static.a', '/usr/cuda/lib64/libnppist_static.a', '/usr/cuda/lib64/libnppisu_static.a', '/usr/cuda/lib64/libnppitc_static.a', '/usr/cuda/lib64/libnpps_static.a', '/usr/cuda/lib64/libnvjpeg_static.a', 'GL', 'EGL', 'GLX', 'nvcuvid', 'va-drm', 'va', 'vdpau', 'X11', 'm', '/usr/lib64/libdrm.a', 'm', 'mfx', 'stdc++', 'dl', 'OpenCL', 'va']
STLIB_gbm = ['gbm', 'dl']
STLIB_gl_wayland = ['wayland-egl', 'wayland-client']
STLIB_gl_x11 = ['vdpau']
STLIB_lcms2 = ['lcms2', 'm', 'pthread']
STLIB_libarchive = ['archive', 'crypto', 'nettle', 'acl', 'lzo2', 'lzma', 'zstd', 'lz4', 'bz2', 'z', 'xml2']
STLIB_libass = ['ass', 'm', 'fontconfig', 'expat', 'fribidi', 'freetype', 'bz2', 'png16', 'm', 'z', 'm', 'z', 'harfbuzz', 'm', 'glib-2.0', 'pcre', 'graphite2', 'brotlidec', 'brotlicommon']
STLIB_libavdevice = ['/usr/lib64/libavdevice.a', '/usr/cuda/lib64/libcublasLt_static.a', '/usr/cuda/lib64/libcublas_static.a', '/usr/cuda/lib64/libcudadevrt.a', '/usr/cuda/lib64/libcudart_static.a', '/usr/cuda/lib64/libcufft_static_nocallback.a', '/usr/cuda/lib64/libcufftw_static.a', '/usr/cuda/lib64/libculibos.a', '/usr/cuda/lib64/libcurand_static.a', '/usr/cuda/lib64/libcusolver_static.a', '/usr/cuda/lib64/libcusparse_static.a', '/usr/cuda/lib64/liblapack_static.a', '/usr/cuda/lib64/libmetis_static.a', '/usr/cuda/lib64/libnppc_static.a', '/usr/cuda/lib64/libnppial_static.a', '/usr/cuda/lib64/libnppicc_static.a', '/usr/cuda/lib64/libnppidei_static.a', '/usr/cuda/lib64/libnppif_static.a', '/usr/cuda/lib64/libnppig_static.a', '/usr/cuda/lib64/libnppim_static.a', '/usr/cuda/lib64/libnppist_static.a', '/usr/cuda/lib64/libnppisu_static.a', '/usr/cuda/lib64/libnppitc_static.a', '/usr/cuda/lib64/libnpps_static.a', '/usr/cuda/lib64/libnvjpeg_static.a', 'GL', 'EGL', 'GLX', 'nvcuvid', 'm', '/usr/lib64/libdrm.a', 'm', 'xcb', 'Xau', 'Xdmcp', 'xcb-shm', 'xcb', 'Xau', 'Xdmcp', 'xcb-shape', 'xcb', 'Xau', 'Xdmcp', 'xcb-xfixes', 'xcb-render', 'xcb-shape', 'xcb', 'Xau', 'Xdmcp', 'GL', '/usr/lib64/libSDL2.a', 'm', 'dl', 'pthread', 'rt', '/usr/lib64/libavfilter.a', '/usr/cuda/lib64/libcublasLt_static.a', '/usr/cuda/lib64/libcublas_static.a', '/usr/cuda/lib64/libcudadevrt.a', '/usr/cuda/lib64/libcudart_static.a', '/usr/cuda/lib64/libcufft_static_nocallback.a', '/usr/cuda/lib64/libcufftw_static.a', '/usr/cuda/lib64/libculibos.a', '/usr/cuda/lib64/libcurand_static.a', '/usr/cuda/lib64/libcusolver_static.a', '/usr/cuda/lib64/libcusparse_static.a', '/usr/cuda/lib64/liblapack_static.a', '/usr/cuda/lib64/libmetis_static.a', '/usr/cuda/lib64/libnppc_static.a', '/usr/cuda/lib64/libnppial_static.a', '/usr/cuda/lib64/libnppicc_static.a', '/usr/cuda/lib64/libnppidei_static.a', '/usr/cuda/lib64/libnppif_static.a', '/usr/cuda/lib64/libnppig_static.a', '/usr/cuda/lib64/libnppim_static.a', '/usr/cuda/lib64/libnppist_static.a', '/usr/cuda/lib64/libnppisu_static.a', '/usr/cuda/lib64/libnppitc_static.a', '/usr/cuda/lib64/libnpps_static.a', '/usr/cuda/lib64/libnvjpeg_static.a', 'GL', 'EGL', 'GLX', 'nvcuvid', 'm', '/usr/lib64/libfribidi.a', '/usr/lib64/libass.a', 'm', '/usr/lib64/libfontconfig.a', '/usr/lib64/libexpat.a', '/usr/lib64/libfribidi.a', '/usr/lib64/libfreetype.a', '/usr/lib64/libbz2.a', '/usr/lib64/libpng16.a', 'm', '/usr/lib64/libz.a', 'm', '/usr/lib64/libz.a', '/usr/lib64/libharfbuzz.a', 'm', '/usr/lib64/libglib-2.0.a', '/usr/lib64/libpcre.a', '/usr/lib64/libgraphite2.a', '/usr/lib64/libbrotlidec.a', '/usr/lib64/libbrotlicommon.a', '/usr/cuda/lib64/libnppig_static.a', '/usr/cuda/lib64/libnppicc_static.a', '/usr/cuda/lib64/libnppc_static.a', '/usr/cuda/lib64/libnppidei_static.a', 'va', '/usr/lib64/libvidstab.a', 'm', 'gomp', 'pthread', '/usr/lib64/libzimg.a', 'stdc++', 'OpenCL', '/usr/lib64/libfontconfig.a', '/usr/lib64/libexpat.a', '/usr/lib64/libfreetype.a', '/usr/lib64/libbz2.a', '/usr/lib64/libpng16.a', 'm', '/usr/lib64/libz.a', 'm', '/usr/lib64/libz.a', '/usr/lib64/libharfbuzz.a', 'm', '/usr/lib64/libglib-2.0.a', '/usr/lib64/libpcre.a', '/usr/lib64/libgraphite2.a', '/usr/lib64/libbrotlidec.a', '/usr/lib64/libbrotlicommon.a', '/usr/lib64/libfreetype.a', '/usr/lib64/libbz2.a', '/usr/lib64/libpng16.a', 'm', '/usr/lib64/libz.a', 'm', '/usr/lib64/libz.a', '/usr/lib64/libharfbuzz.a', 'm', '/usr/lib64/libglib-2.0.a', '/usr/lib64/libpcre.a', '/usr/lib64/libgraphite2.a', '/usr/lib64/libbrotlidec.a', '/usr/lib64/libbrotlicommon.a', 'mfx', 'stdc++', 'dl', '/usr/lib64/libswscale.a', '/usr/cuda/lib64/libcublasLt_static.a', '/usr/cuda/lib64/libcublas_static.a', '/usr/cuda/lib64/libcudadevrt.a', '/usr/cuda/lib64/libcudart_static.a', '/usr/cuda/lib64/libcufft_static_nocallback.a', '/usr/cuda/lib64/libcufftw_static.a', '/usr/cuda/lib64/libculibos.a', '/usr/cuda/lib64/libcurand_static.a', '/usr/cuda/lib64/libcusolver_static.a', '/usr/cuda/lib64/libcusparse_static.a', '/usr/cuda/lib64/liblapack_static.a', '/usr/cuda/lib64/libmetis_static.a', '/usr/cuda/lib64/libnppc_static.a', '/usr/cuda/lib64/libnppial_static.a', '/usr/cuda/lib64/libnppicc_static.a', '/usr/cuda/lib64/libnppidei_static.a', '/usr/cuda/lib64/libnppif_static.a', '/usr/cuda/lib64/libnppig_static.a', '/usr/cuda/lib64/libnppim_static.a', '/usr/cuda/lib64/libnppist_static.a', '/usr/cuda/lib64/libnppisu_static.a', '/usr/cuda/lib64/libnppitc_static.a', '/usr/cuda/lib64/libnpps_static.a', '/usr/cuda/lib64/libnvjpeg_static.a', 'GL', 'EGL', 'GLX', 'nvcuvid', 'm', '/usr/lib64/libpostproc.a', '/usr/cuda/lib64/libcublasLt_static.a', '/usr/cuda/lib64/libcublas_static.a', '/usr/cuda/lib64/libcudadevrt.a', '/usr/cuda/lib64/libcudart_static.a', '/usr/cuda/lib64/libcufft_static_nocallback.a', '/usr/cuda/lib64/libcufftw_static.a', '/usr/cuda/lib64/libculibos.a', '/usr/cuda/lib64/libcurand_static.a', '/usr/cuda/lib64/libcusolver_static.a', '/usr/cuda/lib64/libcusparse_static.a', '/usr/cuda/lib64/liblapack_static.a', '/usr/cuda/lib64/libmetis_static.a', '/usr/cuda/lib64/libnppc_static.a', '/usr/cuda/lib64/libnppial_static.a', '/usr/cuda/lib64/libnppicc_static.a', '/usr/cuda/lib64/libnppidei_static.a', '/usr/cuda/lib64/libnppif_static.a', '/usr/cuda/lib64/libnppig_static.a', '/usr/cuda/lib64/libnppim_static.a', '/usr/cuda/lib64/libnppist_static.a', '/usr/cuda/lib64/libnppisu_static.a', '/usr/cuda/lib64/libnppitc_static.a', '/usr/cuda/lib64/libnpps_static.a', '/usr/cuda/lib64/libnvjpeg_static.a', 'GL', 'EGL', 'GLX', 'nvcuvid', 'm', '/usr/lib64/libavformat.a', '/usr/cuda/lib64/libcublasLt_static.a', '/usr/cuda/lib64/libcublas_static.a', '/usr/cuda/lib64/libcudadevrt.a', '/usr/cuda/lib64/libcudart_static.a', '/usr/cuda/lib64/libcufft_static_nocallback.a', '/usr/cuda/lib64/libcufftw_static.a', '/usr/cuda/lib64/libculibos.a', '/usr/cuda/lib64/libcurand_static.a', '/usr/cuda/lib64/libcusolver_static.a', '/usr/cuda/lib64/libcusparse_static.a', '/usr/cuda/lib64/liblapack_static.a', '/usr/cuda/lib64/libmetis_static.a', '/usr/cuda/lib64/libnppc_static.a', '/usr/cuda/lib64/libnppial_static.a', '/usr/cuda/lib64/libnppicc_static.a', '/usr/cuda/lib64/libnppidei_static.a', '/usr/cuda/lib64/libnppif_static.a', '/usr/cuda/lib64/libnppig_static.a', '/usr/cuda/lib64/libnppim_static.a', '/usr/cuda/lib64/libnppist_static.a', '/usr/cuda/lib64/libnppisu_static.a', '/usr/cuda/lib64/libnppitc_static.a', '/usr/cuda/lib64/libnpps_static.a', '/usr/cuda/lib64/libnvjpeg_static.a', 'GL', 'EGL', 'GLX', 'nvcuvid', 'm', '/usr/lib64/libxml2.a', '/usr/lib64/libz.a', '/usr/lib64/liblzma.a', 'm', '/usr/lib64/libbz2.a', '/usr/lib64/libvapoursynth-script.a', '/usr/lib64/libpython3.8.a', '/usr/lib64/libcrypt.a', 'pthread', 'dl', '/usr/lib64/libutil.a', 'm', '/usr/lib64/libvapoursynth.a', '/usr/lib64/libzimg.a', 'dl', '/usr/lib64/libzimg.a', 'stdc++', '/usr/lib64/libbluray.a', 'dl', 'pthread', '/usr/lib64/libxml2.a', '/usr/lib64/libz.a', '/usr/lib64/liblzma.a', 'm', '/usr/lib64/libfontconfig.a', '/usr/lib64/libexpat.a', '/usr/lib64/libfreetype.a', '/usr/lib64/libbz2.a', '/usr/lib64/libpng16.a', 'm', '/usr/lib64/libz.a', 'm', '/usr/lib64/libz.a', '/usr/lib64/libharfbuzz.a', 'm', '/usr/lib64/libglib-2.0.a', '/usr/lib64/libpcre.a', '/usr/lib64/libgraphite2.a', '/usr/lib64/libbrotlidec.a', '/usr/lib64/libbrotlicommon.a', '/usr/lib64/libz.a', '/usr/lib64/libssl.a', '/usr/lib64/libcrypto.a', '/usr/lib64/libz.a', 'dl', '/usr/lib64/librtmp.a', '/usr/lib64/libz.a', '/usr/lib64/libgmp.a', 'gnutls', '/usr/lib64/libgmp.a', '/usr/lib64/libunistring.a', '/usr/lib64/libatomic.a', '/usr/lib64/libtasn1.a', '/usr/lib64/libidn2.a', '/usr/lib64/libunistring.a', 'p11-kit', '/usr/lib64/libhogweed.a', '/usr/lib64/libgmp.a', '/usr/lib64/libnettle.a', '/usr/lib64/libsrt.a', 'stdc++', 'm', '/usr/lib64/libgcov.a', 'gcc_s', 'gcc', 'pthread', 'c', 'gcc_s', 'gcc', '/usr/lib64/libssl.a', '/usr/lib64/libcrypto.a', '/usr/lib64/libz.a', 'dl', '/usr/lib64/libavcodec.a', '/usr/cuda/lib64/libcublasLt_static.a', '/usr/cuda/lib64/libcublas_static.a', '/usr/cuda/lib64/libcudadevrt.a', '/usr/cuda/lib64/libcudart_static.a', '/usr/cuda/lib64/libcufft_static_nocallback.a', '/usr/cuda/lib64/libcufftw_static.a', '/usr/cuda/lib64/libculibos.a', '/usr/cuda/lib64/libcurand_static.a', '/usr/cuda/lib64/libcusolver_static.a', '/usr/cuda/lib64/libcusparse_static.a', '/usr/cuda/lib64/liblapack_static.a', '/usr/cuda/lib64/libmetis_static.a', '/usr/cuda/lib64/libnppc_static.a', '/usr/cuda/lib64/libnppial_static.a', '/usr/cuda/lib64/libnppicc_static.a', '/usr/cuda/lib64/libnppidei_static.a', '/usr/cuda/lib64/libnppif_static.a', '/usr/cuda/lib64/libnppig_static.a', '/usr/cuda/lib64/libnppim_static.a', '/usr/cuda/lib64/libnppist_static.a', '/usr/cuda/lib64/libnppisu_static.a', '/usr/cuda/lib64/libnppitc_static.a', '/usr/cuda/lib64/libnpps_static.a', '/usr/cuda/lib64/libnvjpeg_static.a', 'GL', 'EGL', 'GLX', 'nvcuvid', '/usr/lib64/libvpx.a', 'm', 'pthread', '/usr/lib64/libvpx.a', 'm', 'pthread', '/usr/lib64/libvpx.a', 'm', 'pthread', '/usr/lib64/libvpx.a', 'm', 'pthread', '/usr/lib64/libwebpmux.a', 'm', '/usr/lib64/libwebp.a', 'm', 'm', '/usr/lib64/liblzma.a', '/usr/lib64/libdav1d.a', 'dl', '/usr/lib64/libsnappy.a', 'stdc++', '/usr/lib64/libz.a', '/usr/lib64/libaom.a', 'm', 'pthread', '/usr/lib64/libfdk-aac.a', 'm', '/usr/lib64/libgsm.a', '/usr/lib64/libmp3lame.a', 'm', '/usr/lib64/libopenjp2.a', 'm', '/usr/lib64/libopus.a', 'm', '/usr/lib64/libspeex.a', 'm', '/usr/lib64/libtheoraenc.a', '/usr/lib64/libtheoradec.a', '/usr/lib64/libogg.a', '/usr/lib64/libvorbis.a', 'm', '/usr/lib64/libogg.a', '/usr/lib64/libvorbisenc.a', '/usr/lib64/libvorbis.a', 'm', '/usr/lib64/libogg.a', '/usr/lib64/libwebp.a', 'm', '/usr/lib64/libx264.a', 'pthread', 'm', 'dl', '/usr/lib64/libx265.a', 'stdc++', 'm', 'gcc_s', 'gcc', 'gcc_s', 'gcc', 'rt', 'dl', '/usr/lib64/libxvidcore.a', 'va', 'mfx', 'stdc++', 'dl', '/usr/lib64/libswresample.a', '/usr/cuda/lib64/libcublasLt_static.a', '/usr/cuda/lib64/libcublas_static.a', '/usr/cuda/lib64/libcudadevrt.a', '/usr/cuda/lib64/libcudart_static.a', '/usr/cuda/lib64/libcufft_static_nocallback.a', '/usr/cuda/lib64/libcufftw_static.a', '/usr/cuda/lib64/libculibos.a', '/usr/cuda/lib64/libcurand_static.a', '/usr/cuda/lib64/libcusolver_static.a', '/usr/cuda/lib64/libcusparse_static.a', '/usr/cuda/lib64/liblapack_static.a', '/usr/cuda/lib64/libmetis_static.a', '/usr/cuda/lib64/libnppc_static.a', '/usr/cuda/lib64/libnppial_static.a', '/usr/cuda/lib64/libnppicc_static.a', '/usr/cuda/lib64/libnppidei_static.a', '/usr/cuda/lib64/libnppif_static.a', '/usr/cuda/lib64/libnppig_static.a', '/usr/cuda/lib64/libnppim_static.a', '/usr/cuda/lib64/libnppist_static.a', '/usr/cuda/lib64/libnppisu_static.a', '/usr/cuda/lib64/libnppitc_static.a', '/usr/cuda/lib64/libnpps_static.a', '/usr/cuda/lib64/libnvjpeg_static.a', 'GL', 'EGL', 'GLX', 'nvcuvid', 'm', '/usr/lib64/libavutil.a', '/usr/cuda/lib64/libcublasLt_static.a', '/usr/cuda/lib64/libcublas_static.a', '/usr/cuda/lib64/libcudadevrt.a', '/usr/cuda/lib64/libcudart_static.a', '/usr/cuda/lib64/libcufft_static_nocallback.a', '/usr/cuda/lib64/libcufftw_static.a', '/usr/cuda/lib64/libculibos.a', '/usr/cuda/lib64/libcurand_static.a', '/usr/cuda/lib64/libcusolver_static.a', '/usr/cuda/lib64/libcusparse_static.a', '/usr/cuda/lib64/liblapack_static.a', '/usr/cuda/lib64/libmetis_static.a', '/usr/cuda/lib64/libnppc_static.a', '/usr/cuda/lib64/libnppial_static.a', '/usr/cuda/lib64/libnppicc_static.a', '/usr/cuda/lib64/libnppidei_static.a', '/usr/cuda/lib64/libnppif_static.a', '/usr/cuda/lib64/libnppig_static.a', '/usr/cuda/lib64/libnppim_static.a', '/usr/cuda/lib64/libnppist_static.a', '/usr/cuda/lib64/libnppisu_static.a', '/usr/cuda/lib64/libnppitc_static.a', '/usr/cuda/lib64/libnpps_static.a', '/usr/cuda/lib64/libnvjpeg_static.a', 'GL', 'EGL', 'GLX', 'nvcuvid', 'va-drm', 'va', 'vdpau', 'X11', 'm', '/usr/lib64/libdrm.a', 'm', 'mfx', 'stdc++', 'dl', 'OpenCL', 'va']
STLIB_libbluray = ['bluray', 'dl', 'pthread', 'xml2', 'z', 'lzma', 'm', 'fontconfig', 'expat', 'freetype', 'bz2', 'png16', 'm', 'z', 'm', 'z', 'harfbuzz', 'm', 'glib-2.0', 'pcre', 'graphite2', 'brotlidec', 'brotlicommon']
STLIB_libplacebo = ['placebo', 'm', 'shaderc_combined', 'lcms2', 'm', 'pthread', 'vulkan', 'stdc++', 'm', 'gcc_s', 'gcc', 'c', 'gcc_s', 'gcc', 'epoxy', 'dl', 'GL', 'pthread', 'm', 'dl', 'EGL', 'pthread', 'm', 'dl', 'Xdamage', 'Xfixes', 'X11-xcb', 'xcb-glx', 'xcb-dri2', 'Xxf86vm', 'Xext', 'X11', 'pthread', 'xcb', 'Xau', 'Xdmcp', 'drm', 'm']
STLIB_luajit = ['luajit-5.1', 'm', 'dl']
STLIB_pulse = ['pulse', 'pulsecommon-13.0']
STLIB_rubberband = ['rubberband']
STLIB_sdl2 = ['SDL2', 'm', 'dl', 'pthread', 'rt']
STLIB_uchardet = ['uchardet', 'stdc++']
STLIB_vaapi = ['va']
STLIB_vaapi_drm = ['va-drm', 'va']
STLIB_vaapi_wayland = ['va-wayland', 'va', 'wayland-client']
STLIB_vaapi_x11 = ['va-x11', 'va']
STLIB_vapoursynth = ['vapoursynth-script', 'python3.8', 'crypt', 'pthread', 'dl', 'util', 'm', 'vapoursynth', 'zimg', 'dl', 'zimg', 'stdc++']
STLIB_vdpau = ['vdpau']
STLIB_vulkan = ['vulkan', 'stdc++', 'm', 'gcc_s', 'gcc', 'c', 'gcc_s', 'gcc']
STLIB_wayland = ['wayland-client', 'wayland-cursor', 'xkbcommon']
STLIB_x11 = ['Xss', 'Xinerama', 'Xrandr', 'Xext', 'Xrender', 'X11', 'pthread', 'xcb', 'Xau', 'Xdmcp']
STLIB_zimg = ['zimg', 'stdc++']
SYSCONFDIR = '/etc'
WAYSCAN = ['/usr/bin/wayland-scanner']
WL_PROTO_DIR = '//usr/share/wayland-protocols'
ZSHDIR = '/usr/share/zsh/site-functions'
cfg_files = ['/builddir/build/BUILD/clone_archive/build/config.h']
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.so'
cstlib_PATTERN = 'lib%s.a'
define_key = []
known_deps = ['wayland', 'pthreads', 'd3d-hwaccel', 'videotoolbox-hwaccel', 'noexecstack', 'macos-media-player', 'vdpau', 'macos-cocoa-cb', 'bsd-fstatfs', 'shaderc-shared', 'glob-win32', 'ffmpeg-strict-abi', 'spirv-cross-static', 'egl-x11', 'coreaudio', 'tvos', 'os-linux', 'javascript', 'win32-internal-pthreads', 'gl', 'mingw', 'cplayer', 'swift', 'iconv', 'dos-paths', 'win32-desktop', 'tests', 'openal', 'd3d9-hwaccel', 'egl-angle', 'opensles', 'wayland-protocols', 'direct3d', 'videotoolbox-gl', 'spirv-cross', 'vaapi', 'asm', 'vdpau-gl-x11', 'rpi-mmal', 'gbm.h', 'sdl2-gamepad', 'ffnvcodec', 'alsa', 'egl', 'sdl2', 'lua', 'shaderc', 'gl-x11', 'vaapi-x-egl', 'plain-gl', 'html-build', 'gpl', 'drm', 'd3d11', 'librt', 'macos-10-11-features', 'cocoa', 'vaapi-vulkan', 'posix-or-mingw', 'ios-gl', 'egl-android', 'bsd-thread-name', 'egl-angle-win32', 'sdl2-video', 'cuda-hwaccel', 'cuda-interop', 'win32-executable', 'vapoursynth', 'osx-thread-name', 'macos-10-14-features', 'gl-dxinterop-d3d9', 'libarchive', 'macos-10-12-2-features', 'glibc-thread-name', 'vaapi-drm', 'linux-fstatfs', 'libass', 'x11', 'gl-dxinterop', 'stdatomic', 'uchardet', 'xv', 'rpi', 'rubberband', 'vulkan', 'pdf-build', 'posix', 'clang-database', 'libmpv-static', 'consio.h', 'lcms2', 'memfd_create', 'zlib', 'libdl', 'debug-build', 'swift-static', 'static-build', 'gl-win32', 'shaderc-static', 'libplacebo', 'dvdnav', 'zimg', 'vaapi-x11', 'egl-helpers', 'dvbin', 'libavdevice', 'egl-angle-lib', 'libmpv-shared', 'libbluray', 'pulse', 'jack', 'lgpl', 'gbm', 'audiounit', 'android', 'build-date', 'vaapi-wayland', 'pthread-debug', 'sdl2-audio', 'ta-leak-report', 'ffmpeg', 'cplugins', 'vaapi-egl', 'libm', 'gl-cocoa', 'cdda', 'wasapi', 'gl-wayland', 'jpeg', 'wayland-scanner', 'manpage-build', 'egl-drm', 'caca', 'spirv-cross-shared', 'glob-posix', 'macos-touchbar', 'glob', 'vt.h', 'uwp', 'optimize']
macbundle_PATTERN = '%s.bundle'
satisfied_deps = ['libdl', 'debug-build', 'gbm.h', 'pthreads', 'wayland', 'sdl2-gamepad', 'shaderc-static', 'vapoursynth', 'libplacebo', 'ffnvcodec', 'cuda-interop', 'noexecstack', 'zimg', 'alsa', 'vdpau', 'vaapi-x11', 'egl-helpers', 'egl', 'libavdevice', 'luajit', 'sdl2', 'lua', 'libarchive', 'shaderc', 'glibc-thread-name', 'gl-x11', 'vaapi-x-egl', 'sdl2-video', 'libbluray', 'vaapi-drm', 'pulse', 'linux-fstatfs', 'egl-x11', 'libass', 'x11', 'vdpau-gl-x11', 'plain-gl', 'gbm', 'gpl', 'drm', 'os-linux', 'build-date', 'gl', 'vaapi-wayland', 'stdatomic', 'librt', 'uchardet', 'cplayer', 'iconv', 'rubberband', 'ffmpeg', 'sdl2-audio', 'cplugins', 'posix-or-mingw', 'vaapi-egl', 'libm', 'vulkan', 'vaapi-vulkan', 'gl-wayland', 'posix', 'jpeg', 'wayland-scanner', 'tests', 'libmpv-static', 'egl-drm', 'wayland-protocols', 'cuda-hwaccel', 'memfd_create', 'glob-posix', 'lcms2', 'glob', 'vaapi', 'asm', 'vt.h', 'zlib', 'optimize']