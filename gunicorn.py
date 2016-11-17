import multiprocessing

bind = "localhost:8000"

# Workers config
workers = multiprocessing.cpu_count() * 2 + 1

threads = multiprocessing.cpu_count() * 2 + 1

timeout = 300

reload = True