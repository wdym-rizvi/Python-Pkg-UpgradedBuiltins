import sys, time
def marquee(text, repeat=3, delay=0.1):
    s = " " * 20 + text + " " * 20
    for _ in range(repeat):
        for i in range(len(s)):
            sys.stdout.write("\r" + s[i:i+20])
            sys.stdout.flush()
            time.sleep(delay)
