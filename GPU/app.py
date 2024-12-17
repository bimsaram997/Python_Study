import pyopencl as cl
platforms = cl.get_platforms()
for platform in platforms:
    devices = platform.get_devices()
    for device in devices:
        print("Device:", device.name)
