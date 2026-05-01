try:
    import psutil
except ImportError:
    psutil = None

def get_running_apps_windows():
    if psutil is None:
        return ["psutil not installed; running apps unavailable"]
    try:
        # Get a list of running processes
        processes = [proc.name() for proc in psutil.process_iter(['name'])]
        return list(set(processes))  # Remove duplicates
    except Exception as e:
        return f"Error: {e}"


def check_running_app():
    running_apps = get_running_apps_windows()
    print("Running Applications:")
    for app in running_apps:
        print(app)


