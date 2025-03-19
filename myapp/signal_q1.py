# Here what i have implement:
# ------------------------------------------------------------------------

# I created a custom Django signal because I wanted to check whether Django signals execute synchronously or asynchronously.
# I added a receiver function with a time.sleep(3) delay because I needed a clear way to see if the main execution would wait for the signal handler to finish.
# I printed timestamps before sending the signal and after it was processed because comparing them would show whether the script was blocked while the signal was executing.
# When I ran the script, I saw that the "After sending signal" message was printed only after the signal handler completed, proving that Django signals run synchronously by default.

import time
import datetime
from django.dispatch import Signal, receiver

from django.conf import settings
settings.configure()

my_signal = Signal()

@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print(f"Signal receiver started at: {datetime.datetime.now()}")
    time.sleep(3)
    print(f"Signal receiver completed at: {datetime.datetime.now()}")

print(f"Before sending signal: {datetime.datetime.now()}")
my_signal.send(sender="test_sender")
print(f"After sending signal: {datetime.datetime.now()}")



# sample out put
# ----------------------------------------------------

# Before sending signal: 2025-03-18 17:02:35.844278
# Signal receiver started at: 2025-03-18 17:02:35.844344

# Signal receiver completed at: 2025-03-18 17:02:38.847410
# After sending signal: 2025-03-18 17:02:38.847514 

