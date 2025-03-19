# Django Signals and Custom Classes

## Django Signals

### Question 1:

**Answer:** Django signals are synchronous by default.

**Filename:** `signal_q1.py`

#### What I Implemented:
- I created a custom Django signal to check whether Django signals execute synchronously or asynchronously.
- I added a receiver function with a `time.sleep(3)` delay to see if the main execution would wait for the signal handler to finish.
- I printed timestamps before sending the signal and after it was processed to compare if the script was blocked while the signal was executing.
- When I ran the script, the "After sending signal" message was printed only after the signal handler completed, proving that Django signals run synchronously by default.

#### How to Run:
```sh
cd myapp
python signal_q1.py
```

#### Sample Output:
```
Before sending signal: 2025-03-18 17:02:35.844278
Signal receiver started at: 2025-03-18 17:02:35.844344

Signal receiver completed at: 2025-03-18 17:02:38.847410
After sending signal: 2025-03-18 17:02:38.847514
```

---

### Question 2:

**Answer:** Django signals run in the same thread as the caller by default.

**Filename:** `signal_q2.py`

#### What I Implemented:
- I created a custom Django signal to check whether Django signals run in the same thread as the caller.
- I used `threading.get_ident()` to get the thread ID, which uniquely identifies the current thread, allowing me to compare the sender and receiver threads.
- I printed the thread ID before sending the signal and inside the receiver to confirm if both were running in the same thread.
- When I ran the script, the sender and receiver had the same thread ID, proving that Django signals execute in the same thread as the caller by default.

#### How to Run:
```sh
cd myapp
python signal_q2.py
```

#### Sample Output:
```
Sender thread ID: 140084689793472
Receiver thread ID: 140084689793472
```

---

### Question 3:

**Answer:** Django signals run in the same database transaction as the caller by default.

**Filename:** `signal_q3.py` (Django management command)

#### What I Implemented:
- I created a custom Django management command to check whether Django signals run in the same database transaction as the caller.
- I used `transaction.atomic()` in the command to ensure all database operations inside it either commit together or roll back together if an error occurs.
- I connected a `post_save` signal to the `User` model to trigger additional database operations right after a user is created.
- Inside the signal handler, I tried to create another `User` with the same username to force a database error and see if it would cause a rollback of the entire transaction.
- I printed the user count before and after creating the user to determine whether the transaction was rolled back when the signal failed.
- When I ran the command, the user count remained the same (no new user was created), proving that Django signals run in the same transaction as the caller by default and roll back if an error occurs inside the signal.

#### How to Run:
```sh
python manage.py signal_q3
```

#### Sample Output:
```
Test user deleted if it existed
User count before: 11
Signal handler triggered, attempting to create another user
Exception in signal handler: UNIQUE constraint failed: auth_user.username
Transaction failed with: UNIQUE constraint failed: auth_user.username
User count after: 11
Difference in counts: 0
CONCLUSION: Signals DO run in the same transaction as the caller. The failed signal caused the entire transaction to roll back, preventing the original user from being created.
```

---

## Custom Classes in Python

### Implementing an Iterable `Rectangle` Class

**Filenames:** `rectangle.py`, `test_rectangle.py`

#### What I Implemented:
- I created a `Rectangle` class to hold `length` and `width` while also being iterable.
- I defined the `__iter__` method to make the class iterable, allowing us to loop over an instance of `Rectangle`.
- I used a generator function inside `__iter__` to yield values one at a time, first returning the length in `{'length': <VALUE>}` format and then the width in `{'width': <VALUE>}` format.
- I tested iteration using both a `for` loop and a list comprehension to confirm that the object correctly yields values in the expected format.

#### How to Run:
```sh
cd myapp
python test_rectangle.py
```

#### Sample Output:
```
Iterating over Rectangle:
{'length': 10}
{'width': 5}

All values: [{'length': 10}, {'width': 5}]
