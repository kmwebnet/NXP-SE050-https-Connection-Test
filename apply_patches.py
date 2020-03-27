from os.path import join, isfile
Import("env")

FRAMEWORK_DIR = env.PioPlatform().get_package_dir("framework-espidf")
patchflag_path = join(FRAMEWORK_DIR, ".patching-done")

# patch file only if we didn't do it before
if not isfile(join(FRAMEWORK_DIR, ".patching-done")):
    original_file = join(FRAMEWORK_DIR, "components", "mbedtls", "mbedtls" , "library" , "ecdh.c")
    patched_file = join("patches", "ecdh.patch")
    assert isfile(original_file) and isfile(patched_file)
    env.Execute("patch %s %s" % (original_file, patched_file))

    original_file = join(FRAMEWORK_DIR, "components", "mbedtls", "mbedtls" , "library" , "ecp.c")
    patched_file = join("patches", "ecp.patch")
    assert isfile(original_file) and isfile(patched_file)
    env.Execute("patch %s %s" % (original_file, patched_file))

    original_file = join(FRAMEWORK_DIR, "components", "mbedtls", "mbedtls" , "library" , "ecdsa.c")
    patched_file = join("patches", "ecdsa.patch")
    assert isfile(original_file) and isfile(patched_file)
    env.Execute("patch %s %s" % (original_file, patched_file))

    original_file = join(FRAMEWORK_DIR, "components", "mbedtls", "mbedtls" , "library" , "ssl_srv.c")
    patched_file = join("patches", "ssl_srv.patch")
    assert isfile(original_file) and isfile(patched_file)
    env.Execute("patch %s %s" % (original_file, patched_file))

    def _touch(path):
        with open(path, "w") as fp:
            fp.write("")

    env.Execute(lambda *args, **kwargs: _touch(patchflag_path))
