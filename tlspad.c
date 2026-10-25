/*
 * libhybris on glibc: hybris lays out bionic static TLS for loaded Android
 * libraries (e.g. libGLES_mali) at fixed offsets from the thread pointer,
 * but glibc threads don't own memory there. Preloading this library puts a
 * large static TLS block directly after the executable's, so TP + offset is
 * valid in every thread. Loaded via /etc/ld.so.preload so it also applies to
 * AT_SECURE processes (file capabilities), where LD_PRELOAD/GLIBC_TUNABLES
 * are ignored.
 */
__attribute__((tls_model("initial-exec"), used))
__thread char hybris_static_tls_pad[32768];
